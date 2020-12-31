'''第六天'''
'''
1.thread.join()方法的作用？
答：
等待至线程中止。这阻塞调用线程直至线程的join()方法被调用中止-
也就是正常退出或者抛出未处理的异常或者是可选的超时发生。
'''
import threading
import time


def t1(name):
    time.sleep(2)
    print(f'starting thread{name}')


t = threading.Thread(target=t1, args=('thread-1',))
t.start()
t.join()
print('done')
