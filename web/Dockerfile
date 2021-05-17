FROM centos:latest

RUN dnf -y install nginx

ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;", "-c", "/etc/nginx/nginx.conf"]