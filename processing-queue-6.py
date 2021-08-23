import time
from multiprocessing import Process, Queue


start = time.perf_counter()


number = []


def func_1(queue):
    nums = queue.get()
    nums.extend([1, 2, 3])
    queue.put(nums)
    print(nums)

   
def func_2(queue):
    nums = queue.get()
    nums.extend([4, 5, 6])
    queue.put(nums)
    print(nums)


q = Queue()
q.put(number)


p1 = Process(target=func_1, args=(q, ))
p2 = Process(target=func_2, args=(q, ))


p1.start()
p2.start()


p1.join()
p2.join()


end = time.perf_counter()


print(end - start)


print(q.get())
