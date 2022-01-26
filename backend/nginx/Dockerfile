from nginx:1.21.5

COPY ./conf/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 8001
EXPOSE 6001

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]