import time
from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor


start = time.perf_counter()


def show(name):
    print(f'Stating - {name}')
    time.sleep(3)
    print(f'Finishing - {name}')


with ProcessPoolExecutor(max_workers=2) as executer:
    names = ['One', 'Two', 'Three', 'Four']
    executer.map(show, names)


end = time.perf_counter()


print(end - start)

