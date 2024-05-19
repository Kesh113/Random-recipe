import time

def timer(func):
    t1 = time.perf_counter()
    func()
    t2 = time.perf_counter()
    print(t2-t1)
