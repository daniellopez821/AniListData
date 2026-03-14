import requests
import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

url = "https://graphql.anilist.co"

query = """
query {
    Page(page:1,perPage:50) {
        media(type: ANIME, sort: TRENDING_DESC){
            title{
                english
                romaji
            }
            genres
            studios(isMain: true){
                nodes{
                    name
                }
            }
        }
    }
}
"""

response = requests.post(url, json={"query": query})

data = response.json()

with open("anilist_top10.csv", mode="a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Rank","Title", "Genre", "Studio"])

    for i, anime in enumerate(data["data"]["Page"]["media"], start=1):
        title = anime["title"]["english"] or anime["title"]["romaji"]
        Genre = anime["genres"]
        studios = ", ".join(studio["name"] for studio in anime["studios"]["nodes"])

        writer.writerow([i, title, Genre, studios])

        print(f"{i}. {title}")
        print(f" Genre: {Genre}")
        print(f" Studio: {studios}")
        print()

    print("CSV file created successfully")




"""
for i, anime in enumerate(data["data"]["Page"]["media"], start=1):
    title = anime["title"]["english"] or anime["title"]["romaji"]
    Genre = anime["genres"]
    studios = ", ".join(studio["name"] for studio in anime["studios"]["nodes"])

    print(f"{i}. {title}")
    print(f" Genre: {Genre}")
    print(f" Studio: {studios}")
    print()
"""