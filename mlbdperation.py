import requests
import csv
from bs4 import BeautifulSoup

url = 'https://mlwbd.one/'

# request send
response = requests.get(url)

# Ceate object parser
soup = BeautifulSoup(response.content, 'html.parser')

items_divs = soup.find_all('div', {'class': 'items'})
selected_items_divs = items_divs[2]

# Find all the article tags inside the items div
articles = selected_items_divs.find_all('article')
# Check the total length of the movie list
print(len(articles))


# Create a new CSV file and write the headers
with open('movie_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Rating', 'Quality', 'Poster'])

    # Loop through each article and extract the data
    for article in articles:
        poster_img = article.find('img')['src']
        rating = article.find('div', {'class': 'rating'}).text.strip()
        quality = article.find('div', {'class': 'mepo'}).find('span', {'class': 'quality'}).text.strip()
        title = article.find('h3').text.strip()

        # Write the data to the CSV file
        writer.writerow([title, rating, quality, poster_img])

print('Data written to CSV file')

