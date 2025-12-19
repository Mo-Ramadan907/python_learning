from flask import Flask,render_template
app = Flask(__name__)
posts = [
    {
        'author':"mohamed ramadan",
        "title":"blog post 1 "
        ,"content":"my first content",
        "date_posted":"april 20 , 2025"
    },
    {
        'author':"mohamed ahmed",
        "title":"blog post 2 "
        ,"content":"my first content",
        "date_posted":"april 22 , 2025"
    }
]
@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="about")
if __name__ == "__main__":
    app.run(debug=True)