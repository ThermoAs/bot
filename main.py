from playwright.sync_api import sync_playwright

from scraper import scrape_all_phrases
from discovery import discover_products
from aggregator import aggregate_by_phrase
from scoring import calculate_niche_score
from sheets import connect, append_raw_products, append_niche_ranking

from config import SEARCH_PHRASES, GOOGLE_CREDS_FILE, GOOGLE_SHEETS_NAME


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        print("Scraping ofert...")

        products = scrape_all_phrases(page, SEARCH_PHRASES)

        urls = [p["url"] for p in products if p["url"]]

        print("Product discovery...")

        discovered = discover_products(page, urls)

        print("Agregacja nisz...")

        niches = aggregate_by_phrase(products)

        scored = []

        for n in niches:
            scored.append(calculate_niche_score(n))

        scored.sort(key=lambda x: x["niche_score"], reverse=True)

        top20 = scored[:20]

        print("Zapis do Google Sheets")

        sheet = connect(GOOGLE_CREDS_FILE, GOOGLE_SHEETS_NAME)

        append_raw_products(sheet, products)
        append_niche_ranking(sheet, top20)

        browser.close()

    print("Gotowe")


if __name__ == "__main__":
    main()
