## Salha Saad Portfolio
Stream One Project: Data Centric Development Milestone Project - Code Institute


## 1. UX

The main aim from this webpage is to help readers in the community finding top ranked and a good read Psychological book. It provides the users with a list of books and it does allow them to add their favoriate ones. The users can also have the opportunity to submit their feedbacks and reviews. The features I have implemented in the project aimed to promote users contribution to this growing form and help in its contents expansion. The idea has been adopted from other similar online forms where everyone can make a collective effort. I will be talking about these features and functionalities in the below sections. 



## 2. Features

### 2.1 Existing Features

All of the below features are using three MongoDB database collections. One collection is called Book and contain the book list. The books_review has the customer review database and the contactform collections has the user contact information pushed via the contact form. 

Throughout the two pages of my design I have made it as easy as possible for the user to access the information and have enjoyable experience. On the home, the user will see a list of selected books with book cover, title, author and clickable Readmore button for more information. The book list contains so far only 12 books but it is expandable. This is becuase the users can easily add their recommended book via filling the form on the left of the screen. To submit book to the database, all of the input fields in the form have to be filled. These include the book name, author name, book's cover url image link, book introduction and the price. As soon as the add button is clicked, a jinja template funtion (insert book) will be called to update MongoDB database collection and re-render the home page. By using the same form,  the user will have the opportunity to modify any of the existed book in the list by submitting another form with the information related to the updated book. The jinja function  in the app.py file will then search the mongodb database using the first two fields in the form (book name and author name). Once the newly added or updated book is added to the database the page gets automatically refreshed.


As said before, once the readmore button below each book is clicked a new page is rendered which will show more information about that book. These information will include book introduction, a link to an external website where to buy this book from and a list of customer reviews. I have made sure to incorporate a mixtures of positive and negative feedback. There is also chance for the user to leave their review. Upon button submission the information will be pushed to the existing record in the mongoDB database as dictionary with key and value pair. I have also add a function to delete a review. All the uer needs to do is to enter her or his name in the name filed of the form and then hit the delete button. The function I have implemented will use the user name to search one particular dictionary record in the mongoDB collection. There will not be any other information for the user to fill in. The book detail page will then be rendered with the updated database collection. 


The contact page is an opportunity for the user if he or she would like to get in touch. The contact me form has a link with jinja function that upon clicking on the submission buttom, the field inputs will be pushed to an existing MongoDB user database collection. The other functionalty that I have added was a google map of my current location. I have used flask_googlemaps module that when it is supplied with the location's Latitude and Longitude, it will allow rendering of google map in a html div element. 

### 2.2 Features Left to Implement

There are one pages in the nav bar (statistic page ) that I would like to develop and build in the near future. I would like to include statistic database such as book selling record over the last few years so the user will be able to see the selling profile of each book as an indication of whether if the book is on demand or not. I would like to make use of d3.js library to make a bar chart or the scatter plots. The database will be incoporated as either MongoDB or Squal database. 


## 3. Technologies Used

I have used the following languages in my project built:

- [html](https://html.com)

- [css](www.w3schools.com)

- [Bootstrap](www.getbootstrap.com)

- [JQuery](www.jquery.com)

- [JavaScript](www.javascript.com)

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
        render_template, redirect, request, url_for, PyMongo
        flask_googlemaps (GoogleMaps)

- [MongoDB](https://www.mongodb.com/)



## 4. Testing 
### 4.1 Version control:

I have asked few people for a feedback on my website in terms of its relevancy and clarity. The feedback was good and the website achieved the intended outcome of providing a book recommendations. One of the feedback was that my website layout and features are presented in the most concise, meaningful way and consistency. They had a comfortable and enjoyable browsing and visualization experiences as the color scheme is concernd. 

All of the nav elements has been tested to insure that the intended page is correctly rendered. As the main aim of this project is to provide the user with a dynamic website, a clickable add, update, delete and submission  buttons are on display to the user to click. I have also checked that the mongoDB has been changed accordingly and all of the website is rendered with the newly updated data. All clickable button have been checked to insure that the correct data types have been correctly rendered and the POST and GET methods are working as intended. 

All links will open in a new tab using 'target="_blank"'. All links have been manually tested to ensure that they are pointing to the correct destination. 

This site was tested across multiple browsers (Chrome, Safari, Internet Explorer, FireFox). I have validated both html files and css file on Markup Validation Service and made the suggested adjustment accordingly. 

### 5.1 Deployment

This site is hosted using GitHub pages, deployed directly from the master branch. The deployed site will update automatically upon new commits to the master branch. To run locally, you can clone this repository directly into the editor of your choice by pasting git clone https://plxsas.github.io/SecondMileStoneProject/ into your terminal. Finally readme file is written to explain what are the main features of this project and how they have been deployed. The project have additionally been deployed on heroku with all required files (requiements.txt, Procfile). I have also set up the IP to 0.0.0.0 and Port to 5000 with the configuration variable in the heroku app. 


