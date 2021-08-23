import time
from multiprocessing import Process


start = time.perf_counter()


def show(name, delay):
    print(f'Stating - {name}')
    time.sleep(delay)
    print(f'Finishing - {name}')


class ShowProcess(Process):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        show(self.name, self.delay)


p1 = ShowProcess('One', 3)
p2 = ShowProcess('Two', 3)


p1.start()
p2.start()


p1.join()
p2.join()

end = time.perf_counter()


print(end - start)

