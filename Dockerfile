FROM ubuntu
CMD /bin/bash
MAINTAINER Stu Cunliffe s_cunliffe@uk.ibm.com
RUN apt-get update
RUN apt-get install -y npm
RUN apt-get install -y python3
RUN apt-get install -y python3-bs4
RUN mkdir -p /usr/src/node-red
WORKDIR /usr/src/node-red
RUN groupadd --force node-red
RUN useradd --home /usr/src/node-red --gid node-red node-red
RUN chown -R node-red:node-red /usr/src/node-red
USER node-red
RUN npm install node-red
EXPOSE 1880/tcp
COPY package.json /usr/src/node-red/package.json
CMD npm start node-red
