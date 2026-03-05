"""
Prosty scoring niszy produktowej.
"""


def score_product(product, all_products):
    """
    Liczy scoring dla pojedynczej oferty.
    """

    score = 0

    price = product["price"]
    sales = product["sales"]

    # Cena 30-200 zł
    if 30 <= price <= 200:
        score += 20

    # Sprzedaż
    if 30 <= sales <= 200:
        score += 20

    # Liczba sprzedawców
    sellers = set(p["seller"] for p in all_products)

    if len(sellers) < 15:
        score += 20

    # Dominujący sprzedawca
    seller_sales = {}

    for p in all_products:
        seller_sales[p["seller"]] = seller_sales.get(p["seller"], 0) + p["sales"]

    if seller_sales:
        max_sales = max(seller_sales.values())
        total_sales = sum(seller_sales.values())

        if max_sales / total_sales < 0.5:
            score += 20

    # Słabe oferty (mało zdjęć)
    weak_offers = [p for p in all_products if p["images"] < 3]

    if len(weak_offers) > len(all_products) * 0.3:
        score += 20

    return score
