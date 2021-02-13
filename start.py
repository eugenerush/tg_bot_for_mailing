from multiprocessing import Process


def first():
    from test import executor, dp
    print('first is starting')


def second():
    from main import client, spam
    print('second is starting')


if __name__ == '__main__':
    p1 = Process(target=first)
    p1.start()
    p2 = Process(target=second)
    p2.start()
    p1.join()
    p2.join()

