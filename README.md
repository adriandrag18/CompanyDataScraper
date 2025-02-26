# CompanyDataScraper

## Overview

This project implements an API to extract and retrieve company data as part of a Software Engineer assignment. The goal is to scrape company details (phone numbers, social media links, and optionally addresses) from a list of websites, analyze the data, scale the process, store it efficiently, and provide a REST API to query company profiles with high match accuracy.

## Ideal High-Level View

The perfect solution in an ideal world—what would this look like if time, tools, and resources weren’t constraints?

- **Goal**: Build a robust, scalable system that extracts comprehensive company data from any website and serves it via a fast, accurate API.
- **Extraction**: A smart web scraper that uses AI to identify and extract all relevant company data (phones, social links, addresses, emails, etc.) with near-100% accuracy, adapting to any website structure.
- **Storage**: A cloud-hosted, searchable database (e.g., Elasticsearch) with real-time updates and infinite scalability.
API: A RESTful API with fuzzy matching, natural language input, and sub-second response times, deployed globally via CDN.
- **Performance**: Scrape thousands of sites in minutes using distributed computing, with zero downtime or rate-limiting issues.

## Implementation

How I actually built it—tools, decisions, and trade-offs.

### Step 1: Data Extraction (Scraping Part)

- **Tools**: Python with requests (fetch pages), beautifulsoup4 (parse HTML), pandas (load CSV).
- **Approach**: Load sample-websites.csv into a list.
Scrape each site for phone numbers (regex), social links (\<a> tags), and optionally addresses (keyword heuristic).
Save to scraped_data.json.
- **Decisions**: Chose BeautifulSoup over Scrapy for simplicity since it’s a small list initially.
Basic regex for phones (\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b) to catch common formats.
Error handling to skip failed requests gracefully.
Status: In progress—tested with 5 sites, refining extraction logic next.

### Step 2: Data Analysis

(To be filled as I complete this step)

### Step 3: Scaling

(To be filled as I complete this step)

### Step 4: Data Retrieval (Storing Part)

- **Tools**: Python, Elasticsearch, Pandas
- **Approach**: Merge scraped data (scrapedData.json) with websites-company-names.csv on 'website' and 'domain'. Store in Elasticsearch index 'company_profiles'.
- **Decisions**: Used Pandas for merging due to familiarity; Elasticsearch for fast, fuzzy querying as recommended.
- **Status**: Implemented—data indexed successfully.

### Step 5: Querying (API Part)

- **Tools**: Python, FastAPI, Elasticsearch
- **Approach**: Built a POST /api/match endpoint accepting name, website, phone, and facebook. Uses Elasticsearch bool query with fuzzy matching on 'all_names' for flexibility.
- **Decisions**: Chose FastAPI over Node.js Express for consistency with Python scraping code and simpler setup for me. Fuzzy matching prioritizes name (via all_names) for broader coverage.
- **Status**: Implemented—returns best match or error if none found.
- **Motivation**: Sticking to Python reduces context-switching and leverages my existing Python knowledge for quicker iteration.

### Bonus: Match Accuracy

(To be filled if I tackle this)

### Potential for Improvement

Where could this go with more time or resources?

Scraping: Use Scrapy for async scraping or ML to detect data patterns dynamically.
Analysis: Add visualizations (e.g., coverage charts) for better insights.
Scaling: Deploy on AWS Lambda for parallel processing beyond 10 minutes.
Storage: Index more fields (e.g., emails) and optimize Elasticsearch mappings.
API: Add caching (Redis) and support for partial matches with confidence scores.
First Impression: The initial scraper could miss complex sites (e.g., JavaScript-heavy ones); a headless browser like Puppeteer could fix that.

## How to Run It

Step-by-step instructions to set up and execute the project.

### Prerequisites

- Python 3.9
- Elasticsearch (running locally on port 9200) or
- Docker (for Elasticsearch)
- Dependencies: pip install -r requirements.txt

### Setup

1. Clone the repo: `git clone <repo-url>`
2. (Optional) Create a virtual environment and activate it: `python -m venv venv & source venv/bin/activate`
3. Install dependencies `pip install -r requiremets.txt`

#### Running the Scraper

- `colima start` (remove)
- Start Elasticsearch: `docker run -d -p 9200:9200 -e "ELASTIC_PASSWORD=myVerySecurePassword" elasticsearch:8.11.0`
- Run: python scrape.py
- Output: Check scrapedData.json for results and companyProfiles index in ES

#### Running the API

- Start Elasticsearch: `docker run -d -p 9200:9200 -e "ELASTIC_PASSWORD=myVerySecurePassword" elasticsearch:8.11.0`
- Store data: `python store.py`
- Run API: `python api.py`
- Test: `curl -X POST "http://localhost:8000/api/match" -H "Content-Type: application/json" -d '{"name": "Greater Boston Zen Center"}'`

## Notes

- Date: February 25, 2025
Time spent so far: ~1 hour (planning + initial scraper draft)

- Date: February 26, 2025
Time spent so far: ~3 hours (planning, scraper, storage, API)
