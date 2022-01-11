FROM node:16

WORKDIR /app

ADD ./app /app/

RUN npm i
RUN npm run build

EXPOSE 7001

RUN chmod 777 /app/runserver.sh

CMD ["/app/runserver.sh"]