FROM python:3.9.9

RUN pip install --upgrade pip
ARG requirements=requirements.txt
WORKDIR /app

ADD . /app/
RUN pip install -r ${requirements}

RUN apt update
RUN apt install -y netcat

EXPOSE 6001
EXPOSE 8001

RUN chmod 777 /app/runserver.sh

CMD ["/app/runserver.sh"]