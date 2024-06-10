from bs4 import BeautifulSoup #bs4 is the library and BeautifulSoup is the specific we want to take from bs4, so we import that specific
import requests #requests is the HTTP library we want to take from
import csv

html_text = requests.get("https://web.archive.org/web/20200518073855if_/https://www.empireonline.com/movies/features/best-movies-2/").text #Getting the website link that we want to take from and then changing the format to .text so we get the text of the html not just the response

souped_html = BeautifulSoup(html_text, 'lxml') ##Inits the lxml parser (what helps make out the actual text from the HTML tags).

movies = souped_html.find_all('h3') #finds all the <h3> tags which contain the movie no. and titles.
movie_names = [] #Starts a list of movies that is initially empty.



for movie in movies: 
    movie_names.append(movie.text.strip()) ##strips the movie names of the html tags and other unnecessary elements.


with open ("100movies.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Movie"])
    for movie in movie_names: #Used chatGPT to tell us how to write it more cleanly, we were originally using the code from our previous scrapers, not realising the zip function creates multiple tuples but in this instance we were not using multiple tuples so out CSV file was being written and looked horrible with loads of unnecessary characters such as: ( ', this made it a single element.
        writer.writerow([movie])

