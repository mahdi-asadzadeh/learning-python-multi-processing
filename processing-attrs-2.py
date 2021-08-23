from multiprocessing import Process, current_process
import time
import os


start = time.perf_counter()


def show(name):
    print(f'Stating - {name}')
    time.sleep(3)
    print(current_process())
    print(os.getpid())
    print('parent id : ', os.getppid())
    print(f'Finishing - {name}')


p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))


p1.start()
p2.start()


print(p1.is_alive())
print(p2.is_alive())

p1.join()
p2.join()


end = time.perf_counter()


print(end - start)
