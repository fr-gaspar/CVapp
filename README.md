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
 - The app is able to perform object detection and image classification. I started by implementing only the object detection and then built the image classification on top of it. After i added the image classification cloud deployment stopped working properly as explained in next topic.
 - Unfortunately i had trouble setting up the billing options with other providers (GCloud, AWS and Heroku) and i had to settle for Render, the only free cloud development tool i was able to find. This caused some issues after i upgraded the app to support more functionalites, the cloud environment runs out of memory for all the dependencies that need to be installed and i am not able to make a deployment. With this being said i am fairly confident that this version is able to be deployed on other platforms.
 - The local version works just fine.
 - For both functionalities the user is able to chose which objects to detect and look for in the images (they are hardcoded though, maybe having a selection of objects on the frontend for the user to chose could be interesting, but once i started adding them the UI became cluttered)
 - The image classification has a customizable confidence threshold for the detection. Lower values will be able to return more objects, though with more false positives, while a higher value will return fewer objects but with higher accuracy

