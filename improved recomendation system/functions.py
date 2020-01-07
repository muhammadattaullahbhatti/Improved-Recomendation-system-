from flask import Flask , render_template , request, url_for, redirect
import json,ast
import math
import re
import csv

def KNN(standardMovie):
    sortedMoviesList = []
    with open("final.csv",encoding="UTF8") as csv_file:
        moviesList = csv.reader(csv_file, delimiter=',') 
        next(moviesList, None)
        for movie in moviesList:
            if(movie[0]!=standardMovie[0]):
                euclideanDistance = 0
                movieDistance=[]
                for i in range(3,21):
                    euclideanDistance += pow((float(movie[i])-float(standardMovie[i])),2)
                euclideanDistance = math.sqrt(euclideanDistance)
                sortedMoviesList.append([euclideanDistance,movie[0],'https://image.tmdb.org/t/p/original'+movie[2]])
    return sorted(sortedMoviesList, key=lambda x: x[0])
