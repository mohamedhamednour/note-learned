import time
from functools import lru_cache

def fib_no_cache(n):
    if n < 2:
        return n
    return fib_no_cache(n-1) + fib_no_cache(n-2)

@lru_cache(maxsize=None)
def fib_with_cache(n):
    if n < 2:
        return n
    return fib_with_cache(n-1) + fib_with_cache(n-2)

start = time.time()
print(fib_no_cache(30))  # حساب بدون كاش
end = time.time()
print("Time without cache:", end - start, "seconds")

start = time.time()
print(fib_with_cache(30))  # حساب مع كاش
end = time.time()
print("Time with cache (first call):", end - start, "seconds")

start = time.time()
print(fib_with_cache(30))  # استدعاء ثاني مع الكاش
end = time.time()
print("Time with cache (second call):", end - start, "seconds")
