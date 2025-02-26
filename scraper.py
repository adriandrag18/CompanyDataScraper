import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
import os
from clientElasticsearch import EsClient


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
            'domain': domain,
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

    print("Scraping complete! Results saved to scrapedData.json")

    storeInEs = os.getenv('STORE_IN_ES', 'false').lower() == 'true'
    if storeInEs:
        esClient = EsClient()
        companyDf = pd.read_csv('websites-company-names.csv')
        mergedDf = pd.merge(
            pd.DataFrame(results), companyDf, left_on='domain', right_on='domain', how='right'
        ).replace({pd.NA: None, float('nan'): None})

        for _, row in mergedDf.iterrows():
            doc = {
                'domain': domain,
                'website': row['website'],
                'phones': row['phones'],
                'socialLinks': row['socialLinks'],
                'address': row['address'],
                'commercialName': row['company_commercial_name'],
                'legalName': row['company_legal_name'],
                'allNames': row['company_all_available_names']
            }
            esClient.index(index='companyProfiles', id=row['website'], body=doc)
        print(f"Stored {esClient.count('companyProfiles')} documents in Elasticsearch")


if __name__ == '__main__':
    main()