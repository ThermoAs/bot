"""
Obsługa Google Sheets.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def connect(creds_file, sheet_name):
    """
    Łączy z Google Sheets.
    """

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        creds_file,
        scope
    )

    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1

    return sheet


def append_rows(sheet, rows):
    """
    Dodaje dane do arkusza.
    """

    values = []

    for r in rows:
        values.append([
            r["phrase"],
            r["title"],
            r["price"],
            r["sales"],
            r["seller"],
            r["opinions"],
            r["smart"],
            r["images"],
            r["score"]
        ])

    sheet.append_rows(values)
