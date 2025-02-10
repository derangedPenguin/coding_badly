from time import perf_counter
from typing import Callable

from functools import wraps

class TimeTracker:

    times = {}

    def get_avgs(self) -> dict:
        # visual_dict = {}
        # for func_name, array in self.times.items():
        #     if len(array) != 0:
        #         visual_dict[func_name] = sum(array)/len(array)
        # return visual_dict
        return {name:(('did not run') if (len(array) == 0) else (sum(array)/len(array))) for name, array in self.times.items()}

    def track_time(self, func) -> Callable:
        self.times[func.__name__] = set()
        @wraps(func)
        def wrapper(*args):
            start_time = perf_counter()
            val = func(*args)
            self.times[func.__name__].add(perf_counter() - start_time)
            return val
        return wrapper

#tests
if __name__ == "__main__":
    time_tracker = TimeTracker()

    @time_tracker.track_time
    def thingymabobber():
        sum = 0
        for i in range(5000000):
            sum += 1
        return sum

    print(thingymabobber())
    for i in range(50):
        thingymabobber()
    print(time_tracker.times)
    print(time_tracker.get_avgs())