#https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States
import requests
from bs4 import BeautifulSoup

# URL of the Wikipedia page with the U.S. Presidents list
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Send a GET request to fetch the HTML content of the page
response = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the presidents
table = soup.find('table', {'class': 'wikitable'})

# Loop through the rows of the table and print the content of each cell
rows = table.find_all('tr')[1:]  # Skip the header row
for row in rows:
    cells = row.find_all('td')
    if len(cells) > 1:
        president_name = cells[1].text.strip()
        years_in_office = cells[2].text.strip()

        # Clean the name by removing text inside square brackets using string methods
        president_name_clean = president_name.split('[')[0].strip()

        print(f"President: {president_name_clean}, Years in Office: {years_in_office}")
