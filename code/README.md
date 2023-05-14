# Tascii
Prototype for the Tascii web app

## Configuring the project
1. Install the required dependencies with

    ```pip install -r requirements.txt```
    

2. Run script to host local server using Django

    ```python manage.py runserver```

3. Open a browser and view the locally hosted application

## About the Project
This web application is built on top of Django's backend framework. We used this framework to manage data for users and posts. The `tascii_prototype` directory contains mostly boilerplate to set up the project, and it also contains the base template html file that all other templates extend. Static files are collected in the `static` directory. Most of the code for the application is stored in the `feed` directory. This directory contains the forms, models, views, and HTML templates that allow the site to function.

Django was extremely helpful throughout the development process as it allowed us to work in data from sqlite relatively seamlessly. Views in Django allowed us to query our database and dynamically render HTML templates. 

## More Info

To visit the live web application, [Click Here](https://calm-plateau-71093.herokuapp.com/)

You can learn more about the project in our [Github Repo](https://github.com/alexracape/tascii)
