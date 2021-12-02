"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


# Replace this with routes and view functions!
@app.route('/')
def show_homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/movies')
def view_all_movies():
    """View all movies."""

    all_movies = crud.return_all_movies()
    print(all_movies)
    print("*"*50)
    return render_template("all_movies.html", movies=all_movies)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
