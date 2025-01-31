<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">HNG Stage One Task for Backend Track</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> An API that returns customs json data that contains my email, this github repo and dateime
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

I built a Django REST Framework (DRF) API that returns a JSON response containing my email, the project's GitHub URL, and the current datetime in ISO 8601 format. To achieve this, I used Django’s JsonResponse to structure the output dynamically. I then deployed the API on Vercel, utilizing a vercel.json configuration file to specify the build settings and enable CORS for all origins. Setting up the deployment involved configuring a Python runtime, ensuring all dependencies were included in a requirements.txt file, and linking the project to Vercel for seamless automatic deployments from GitHub. To make the API accessible from any frontend or external client, I explicitly enabled CORS in the vercel.json file, allowing cross-origin requests without restrictions. After deployment, I tested the API using tools like Postman and browser-based API clients to confirm it returned the expected JSON response.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

Step 1: Clone the Repository

        git clone project_repo
        cd project_folder


Step 2: Create a Virtual Environment
        # Create a virtual environment
        python -m venv venv  

        # Activate the virtual environment
        # On Windows
        venv\Scripts\activate  

        # On macOS/Linux
        source venv/bin/activate  



### Installing

pip install -r requirements.txt  


## 🔧 Configure Django Settings

      INSTALLED_APPS = [
          'rest_framework',
          'corsheaders',  # If CORS is required
          'your_app_name',
      ]

      MIDDLEWARE = [
          'corsheaders.middleware.CorsMiddleware',  # Enable CORS if needed
          'django.middleware.common.CommonMiddleware',
      ]

  # Allow all origins (Modify for security in production)
  CORS_ALLOW_ALL_ORIGINS = True


### Apply Migrations

python manage.py migrate  


## 🎈 Usage <a name="usage"></a>

Use Postman, a browser, or curl to send a request and check the response:

curl http://127.0.0.1:8000/

## Response 
  {
  "email": "israelshedrack913@gmail.com",
  "github": "https://github.com/Asuraking913/HNG-backend-track",
  "datetime": "date-time"
  }



## 🚀 Deployment <a name = "deployment">Vercel</a>

Add additional notes about how to deploy this on a live system.

## ⛏️ Built Using <a name = "built_using">Python's Django's Rest Framework</a>
##  Built Using <a name href="https://hng.tech/hire/python-developers">HNG Back Link</a>


## ✍️ Authors <a name = "authors">Israel Shedrack</a>

- [@kylelobo](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.


