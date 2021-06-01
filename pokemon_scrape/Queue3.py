# priority queue

#item with lowest value gets ouputed first, no oder needed, the lowest value will be outputed first
import queue
import time

q = queue.PriorityQueue()

#tuple with data, reprsented as a string
q.put((1, 'Priority 1'))
q.put((3, 'Prioirty 3'))
q.put((4 ,'Priority 4'))
q.put((2 ,'Priority 2'))



#putting in 4 items, with PriorityQueue
for i in range(q.qsize()):
    print(q.get()[1])



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
