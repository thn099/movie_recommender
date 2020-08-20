from flask import Flask, render_template, request
from flaskapp import app
from flaskapp.recommender import Recommender

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		movie_input = request.form["movie"]
		# TODO: validate input
		recommender = Recommender('movie_dataset.csv')
		data = recommender.get_recommended_movies(movie_input, 20)
		return render_template("home.html", data=data)
	return render_template("home.html")
