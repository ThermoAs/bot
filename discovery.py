from config import MAX_DISCOVERED_PRODUCTS, VISITED_PRODUCTS


def discover_products(page, product_urls):
    """
    Otwiera strony ofert i zbiera podobne produkty.
    """

    discovered = []
    seen = set()

    for url in product_urls:

        if url in VISITED_PRODUCTS:
            continue

        try:

            VISITED_PRODUCTS.add(url)

            page.goto(url)
            page.wait_for_timeout(2000)

            links = page.query_selector_all("a")

            for link in links:

                href = link.get_attribute("href")

                if not href:
                    continue

                if "allegro.pl/oferta" not in href:
                    continue

                if href in seen:
                    continue

                title = link.inner_text()

                if not title:
                    continue

                seen.add(href)

                discovered.append({
                    "title": title,
                    "url": href
                })

                if len(discovered) >= MAX_DISCOVERED_PRODUCTS:
                    return discovered

        except Exception:
            continue

    return discovered
