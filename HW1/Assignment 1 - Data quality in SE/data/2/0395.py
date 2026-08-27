from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required  # JWT ---  JSON web token
from secure import authenticate, identity
from user import User, RegisterdUser


# create app instance

app = Flask(__name__)
# create api instance of app

api = Api(app)
app.secret_key = 'rahul@123'
# will create an endpoint 127.0.0.0:5000/auth
jwt = JWT(app, authenticate, identity)

# create in-memory database of books
books = [
    {
        'ISBN': '978-354-216',
        'author': 'Jon Mac',
        'name': 'The man',
        'quantity': 20
    },
    {
        'ISBN': '128-689-341',
        'author': 'Michael Jack',
        'name': 'Although what',
        'quantity': 10
    }
]

# create a Resource Book


class Book(Resource):
    # get book by ISBN
    @jwt_required()
    def get(self, ISBN):
        # search for the book with the ISBN , return it otherwise return a message
        for book in books:
            if book["ISBN"] == ISBN:
                return book
        return " Book Not Found"

    # create book
    def post(self, ISBN):
        # check whether ISBN exists or not
        pos = 0
        for book in books:
            if book["ISBN"] == ISBN:
                # add only quantity
                book["quantity"] = book["quantity"] + 1

                # this line will not work the way we expect it to work.
                # books.extend(book)
                books[pos] = book
                return book, 201
            pos = pos+1
        # otherwise add the book to the books db

        # collect data
        payload = request.get_json()
        isbn = payload["ISBN"]
        author = payload["author"]
        name = payload["name"]
        quantity = payload["quantity"]
        newbook = {
            "ISBN": isbn,
            "author": author,
            "name": name,
            "quantity": quantity
        }

        # add this payload to books
        books.append(newbook)
        return newbook

    def delete(self, ISBN):
        # if the ISBN exists, delete that book
        pos = 0
        for book in books:
            if book["ISBN"] == ISBN:
                # we found the book
                books.pop(pos)
                return "Book Deleted"
            pos = pos+1
        # else send a message that the book is not in the store
        return "No book with the ISBN number found"

    def put(self, ISBN):
        pos = 0
        for book in books:
            if book["ISBN"] == ISBN:
                # The book is already there, so update the quantity
                book["quantity"] = book["quantity"] + 1
                books[pos] = book
                return "Book quantity updated by 1"
            pos = pos+1

        # add the book if it is not in the books list
        payload = request.get_json()
        isbn = payload["ISBN"]
        author = payload["author"]
        name = payload["name"]
        quantity = payload["quantity"]
        newbook = {
            "ISBN": isbn,
            "author": author,
            "name": name,
            "quantity": quantity
        }

        # add this payload to books
        books.append(newbook)
        return newbook, 201


# Resource for getting all books from the db


class BookList(Resource):
    # returns all the books in the store
    def get(self):
        return books


# create end points to the resource
api.add_resource(Book, '/book/<ISBN>')
api.add_resource(BookList, '/books')  # returns all the books
api.add_resource(RegisterdUser, '/register')
# run the app
app.run(debug=True)
