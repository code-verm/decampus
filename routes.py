from app import app
from flask import Flask, render_template
@app.route('/')
#def home():
#    return "Hello from Decampus!"
def index():
  # Example of fetching data for the homepage
    return render_template('index.html') #, books=books)  # Pass data to the template

#@app.route('/books')
#def books():
 #   return render_template('books.html')
