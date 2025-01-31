from flask import Flask, render_template, render_template_string, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method.upper() == "GET":
        title = "Book shop"
        books = []
        with open("db/db.json", "r") as f:
            books = json.loads(f.read())
        
        return render_template("index.html", title=title, books=books)
    else:
        
        name = request.form.get("name")
        author = request.form.get("author")
        
        books:list = []
        with open("db/db.json", "r") as f:
            books = json.loads(f.read())
            
        books.append({"name": name, "author": author})
        
        with open("db/db.json", "w") as f:
            f.write(json.dumps(books))
        return "ok"
            
        
       




app.run(debug=True)