#difference between LIFO and FIFO

#0   1   2   3   4 
import queue
q = queue.Queue()

for i in range(10):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
    
    
print('\n')    
    
#4   3   2   1   0
import queue
q = queue.LifoQueue()

for i in range(10):
    q.put(i)
    
while not q.empty():
    print(q.get(), end = '   ')
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
