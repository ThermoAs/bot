"""
Główny plik aplikacji.
"""

from scraper import scrape_all_phrases
from scoring import score_product
from sheets import connect, append_rows
from config import SEARCH_PHRASES, GOOGLE_SHEETS_NAME, GOOGLE_CREDS_FILE


def main():

    print("Scraping Allegro...")

    products = scrape_all_phrases(SEARCH_PHRASES)

    print("Liczenie scoringu...")

    for p in products:
        p["score"] = score_product(p, products)

    print("Łączenie z Google Sheets...")

    sheet = connect(GOOGLE_CREDS_FILE, GOOGLE_SHEETS_NAME)

    append_rows(sheet, products)

    print("Gotowe.")


if __name__ == "__main__":
    main()
