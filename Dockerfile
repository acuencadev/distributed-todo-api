FROM python:3.8.1-slim-buster
LABEL maintainer="sphi02ac@gmail.com"

ENV INSTALL_PATH /todo_api
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "todo_api.app:create_app()"
