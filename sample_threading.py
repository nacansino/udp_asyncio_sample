import threading

x = 10

def prints(Text,increment):
    global x
    print(Text)
    x += increment

thread1 = threading.Thread(target=prints, args=("I am T1\n",5))
thread2 = threading.Thread(target=prints, args=("I am T2\n",100)) #Create threads and pass arguments to function
thread1.start()
thread2.start()             #Start threads

thread1.join()      #Wait until thread1 has finished execution
thread2.join()      #Wait until thread2 has finished execution
print("I am the main thread, the two threads are done")
print(x)