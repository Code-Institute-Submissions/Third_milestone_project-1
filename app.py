import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = 'mongodb+srv://plxsas:Salha2019@cluster1.cqq5g.mongodb.net/Books_list?retryWrites=true&w=majority'


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("books.html", 
                           books=mongo.db.Books.find(),names=mongo.db.Books.find())

@app.route('/detail_book/<name>')
def detail_book(name):
    book = mongo.db.Books.find_one({'name':name})
    review = mongo.db.Books_reviews.find_one({'name':name})
    return render_template('detail_book.html', books=book,reviews=review)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)