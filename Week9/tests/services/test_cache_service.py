from src.services.cache_service import get_cache


def test_cache_miss():
    value = get_cache("non-existing-key")
    assert value is None
