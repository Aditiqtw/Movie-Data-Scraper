# Movie Data Scraper
Movie Data Scraper
This project is a Python-based web scraper designed to extract and save data from top-rated movie websites into an Excel file. Leveraging libraries such as requests, BeautifulSoup, and xlwt, this tool efficiently retrieves movie information, making it easy to analyze and store.

Features
Data Extraction: Scrapes movie titles, URLs, and descriptions from specified websites.
Excel Export: Saves the extracted data into a structured Excel file for easy viewing and analysis.
Error Handling: Implements robust error handling to manage potential issues during scraping, such as missing elements or connection problems.
Customizable Headers: Allows for the modification of HTTP request headers to mimic different user agents.
Requirements
Python 3.x
requests library
beautifulsoup4 for HTML parsing
xlwt for Excel file creation
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Movie-Data-Scraper.git
cd Movie-Data-Scraper
Install the required libraries:

bash
Copy code
pip install requests beautifulsoup4 xlwt
Usage
Run the script:

bash
Copy code
python requestsProxy.py
The scraped data will be saved in an Excel file named movies_top100.xls.


