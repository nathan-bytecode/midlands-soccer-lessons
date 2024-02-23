# Midlands Soccer Lessons

![Am I responsive](/static/images/readme/am%20i%20responsive.png)

This project is a website for soccer lessons based in the midlands of Ireland. The user's aim is to be able to create an account, login, edit and delete as needed. The user should also be able to view, book and manage soccer training courses with the option of selecting from three distinct venues.

This project is aimed to target ages 7-21 boys and 9-21 girls who are interested in developing their soccer skills.

## - Nathan Nicholson

## [Live site](https://8000-nathanbytec-midlandssoc-zjji9p2macp.ws-eu108.gitpod.io/)

## Table of Content

1. UX
2. Agile Development
3. Features
4. Features Left to Implement
5. Technology used
6. Testing
7. Bugs
8. Deployment
9. Credits
10. Acknowledgements

### UX

#### Pre-project Planning
![Database structure](/static/images/readme/UX%20-%20Preproject%20Planning.png)

* When I decided on my initial idea of Midlands Soccer Lessons I knew I needed to understand what  type of data I would need to store and the relationships between them.
* I created the above diagram on lucidchart.
* As of now when the project is finished the only field not implemented is the confirmation status in the Booking model as I ran out of time.

### UX Design
#### Overview
As Midlands Soccer Lessons is a website that targets parents who have kids from the ages 7 for boys and 9 for girls upwards, I wanted to design the website with a bright welcoming feel. For each course available a photo was carefully selected to attract interest. 
The main goal of the website is to allow users to view some photos of the venue, see what the courses have to offer, choose from the different options and then the user can create an account and use it to make bookings for soccer lessons.

#### Wireframes
As displayed below, this wireframe was a great guide for me to design the home landing page.

![Home page landing](/static/images/readme/Wireframe%20-%20home%20landing.png)


Here its easy to see how I drew inspiration from this wireframe but the project's profile page itself is not exactly as planned.
I've not included the following: user profile image, user's display of a phone number, booking status and the opttion to delete user account as I ran out of time.

![Profile page](/static/images/readme/Profile%20page%20wireframe.png)


### Agile Development
### Agile Overview
This project was started alongside a GitHub Projects Page to track and manage the expected workload ahead. The aim was to set out my expected workload, list the epics and then break them down into user stories or bite sized tasks to work towards and ultimately finish the site in good time.

To see Kanban please [click here](https://github.com/users/nathan-bytecode/projects/9).

### User Stories
The user stories tool served as a checklist throughout this project and enabled me to keep on the right track. User stories #8 and #9 are still in the To Do list as I ran out of time to implement.

1. [USER STORY: Deploy Website#1](https://github.com/users/nathan-bytecode/projects/9/views/1?pane=issue&itemId=49518992)
2. [USER STORY: Admin Panel#2](https://github.com/users/nathan-bytecode/projects/9?pane=issue&itemId=49518994)
3. [USER STORY: Create an account (CRUD)#3](https://github.com/users/nathan-bytecode/projects/9/views/1?pane=issue&itemId=49518995)
4. [USER STORY: Base Template#4](https://github.com/users/nathan-bytecode/projects/9/views/1?pane=issue&itemId=49518996)
5. [USER STORY: Make a Booking#5](https://github.com/users/nathan-bytecode/projects/9/views/1?pane=issue&itemId=49518997)
6. [USER STORY: Courses#7](https://github.com/users/nathan-bytecode/projects/9/views/1?pane=issue&itemId=49518998)
7. [USER STORY: Edit Profile (CRUD)#8](https://github.com/users/nathan-bytecode/projects/9?pane=issue&itemId=49518999)
8. [USER STORY: Delete Profile (CRUD)#9](https://github.com/users/nathan-bytecode/projects/9?pane=issue&itemId=49519001)

### Features
#### User based features
* Users can create an account (Create).
* Users can log into their account.
* Users can log out of their account.
* Users can make a booking through the booking form (Create).
* Users can access their profile page and view their bookings (Read).
* Users can edit their booking (Update).
* Users can delete bookings from their profile page (Delete).

#### Website features
##### Home page
* Book today link to give user quick access to booking form.
* Website's logo is link to reload home page.
* Dynamic head bar informs user if they are logged in.
* If they user chooses to learn more about the available courses they can click the link to take them to the courses page.

##### Bookings page
* Gives user access to a booking form
* Prevents booking form access if the user is not registered or logged in.

##### Courses page
* Displays more information about available courses for user to select from.

##### Profile page
* If the user is not logged in they are advised to in order to make a booking.
* Upon logged in, the user can use the profile page to view, edit, delete their bookings.

### Features Left to Implement
* Delete account. 
* Update account details.
* Booking confirmation status.
* Notify user of booking decline or acceptance.
* Narrow the time selection down to more reasonable choice when making a booking.
* Add a calendar widget that displays dates already full and what dates are available.

### Technologies Used

#### Html
Used to structure my webpages and the base templating language.

#### CSS
Custom CSS was written on large chunks of this site to make it as close to the wireframes as I felt it needed to be.

#### JavaScript
Used to add timeout function for messages as well as to enable the menu on index.html.

#### Python
Used for the logic in this project.

#### Django
Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

#### Font Awesome
Icon library used for the profile and admin panel section.

#### Bootstrap 5
Used as the base front end framework to work alongside Django.

#### GitHub
Used to store the code for this project & for the projects Kanban board used to complete it.

#### Heroku
Used to host and deploy this project.

#### ElephantSQL - PostgreSQL
ElephantSQL - PostgreSQL was used as the database for this project during development and in production.

#### Cloudinary
Used to host the static files for this project including user profile images.

#### Git
Used for version control throughout the project and to ensure a good clean record of work done was maintained.

### Testing

For this project I used manual testing by creating a table using Google Sheets.

#### Account Registration tests
![Account registration - create](/static/images/readme/User%20-%20Create.png)

#### Security tests
![Security tests](/static/images/readme/Security%20tests.png)

#### Booking tests
![Booking tests](/static/images/readme/Booking%20tests.png)

#### CRUD tests
![Read, update, delete tests](/static/images/readme/User%20-%20Read,%20Update,%20Delete.png)

#### HTML W3 Validation
![HTML W3 Validation](/static/images/readme/w3%20html%20validator%20complete.png)

#### CSS Validation
![CSS Validation](/static/images/readme/jigsaw%20validator%20for%20css%20complete.png)

### Bugs
Throughout my project right until the end I could not find why the Social Media heading was underline. To try bring a better UX I even underlined the Contact heading beside it to make it seem on purpose. Only after running my website through the HTML checker did I realise I was missing the letter 'l' for the '<ul>' element. 
![Social Media heading underline bug](/static/images/readme/bug1%20-%20Social%20Meida%20underline.png)

### Deployment
To deploy the project through Heroku I followed these steps:

* Sign up / Log in to Heroku.
* From the main Heroku Dashboard page select 'New' and then 'Create New App'.
* Give the project a name - I decided on the midlands-soccer-lessons and selected EU as that is the closes region to me.
* After this you select select create app.
* Navigate to the resources tab.
* Add the database to the app, in the add-ons section search for 'Heroku Postgres', select the package that appears and add 'Heroku Postgres' as the database.
* Click on the setting tab.
* Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.

--- 

* Inside the Django app repository create a new file called env.py.
* Within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from Heroku.
* The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here".
* Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here".
* Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE.
* In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url.
* Insert the line if os.path.isfile("env.py"): import env.
* Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY').
* Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
* In the terminal migrate the models over to the new database connection

---

* Navigate in a browser to cloudinary, log in, or create an account and log in.
* From the dashboard - copy the CLOUDINARY_URL to the clipboard.
* In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here".
* In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars.
* Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
this key value pair must be removed prior to final deployment.
* Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.

---

* In the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
* Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
* Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]

---

* Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com.
* In your code editor, create three new top level folders, media, static, templates
* Create a new file on the top level directory - Procfile
 within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi

---

* In the terminal, add the changed files, commit and push to GitHub
* In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
* Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

### Credits

#### Code Institute
Thanks to Code Institute's new Django module I was able to go through the walkthrough and compare as needed.

#### Tony Teaches Tech
I've came across this YouTube Tony who has very short breakdowns of CRUD functionality and found him a reliable resource during this project.

### Acknowledgements

#### John Dickson
When I seemed to hit a hall in connecting my database model to display via the user's frontend actions, I sent out a plea for help in Slack's PP4 channel. To my suprise, John a former student reached out to me and kindly gave me his time to explain where my code was off and guide me as needed. As it was a race against time, I truly feel like I wouldn't have succeded without his help. Thank you John.