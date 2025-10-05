FROM python:3.13.7

WORKDIR /code

RUN pip install "fastapi[standard]" pydantic pandas requests

COPY ./app /code/app

EXPOSE 8081

CMD ["fastapi", "run", "app/main.py", "--port", "8081", "--host", "0.0.0.0"]