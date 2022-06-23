from threading import Event, Thread
from queue import Queue
from time import sleep


event = None
fila = None


class Worker(Thread):
    def __init__(self, target, queue, *, name='Worker'):
        super().__init__()
        self.name = name
        self.queue = queue
        self._target = target
        self._stoped = False
        print(self.name, 'started', end='\n')

    def run(self):
        event.wait()
        while not self.queue.empty():
            item = self.queue.get()
            print(self.name, f'item: {item}')
            if item == 'Kill':
                self.queue.put(item)
                self._stoped = True
                break
            self._target(item)

    def join(self):
        while not self._stoped:
            sleep(0.1)


def create_queue(ids: list, queue_maxsize: int):
    global event, fila
    event = Event()
    fila = Queue(maxsize=queue_maxsize)
    [fila.put(item) for item in ids]
    event.set()
    fila.put('Kill')
    return fila


def get_workers(function, queue, qtd_workers: int):
    """Retorna um número n de Threads."""
    return [Worker(target=function, queue=queue, name=f'Worker[{n}]')
            for n in range(qtd_workers)]
