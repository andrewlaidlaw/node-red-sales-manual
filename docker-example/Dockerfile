# Use existing Node Red container
FROM registry.redhat.io/rhscl/nodejs-14-rhel7
LABEL maintainer="Andrew Laidlaw [andrew.laidlaw@uk.ibm.com]"

# Copy source files into the container
COPY sales-manual-reader-flow.json /usr/src/node-red/sales-manual-reader-flow.json
COPY package.json /usr/src/node-red/package.json

# Expose default Node Red port
EXPOSE 1880/tcp

# Proxy settings only needed for our local environment, could be passed at build
#ENV http_proxy http://9.196.156.29:3128
#ENV https_proxy http://9.196.156.29:3128

# Set user and required environmetn variables
#USER nodered
ENV HOME /usr/src/node-red
#WORKDIR /usr/src/node-red

# Run Node Red including our predefined flows
CMD node-red /usr/src/node-red/sales-manual-reader-flow.json