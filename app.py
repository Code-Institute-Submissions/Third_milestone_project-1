import os
from flask import Flask, render_template, redirect, request, url_for, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://plxsas:Salha2019@cluster1.cqq5g.mongodb.net/Books_list?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", 
                           books=mongo.db.Books.find())


@app.route('/insert_book', methods=['POST'])
def insert_book():
    book = mongo.db.Books
    book.insert_one(request.form.to_dict())
    return redirect(url_for('get_books'))


@app.route('/update_book')
def update_book():
    name = request.values.get("name")
    book = mongo.db.Books.find_one({"name": name})
    if request.method == "POST":
        book.update(
        {
            'name': request.form.get('name'),
            'author': request.form.get('author'),
            'description': request.form.get('description'),
            'price': request.form.get('price'),
            'image': request.form.get('image')
        })
    return redirect(url_for('get_books'))


                           
@app.route('/detail_book/<book_id>/<book_name>')
def detail_book(book_id, book_name):
    book = mongo.db.Books.find_one({"_id": ObjectId(book_id)})
    review = mongo.db.books_reviews.find_one({"name": book_name})
    return render_template('detail_book.html', book=book, reviews=review)

@app.route('/add_review/<book_name>')
def add_review(book_name):
    book = mongo.db.Books.find_one({"name": book_name})
    review = mongo.db.books_reviews.find_one({"name": book_name})
    return render_template('addreview.html', review=review, book=book)


@app.route('/insert_review/<review_id>/<book_name>/<book_id>', methods=['POST'])
def insert_review(review_id, book_name,book_id):
    name = request.values.get("name")    
    review = request.values.get("review")    
    date = request.values.get("date")       
    mongo.db.books_reviews.update({"_id": ObjectId(review_id)}, {"$set": { name: {"review": review, "date": date}}}) 
    return redirect(url_for('detail_book', book_id=book_id, book_name=book_name))
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)