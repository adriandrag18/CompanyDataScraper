import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json

def scrapeWebsite(domain: str):
    url = f'http://{domain}'
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        phones = extractPhoneNumbers(soup)
        socialLinks = extractSocialMediaLinks(soup)
        address = extractAddress(soup)
        
        return {
            'website': url,
            'phones': phones if phones else None,
            'socialLinks': socialLinks if socialLinks else None,
            'address': address
        }
    
    except requests.RequestException as e:
        print(f"Failed to scrape {url}: {e}")
        return {'website': url, 'phones': None, 'socialLinks': None, 'address': None}


def extractAddress(soup):
    address = None
    address_keywords = ['street', 'avenue', 'road', 'city', 'zip']
    for text in soup.stripped_strings:
        if any(keyword in text.lower() for keyword in address_keywords):
            address = text
            break
    return address


def extractSocialMediaLinks(soup):
    social_links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if 'facebook.com' in href:
            social_links.append(href)
        elif 'twitter.com' in href:
            social_links.append(href)
    return social_links


def extractPhoneNumbers(soup):
    phone_pattern = r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'
    phones = re.findall(phone_pattern, soup.get_text())
    phones = list(set(phones))
    return phones


def main():
    df = pd.read_csv('websites.csv')
    domains = df['domain'].tolist()
    print(domains[:5])
    results = []
    for domain in domains[:5]:
        print(f"Scraping {domain}...")
        result = scrapeWebsite(domain)
        results.append(result)

    with open('scrapedData.json', 'w') as f:
        json.dump(results, f, indent=2)

    print("Scraping complete! Results saved to scraped_data.json")


if __name__ == '__main__':
    main()