import requests
import json

# Take user input for the query
query = input("What type of news are you interested in? ")

# Construct the API URL with the user query and your API key
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-07-07&sortBy=publishedAt&apiKey=ed072b4aace54b2da1a7abf4ed378396"

# Make the API request
r = requests.get(url)
news = json.loads(r.text)

# Iterate through each article and print title and description
for article in news["articles"]:
    print("Title:", article["title"])
    print("Description:", article["description"])
    print("--------------------------------------")
