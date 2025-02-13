import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time= time.time()
        result= func(*args, *kwargs)
        print(func)
        time_taken= time.time() - start_time
        print(f"Total time taken {time_taken}")
        return result
    return wrapper

@timer
def time_test():
    for _ in range(1000000):
        pass

@timer
def time_test2():
    time.sleep(2)

time_test()
time_test2()