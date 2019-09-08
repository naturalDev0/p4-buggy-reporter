# [Buggy-Reporter](https://buggyreporter-tl.herokuapp.com/)

TGC project #4 - A bug tracker portal for users to report and creating a community where professionals can intervened the problems. The platform will allow users to login and make donations to the portal as well.

## UI/UX

### Interface
[ Enter something here ... ]

### Experience
User Stores: --> *(e.g. As a user type, I want to perform an action, so that I achieve a goal.)*
[ Enter something here ... ]

*As a user...*
1. I want to create bug requests, so that I can report a bug.
1. I want to create categories for different bug requests, so that I can categorise the requests.
1. I want to create tags for different bug requests, so that apply different tags that is suitable.
1. I want to delete bug requests, so that I can remove them when necessary.
1. I want to edit bug requests, so that I can amend them when necessary.
1. I want to make donation on the website, so that I can support the organisation when possible.
1. I want to create a profile, so that I can personalize my own account.
1. I want to create an account, so that I can view the bug requests reported by me.

## Features
 
### Existing
*Users can...*
* Feature 1 - Create bug requests
* Feature 2 - View bug requests
* Feature 3 - Edit bug requests
* Feature 4 - Make donation to the website
* Feature 5 - Create an account
* Feature 6 - Authentication - Login and Logout

### Future
*Users can...*
* Feature 1 - Delete bug requests
* Feature 2 - Search bug requests
* Feature 3 - Filter bug requests by categories
* Feature 4 - Filter bug requests by tags
* Feature 5 - View bug requests created in that user account


## Technologies Used

1. HTML5 --- *required*
1. CSS3 --- *required*
    1. Mainly for custom styling using ...
        1. IDs - Overwrite the existing
        1. Classes - 
1. JavaScript --- *required*
    1. Accompanied with Bootstrap
1. [Bootstrap 4.3.1](https://getbootstrap.com/)
1. [SQL]()
    1. Perform database querying when needed (especially checking if data has been inserted...)
1. [Python 3.6.8](https://docs.python.org/3.6/)
1. [Django](https://www.djangoproject.com/)

### Platform
1. [AWS Cloud9 - IDE](https://aws.amazon.com/cloud9/)
    1. Development use
1. [Heroku](https://www.heroku.com/)
    1. Deploy to hosting server for a live website

## Testing

*These are the tests has been done so far ...*

1. Donate form:
    1.
    1.
    1.
    1.
    1.


<hr/>

## Deployment

*[Please take note that your project environment will be different ...]*

* The website is currently hosted on Heroku, developed on AWS Cloud 9 IDE platform and the source code is stored on Github Repository. Occasionally, I would perform some lightweight code edits using Microsoft Visual Studio (VS) Code (e.g. README.md).

### Steps deployment

1. Create a new repository for your project on your local computer.
    ```
    git init .                  // initialize repo with all files
    git add .                   // add all files into local staging
    git status                  // check if any files are left out before commiting
    git commit -m "message"     // commit change with message of your files into repo
    ```
1. Add your remote git link for uploading your files onto Github later on.
    ```
    // add your remote repo link
    git remote add origin https://github.com/naturalDev0/p4-buggy-reporter.git
    ```
1. Push your files onto your remote
    ```
    // upload your files into your remote repo
    git push -u origin master
    ```

1. Should you have the interest to work the files offline, you can do so by cloning a copy.
    ```
    // Clone the selected repo offline
    git clone https://github.com/naturalDev0/p4-buggy-reporter.git
    ```

    NOTE: All commits are pushed to master branch, as currently there is no intention of creating new branches.
<br/><br/>

1. Install dependencies and folders
    ```
    sudo apt install libpq-dev python3-dev
    sudo pip3 install gunicorn
    sudo pip3 install psycopg2
    sudo pip3 install whitenoise
    ```
    1. Add Whitenoise to the '*MIDDLEWARE*' inside ***settings.py***
        ```
        MIDDLEWARE = [
            .....
            'whitenoise.middleware.WhiteNoiseMiddleware'
        ]
        ```
    2. Include the following file paths inside ***settings.py***
        ```
        STATIC_URL = '/static/'
        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
        
        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        ```
    3. Make sure not to forget the following folders as Django require them in order to run app.
        1. ***static/***
        1. ***staticfiles/***
        1. ***media/***
        1. Remove media/ from the .gitignore file temporarily. (If you have added /media inside there).

    1. Create an requirements.txt file using bash
        ```
        pip3 freeze --local > requirements.txt
        ```
    
    1. *Include the relevant .gitignore file. Make sure migrations folder are not excluded*

    1.  Put staticfiles/  and media/ inside .gitignore
    
    1. Log into heroku by typing in heroku login and pressing ENTER

    1. Create an app ( do it via the command line, don't do it via the Heroku webpage). If you opt for the command line and the push to Heroku.
        ```
        heroku create <PROJECT NAME>
        
        // Check if heroku remote has been added
        git remote -v 
        ```
    
1. Install Postgre SQL
    1. Run the following command in terminal
        ```
        heroku addons:create heroku-postgresql
        sudo pip3 install dj_database_url
        ```
    1. Check the url of the database:
        ```
        heroku config
        ```    
    1. Add the URL to the database configurations inside settings.py
        ```
        # import at the top
        import dj_database_url
        # then...
        DATABASES = {'default': dj_database_url.parse(<DATABASE_URL_FROM_HEROKU>)}
        ```
    1. Migrate your database
        ```
        python3 manage.py migrate
        ```

1. Add in environment variables
    <p>You must add all the environment variables in your .bashrc over to Heroku. There are two ways to do it - through the web dashboard, or using the bash CLI.</p>
    
    *Method 1* - Refer https://devcenter.heroku.com/articles/config-vars and look for the Dashboard section.
    
    *Method 2* - Using Bash
    <p>For example, if I have the following in my .bashrc</p>
    
    ```
    export STRIPE_PUBLISHABLE_KEY="pk_test_aaa"
    export STRIPE_SECRET_KEY="sk_test_bbb"
    export UPLOADCARE_SECRET_KEY="8057…."
    export UPLOADCARE_PUBLIC_KEY="4466..."
    ```
    1. First, make sure you are logged into Heroku, in the terminal, by typing:
        ```
        heroku login
        ```
    1. Then type into the terminal, following the examples below, to set your environment variables. Press [ENTER] at the end of each line.
        ```        
        heroku config:set STRIPE_PUBLISHABLE_KEY=pk_test_aaa
        heroku config:set STRIPE_SECRET_KEY=sk_test_bbb
        …
        ```
1. Deploying
    1. Commit the changed files
        ```
        sudo pip3 freeze --local > requirements.txt
        sudo git add .
        git commit -m "<YOUR COMMENT MESSAGE>"
        git push origin master
        ```
    2. Create the procfile:
        ```
        touch Procfile
        ```
    3. And open up the file and enter into the Procfile:
        ```
        web: gunicorn <PROJECT_FOLDER>.wsgi:application
        ```
    
    4. Add the URL of the heroku app into the ALLOWED_HOST inside ***settings.py***

    5. Add and commit, and create the superuser on the Heroku app:
        ```
        sudo git add .
        sudo git push heroku master
        heroku run python manage.py createsuperuser
        ```
1. Re-Deploying (- When necessary -)

    When do you need it? Only when you perform the following ...
    * You change any of the .py files (urls, models, views etc.)
    * You add in any new libraries via pip install
    * You make a change to the readme.md

    To redeploy:
    1. Add the changes to git
    1. Commit
    1. Push to heroku
    1. If you have made any changes to any model files, you need to make migrations and then remigrate


## Credits

### Content
* *All contents are written by me.*

### Media
* [Pexels](https://www.pexels.com/)
    1. [blurred-background-cellphone-coffee.jpg](https://www.pexels.com/photo/man-with-hand-on-temple-looking-at-laptop-842554/)
    2. [blackboard-chalkboard-communication.jpg](https://www.pexels.com/photo/blackboard-business-chalkboard-concept-355988/)
* [Google Font - Raleway](https://fonts.google.com/?selection.family=Raleway)

### Acknowledgements
*I would like to thank the following sources...*
* Trent Global College's lecturer - Paul, for his tips and advice

<br/>

*This website is for educational use only.*