import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links_with_images(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all links and their associated images
        links_with_images = []
        for link_tag in soup.find_all('a', href=True):
            link = urljoin(url, link_tag['href'])

            # Extract images associated with the link
            images = [urljoin(url, img['src']) for img in link_tag.find_all('img', src=True)]

            links_with_images.append({
                'link': link,
                'images': images
            })

        return links_with_images
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
        return None

# Example usage:
url_to_scrape = 'https://www.flipkart.com/'
result = extract_links_with_images(url_to_scrape)

if result:
    for entry in result:
        print(f"Link: {entry['link']}")
        print(f"Images: {entry['images']}")
        print("\n")
