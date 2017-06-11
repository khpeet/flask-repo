from flask import Flask, render_template #render_template for displaying web templates (html, css, etc)
#python looks for css in /static/css folder

#instatiate flask class and get the name of file (main or example1)
app=Flask(__name__)

#define homepage path (root) localhost:5000
@app.route('/')
def home():
    return render_template("home.html")

#define homepage path (root) localhost:5000/about/
@app.route('/about/')
def about():
    return render_template("about.html")

#run the app
if __name__ == "__main__":
    app.run(debug=True)
