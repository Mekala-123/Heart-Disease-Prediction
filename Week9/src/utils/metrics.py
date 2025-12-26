import logging

logging.basicConfig(level=logging.INFO)

def log_hit(key: str) -> None:
    logging.info(f"CACHE HIT: {key}")

def log_miss(key: str) -> None:
    logging.info(f"CACHE MISS: {key}")
