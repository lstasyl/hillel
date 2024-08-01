import functools
import requests
from collections import defaultdict, OrderedDict


def lfu_cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._frequency[cache_key] += 1
                return deco._cache[cache_key]

            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                # Видаляємо елемент з найменшою частотою
                least_frequent_key = min(deco._frequency, key=deco._frequency.get)
                del deco._cache[least_frequent_key]
                del deco._frequency[least_frequent_key]

            deco._cache[cache_key] = result
            deco._frequency[cache_key] = 1
            return result

        deco._cache = OrderedDict()
        deco._frequency = defaultdict(int)
        return deco

    return internal

@lfu_cache(max_limit=10)
def fetch_url(url, first_n=100):
    """Fetch a given URL"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content

if __name__ == "__main__":
    url = "https://www.google.com"
    content = fetch_url(url)
    print(content)

