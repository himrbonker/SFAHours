from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    entries = [
        {"name": "Alex", "org": "Food Bank", "hours": 3, "date": "2026-05-01"},
        {"name": "Jordan", "org": "Animal Shelter", "hours": 5, "date": "2026-05-10"},
        {"name": "Sam", "org": "Library", "hours": 2, "date": "2026-05-15"},
    ]
    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
