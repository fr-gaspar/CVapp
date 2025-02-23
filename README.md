# CVapp

## To run locally:
- MUST USE THE LOCAL VERSION (The one sent in email)
- first run the CV_API.py file located in the backend folder
- then run the Frontend.py using this line in a cmd line that is in the correct directory: streamlit run Frontend.py --server.port 8501 --server.headless true
- Should be running in 127.0.0.0:8000/docs and localhost:8501 respectively

## To run on cloud:
- Backend located on https://cv-backend-lc0e.onrender.com
- Frontend located on https://cv-frontend-zxd1.onrender.com
- The cloud provider has a policy to shutdown innactive deployments, if this is checked after a few days it may need to be redeployed again,just send me a message and ill put it back up again


 ### Notes
 - Unfortunately i had trouble setting up the billing options with other providers (GCloud, AWS and Heroku) and i had to settle for Render, the only free cloud development tool i was able to find. This caused some issues after i upgraded the app to support more functionalites, the cloud environment runs out of memory for all the dependencies that need to be installed and i am not able to make a deployment. With this being said i am fairly confident that this version is able to be deployed on other platforms.
 - The local version works just fine.

