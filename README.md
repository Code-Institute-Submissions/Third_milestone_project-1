## Salha Saad Portfolio
Stream One Project: Data Centric Development Milestone Project - Code Institute


## 1. UX

I have designed this webpage to help readers finding good read and top ranked books on Psychology. The main aim was to provide users with a list of books as well as allowing them to add their favoriate books to the existing list and the functionality of submitting feedbacks on a specific book. I wanted the users to make a contirbution to this project by helping in its contents expansion. The idea is similar to some online form where everyone can provide help by making a collective effort. I have incoportated number of features to achieve the above goal which I will be explaining in depth in the next paragraph under the features section. 



## 2. Features

Throughout the two pages of my design I have made it as easy as possible for the user to access the information and have enjoyable experience. On the home, the user will see a list of books with book cover, title, author and clickable Readmore button for more information. The book list contain so far only 12 books but it is expandable. This is becuase the user can fill in the form on the left of the screen with the required information (book name, author name, book's cover url image, book introduction and prices). As soon these information are there you can click the add button. The button is linked with a jinja template funtion that will update MongoDB database and then render the current page with the newly update database. Additionally the user will have the opportunity to modify any of the book on the list by filling the information in the form with the new information. The jinja function in the app.py file with search the mongodb database using the first two fields in the form (book name and author name). Once the newly added or updated book is added to the database the page gets automatically refreshed.


As said before, once the readmore button is clicked a new page is rendered which will show more information about each book. These information will include book introduction, a link to an external website where to buy this book from and a list of customer reviews. I have made sure to incorporate a mixtures of positive and negative feedback. There is also chance for the user to leave their review. Upon button submission the information will be pushed to the existing record in the mongoDB database as key and value. I have also add a function to delete a review. All the uer needs to do is to enter her or his name in the name filed of the form and then hit the delete button. The function I have implemented will use the user name to search one particular dictionary record in the mongoDB collection. There will not be any other information for the user to fill in. The book detail page will then be rendered with the updated database collection. 


The contact page is an opportunity for the user if he or she would like to get in touch. I have also make sure there the address is list out there with an email address and a link to social media accounts. I have made a usage of flask_googlemaps module to use Googlemaps functionality inside my app. You then need to supply the googlemap functin with latitute and longitute coordinate inside the html template. 

## 2.1 Features Left to Implement

There are one pages in the nav bar (statistic page ) that I would like to develop and build in the near future. I would like to some statistical data such as book selling record over the last few years so the user will be able to see the selling profile as an indication whether if the book is on demand or not. I would like to make use of d3.js library to make a bar chart of the selling products. The database will be incoporated within MongoDB or Squal database. 


I will also be developing the login, resigteration options in the header so the user can create their own account. 

## 3. Technologies Used

I have used the following languages in my project built:

HTML
CSS
Bootstrap
JQuery 
JavaScript
EmailJS
Flask (render_template, redirect, request, url_for)
flask_pymongo library (PyMongo module)
bson.objectid (ObjectId)
flask_googlemaps (GoogleMaps)

## 4. Technologies Used

The project as it is stand at the moment has made use of the following coding languages:

- [JQuery](https://jquery.com)
    - The project uses **JQuery** to simplify DOM manipulation.

- [JavaScript](www.javascript.com)
    - The project uses **d3.js library** to write functions for data visualization.


## 4. Testing 
### 4.1 Version control:

I have asked few people for a feedback on my website in terms of its relevancy and clarity. The feedback was good and the website achieved the intended outcome of providing a summary on the gender gap in Europe. One of the feedback was that my website layout and features are presented in the most concise, meaningful way and consistency. They had a comfortable and enjoyable browsing and visualization experiences as the color scheme is concernd. 

All of the dropdown's elements in the side bar has been tested to insure that the intended page is correctly rendered. As the main aim of this project is to provide the user with a direct comparison, a clickable men and women buttons are on display to the user to toggle between the two gender data. I have mantually tested them and are perfectly working. 

I have also tested the responsive design of the graph on the salary gap page and is working as intended. Hovering over on any of the bars or segments of the graph will display the desired results.  

They can view both the live version and the GitHub repository by clicking on the Font Awesome icons. They were also able to download source code by clicking on the download button on the nav bar of each page. 

In the side bar, I have added two clickable buttons. One for downloading the sources code of this project from the GitHub page and the other for directing the reader to an external web page if further reading is required. They are both tested and are working. 

All clickable button have been checked to insure that the correct data types have been correctly rendered. 

All links will open in a new tab using 'target="_blank"'. All links have been manually tested to ensure that they are pointing to the correct destination. 

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox). I have validated both html files and css file on Markup Validation Service and made the suggested adjustment accordingly. 

### 5.1 Deployment

This site is hosted using GitHub pages, deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. In order for the site to deploy correctly on GitHub pages, the landing page must be named index.html. To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://plxsas.github.io/SecondMileStoneProject/ into your terminal. Finally readme file is written to explain what are the main features of this project and how they have been deployed. 



