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
def get_tasks():
    return render_template("books.html", 
                           books=mongo.db.Books.find())
                           
@app.route('/detail_book/<book_id>/<book_name>')
def detail_book(book_id, book_name):
    book = mongo.db.Books.find_one({"_id": ObjectId(book_id)})
    review = mongo.db.books_reviews.find_one({"name": book_name})
    return render_template('detail_book.html', book=book, reviews=review)

@app.route('/add_review/<review_id>')
def add_review(review_id):
    review = mongo.db.books_reviews.find_one({"_id":ObjectId(review_id)})
    return render_template('addreview.html', review=review)


@app.route('/insert_review/<review_id>', methods=['POST'])
def insert_review(review_id):
    name = request.values.get("name")    
    review = request.values.get("review")    
    date = request.values.get("date")       
    mongo.db.books_reviews.update({"_id": ObjectId("5f78555d682198206cebbf7d")}, {"$set": { name: {"review": review, "date": date}}}) 
    return redirect(url_for('/detail_book/<book_id>/<book_name>'))



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)