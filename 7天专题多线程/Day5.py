'''第五天'''
'''
1.threading.local的作用？
答：python提供了threading.local类，将这个类实例化得到一个全局对象，
但是不同线程使用这个对象存储的数据对其他线程不可见，本质上就是不同的线程使用这个对象
时为其创建一个独立的字典
'''
'''
2.请用代码演示一下互斥锁
答：
互斥锁是一种独占锁，同一时刻只有一个线程可以访问共享的数据。使用很简单，初始化锁对象，
然后将锁当做参数传递给任务函数，在任务中加锁，使用后释放锁。
'''
import threading
import time
lock1=threading.Lock()
num=0
def puls(lk):
    global num
    lk.acquire()
    for _ in range(10000000):
        num+=1
    print('子线程%s运算结束后，num=%s'%(threading.current_thread().getName(),num))
    lk.release()

# if __name__ == '__main__':
#     for i in range(2):
#         t=threading.Thread(target=puls,args=(lock1,))
#         t.start()
#     time.sleep(2)
#     print("最终",num)
'''
3.什么是僵尸进程和孤儿进程？怎么避免僵尸进程？
答：
孤儿进程：父进程退出，子进程还在运行的这些子进程都是孤儿进程，
孤儿进程将被init 进程（进程号为1）所收养，并由init 进程对他们完成状态收集工作。
僵尸进程：进程使用fork 创建子进程，如果子进程退出，
而父进程并没有调用wait 或waitpid 获取子进程的状态信息，
那么子进程的进程描述符仍然保存在系统中的这些进程是僵尸进程。
避免僵尸进程的方法：
1.fork 两次用孙子进程去完成子进程的任务
2.用wait()函数使父进程阻塞
3.使用信号量，在signal handler 中调用waitpid,这样父进程不用阻塞
'''
#windows没有fork
# import os, sys, time
#
# pid = os.fork()
# getpid = os.getpid()
# getppid = os.getppid()
#
# if pid == 0:
#     print("子进程 pid={}, getpid={}, getppid={}".format(pid, getpid, getppid))
# else:
#     print("主进程 pid={}, getpid={}, getppid={}".format(pid, getpid, getppid))
#     time.sleep(100)  # 在主进程结束sleep之前，子进程就会成为僵尸进程