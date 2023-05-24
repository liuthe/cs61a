import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Base URL for the lecture slides
base_url = "https://cs61a.org/assets/slides/"

# URL of the lecture page
url = "https://cs61a.org/"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = [link for link in soup.find_all('a')]

# Create a directory to store the downloaded files
if not os.path.exists('pdf_files'):
    os.makedirs('pdf_files')

# Loop through each link on the page
for link in links:
    link_url = link.get('href')
    if link_url and not link_url.startswith('#') and not link_url.startswith('mailto:'):
        if link_url.endswith('.pdf'):
            # If the link is a direct PDF link, download it
            file_name = link_url.split('/')[-1]
            file_path = os.path.join('pdf_files', file_name)
            print(f'Downloading {file_name}...')
            file_response = requests.get(urljoin(base_url, link_url))
            with open(file_path, 'wb') as f:
                f.write(file_response.content)
            print(f'{file_name} downloaded successfully!')
        else:
            # If the link is not a PDF link, follow it and download any PDF files that are linked on the resulting page
            link_response = requests.get(urljoin(url, link_url))
            link_soup = BeautifulSoup(link_response.content, 'html.parser')
            pdf_links = [pdf_link for pdf_link in link_soup.find_all('a') if pdf_link.get('href') is not None and pdf_link.get('href').endswith('.pdf')]
            for pdf_link in pdf_links:
                pdf_url = pdf_link.get('href')
                file_name = pdf_url.split('/')[-1]
                file_path = os.path.join('pdf_files', file_name)
                print(f'Downloading {file_name}...')
                pdf_response = requests.get(urljoin(base_url, pdf_url))
                with open(file_path, 'wb') as f:
                    f.write(pdf_response.content)
                print(f'{file_name} downloaded successfully!')

