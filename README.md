# Público News Scraper

This tool allows for the extraction of news articles from the [Público](https://www.publico.pt). The scrapper joins the news metadata from the Público API with the texts by scrapping the news URL.

## Setup & Usage Instructions

Below are the steps to set up your environment and run the scraper on your machine.

### Environment Setup

1. Create and activate a Python virtual environment.

```shell
virtualenv venv --python=python3.8
source venv/bin/activate
```

2. Install the project dependencies.

```shell
pip install -r requirements.txt
```

### Scraping Data

To scrape news articles for a specific date range, use the following command:

```shell
python scrape.py
```
