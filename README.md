# ms3-crew-dictionary
Cruise Ship Crew have their own language and as part of my Milestone 3 project I'm creating a dictionary of ship related terms and crew language.

Since working on a cruise ship I tried to find a resource where I can remember the words and terminology I used onboard with my fellow crew memebers. As we all know, any language that is not used is lost. I did not want to lose this language so I developed a dictionary where I can store all the words I used while working on ships. 
I also hope to release this website once it is graded for the milestone project and after a few more fixes which need to be done and those are referenced in the readme below. 

# UX

![Am I responsive image](readme_img/amiresponsive_cruise_ship_crew_dictionary.jpg "Responsive design for Cruise Ship Crew Dictionary")

The main focus of this dictionary are the words and definitions submitted by users. For this reason, the landing page allows anyone, whether registered or unregistered to browse the list of words in the dictionary. 
The design is clean with few distractions to alow for focus to the words themselves. The main dictionary page is paginated to prevent endless scrolling as more words are added and features a search bar where users can search for words or definitions.
When landing on the first page, users can navigate to the "About" page which explains the purpose of the dictionary, users can register an account or log in if they already have an account. The design of the page is minimalist and simple as the whole purpose of the site is to allow users to browse and/or add words to the dictionary. 

## General
The Cruise Ship Crew Dictionary is a simple dictionary designed in a minimalist style. The main elements of the page are the navigation bar at the top of the page, the main body where the words and definitions are displayed and the footer. Users are able to browse the dictionary and search for words and definitions without registering or logging in. For those who would like to contribute to the dictionary, they have the option to register an account in order to submit new words. When a user logs in, they are redirected to a user dashboard where they can see all of the words they have submitted separated into those which have been approved by an editor or administrator, and those words which are pending approval. Overall, the website follows a similar design pattern on all pages which was achieved using bootstrap as the front end framework. 

## User Stories
- As a user I want to find out the meaning of a word
  - The dictionary focuses on words and their definitions on the main page. Users can visit the dictionary and find the word and definition. 

- As a user I want to quickly search for a word
  - The dictionary has a built in search function where users can search for specific words or terms in definitions.

- As a user I want to contribute to the dictionary
  - Users can register for an account and add words and definitions

- As a user I want to edit words already submitted
  - Users do not have the right to edit words, however, users can be made into editors by the administrator and then have the ability to edit

- As an editor I want to control what users submit
  - Any submitted word must be approved by an editor or administrator before it is published in the dictionary. 

## Wireframes
The wireframes were created at the beginning and throughout the project to aid with the front end design. Below are links to the original designs for both desktop and mobile. 

[Dictionary Home Page](wireframes/home_page.png "Desktop and Mobile - Home Page")

[Log In Page](wireframes/log_in_page.png "Desktop and Mobile - Log In Page")

[Register Page](wireframes/register_page.png "Desktop and Mobile - Register Page")

[User Dashboard](wireframes/user_dashboard.png "Desktop and Mobile - User Dashboard")

[Editor Dashboard](wireframes/editor_dashboard.png "Desktop and Mobile - Editor Dashboard")

[Admin Panel](wireframes/admin_panel.png "Desktop and Mobile - Admin Panel")


# Features

## Dictionary
The dictionary is set as the main and landing page of the website. When a visitor navigates to the website they will see the dictionary. The dictionary consists of the navigation bar on the top, a title, a search bar, words and definitions and a footer element. The main parts of the dictionary are the search bar and the word cards which are displayed underneath. Visitors can search for specific words or terms in the definitions or they can browse the list of words. The list of words is paginated and each page will show 5 word cards.

## Navigation

The navigation bar at the top of the page has the page title and logo aligned to the left side and the links aligned to the right side. The links displyed on the navigation bar change depending on the log in status of the user. If a visitor is not logged in, they will see a link for the home page, the about page, the register page and the log in page. 

If a user is logged in, they do not see the register and log in page links, but instead see a "User Tools" dropdown menu. 
In the user tools menu, logged in users can see their profile dashboard, they can submit a new word, change their password and log out. 
## Footer
The footer is standard across all pages on the website and it shows the mission statement for the website, a contact link which links to a contact page (The contact page is not set up to work), a sitemap which is currently dissabled and the about page. There is also a copyright symbol at the very bottom. 

## About
The about page provides information about the dictionary and the reason why it was created.

## Register
The register page offers visitors the posiblity to register to become users and contribute to the dictionary. 
The visitor needs to select a username and password. Form validation is in place to make sure the username is not shorter than 5 characters. Another form validation rule is to make sure the user inputs the same password twice to avoid any typos. If the passwords don't match, the user will be prompted to correct it. 
If the username the user choses is already taken, the application will inform the user to choose another username.
If the user on this page already has an account, there is a link underneath the submit button to take them to the log in page. 

## Log In
Users who have an account can submit their username and password to log into their account. 
If a visitor does not have an account, a link at the bottom of the form will take them to the registration page. 
Once the user enters their username and password and logs in, they will be taken to their user dashboard. 


## User Tools
When a user logs in, the "Register" and "Log In" links on the navigation bar will change to a "User Tools" dropdown menu. 
In the user tools, the user can access their dashboard, submit a new word to the dictionary, change their password and log out. 
The user tools were put into a dropdown menu as a design decition to not clutter the navigation bar, especially no mobile devices. 
## Profile Dashboard
When a user logs into their account, they will be taken directly to the user dashboard. Depending on the user type, they will see a different dashboard. 
If a regular user logs in, they will see the page title as "[username] Dashboard". Underneath the title is a button to submit a new word to the dictionary and underneath that is an accordion with two sections. The first section is a list of all words the user has submitted and which were approved. The second section are all words that the user has submitted which are waiting to be approved by an editor or admin. 

Editors see everything a user sees, but they have an additional section on the top of the accordion with a list of words waiting for approval. 

Administrators see everything the editor sees, however, next to the submit a word button, administrators will see a button to change user status. 
## Submit Word
All registered users, editors and administrators can submit a new word. 
Submitting a new word is done through a form which has the following elements: 
- Word - which word is being defined
- Type - what is the word type (noun, verb, adjective)
- Definition - what is the definition of the word?
- Use in sentence - how to use the word in a sentence

Users then have a choice to submit their word or to cancel and return to the dashboard. 
## Change Password
If a user wishes to change their password, they will be prompted for their old password and to enter a new password. There is a form validator on the server side to make sure the old password is correct as well as a client side validator to make sure the new password has been entered correctly twice. 

## 404 pages
If a user navigates to a page which does not exist or if they do not have permission to access, they will be directed to a 404 error page. 

## Search
On the main dictionary page, users can search for specific words located either in the word field or the definition. 

# Features to implement in future updates

## 

# User Types and permissions
There are four types of users that this website is designed for:

## Visitor
A visitor is anyone who navigates to this website and can see the dictionary. Visitors can view words and definition, the about page and they can register for an account. 
The page is fully functional for read only access for visitors. 
## User
A visitor who registeres for an account automatically becomes a "user". Users have the same rights as visitors, plus they have access to a dashboard and to submit words to the dictionary. 
Any word a user submits is first sent to an editor to check and approve. Once approved, the word is published to the dictionary. 
## Editor
Editors have all the rights of a user, but also have the responsibility to check and approve user submitted words. Editors can also edit and delete words from the dictionary.
## Admin
Administrators have all the rights of an editor, but they also have the right to change user types for all users between user / editor / admin. They can change any user except themselves. This is a security feature so that an administrator doesn't accidentaly change their own permissions. 
# CRUD - Create, Read, Update and Delete
As part of the milestone project, we have to demonstrate that our application can perform CRUD operations.

|   	|  Create 	|  Read 	| Update  	| Delete  	|
|---	|---	|---	|---	|---	|
| Visitor  	| No  	| Yes  	| No  	| No  	|
|  User 	| Yes  	|  Yes 	| Yes  	|  No 	|
| Editor  	|  Yes 	| Yes  	| Yes  	| Yes  	|
| Admin  	|  Yes 	| Yes  	| Yes  	|  Yes 	|

As seen in the table above, all CRUD functionality is present in the application, however, CRUD operations are restricted to some user types. 

## Create

### Submit new word
All users, editors & admins are able to submit new words to the dictionary. Each submission creates a new record in the database.

### Register new user
Anyone who does not have an account is able to register for an account. The register function creates a new record in the database for that user. 

## Read

### Display words from the database
All visitors, users, editors and admins are able to read records from the database in the form of words in the dictionary. The application reads from the words collection in the database and displays the words in the dictionary.

### Search
All visitors, users, editors and admins are able to search for words within the dictionary. This function reads from the database and displays the searched terms on the search page

### Search by "submitted by"
All visitors, users, editors and admins are able to search by user submitted words. Each word card in the dictionary has an entry of who submitted this word. By clicking on the link, the application reads from the database and displays all words submitted and approved by that particular user. 

## Update

### Edit words
All editors and administrators have the ability to update or edit words submitted by other users. Editors and administrators can see edit buttons next to each word in the dictionary itself, or on their user dashboards. When editing a word, the application updates the record of that word with new values.

Users have the ability to update words which they have submitted before the words are approved. This option is available in the user dashboard for each user. The application updates the values in the record for that word and sends the word to an editor or administrator for review. 

### Edit user types
Admins have the right to update user types. Admins have an additional option in the dashboard where they can choose a user and update their type between user / editor / admin. However, administrators cannot update their own type as a security measure so that they do not accidentally remove their own permissions. 

## Delete

### Reject words
Editors and administrators have the ability to reject words submitted by other users. The application then removes that word from the collection.

### Delete word
Editors and administrators have the ability to delete words which have been submitted and approved. This is in case a word is approved accidentally so that it can be deleted from the dictionary. The application removes the word from the collection. 


# Technologies Used

## Languages
* [HTML](https://en.wikipedia.org/wiki/HTML) - HyperText Markup Language - used to build up the foundation of the webpages in this project. Mostly used in files ending in `.html`
* [CSS](https://en.wikipedia.org/wiki/CSS) - Cascading Style Sheets - Used to style the pages in this project. Located in files ending with `.css`
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - JavaScript - Used to provide form validation on the Register and Change Password Pages. File ending in `.js`
* [Python](https://www.python.org/) - Used to build the back end of the web application. Stored in files ending with `.py`

## Libraries

* [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - A front end framework used extensivelly in this project
* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - A lightweight WSGI web application framework used for routing and backend of this project.
* [Jinja](https://www.palletsprojects.com/p/jinja/) - Template engine used to render web pages and components
* [Pymongo](https://pypi.org/project/pymongo/) - a component imported into Python to allow access and CRUD operations with a mongoDB database

## Hosting

* [Heroku](https://www.heroku.com/home) - A web hosting service that supports Python applications.
## Tools

* [MongoDB Atlas](https://www.mongodb.com/) - Document database to store data using NOSQL for this project
* [GitHub](https://github.com/) - A cloud based code repository used to store all code files for this project
* [VSCode](https://code.visualstudio.com/) - A cross platform code editor used to develop this project
* [Microsoft Edge](https://www.microsoft.com/en-us/edge?r=1) - Web browser used for testing and page preview
* [Google Chrome](https://www.google.com/intl/en_ie/chrome/) - Web browser user for testing
* [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) - Web browser used for testing
* [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - Used to design the tables used in this readme file
* [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjw-e2EBhAhEiwAJI5jg_33A7TEqNM59vO9PjRpE-ZjzkpAgjcfU7TXsKZhu4a3puGdzFaM3hoCqIUQAvD_BwE) - Wireframe creation tool. Used to design initial templates for the website pages

## Testing
* [Am I Responsive](http://ami.responsivedesign.is/) - Testing responsive design
* [W3C Markup Validation Service](https://validator.w3.org/) - Testing that all HTML code is valid
* [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Testing that all CSS code is valid
* [JS Hint](https://jshint.com/) - Testing that all javascript code is valid
* [PEP8 Online](http://pep8online.com/) - Testing that all python code is valid
* [GTMetrix](https://gtmetrix.com/) - Loading time testing



# Testing

## Code Validation

## Manual Testing


## Testing Scenarios

# Deployment

## Heroku

## Local Deployment


# Credits

## Media

* [TopPNG](https://toppng.com/cruise-ship-clip-art-cruise-ship-encode-clipart-to-cruise-ship-clipart-black-and-white-PNG-free-PNG-Images_164796) - Favicon and Navbar brand image
* [Pixabay](https://pixabay.com/photos/lighthouse-light-sea-beacon-coast-2611199/) - Image used in "About" page by Evgeni Tcherkasski

## Dictionary terms
Some words in this dictionary were taken from the below resources

* [Ship Dictionary](https://onboardwithlouis.wordpress.com/dictionary/)
* [Cruise Ship Diary](https://milimundo.com/typical-crew-vocabulary-cruise-ships/)
* [Cruise Ship Crew Dictionary](https://crew-center.com/cruise-ship-crew-dictionary-0)

## Code
Code snippets implemented in this project are credited below and in the file comments:

* [Footer Sticks to bottom of the page](https://stackoverflow.com/questions/40853952/bootstrap-footer-at-the-bottom-of-the-page/60780493#60780493) - Credit to Robert Beckson
* [Flask Error Handling](https://www.askpython.com/python-modules/flask/flask-error-handling) - Tutorial for Flask error handling
* [Pagination](https://github.com/mirofrankovic/cookbook-trisport-project-03/blob/master/app.py#L26-L103) - Taken from project "cookbook-trisport-project-03" by mirofrankovic and modiffied to suit this project
* [Check if authenticated user](https://github.com/NgiapPuoyKoh/ai-chat-annotator/blob/7b37842579f8d1783de8d11be544f9790b248f05/app.py#L534) - Taken from project ai-chat-annotator by NgiapPuoyKoh


## Acknowledgements

My mentors Ignatius Ukwuoma and Guido Cecilio who provided feedback, learning resources and most importantly their time to ensure this project is completed and that the learning outcomes are achieved. 

The Code Institute Slack community who helped in time of crisis and for providing feedback and peer review. Most of the provided suggestions have made it to the final product. 





