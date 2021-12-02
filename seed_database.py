"""drops, creates and automatically populate the databse with data"""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary. Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )

    # Our code:
    # date_str = movie["release_date"]
    # format = "%Y-%m-%d"
    # date = datetime.strptime(date_str, format)
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

    # TODO: create a movie here and append it to movies_in_db

for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    # TODO: create a user here
    db_user = crud.create_user(email, password)

    # TODO: create 10 ratings for the user
    # we want to get a random movie using choice
    # for that random movie, we want to assign a random rating

    for _ in range(10):
        random_movie = choice(movies_in_db)
        random_score = randint(1,5)

        random_rating = crud.create_rating(db_user, random_movie, random_score)