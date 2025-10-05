FROM python:3.13.7

WORKDIR /code

RUN pip install "fastapi[standard]" pydantic pandas

COPY ./app /code/app

EXPOSE 8080

CMD ["fastapi", "run", "app/main.py", "--port", "8080", "--host", "0.0.0.0"]