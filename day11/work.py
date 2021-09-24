# -*- coding: utf-8 -*-
# @Author  : caijizhi
# @FileName: work.py
# @Software: PyCharm
import threading
from threading import Thread
import time
lock = threading.Lock()  # 创建锁
basket = 0

class cooker(Thread):
    count = 0
    def run(self) -> None:
        global basket
        while True:
            if basket>=500:
                print('篮子满了，等一会')
                time.sleep(3)
            else:
                with lock:
                    self.count = self.count+1
                    basket = basket + 1
                    print('厨师做了一个还有',basket,'个')

class buyer(Thread):
    money = 3000
    count = 0
    name = ''
    def run(self) -> None:
        global basket
        while self.money>0:
            if basket>0:
                self.money = self.money-2
                self.count = self.count+1
                with lock:
                    basket = basket - 1
                print(f'{self.name}买走一个')

            else:
                print('篮子空了，等一哈')
                time.sleep(2)
        print(self.name,'买了',self.count,'还有',self.money,'元')
if __name__ == '__main__':

    c1 = cooker()
    c2 = cooker()
    c3 = cooker()
    b1 = buyer()
    b2 = buyer()
    b3 = buyer()
    b4 = buyer()
    b5 = buyer()
    b6 = buyer()
    b1.name = 'AA'
    b2.name = 'BB'
    b3.name = 'CC'
    b4.name = 'DD'
    b5.name = 'EE'
    b6.name = 'FF'
    c1.setDaemon(True)
    c2.setDaemon(True)
    c3.setDaemon(True)
    c1.start()
    c2.start()
    c3.start()
    b1.start()
    b2.start()
    b3.start()
    b4.start()
    b5.start()
    b6.start()



