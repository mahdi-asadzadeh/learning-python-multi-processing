import time
from multiprocessing import Process


start = time.perf_counter()


def show(name):
    print(f'Stating - {name}')
    time.sleep(3)
    print(f'Finishing - {name}')


p1 = Process(target=show, args=('One',), daemon=True)
p2 = Process(target=show, args=('Two',), daemon=True)


p1.start()
p2.start()


end = time.perf_counter()


print(end - start)

