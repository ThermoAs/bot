import math


def calculate_niche_score(niche):

    total_sales = niche["total_sales"]
    sellers = niche["sellers"]
    monopoly_index = niche["monopoly_index"]
    avg_price = niche["avg_price"]

    demand_score = math.log(total_sales + 1)

    competition_score = 1 / sellers if sellers else 0

    monopoly_score = 1 - monopoly_index

    price_score = 1 if 30 <= avg_price <= 200 else 0

    final_score = (
        demand_score * 0.35 +
        competition_score * 0.30 +
        monopoly_score * 0.25 +
        price_score * 0.10
    )

    niche["niche_score"] = round(final_score, 3)

    return niche
