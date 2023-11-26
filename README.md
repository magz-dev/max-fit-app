# Sport Style Hub

### Frameworks, Libraries & Programs Used
* Bootstrap 4.6 - The framework for the website. Additional CSS styling was also implemented in style.css.
* Git -  For version control.
* GitHub -  To save and store the files for the website.
* Google Dev Tools - To troubleshoot and test features, solve issues with responsiveness and styling.
* Django - Python-based Web Framework.
* AllAuth - Integrated Django authentication & sign in.
* JQuery - JavaScript library for making JavaScript quicker and easier to write.
* Font Awesome - Used to add icons to the site.
* Pillow - Python Imaging Library.
* Psycopg2 - Postgres adaptor to allow smooth communication between the backend and the database.
* Stripe - Stripe package part of the Stripe ecosystem to manage secure online payments.
* SQlite -  Used as the built in Django database for development.
* ElephanSQL - Postgres-based database host. Used to host the database for the live production app.
* Djando Countries - Django application that provides country choices for forms.
  
### Languages Used
* HTML5
* CSS3
* Javascript
* Python

### Media
* Favicon, logo and delivery icon is from [Icons8](https://icons8.com/).
* Background photo is from [Adobe Stock](https://stock.adobe.com/uk/)

## Deployment and Local Development

### Deployment 
The project is deployed using Heroku. To deploy the project:
#### Create the Live Database
We have been using the sqlite3 database in development, however this is only available for use in development so we will need to create a new external database which can be accessed by Heroku.

1. Go to the ElephantSQL dashboard and click the create new instance button on the top right.
2. Name the plan (your project name is a good choice), select tiny turtle plan (this is the free plan) and choose the region that is closest to you then click the review button.
3. Check the details are all correct and then click create instance in the bottom right.
4. Go to the dashboard and select the database just created.
5. Copy the URL (you can click the clipboard icon to copy)

#### Heroku app setup

1. From the Heroku dashboard, click the new button in the top right corner and select create new app.
2. Give your app a name (this must be unique), select the region that is closest to you and then click the create app button bottom left.
3. Open the settings tab and create a new config var of DATABASE_URL and paste the database URL you copied from elephantSQL into the value (the value should not have quotation marks around it).

#### Preparation for deployment in GitPod
1. Install dj_database_url and psycopg2 (they are both needed for connecting to the external database you've just set up):
   
```
pip3 install dj_database_url==0.5.0 psycopg2
```
2. Update your requirements.txt file with the packages just installed:
   
```
pip3 freeze > requirements.txt
```

3. In settings.py underneath import os, add `import dj_database_url`
4. Find the section for DATABASES and comment out the code. Add the following code below the commented out database block, and use the URL copied from elephantSQL for the value:
   
(NOTE! don't delete the original section, as this is a temporary step whilst we connect the external database. Make sure you don't push this value to GitHub - this value should not be saved to GitHub, it will be added to the Heroku config vars in a later step, this is temporary to allow us to migrate our models to the external database)
```
DATABASES = {
    'default': dj_database_url.parse('paste-elephantsql-db-url-here')
}

```
5. In the terminal, run the show migrations command to confirm connection to the external database:
   
```
python3 manage.py runserver
```

6. If you have connected the database correctly you will see a list of migrations that are unchecked. You can now run migrations to migrate the models to the new database:
```
python3 manage.py migrate
```

7. Create a superuser for the new database. Input a username, email and password when directed.
```
python3 manage.py createsuperuser
```

8. You should now be able to go to the browser tab on the left of the page in elephantsql, click the table queries button and see the user you've just created by selecting the auth_user table.
9. We can now add an if/else statement for the databases in settings.py, so we use the development database while in development (the code we commented out) - and the external database on the live site (note the change where the db URL was is now a variable we will use in Heroku):
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
      'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
      }
    }
```

10. Install gunicorn which will act as our webserver and freeze this to the requirements.txt file:
```
pip3 install gunicorn
pip3 freeze > requirements.txt
```

11. Create a Procfile in the root directory. This tells Heroku to create a web dyno which runs gunicorn and serves our django app. Add the following to the file (making sure not to leave any blank lines underneath):
```
web: gunicorn seaside_sewing.wsgi:application
```

12. Log into the Heroku CLI in the terminal and then run the following command to disable collectstatic. This command tells Heroku not to collect static files when we deploy:
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app heroku-app-name-here
```

13. We will also need to add the Heroku app and localhost (which will allow GitPod to still work) to ALLOWED_HOSTS = [] in settings.py:
```
ALLOWED_HOSTS = ['{heroku deployed site URL here}', 'localhost' ]
```

14. Save, add, commit and push the changes to GitHub. You can then also initialize the Heroku git remote in the terminal and push to Heroku with:
```
heroku git:remote -a {app name here}
git push heroku master
```

15. You should now be able to see the deployed site (without any static files as we haven't set these up yet).
16. To enable automatic deploys on Heroku, go to the deploy tab and click the connect to GitHub button in the deployment method section. Search for the projects repository and then click connect. Click enable automatic deploys at the bottom of the page.


#### Generate a SECRET KEY & Updating Debug
1. Django automatically sets a secret key when you create your project, however we shouldn't use this default key in our deployed version, as it leaves our site vulnerable. We can use a random key generator to create a new SECRET_KEY which we can then add to our Heroku config vars which will then keep the key protected.

2. Django Secret Key Generator is an example of a site we could use to create our secret key. Create a new key and copy the value.
3. In Heroku settings create a new config var with a key of SECRET_KEY. The value will be the secret key we just created. Click add.
4. In settings.py we can now update the SECRET_KEY variable, asking it to get the secret key from the environment, or use an empty string in development:
```
SECRET_KEY = os.environ.get('SECRET_KEY', ' ')
```

5. We can now adjust the `DEBUG` variable to only set DEBUG as true if in development:
```
DEBUG = 'DEVELOPMENT' in os.environ
```

6. Save, add, commit and push these changes.

## Credits

### Code
* Bootstrap 4 - Bootstrap Library used throughout the project to add style. Bootstrap 4 was also used to make the site responsive by using the Bootstrap Grid System.
* Code Institute's learning content.
* [W3Schools](https://www.w3schools.com/default.asp)
* Stack Overflow
* [Javascript tutorial](https://www.youtube.com/watch?v=fbXHOVp_L_4)

### Acknowledgements
* Tutor support from the Code Institute.
* My Mentor for helpful comments and supportive feedback.
* Slack community for project assistance.
  
