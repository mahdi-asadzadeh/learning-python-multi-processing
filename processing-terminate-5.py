import time
from multiprocessing import Process


start = time.perf_counter()


def show(name):
    print(f'Stating - {name}')
    time.sleep(3)
    print(f'Finishing - {name}')


p1 = Process(target=show, args=('One',))
p2 = Process(target=show, args=('Two',))


p1.start()
p2.start()


p1.terminate()
p2.terminate()


p1.join()
p2.join()


print(p1.exitcode)
print(p2.exitcode)


print(p1.is_alive())
print(p2.is_alive())


end = time.perf_counter()


print(end - start)
