"""
Konfiguracja bota Allegro.
"""

SEARCH_PHRASES = [
    "mata do jogi",
    "organizer do szuflady",
    "lampka nocna led"
]

GOOGLE_SHEETS_NAME = "allegro_product_research"
GOOGLE_CREDS_FILE = "credentials.json"

# limity
MAX_OFFERS_PER_PHRASE = 30
MAX_DISCOVERED_PRODUCTS = 50

# cache odwiedzonych produktów
VISITED_PRODUCTS = set()
