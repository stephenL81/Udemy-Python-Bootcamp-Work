import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_web_page = response.text

soup = BeautifulSoup(movies_web_page, "html.parser")

movies_html = soup.find(name="div", class_="entity-info-items__list")
names = movies_html.find_all("a")
movies_initial_list = []
for item in names:
    movies_initial_list.append(item.text)

movies_initial_list.reverse()
the_list = []

for movie in movies_initial_list:
    if movie.endswith(", The"):
        the_list.append(f"The {movie[:-5]}")
    else:
        the_list.append(movie)

with open("movies.txt", mode="w") as file:
    number = 1
    for movie in the_list:
        file.write(f"{number}) {movie}\n")
        number+=1
