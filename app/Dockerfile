FROM centos:latest

RUN useradd -u myblog

WORKDIR /home/boovoice

RUN dnf -y install curl
RUN curl -sL https://rpm.nodesource.com/setup_14.x | sudo bash -
RUN dnf -y install nodejs
RUN npm update -g npm
RUN curl -sL https://dl.yarnpkg.com/rpm/yarn.repo | tee /etc/yum.repos.d/yarn.repo
RUN dnf -y install yarn
RUN dnf -y install gcc-c++ make

RUN npm install -g express
RUN npm install -g express-generator

CMD [sh, -c, npm install && npm start]