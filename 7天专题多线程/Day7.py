'''第七天'''
'''
1.setDaemon方法的作用？
答：
属性daemon的值默认为False，如果需要修改，必须在调用start()方法启动线程之前进行设置。
如果某个子线程的daemon的属性为False，主线程结束时会检测该子线程是否结束，如果该子线程还在
运行，则主线程会等待它运行完成后再退出。
如果某个子线程的daemon属性为True，主线程运行结束时不对这个子线程进行检测而直接退出，同时
所有daemon值为True的子线程将随主线程一起结束，而不论是否运行完成。
'''
import threading
import time


def t1(name):
    time.sleep(2)
    print(f'starting thread {name}')


t = threading.Thread(target=t1, args=('thread-1',))
t.setDaemon(True) #会发现子线程还没运行完随着主线程结束就结束了
t.start()
print('done')

'''
2.多线程之间如何通信？
答：最简单的方法是建立一个全局变量。几个子线程共同操作这个全局变量
或者使用queue库中的线程安全队列
'''
from queue import Queue
from threading import Thread
import time

# A thread that produces data
def producer(out_q):
    data = 'some data'
    print(f'put data => {data}')
    out_q.put(data)

# A thread that consumes data
def consumer(in_q):
    time.sleep(1)
    data = in_q.get()
    print(f'get data <= {data}')

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()

t1.join()
t2.join()
'''
3.说说Condition条件变量
答：使用Condition对象可以在某些事件触发或者达到特定的条件后才处理数据。Condition除了
具有Lock对象的acquire方法和release方法外，还提供了wait和notify方法。
线程首先acquire一个条件变量锁，如果条件不足，则该线程wait，如果满足就执行线程，甚至可以
notify其他线程。其他处于wait状态的线程接到通知后会重新判断条件。
'''
import threading,time
class Consumer(threading.Thread):
    def __init__(self,cond,name):
        super().__init__()
        self.cond=cond
        self.name=name

    def run(self) -> None:
        time.sleep(1)
        self.cond.acquire()
        print(self.name+':我这两件商品一起买，可以便宜点吗')
        self.cond.notify()
        self.cond.wait()
        print(self.name+':我已经提交了订单了，你修改下价格')
        self.cond.notify()
        self.cond.wait()
        print(self.name+':收到，我支付成功了')
        self.cond.notify()
        self.cond.wait()
        print(self.name+':等待收货')

class Producer(threading.Thread):
    def __init__(self,cond,name):
        super().__init__()
        self.cond=cond
        self.name=name

    def run(self) -> None:
        self.cond.acquire()
        self.cond.wait()
        print(self.name+':可以的，你提交订单吧')
        self.cond.notify()
        self.cond.wait()
        print(self.name+':好了，我已经修改了')
        self.cond.notify()
        self.cond.wait()
        print(self.name+':嗯，收款成功，马上给你发货')
        self.cond.release()
        print(self.name+':发货商品')

cond=threading.Condition()
consumer=Consumer(cond,'买家')
producer=Producer(cond,'卖家')
consumer.start()
producer.start()