import json
from pathlib import Path

import requests
from bs4 import BeautifulSoup

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True)


def get_text(url: str) -> str:
    """Extracts the text from a news article given its url."""
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    text_element = soup.find(name="div", id="story-body")
    text = "\n".join(
        p_element.text
        for p_element in text_element.find_all("p")
    )
    return text


def main():
    max_id = 3_000_000
    for news_id in range(max_id):
        print(f"Working in id {news_id}/{max_id}")
        url = f'https://www.publico.pt/api/content/news/{news_id}'

        try:
            response = requests.get(url, timeout=10)
        except:
            print(f"Did not get a response from url {url}")
            continue

        if response.status_code == 200:
            print("\tFound content.")
            content = response.json()
            news_url = content["shareUrl"]

            try:
                text = get_text(news_url)
            except:
                print(f"\tWas not able to extract text from {news_url}.")
                continue

            if not text:
                continue

            content["texto"] = text

            with open(DATA_PATH / f"{news_id}.json", "w") as fout:
                json.dump(content, fout, indent=4)


if __name__ == "__main__":
    main()
