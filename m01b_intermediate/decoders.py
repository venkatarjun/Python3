from datetime import datetime
import time
def logger(func):
    def wrapper():
        print("-"*40)
        print("exceutin starterd")
        func()
        print("exceution complete")
        print("-"*40)
    return wrapper
@logger
def demo_function():
    print("exceutoing task")
    time.sleep(3)
    print("task completed")

demo_function()
 