import re
from config import MAX_OFFERS_PER_PHRASE

BASE_URL = "https://allegro.pl/listing?string="


def extract_number(text):
    """
    Wyciąga pierwszą liczbę z tekstu.
    """
    if not text:
        return 0

    numbers = re.findall(r"\d+", text.replace(" ", ""))
    return int(numbers[0]) if numbers else 0


def scrape_phrase(page, phrase):
    """
    Scrape pierwszej strony wyników Allegro.
    """

    results = []

    search_url = BASE_URL + phrase.replace(" ", "+")

    page.goto(search_url)
    page.wait_for_timeout(3000)

    offers = page.query_selector_all("article")

    for offer in offers[:MAX_OFFERS_PER_PHRASE]:

        try:

            title_el = offer.query_selector("h2")
            title = title_el.inner_text() if title_el else ""

            link_el = offer.query_selector("a")
            link = link_el.get_attribute("href") if link_el else ""

            price_el = offer.query_selector('[data-testid="price"]')
            price = extract_number(price_el.inner_text()) if price_el else 0

            sales_el = offer.query_selector("span:has-text('kupionych')")
            sales = extract_number(sales_el.inner_text()) if sales_el else 0

            seller_el = offer.query_selector("a[data-testid='seller-name']")
            seller = seller_el.inner_text() if seller_el else ""

            smart = bool(offer.query_selector("img[alt='Smart!']"))

            images = len(offer.query_selector_all("img"))

            results.append({
                "phrase": phrase,
                "title": title,
                "url": link,
                "price": price,
                "sales": sales,
                "seller": seller,
                "smart": smart,
                "images": images
            })

        except Exception:
            continue

    return results


def scrape_all_phrases(page, phrases):

    all_results = []

    for phrase in phrases:

        try:
            data = scrape_phrase(page, phrase)
            all_results.extend(data)

        except Exception:
            continue

    return all_results
