from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")
soup.prettify()

#class="jsx-4245974604"

h3_tag = soup.find_all(name="h3", class_="title")

value = []
movie_titles = [tag.getText() for tag in h3_tag]
list_movies = movie_titles[::-1]

with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in list_movies:
        file.write(f"{movie} \n")