from flask import Flask , render_template , request, url_for, redirect
import json,ast
import math
import re
import csv

"""
def Superclean(movie):
    listofGenres = []
    listofSpokenLanguages = []
    listofProdComp = []
    posterPath=""
    movieData = {"genres":"","overview":"","popularity":"","poster_path":"","release_date":"","spoken_languages":"","title":"","vote_average":""}

    #match = re.findall(r'\'([^\']*)\'', movie[0])
    listofGenres=ast.literal_eval(movie[0])
    #for item in match:
     #   listofGenres.append(item)

    posterPath = 'https://image.tmdb.org/t/p/original'+movie[3]

    #match = re.findall(r'\'([^\']*)\'', movie[5])
    match=ast.literal_eval(movie[5])
    #for item in match:
     #   listofSpokenLanguages.append(item)
 
    
    movieData['genres'] = listofGenres
    movieData['overview'] = movie[1]
    movieData['popularity'] = movie[2]
    movieData['poster_path'] = posterPath
    movieData['title'] = movie[6]
    movieData['vote_average'] = movie[7]
    movieData['release_date'] = movie[4]
    movieData['spoken_languages'] = listofSpokenLanguages
    movieData['production_companies'] = listofProdComp

    return movieData
"""
def KNN(standardMovie):
    sortedMoviesList = []
    #print(standardMovie)
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
                posterPath = 'https://image.tmdb.org/t/p/original'+movie[2]
                sortedMoviesList.append([euclideanDistance,movie[0],'https://image.tmdb.org/t/p/original'+movie[2]])
        #print(sortedMoviesList[1])   
        sortedMoviesList = sorted(sortedMoviesList, key=lambda x: x[0])
        
    return sortedMoviesList

    '''
    with open("final.csv",encoding="UTF8") as csv_file:
        moviesList = csv.reader(csv_file, delimiter=',') 
        next(moviesList, None)
        for movie in moviesList:
            movie = Superclean(movie)
            if(movie['title']!=standardMovie['title']):
                movieDistance=[]
                euclideanDistance = 0  
        
# considering title also as by google in priority
            euclideanDistance+=pow((float(movie['popularity'])-float(standardMovie['popularity'])),2)
            euclideanDistance+=pow((float(movie['release_date'])-float(standardMovie['release_date'])),2)
            euclideanDistance+=pow((float(movie['vote_average'])-float(standardMovie['vote_average'])),2)

 # genres cosidering                       
            #print("movie",movie['genres'])
            #print("standardMovie",standardMovie['genres']) 
            for i in range(len(movie['genres'])):
                euclideanDistance+=(pow((movie['genres'][i]-standardMovie['genres'][i]),2)*2)
            #print(euclideanDistance,movie['title'])
# spoken_languages cosidering                
            for i in range(len(movie['spoken_languages'])):
                euclideanDistance+=pow((movie['spoken_languages'][i]-standardMovie['spoken_languages'][i]),2)
                    
 
            euclideanDistance = math.sqrt(euclideanDistance)
            movieDistance.append(euclideanDistance)
            movieDistance.append(movie['title'])
            movieDistance.append(movie['poster_path'])
            sortedMoviesList.append(movieDistance)
        

        
        sortedMoviesList = sorted(sortedMoviesList, key=lambda x: x[0])
# popularity
        standardPopularity = float(standardMovie['popularity'])
        neighbourPopularity = float(movie['popularity'])
        popularityDifference = standardPopularity - neighbourPopularity
        popularity = pow( popularityDifference,2)
# RElease Date
        standardreleaseDate = float(standardMovie['release_date'])
        neighbourreleaseDate = float(movie['release_date'])
        releaseDateDifference = standardreleaseDate - neighbourreleaseDate
        releaseDate = pow(releaseDateDifference,2)
# rating
        standardrating = float(standardMovie['vote_average'])
        neighbourrating = float(movie['vote_average'])
        ratingDifference = standardrating -neighbourrating
        rating = pow(ratingDifference,2)
''' 

