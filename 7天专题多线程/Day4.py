'''第四天'''
'''
1.如何创建一个新的线程？
使用threading.Thread实例化对象
'''
import threading
import time
# 使用Thread对象将要执行的任务函数作为参数传入
def job1(name):
    print(f'starting thread{name}')


t = threading.Thread(target=job1, args=('thread-1',))
t.start()

time.sleep(2)
print('done')
# 继承Thread类并且重写run方法
class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self) #创建自己的继承的线程需要把这个加上
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      print_time(self.name, self.counter, 5)
      print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
   while counter:
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("Exiting Main Thread")
'''
3.什么是死锁？
若干子线程在系统资源竞争时，都在等待对方对某部分资源解除占用状态，结果是谁也不愿先解锁，互相干等着，程序无法执行下去，这就是死锁。
下面的例子,程序会永远卡在那里
'''
from threading import Lock
import time

lock1 = Lock()
lock2 = Lock()

def work1(num):
    lock1.acquire()  # lock1上锁
    time.sleep(1)
    print("in work1")
    lock2.acquire()  # lock2上锁
    print("work1-----")
    lock2.release()  # lock2解锁
    lock1.release()  # lock1解锁

def work2(num):
    lock2.acquire()  # lock2加锁
    print("in work2")
    lock1.acquire()  # lock1加锁
    print("work1-----")
    lock1.release()  # lock1解锁
    lock2.release()  # lock2解锁
# t1 = threading.Thread(target=work1,args=(1000000,))
# t2 = threading.Thread(target=work2, args=(1000000,))
# t1.start()
# t2.start()
'''
3.介绍一下python的线程同步？
一、 setDaemon(False) 当一个进程启动之后，会默认产生一个主线程，
因为线程是程序执行的最小单位，当设置多线程时，主线程会创建多个子线程，
在Python中，默认情况下就是setDaemon(False),主线程执行完自己的任务以后，
就退出了，此时子线程会继续执行自己的任务，直到自己的任务结束。

二、 setDaemon（True) 当我们使用setDaemon(True)时，这是子线程为守护线程，
主线程一旦执行结束，则全部子线程被强制终止

三、 join（线程同步) join 所完成的工作就是线程同步，即主线程任务结束以后，
进入堵塞状态，一直等待所有的子线程结束以后，主线程再终止。当设置守护线程时，
含义是主线程对于子线程等待timeout的时间将会杀死该子线程，最后退出程序，
所以说，如果有10个子线程，全部的等待时间就是每个timeout的累加和，
简单的来说，就是给每个子线程一个timeout的时间，让他去执行，时间一到，
不管任务有没有完成，直接杀死。没有设置守护线程时，
主线程将会等待timeout的累加和这样的一段时间，时间一到，
主线程结束，但是并没有杀死子线程，子线程依然可以继续执行，
直到子线程全部结束，程序退出。
'''