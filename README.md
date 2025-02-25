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

Tools: Python with requests (fetch pages), beautifulsoup4 (parse HTML), pandas (load CSV).
Approach:
Load sample-websites.csv into a list.
Scrape each site for phone numbers (regex), social links (\<a> tags), and optionally addresses (keyword heuristic).
Save to scraped_data.json.
Decisions:
Chose BeautifulSoup over Scrapy for simplicity since it’s a small list initially.
Basic regex for phones (\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b) to catch common formats.
Error handling to skip failed requests gracefully.
Status: In progress—tested with 5 sites, refining extraction logic next.

### Step 2: Data Analysis

(To be filled as I complete this step)

### Step 3: Scaling

(To be filled as I complete this step)

### Step 4: Data Retrieval (Storing Part)

(To be filled as I complete this step)

### Step 5: Querying (API Part)

(To be filled as I complete this step)

### Bonus: Match Accuracy

(To be filled if I tackle this)
Potential for Improvement
Where could this go with more time or resources?

Scraping: Use Scrapy for async scraping or ML to detect data patterns dynamically.
Analysis: Add visualizations (e.g., coverage charts) for better insights.
Scaling: Deploy on AWS Lambda for parallel processing beyond 10 minutes.
Storage: Index more fields (e.g., emails) and optimize Elasticsearch mappings.
API: Add caching (Redis) and support for partial matches with confidence scores.
First Impression: The initial scraper could miss complex sites (e.g., JavaScript-heavy ones); a headless browser like Puppeteer could fix that.

## How to Run It

Step-by-step instructions to set up and execute the project.

Prerequisites
Python 3.x
Node.js (for API, TBD)
Elasticsearch (TBD)
Dependencies: pip install requests beautifulsoup4 pandas

### Setup

1. Clone the repo: `git clone <repo-url>`
2. Place `sample-websites.csv` in the root directory.
3. Create a virtual environment:

   ```bash
   python -m venv venv
    ```

4. Activate it Mac/Linux: `source venv/bin/activate`
5. Install dependencies `pip install -r requiremets.txt`

#### Running the Scraper

Run: python scrape.py
Output: Check scraped_data.json for results.

#### Running the API

(To be filled once API is built)

## Notes

Current date: February 25, 2025
Time spent so far: ~1 hour (planning + initial scraper draft)