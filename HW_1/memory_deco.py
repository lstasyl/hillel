import tracemalloc
import functools
import requests


def memory_deco(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = f(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage: {current / 10**6}MB; Peak: {peak / 10**6}MB")
        return result
    return wrapper

@memory_deco
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


if __name__ == "__main__":
    url = "https://www.example.com"
    content = fetch_url(url)
    print(content)
