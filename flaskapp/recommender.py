import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Recommender:

	def __init__(self, file):
		self.df = pd.read_csv(file)


	def get_title_from_index(self, index):
		return self.df[self.df.index == index]["title"].values[0]


	def get_index_from_title(self, title):
		return self.df[self.df.title == title]["index"].values[0]


	def combine_features(self, row):
	    return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']


	def get_recommended_movies(self, movie_input):
		features = ["keywords", "cast", "genres", "director"]

		for feature in features:
			self.df[feature] = self.df[feature].fillna('') 

		self.df["combined_features"] = self.df.apply(self.combine_features, axis=1) 

		cv = CountVectorizer() 
		
		count_matrix = cv.fit_transform(self.df["combined_features"]) 

		cosine_sim = cosine_similarity(count_matrix)

		movie_index = self.get_index_from_title(movie_input)

		similar_movies = list(enumerate(cosine_sim[movie_index])) 
		
		sorted_similar_movies = sorted(similar_movies,key=lambda x:x[1],reverse=True)[1:]

		output = []
		for i in range(10):
			output.append(self.get_title_from_index(sorted_similar_movies[i][0]))

		return output
