#Salha Saad Portfolio
Stream One Project: Data Centric Development Milestone Project - Code Institute


UX

I have designed this webpage to help readers finding good read and top ranked books on Psychology. The main aim was to provide users with a list of books as well as allowing them to add their favoriate books to the existing list and the functionality of submitting feedbacks on a specific book. I wanted the users to make a contirbution to this project by helping in its contents expansion. The idea is similar to some online form where everyone can provide help by making a collective effort. I have incoportated number of features to achieve the above goal which I will be explaining in depth in the next paragraph under the features section. 



Features

Throughout the two pages of my design I have made it as easy as possible for the user to access the information and have enjoyable experience. On the home, the user will see a list of books with book cover, title, author and clickable Readmore button for more information. The book list contain so far only 12 books but it is expandable. This is becuase the user can fill in the form on the left of the screen with the required information (book name, author name, book's cover url image, book introduction and prices). As soon these information are there you can click the add button. The button is linked with a jinja template funtion that will update MongoDB database and then render the current page with the newly update database. Additionally the user will have the opportunity to modify any of the book on the list by filling the information in the form with the new information. The jinja function in the app.py file with search the mongodb database using the first two fields in the form (book name and author name). Once the newly added or updated book is added to the database the page gets automatically refreshed.  



