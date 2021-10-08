FROM alpine:latest

RUN apk update \
    && apk add python3 py3-pip
RUN python3 -m pip install django

RUN mkdir app
ADD djangoRedditApp/ app
WORKDIR app/

RUN python3 -m pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["python3","manage.py", "runserver", "0.0.0.0:8080"]