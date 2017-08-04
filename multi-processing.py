from multiprocessing import pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p=pool
    for i in range(5):
        p.AsyncResult(long_time_task)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
