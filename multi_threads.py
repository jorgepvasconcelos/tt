import pickle
from contextlib import contextmanager
from pprint import pprint
from worker import create_queue, get_workers


@contextmanager
def timeit(*args):
    start_time = datetime.now()
    yield
    time_elapsed = datetime.now() - start_time
    print(f'Tempo total (hh:mm:ss.ms) {time_elapsed}')


def baixa_(id: int):

    try:

    except:
        traceback.print_exc()
    finally:
        session.close()


if __name__ == '__main__':
    linhas = []
    with timeit():
        ids = [405448,
                       405447,
                       ]

        queue = create_queue(ids=ids, queue_maxsize=10)
        print(queue.queue)
        print(f"{'--' * 20}criando os Workers{'--' * 20}")
        thrs = get_workers(function=baixa_, queue=queue, qtd_workers=4)
        print(f"{'--' * 20}iniciando os Workers{'--' * 20}")
        [th.start() for th in thrs]
        print(f"{'--' * 20}iniciando os Joins{'--' * 20}")
        [th.join() for th in thrs]

    pprint(linhas)
