from src.core.redis import redis_client
from src.utils.metrics import log_hit, log_miss


def get_cache(key: str) -> str | None:
    """
    Fetch value from Redis cache.
    """
    value = redis_client.get(key)
    if value:
        log_hit(key)
        return value
    log_miss(key)
    return None


def set_cache(key: str, value: str, ttl: int) -> None:
    """
    Store value in Redis with TTL.
    """
    redis_client.setex(key, ttl, value)


def invalidate_cache(pattern: str) -> None:
    """
    Delete cache keys matching pattern.
    """
    for key in redis_client.scan_iter(pattern):
        redis_client.delete(key)
