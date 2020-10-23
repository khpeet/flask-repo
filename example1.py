from flask import Flask, render_template #render_template for displaying web templates (html, css, etc)

#instatiate flask class and get the name of file (main or example1)
app=Flask(__name__)

#define homepage path
@app.route('/')
def home():
    return render_template("home.html")

#define about page
@app.route('/about/')
def about():
    return render_template("about.html")

#run the app
if __name__ == "__main__":
    app.run(debug=True)
    #test
