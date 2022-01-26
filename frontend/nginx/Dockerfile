from nginx:1.21.5

COPY wait.sh /wait.sh

RUN chmod +x /wait.sh

EXPOSE 9001

RUN rm /etc/nginx/conf.d/default.conf
COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf

CMD ["/wait.sh", "frontend:7000", "--", "nginx", "-g", "daemon off;"]

