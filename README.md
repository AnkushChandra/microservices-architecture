# Microservices Architecture

## What Are Microservices?

**Microservices architecture** is an architectural style where an application is composed of small, independent services that communicate through APIs.  
Each microservice is responsible for a specific business capability and can be developed, deployed, and scaled independently.

To serve a single user request, a microservices-based application may call multiple internal microservices to compose a response.

> Reference: Google Cloud — ["What is Microservices Architecture?"](https://cloud.google.com/learn/what-is-microservices-architecture)

---

## High-Level Architecture

```
Client
  |
  | 1. POST /lookup { productID }
  v
Aggregator
  |\
  | \-- 2a. GET /item-info/items/{productID}
  |       -> { id, name string }
  |
  | \-- 2b. GET /stock-info/items/{productID}
  |       -> { id, count integer }
  |
  | 3. Merge + check errors
  v
Client
```

### Services Overview
- **Aggregator** – The public entry point. Calls other services and merges results.
- **Item Info Service** – Provides product metadata (`productID`, `name`).
- **Stock Service** – Provides inventory information (`productID`, `available`).

---

## API Definitions

### **Aggregator**
**POST** `/lookup`  
**Body:**
```json
{ "productID": "XYZ-12345" }
```

**200 OK**
```json
{
  "productID": "XYZ-12345",
  "name": "Amayon Basics Wipes",
  "available": 210
}
```

**404 Not Found**
```json
{ "error": "Product not found" }
```

---

### **Item Info Service**
**GET** `/item-info/items/{productID}`

**200 OK**
```json
{ "productID": "XYZ-12345", "name": "Amayon Basics Wipes" }
```

**404 Not Found**
```json
{ "error": "Product not found" }
```

---

### **Stock Service**
**GET** `/stock-info/items/{productID}`

**200 OK**
```json
{ "productID": "XYZ-12345", "available": 210 }
```

**404 Not Found**
```json
{ "error": "Product not found" }
```

---

## Final Aggregation Logic

| Item Info | Stock Info | Aggregator Response |
|------------|-------------|---------------------|
| 404 | Any | 404 Product not found |
| 200 | 200 | 200 with merged info |
| 200 | 404 | 200 with available = 0 |

---

## Pseudo Databases

Each service uses a small CSV file as a mock database:

### Item Info Service
| productID | name |
|------------|------|
| XYZ-12345 | Amayon Basics Wipes |

### Stock Service
| productID | available |
|------------|-----------|
| XYZ-12345 | 210 |

At runtime, each service reads its CSV file to simulate querying a real database.

---

## Tasks

### Implement the following Python modules:
- `client.py` – Sends a `productID` to the aggregator.
- `aggregator.py` – Handles `/lookup` and calls the two backend services.
- `iteminfo.py` – Returns product name from a CSV “database”.
- `stockinfo.py` – Returns stock count from a CSV “database”.

### Create Dockerfiles for:
- Aggregator
- Item Info Service
- Stock Info Service

Each Docker container should:
1. Contain a FastAPI app (`main.py`).
2. Be deployable on **Google Cloud Run**.

---

## Deployment

1. Build and push each Docker image:
   ```bash
   docker build -t us-west2-docker.pkg.dev/<project-id>/<repo-name>/aggregator:tag .
   docker build -t us-west2-docker.pkg.dev/<project-id>/<repo-name>/item-info:tag .
   docker build -t us-west2-docker.pkg.dev/<project-id>/<repo-name>/stock-info:tag .
   ```

2. Deploy to Cloud Run:
   ```bash
   gcloud run deploy aggregator --image us-west2-docker.pkg.dev/<project-id>/<repo-name>/aggregator:tag --platform managed
   gcloud run deploy iteminfo --image us-west2-docker.pkg.dev/<project-id>/<repo-name>/item-info:tag
   gcloud run deploy stockinfo --image us-west2-docker.pkg.dev/<project-id>/<repo-name>/stock-info:tag --platform managed
   ```

3. Save your public aggregator URL in `myURL.txt`  
   Example:
   ```
   https://pc-611571974386.us-west2.run.app/lookup
   ```

---

## 🧪 Testing

Using `client.py`, test all scenarios in the “Final Aggregation” section and log results in **results.txt**.

Example tests:
1. Valid product in both services.
2. Product missing in stock service.
3. Product missing in both services.

---

## 📁 Repository Structure

```
repo-root/
├── clientd/
│   └── client.py
│
├── aggregatord/
│   ├── Dockerfile
│   └── app/
│       ├── main.py
│       └── model/
│           └── aggregator.py
│
├── stockinfod/
│   ├── Dockerfile
│   └── app/
│       ├── main.py
│       └── model/
│           └── stockinfo.py
│
├── iteminfod/
│   ├── Dockerfile
│   └── app/
│       ├── main.py
│       └── model/
│           └── iteminfo.py
│
├── results.txt 
└── myURL.txt
```
