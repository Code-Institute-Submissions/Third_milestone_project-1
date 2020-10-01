from pymongo import MongoClient

# Create connection to MongoDB
client = MongoClient(
    host='127.0.0.1:3306',  # <-- IP and port go here
    username="plxsas",
    password="Salha2019",
)
db = client['Books_list']
collection = db['Books_reveiws']
db.Books_reviews.insertOne( {'website': 'www.carrefax.com', 'author': 'Daniel Hoadley', 'colour': 'purple'} );

# Build a basic dictionary
d = {'website': 'www.carrefax.com', 'author': 'Alex Hoadley', 'colour': 'purple'}

# Insert the dictionary into Mongo
Books_reviews.insert_one(d)




db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})

db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})

db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})

db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})

db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})

db.Books_reviews.insertOne({"name":"l","review_1":{"review":"","name":"","date":""},"review_2":{"review":"","name":"","date":"24/05/2019"},"review_3":{"review":"","name":"","date":"30/12/2017"},"review_4":{"review":"","name":"", "date":"03/08/2019"}})
