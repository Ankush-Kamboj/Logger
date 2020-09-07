# Logger
Django Login&Register User App
In this application you can register user and login to see your profile. If you haven't created your profile after login you will be taken to create profile page.

## Features
* Custom Users Model in Django and it can be accessed in django admin also.
* Database - MySQL
* Register, Login, Logout
* Login is required to access Profile and create profile pages.

## Author
Ankush Kamboj

## Installation
### Prerequisities

#### 1. Install Python
Install python and python-pip. Follow the steps from the below reference document based on your Operating System. Reference: https://docs.python-guide.org/starting/installation/
#### 2. Install MySQL
Install mysql. Follow the steps form the below reference document based on your Operating System. Reference: https://dev.mysql.com/doc/refman/5.5/en/

#### 3. Setup Virtual Environment
Create a virtual environment and activate it.

#### 4. Clone git repository

    git clone "https://github.com/Ankush-Kamboj/Logger.git"

#### 5. Install requirements
	cd Logger
	pip install -r requirements.txt

#### 6. Edit project settings

    # open settings file
    settings.py

	# Edit Database configurations with your MySQL configurations.
	# Search for DATABASES section.
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': ''<database-name>,
	        'USER': '<mysql-user>',
	        'PASSWORD': '<mysql-password>',
	        'HOST': '<mysql-host>',
	        'PORT': '<mysql-port>',
	    }
	}

#### 7. Run the server
	# Make migrations
	python manage.py makemigrations
	python manage.py migrate

	# Run the server
	python manage.py runserver
  
Try opening http://localhost:8000/ and you are good to go.

### URLs
#### 1. http://localhost:8000
![Homepage](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/homepage.PNG)
#### 2. http://localhost:8000/login
![Login](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/login.PNG)
#### 3. http://localhost:8000/register
![Register](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/register.PNG)
#### 4. http://localhost:8000/logout
![Logout](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/logout.PNG)
#### 5. http://localhost:8000/createprofile
![CreateProfile](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/createprofile.PNG)
#### 6. http://localhost:8000/(After Login)
![Profile](https://github.com/Ankush-Kamboj/Logger/blob/master/screenshots/profile.PNG)
