import threading

def methodone():
    for x in range(1000):
        print("Vishnu ")

def methodtwo():
    for x in range(1000):
        print("Sharma")


one = threading.Thread(target=methodone)
two = threading.Thread(target=methodtwo)

one.start()
# two.start()
#
# # one.join()
# # two.join()
# Without join() , this will be printed immediately in start of the threads.
print("Checking it's printing order")
