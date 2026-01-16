"""Configuration for data generation."""

# ==================== MERCHANT CATEGORIES ====================
MERCHANT_CATEGORIES = [
    'grocery',
    'restaurant',
    'gas_station',
    'pharmacy',
    'electronics',
    'clothing',
    'entertainment',
    'travel',
    'utilities',
    'online_retail'
]

# ==================== TYPICAL SPENDING BY CATEGORY ====================
CATEGORY_SPENDING_RANGES = {
    'grocery': (20, 150),
    'restaurant': (15, 80),
    'gas_station': (30, 70),
    'pharmacy': (10, 100),
    'electronics': (50, 500),
    'clothing': (30, 200),
    'entertainment': (20, 150),
    'travel': (100, 1000),
    'utilities': (50, 300),
    'online_retail': (25, 250)
}

# ==================== GEOGRAPHIC BOUNDARIES ====================
# US bounding box (approximately)
US_LAT_RANGE = (25.0, 49.0)  # Southern to Northern US
US_LON_RANGE = (-125.0, -66.0)  # Western to Eastern US

# ==================== FRAUD PROBABILITIES ====================
FRAUD_PROBABILITY = 0.02  # 2% of transactions are fraudulent
