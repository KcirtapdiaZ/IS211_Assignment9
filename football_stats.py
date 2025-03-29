# Scrapping from https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'

# List of player indices to use 2 characters for the team name
special_players = [2, 8, 10, 13, 14]  # Adjusting for 0-based index

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table containing player statistics
    table = soup.find('table', {'class': 'TableBase-table'})

    # Get the rows of the table
    rows = table.find_all('tr')[1:21]  # Get only the top 20 players, excluding the header row

    # Loop through each row and extract the necessary information
    for i, row in enumerate(rows):
        columns = row.find_all('td')

        if len(columns) > 8:  # Ensure there are enough columns to extract

            # Extract the combined player info from the first column (name, position, team)
            player_column = columns[0].get_text(strip=True)

            # Split the player info at "QB" and ensure the player name and team are correctly extracted
            player_info = player_column.split('QB')

            if len(player_info) > 1:
                # The player name is before "QB", and the team is after it
                player_name = player_info[0].strip()

                # Determine whether to use 2 or 3 characters for the team code
                team_name = player_info[1][0:3].strip()  # Default to 3 characters

                # If it's one of the special players (with 2-character team names), use 2 characters for the team code
                if i in special_players:
                    team_name = player_info[1][0:2].strip()  # Use only 2 characters for the team code

            # Extract touchdowns from the 9th column (index 8)
            touchdowns_column = columns[8].get_text(strip=True)

            # Print the player’s stats without modifying the player name
            print(f"Player: {player_name}, Position: QB, Team: {team_name}, Touchdowns: {touchdowns_column}")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)

