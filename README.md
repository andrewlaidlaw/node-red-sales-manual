# Sales Manual Chatbot interface
Originally developed by [David Spurway](https://github.com/DSpurway/node-red-sales-manual) with help from [Stuart Cunliffe](https://github.com/cunlifs/node-red-sales-manual).

## Deployment
This Github repository is designed to be a target for a Red Hat Openshift build using the included Dockerfile. This will build and deploy a new container image that includes the Node-Red environment that manages the presentation logic, as well as some Python scripts that are used for analysis of text. This deployment connects to the [IBM Watson Assistant](https://cloud.ibm.com/catalog/services/watson-assistant) service in the [IBM Cloud](https://cloud.ibm.com/) to manage the chatbot interactions in natural language.

## Settings
To run correctly, you will need to pass in the appropriate credentials as Environment Variables. When using Red Hat Openshift this can be done using a Secret resource with key-value pairs for each of the required fields. The following varaibales need to be set, using credentials from the **IBM Watson Assistant** service:
- ASSISTANT_APIKEY
- ASSISTANT_ENDPOINT
- ASSISTANT_WORKSPACE_ID

---
Based on the original container image by by Stuart Cunliffe:
### node-red-python
Node red with Python (beautiful soup)
