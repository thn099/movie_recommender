from flask import Flask, render_template, request
from flaskapp import app
from flaskapp.recommender import Recommender
import pandas as pd


@app.route('/')
def home():
	df = pd.read_csv("movie_dataset.csv")
	movie_list = df["title"].tolist()
	query_parameters = request.args
	movie_input = query_parameters.get('input')
	if movie_input:
		recommender = Recommender(df)
		recommendations = recommender.get_recommended_movies(movie_input, 50)
		return render_template("home.html", input=movie_input, movie_list=movie_list, recommendations=recommendations)
	else:
		return render_template("home.html", movie_list=movie_list)
