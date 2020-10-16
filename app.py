import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_googlemaps import GoogleMaps
from flask_wtf import Form
from wtforms import TextField, TextAreaField, SubmitField
 
class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

  
app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://plxsas:Salha2019@cluster1.cqq5g.mongodb.net/Books_list?retryWrites=true&w=majority'

mongo = PyMongo(app)
GoogleMaps(app)
app.secret_key = 'development key'

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", 
                           books=mongo.db.Books.find())

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact2.html', form=form)

@app.route('/insert_book',  methods=['POST'])
def insert_book():
    book = mongo.db.Books
    review = mongo.db.books_reviews
    book.insert_one(request.form.to_dict())
    name = request.form.get("name")
    review.insert_one({"name": name})
    return redirect(url_for('get_books'))


@app.route('/update_book',  methods=['POST'])
def update_book():
    name = request.form.get("name")
    author = request.form.get("author")
    description = request.form.get("description")
    price = request.form.get("price")
    image = request.form.get("image")
    mongo.db.Books.update_one({"name": name, "author": author}, {"$set": {"name": name, "author": author, "description": description, "price": price, "image": image}})
    return redirect(url_for('get_books'))


                           
@app.route('/detail_book/<book_id>/<book_name>')
def detail_book(book_id, book_name):
    book = mongo.db.Books.find_one({"_id": ObjectId(book_id)})
    review = mongo.db.books_reviews.find_one({"name": book_name})
    return render_template('detail_book.html', book=book, reviews=review)


@app.route('/insert_review/<review_id>/<book_name>/<book_id>', methods=['POST'])
def insert_review(review_id, book_name,book_id):
    name = request.form.get("name")    
    review = request.form.get("review")    
    date = request.form.get("date")      
    mongo.db.books_reviews.update({"name": book_name}, {"$set": { name: {"review": review, "date": date}}}) 
    return redirect(url_for('detail_book', book_id=book_id, book_name=book_name))


@app.route('/delete_review/<review_id>/<book_name>/<book_id>', methods=['POST'])
def delete_review(review_id, book_name,book_id):
    name = request.form.get("name") 
    mongo.db.books_reviews.update({"_id": ObjectId(review_id)}, {"$unset": {name: 1 }})
    return redirect(url_for('detail_book', book_id=book_id, book_name=book_name))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)