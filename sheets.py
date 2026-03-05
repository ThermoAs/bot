import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect(creds_file, sheet_name):

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        creds_file,
        scope
    )

    client = gspread.authorize(creds)

    return client.open(sheet_name).sheet1


def append_raw_products(sheet, products):

    rows = []

    for p in products:

        rows.append([
            p["phrase"],
            p["title"],
            p["price"],
            p["sales"],
            p["seller"],
            p["images"],
            p["url"]
        ])

    sheet.append_rows(rows)


def append_niche_ranking(sheet, niches):

    rows = []

    for n in niches:

        rows.append([
            n["phrase"],
            n["total_sales"],
            n["sellers"],
            n["avg_price"],
            n["monopoly_index"],
            n["niche_score"]
        ])

    sheet.append_rows(rows)
