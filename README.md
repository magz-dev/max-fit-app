# Sport Style Hub

[View the life project here.](https://sportstylehub-73c15c72aa03.herokuapp.com/)

![image](https://github.com/magz-dev/sport-style-hub/assets/97630146/71824cdd-c0d1-4e4f-b78e-cb2b736b8119)

- - -
## User Experience

###  User Stories

#### As a first time user:
  -  I want to understand the purpose of the site immediately upon entering.
  -  I want to be able to find what I need easily and for the navigation to be easy to follow and intuitive.
  -  I want to be able to view the site on a range of device sizes.
  -  I want to be able to find promotional coupons.
  -  I want to get feedback when interacting with the site.

#### As a frequent user:
  -  I want to be able to browse products easily, with options to filter and search to find things I need.
  -  I want to be able to find out information about products.
  -  I want to see ratings or reviews of a product to know more about the quality and whether it is right for me.
  -  I want to be able to shop for multiple items at once, from across the site.
  -  I want to be able to edit my shopping bag.
  -  I want to know what I will be charged for delivery.
  -  I want to be able to return to the main site without having to use the browser buttons.

#### As a user with an account:
  -  I want my account to be easy to set up.
  -  I want my payment and order to be fully secure and trustworthy.
  -  I want to be able to apply a discount code to my shopping bag.
  -  I want to see my order history.
  -  I want to be able to update and save my personal information.
  -  I want to leave reviews of products I have purchased.
  -  I want to be able to edit my reviews.
  -  I do not want admins or other customers to be able to change my reviews.

#### As an admin of the site:
  -  I want to be able to add, remove and edit products.
  -  I want all the admin controls to be quick and easy to find and use.

- - -

## Design

### Typography

Google Fonts was used for the following fonts:

* Permanent Marker is used for headings on the site. It is a cursive font.

### Media
* Favicon and logo icon is from [Icons8](https://icons8.com/).
* Background photo is from [Adobe Stock](https://stock.adobe.com/uk/).
* Products are from [JD Sports](https://www.jdsports.co.uk/).

### Wireframes

[Wireframes](docs/wireframes) were created for mobile, tablet and desktop.

- - -

## Technologies Used

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
* SQlite3 -  Used as the built in Django database for development.
* ElephanSQL - Postgres-based database host. Used to host the database for the live production app.
* Djando Countries - Django application that provides country choices for forms.
* [Am I Responsive](https://ui.dev/amiresponsive) - To create the responsive images of the site on a variety of device sizes.
* [Balsamiq](https://balsamiq.com/) - Used to create wireframes.
* [Google Dev Tools](https://developer.chrome.com/docs/devtools/) - To troubleshoot, test features and solve issues with responsiveness and styling.
* [Pip](https://pypi.org/project/pip/) - A tool for installing Python packages.

### Languages Used
* HTML5
* CSS3
* Javascript
* Python

### Stripe

[Stripe](https://stripe.com/gb) has been used in the project to implement the payment system.

Stripe for the website is currently in developer mode, which allows us to be able to process test payments to check the function of the site.

- - -

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

#### Set up AWS hosting for static and media files
! NOTE: These instructions are for setting up AWS hosting as of 5/1/23 - these may change slightly in future versions of AWS.
1. Sign up or login to your aws amazon account on the top right by using the manage my account button and then navigate to S3 to create a new bucket.

2. The bucket will be used to store our files, so it is a good idea to name this bucket the same as your project. Select the region closest to you. In the object ownership section we need to select ACLs enabled and then select bucket owner preferred. In the block public access section uncheck the block public access box. You will then need to tick the acknowledge button to make the bucket public. Click create bucket.

3. Click the bucket you've just created and then select the properties tab at the top of the page. Find the static web hosting section and choose enable static web hosting, host a static website and enter index.html and error.html for the index and error documents (these won't actually be used.)

4. Open the permissions tab and copy the ARN (amazon resource name). Navigate to the bucket policy section click edit and select policy generator. The policy type will be S3 bucket policy, we want to allow all principles by adding * to the input and the actions will be get object. Paste the ARN we copied from the last page into the ARN input and then click add statement. Click generate policy and copy the policy that displays in a new pop up. Paste this policy into the bucket policy editor and make the following changes: Add a /* at the end of the resource value. Click save.

5. Next we need to edit the the cross-origin resource sharing (CORS). Paste in the following text:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

6. Now we need to edit the access control list (ACL) section. Click edit and enable list for everyone(public access) and accept the warning box.

#### Creating AWS groups, policies and users
1. Click the services icon on the top right of the page and navigate to IAM - manage access to AWS services. On the left hand navigation menu click user groups and then click the create group button in the top right. This will create the group that our user will be placed in.
2. Choose a name for your group - for example manage-seaside-sewing, and click the create policy button on the right. This will open a new page.
3. Click on the JSON tab and then click the link for import managed policy on the top right of the page.
4. Search for S3 and select the one called AmazonS3FullAccess, then click import.
5. We need to make a change to the resources, we need to make resources an array and then change the value for resources. Instead of a * which allows all access, we want to paste in our ARN. followed by a comma, and then paste the ARN in again on the next line with /* at the end. This allows all actions on our bucket, and all the resources in it.
6. Click the next: tags button and then the next:review .
7. Give the policy a name and description (e.g. seaside-sewing-policy | Access to S3 bucket for seaside sewing static files.) Click the create policy button.
8. Now we need to atach the policy we just created. On the left hand navigation menu click user groups, select the group and go to the permissions tab. Click the add permissions button on the right and choose attach policies from the dropdown.
9. Select the policy you just created and then click add permissions at the bottom.
10. Now we'll create a user for the group by clicking on the user link in the left hand navigation menu, clicking the add users button on the top right and giving our user a username (e.g. seaside-sewing-staticfiles-user). Select programmatic access and then click the next: permissions button.
11. Add the user to the group you just created and then click next:tags button, next:review button and then create user button.
12. You will now need to download the CSV file as this contains the user access key and secret access key that we need to insert into the Heroku config vars. Make sure you download the CSV now as you won't be able to access it again.

#### Connecting Django to our S3 bucket
1. Install boto3 and django storages and freeze them to the requirements.txt file.
   ```
   pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
2. Add `storages` to the installed apps in settings.py
3. Add the following code in settings.py to use our bucket if we are using the deployed site:
```
if 'USE_AWS' in os.environ:
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=9460800',
    }
    
    AWS_STORAGE_BUCKET_NAME = 'enter your bucket name here'
    AWS_S3_REGION_NAME = 'enter the region you selected here'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    ```
    
4. In Heroku we can now add these keys to our config vars.
5. Remove the DISABLE_COLLECTSTATIC variable.
6. Create a file called custom_storages.py in the root and import settings and S3Botot3Storage. Create a custom class for static files and one for media files. These will tell the app the location to store static and media files.
7. Add the following to settings.py to let the app know where to store static and media files, and to override the static and media URLs in production.
```
STATICFILES_STORAGE = 'custom_storages.StaticStorage'
STATICFILES_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
MEDIAFILES_LOCATION = 'media'

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
8. Save, add, commit and push these changes to make a deployment to Heroku. In the build log you should be able to see that the static files were collected, and if we check our S3 bucket we can see the static folder which has all the static files in it.
9. Navigate to S3 and open your bucket. We now want to create a new file to hold all the media files for our site. We can do this by clicking the create folder button on the top right and naming the folder media.

#### Setting up Stripe
1. We now need to add our Stripe keys to our config vars in Heroku to keep these out of our code and keep them private. Log into Stripe, click developers and then API keys.
2. Create 2 new variables in Heroku's config vars - for the publishable key (STRIPE_PUBLIC_KEY) and the secret key (STRIPE_SECRET_KEY) and paste the values in from the Stripe page.
3. Now we need to add the WebHook endpoint for the deployed site. Navigate to the WebHooks link in the left hand menu and click add endpoint button.
4. Add the URL for our deployed sites WebHook, give it a description and then click the add events button and select all events. Click Create endpoint.
5. Now we can add the WebHook signing secret to our Heroku config variables as STRIPE_WH_SECRET.
6. In settings.py:
   
```
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY', '')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', '')
STRIPE_WH_SECRET = os.getenv('STRIPE_WH_SECRET', '')
```

### Local Development

#### How to Fork
To fork the repository:

1. Log in (or sign up) to GitHub.
2. Go to the repository for this project, seaside-sewing.
3. Click on the fork button in the top right of the page.

### How to Clone

#### To clone the repository:

1. Log in (or sign up) to GitHub
2. Go to the repository for this project, seaside-sewing.
3. Click the Code button, select whether you would like to clone with HTTPS, SSH or the GitHub CLI and copy the link given.
4. Open the terminal in your chosen IDE and change the current working directory to the location you would like to use for the cloned repository.
5. Type the following command into the terminal git clone followed by the link you copied in step 3.
6. Set up a virtual environment (this step is not required if you are using the Code Institute template and have opened the repository in GitPod as this will have been set up for you).
7. Install the packages from the requirements.txt file by running the following command in the terminal:    
```
pip3 install -r requirements.txt
```

- - -

## Testing

Please refer to the [TESTING.md](TESTING.md) file for all testing performed.

- - -

## Credits

### Code

* Bootstrap 4 - Bootstrap Library used throughout the project to add style. Bootstrap 4 was also used to make the site responsive by using the Bootstrap Grid System.
* Code Institute's learning content.
* Code Institute's walkthrough project for Boutique Ado.
* [W3Schools](https://www.w3schools.com/default.asp)
* Stack Overflow
* [Javascript tutorial](https://www.youtube.com/watch?v=fbXHOVp_L_4)
* [Django Tutorial](https://www.youtube.com/watch?v=gsW5gYTNi34)
* Slack community
* [Coupon model idea](https://github.com/JoeyyScott/gamer-supplies)

### Acknowledgements

* Tutor support from the Code Institute.
* My Mentor for helpful comments and supportive feedback.
* Slack community for project assistance.
* Kera Cudmore for readme examples.
  
