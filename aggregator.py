def aggregate_by_phrase(products):
    """
    Agreguje dane ofert na poziomie niszy (frazy).
    """

    niches = {}

    for p in products:

        phrase = p["phrase"]

        if phrase not in niches:

            niches[phrase] = {
                "offers": 0,
                "sellers": set(),
                "total_sales": 0,
                "prices": [],
                "seller_sales": {}
            }

        niche = niches[phrase]

        niche["offers"] += 1
        niche["sellers"].add(p["seller"])
        niche["total_sales"] += p["sales"]
        niche["prices"].append(p["price"])

        niche["seller_sales"][p["seller"]] = \
            niche["seller_sales"].get(p["seller"], 0) + p["sales"]

    results = []

    for phrase, data in niches.items():

        sellers = len(data["sellers"])
        total_sales = data["total_sales"]

        avg_price = sum(data["prices"]) / len(data["prices"])

        top_seller_sales = max(data["seller_sales"].values())

        monopoly_index = (
            top_seller_sales / total_sales if total_sales else 0
        )

        results.append({
            "phrase": phrase,
            "offers": data["offers"],
            "sellers": sellers,
            "total_sales": total_sales,
            "avg_price": avg_price,
            "top_seller_sales": top_seller_sales,
            "monopoly_index": monopoly_index
        })

    return results
