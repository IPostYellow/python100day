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
'''
2.说说线程的几种状态
答：
new:线程对象已经创建，还没有在其上调用start()方法
runable:
1.当线程有资格运行，但调度程序还没有将它列为运行线程时线程所处的状态
2.当start方法被调用时，线程首先进入可运行状态
3.在线程运行之后或者从阻塞、等待或睡眠状态回来后，也返回到可运行状态
running:
1.线程调度程序从可运行池中选择一个线程作为当前线程时线程所处的状态
2.这也是线程进入运行状态的唯一一种方式
waiting/block/sleep:
1.这是线程有资格运行时它所处的状态
2.实际上这三个状态组合为一种，有共同点是：线程仍旧是活的(可运行的)，但是当前没有条件运行
terminated:线程在完成执行或者异常中止时进入终止状态
'''
'''
3.说说多线程中的信号量(semaphore)
答：
信号量是一个内部数据，用于标明当前的共享资源可以有多少并发读取
每当线程想要读取关联了信号量的共享资源时，必须调用acquire()，此操作减少信号量的内部变量，如果此变量的值非负，
那么分配该资源的权限。如果是负值，那么线程被挂起，直到有其他的线程函数释放资源
当线程不需要该共享资源，必须通过release()释放。这样，信号的内部变量增加，在信号量等待队列中排最前面的线程会拿
到共享资源的权限。
信号量通常用于防范容量有限的资源，例如数据库服务器。一般而言，信号量可以控制释放固定量的线程。比如启动100个线程，
信号量的控制值设为5，那么前5个线程拿到信号量后，其余线程只能阻塞，等到这5个线程释放信号量锁之后才能去拿锁
'''
import threading
import time

def func(n):
    with semaphore:
        time.sleep(10)
        print("Thread:", n)
semaphore = threading.BoundedSemaphore(5)
tread_list=[]
for i in range(20):
    t=threading.Thread(target=func,args=(i,))
    tread_list.append(t)
    t.start()

for j in tread_list:
    j.join()
print("all threads done")
