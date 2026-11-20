from statistics import median

def compute_authoritative_price(prices):
    values = [p["price_value"] for p in prices]
    med = median(values)
    clean = [v for v in values if abs(v - med) < 0.4 * med]
    return sum(clean) / len(clean), "median_outlier_rejection"