"""
Problem: Print in Order (LeetCode #1114)
Thread Synchronization via Events/Semaphores
"""

import threading

class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst) -> None:
        printFirst()
        self.first_done.set()

    def second(self, printSecond) -> None:
        self.first_done.wait()
        printSecond()
        self.second_done.set()

    def third(self, printThird) -> None:
        self.second_done.wait()
        printThird()

if __name__ == "__main__":
    output = []
    foo = Foo()
    t3 = threading.Thread(target=foo.third, args=(lambda: output.append("third"),))
    t1 = threading.Thread(target=foo.first, args=(lambda: output.append("first"),))
    t2 = threading.Thread(target=foo.second, args=(lambda: output.append("second"),))

    t3.start()
    t2.start()
    t1.start()
    t1.join()
    t2.join()
    t3.join()
    assert output == ["first", "second", "third"]
    print("✅ All Concurrency tests passed!")
