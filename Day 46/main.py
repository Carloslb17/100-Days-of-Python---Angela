from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID=
SPOTIPY_CLIENT_SECRET=


#user_answer = input("Which year do you want to travel to? Type this date in this format YYYY-MM-DD: \n")

# Step 1 - Download the music list bill board from the webpage
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/2022-08-12/")
song_web_page = response.text

# Retieve the data from the billboard
soup = BeautifulSoup(song_web_page, "html.parser")
soup.prettify()
song_lists = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

song_titles = [(tag.getText()).strip() for tag in song_lists]
print(song_titles)

data = pd.DataFrame(columns=["Name", "Market Cap (US$ Billion)"])
name_list = []
market = []
col = []

for row in soup.find_all('tbody')[2].find_all('tr'):
    col.append(row.find_all('td'))
    # Write your code here

for row in range(0, len(col) - 1)
    try:
        data = market.append({  # 'Rank': col[0].text.strip(),
            'Name': col[row][1].getText(),
            'Market Cap (US$ Billion)': col[row][2].getText()}, ignore_index=True)
    except:
        continue

# Step 2 - Conecction with Spotify


scope = "user-library-read"


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri="https://example.com/",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = "2022"
for song in song_titles:
    result = sp.search(q=f"track:{song}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

print(len(song_uris))
