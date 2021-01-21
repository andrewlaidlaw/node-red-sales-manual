# Sales Manual Chatbot interface
Originally developed by [David Spurway](https://github.com/DSpurway/node-red-sales-manual) with help from [Stuart Cunliffe](https://github.com/cunlifs/node-red-sales-manual).

## Deployment
This Github repository is designed to be a target for a Red Hat Openshift build using the included Dockerfile. This will build and deploy a new container image that includes the Node-Red environment that manages the presentation logic, as well as some Python scripts that are used for analysis of text. This deployment connects to the [IBM Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant) service in the [IBM Cloud](https://cloud.ibm.com/) to manage the chatbot interactions in natural language.

## Settings
To run correctly, you will need to pass in the appropriate credentials as Environment Variables. When using Red Hat Openshift this can be done using a Secret resource with key-value pairs for each of the required fields. The following varaibales need to be set, using credentials from the **IBM Watson Assistant** service:
- ASSISTANT_APIKEY
- ASSISTANT_ENDPOINT
- ASSISTANT_WORKSPACE_ID

## Endpoints
`/bot` - The primary endpoint for a user of the chatbot, allowing them to interact with the service
`/botchat` - The endpoint for values to be passed to the chatbot, not for general access
`/healthz` - An endpoint to enable healthchecks and get confirmation of a running pod
`/` - The root endpoint gives access to the Node-Red environment to make changes to the application

## Microservices version
The application can also be run as a set of Microservices, each deployed and scaled independently. These are written in different languages but can all be built using the source-to-image capabilities of OpenShift Container Platform. There are 3 services to deploy in the same namespace / project - ideally within the same app designation.
### Node Red App
*node-red-app*: this is the main service, providing the front end and all interactions with the **IBM Watson Assistant** service hosted onthe IBM Cloud. This is a *node-js* application with the endpoints listed above.
To deploy, use the context directory of `/node-red-app` when pulling from this GitHub repository.
This service will need to have environment variables applied (through a Secret or similar) for the **IBM Watson Assistant** service as listed above.
If deploying behind a proxy, this will also need the standard `HTTP_PROXY` and `HTTPS_PROXY` environment variables to be set, as well as a `NO_PROXY` variable that includes the *smfinder* and *smreader* service endpoints.
### SMFinder Webapp
*smfinder-webapp*: this service will find the appropriate Sales Manual URL for a given Machine Type / Model Number (MTM). This is a *python* application with two endpoints:
`/` - the main entry point, requires a GET call with argument **mtm** providing the Machine Type / Model Number of a server, ie `http://<smfinder>/?mtm=8335-gth`. This service returns a text string with the URL of the requested sales manual, or the text string "Missing" if a URL cannot be found.
`/healthz` - An endpoint to enable healthchecks and get confirmation of a running pod.
To deploy, use the context directory of `/smfinder-webapp` when pulling from this GitHub repository.
If deploying behind a proxy, this will also need the standard HTTP_PROXY and HTTP_PROXY environment variables to be set.
This service does not need it's own route allocating, unless external access is required for other uses.
### SMReader Webapp
*smreader-webapp*: this service will collect and interpret the sales manual at the URL passed to it. This is a *python* application with two endpoints:
`/` - the main entry point, requires a GET call with argument **url** providing the URL of a sales manual for an IBM Power Systems server, ie `http://<smreader>/?url=https://www-01.ibm.com/common/ssi/rep_sm/5/877/ENUS8335-_h05/index.html`. This service returns a JSON object. If a sales manual is found and can be parsed correctly, this JSON object will include a `result = "Success"` message and entries for the various important dates: `announce`, `available`, `wdfm`, `eos`, as well as the values for the `mtm` and the passed in `url`.
`/healthz` - An endpoint to enable healthchecks and get confirmation of a running pod.
To deploy, use the context directory of `/smreader-webapp` when pulling from this GitHub repository.
If deploying behind a proxy, this will also need the standard HTTP_PROXY and HTTP_PROXY environment variables to be set.
This service does not need it's own route allocating, unless external access is required for other uses.

---
Based on the original container image by by Stuart Cunliffe:
### node-red-python
Node red with Python (beautiful soup)
