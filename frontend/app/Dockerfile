FROM node:17

WORKDIR /app

ADD . /app/

EXPOSE 7001
EXPOSE 9001

RUN chmod 777 /app/runserver.sh

CMD ["/app/runserver.sh"]