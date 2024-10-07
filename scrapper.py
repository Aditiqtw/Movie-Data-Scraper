import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time

# Create a workbook and add a worksheet
workbook = Workbook()
sheet = workbook.active
sheet.title = "Top Movies"
sheet.append(['Number', 'Movie URL', 'Movie Name', 'Movie Introduction'])

# Set the URL and headers
url = "https://www.imdb.com/chart/top/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Function to fetch and parse the HTML page
def fetch_movies(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for request errors
        return response.content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

# Function to parse the movies from the HTML content
def parse_movies(content):
    movies = []
    soup = BeautifulSoup(content, 'html.parser')
    movie_table = soup.find('tbody', class_='lister-list')
    
    if not movie_table:
        print("Error: Unable to find the movies table on the page.")
        return movies
    
    for row in movie_table.find_all('tr'):
        title_column = row.find('td', class_='titleColumn')
        movie_name = title_column.a.text
        movie_url = "https://www.imdb.com" + title_column.a['href']
        
        # Fetch movie details page
        movie_page = requests.get(movie_url, headers=headers)
        movie_soup = BeautifulSoup(movie_page.content, 'html.parser')
        movie_content = movie_soup.find('div', class_='summary_text')
        
        # Handling cases where the introduction might not be found
        movie_intro = movie_content.text.strip() if movie_content else "No introduction available"
        
        movies.append({
            'name': movie_name,
            'url': movie_url,
            'introduction': movie_intro
        })
    return movies

# Fetch and parse movies
content = fetch_movies(url)
if content:
    movies_list = parse_movies(content)

    # Save the movies to the Excel sheet
    for i, movie in enumerate(movies_list, start=1):
        sheet.append([i, movie['url'], movie['name'], movie['introduction']])
    
    workbook.save('top_movies.xlsx')
    print("Movies data saved successfully in 'top_movies1.xlsx'.")

print("Scraping completed.")
