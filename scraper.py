"""
Scraper Allegro oparty o Playwright.

Pobiera dane z pierwszej strony wyników wyszukiwania.
"""

from playwright.sync_api import sync_playwright
import re


BASE_URL = "https://allegro.pl/listing?string="


def extract_number(text):
    """
    Wyciąga liczbę z tekstu.
    """
    if not text:
        return 0

    numbers = re.findall(r"\d+", text.replace(" ", ""))
    return int(numbers[0]) if numbers else 0


def scrape_phrase(phrase):
    """
    Scrape pierwszej strony wyników dla danej frazy.
    """

    results = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        search_url = BASE_URL + phrase.replace(" ", "+")

        page.goto(search_url)
        page.wait_for_timeout(3000)

        offers = page.query_selector_all('[data-role="offer"]')

        for offer in offers:

            try:

                title_el = offer.query_selector("h2")
                title = title_el.inner_text() if title_el else ""

                price_el = offer.query_selector('[data-testid="price"]')
                price_text = price_el.inner_text() if price_el else ""

                price = extract_number(price_text)

                sales_el = offer.query_selector("span:has-text('kupionych')")
                sales = extract_number(sales_el.inner_text()) if sales_el else 0

                seller_el = offer.query_selector("a[data-testid='seller-name']")
                seller = seller_el.inner_text() if seller_el else ""

                opinion_el = offer.query_selector("span:has-text('%')")
                opinions = extract_number(opinion_el.inner_text()) if opinion_el else 0

                smart = bool(offer.query_selector("img[alt='Smart!']"))

                images = len(offer.query_selector_all("img"))

                results.append({
                    "phrase": phrase,
                    "title": title,
                    "price": price,
                    "sales": sales,
                    "seller": seller,
                    "opinions": opinions,
                    "smart": smart,
                    "images": images
                })

            except Exception:
                continue

        browser.close()

    return results


def scrape_all_phrases(phrases):
    """
    Scrape wielu fraz.
    """

    all_results = []

    for phrase in phrases:
        data = scrape_phrase(phrase)
        all_results.extend(data)

    return all_results
