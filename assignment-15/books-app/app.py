from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Book მოდელი
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author = db.Column(db.String(200))
    year = db.Column(db.Integer)


# წიგნების დამატება მაგალითისთვის
def seed_books():
    if Book.query.count() == 0:
        books = [
            Book(title="1984", author="George Orwell", year=1949),
            Book(title="The Hobbit", author="J.R.R. Tolkien", year=1937),
            Book(title="To Kill a Mockingbird", author="Harper Lee", year=1960),
            Book(title="Pride and Prejudice", author="Jane Austen", year=1813),
        ]

        db.session.bulk_save_objects(books)
        db.session.commit()


with app.app_context():
    db.create_all()
    seed_books()


# 1. მთავარი გვერდი
@app.route('/')
def home():
    return redirect(url_for("books"))


# 2. ახალი წიგნის დამატება
@app.route('/book', methods=['GET', 'POST'])
def create_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = request.form["year"]

        new_book = Book(title=title, author=author, year=year)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for("books"))

    return render_template("create_book.html")


# 3. წიგნის ინფორმაციის განახლება
@app.route('/update_book/<int:book_id>', methods=["GET", "POST"])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)

    if request.method == "POST":
        book.title = request.form["title"]
        book.author = request.form["author"]
        book.year = request.form["year"]
        db.session.commit()
        return redirect(url_for("books"))

    return render_template("update_book.html", book=book)


# 4. კონკრეტული წიგნის ნახვა
@app.route('/get_book/<int:book_id>')
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template("book_detail.html", book=book)


# 5. ყველა წიგნის ინფორმაციის ნახვა
@app.route('/books')
def books():
    books = Book.query.all()
    return render_template("books.html", books=books)


# 6. წიგნის წაშლა
@app.route('/delete_book/<int:book_id>', methods=["POST"])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("books"))


if __name__ == '__main__':
    app.run(debug=True)
