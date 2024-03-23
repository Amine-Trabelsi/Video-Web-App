# Video Player using Django + Vue
Elevate your video streaming experience with our Django and Vue.js powered video player. 

Seamlessly combining the robustness of Django for the backend and the dynamic interactivity of Vue.js for the frontend, this project lays the foundation for a sophisticated video streaming platform.

* Django Backend: Utilize the power of Django's ORM and routing capabilities to manage user authentication, video metadata, and streaming endpoints.

* Vue.js Frontend: Enhance user engagement with Vue.js components, offering a seamless and responsive video playback experience.

* Basic Functionality: The project provides a solid starting point with essential features for video playback and management. However, it offers ample room for customization and expansion to meet your specific requirements.


### Better Practices to keep in mind
* As your project scales and video storage needs increase, cloud storage offers a more scalable and performant solution.

* Spend some time on the frontend to make an unforgettable user experience

* Customize the controls of the vue-plyr video player according to your preferences.

### Options
* Add different resolutions support.

* Add other fields to the video Model (e.g., genre, ratings, ...)

* Security: Implement proper user authentication and authorization mechanisms in your Django REST Framework API to control access to video URLs.

* Video Transcoding (Optional): Consider using a service like Amazon Elastic Transcoder or FFmpeg to transcode uploaded videos into various formats for optimal playback across different devices/browsers.

# Executing the Code
To evaluate the code, it's necessary to run both the backend and frontend concurrently.
## Running the Backend

### Create virtual environment (optional)
Note: this is different based on the operating system.
```
python -m venv env
env\scripts\activate.bat
```

### Install requirements
```
pip install -r requirements.txt
```

### Compile
```
python backend\manage.py runserver
```

## Running the Frontend

### Project setup
```
npm install
```

#### Compiles and hot-reloads for development
```
npm run serve
```

#### Compiles and minifies for production
```
npm run build
```

#### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

## Database options

1) Set Up the Cloud Database:
Create a new database instance on a chosen cloud Database provider. Configure the database settings such as the database engine (e.g., MySQL, PostgreSQL, MongoDB), storage capacity, and access control.
Database Configuration:


2) Update Backend Configuration:
Update the backend application configuration to use the connection details of the cloud database.


3) Testing and Debugging:
Test the database connection from your Python backend application to ensure that it can read and write data to the cloud database successfully. Debug any connection issues or errors that may arise during testing.

4) Security Considerations:
Implement security best practices such as encrypting database connections (e.g., using SSL/TLS), enforcing access controls and authentication mechanisms, and regularly updating database credentials.

5) Monitoring and Maintenance:
Set up monitoring and logging for your cloud database to track performance metrics, monitor for anomalies, and troubleshoot any issues that may arise. Regularly perform maintenance tasks such as database backups, updates, and optimizations to ensure the reliability and performance of your database.


## Deployment Options

1) Deploy Both Applications Together:
Package the Vue.js frontend and Python backend into a single deployment unit. This can be achieved by bundling both applications into a single Docker container or deploying them as separate services on the same server.

2) Expose Only Frontend to the Public:
Configure a web server (e.g., Nginx or Apache) to proxy requests to the Vue.js frontend and serve it to the public. Ensure that only the frontend routes are exposed externally.
Internal Access to Backend:
Configure a web server to forward requests to the backend API to a different internal port or path that is not accessible from the public internet. This ensures that the backend API remains private and accessible only internally.

3) Secure Backend Access:
Implement additional security measures such as IP whitelisting, VPN access, or authentication mechanisms to restrict access to the backend API. This ensures that only authorized users or systems can access the backend.

4) Deployment Considerations:
Depending on the choice of deployment platform (e.g., cloud provider, container orchestration platform), ensure that network configurations are set up to allow internal communication between the frontend and backend components while restricting external access to the backend.

5) Testing and Monitoring:
Test the deployed applications to ensure that frontend-backend communication is functioning correctly in the production environment.
Set up monitoring and logging for both frontend and backend to track performance, errors, and user interactions.
