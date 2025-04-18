FROM python:3.11

WORKDIR /fastapi_project

COPY ./requirements.txt /fastapi_project/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /fastapi_project/requirements.txt

COPY ./app /fastapi_project/app

CMD [ "fastapi", "run", "--host", "0.0.0.0", "--port", "80" ]