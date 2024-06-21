class Queue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.Q = [0] * max_size
        self.num = 0
        self.first = 0
    def enqueue(self, item):
        if self.num >= self.max_size:
            raise Exception("Queue overflow")
        self.Q[(self.num + self.first) % self.max_size] = item
        self.num += 1
    def dequeue(self):
        if self.num == 0:
            raise Exception("Queue empty")
        item = self.Q[self.first]
        self.first = (self.first + 1) % self.max_size
        self.num -= 1
        print(self.Q)
        return item
    def front(self):
        if self.num == 0:
            raise Exception("Queue empty")
        return self.Q[self.first]
    def is_empty(self):
        return self.num == 0
    def size(self):
        return self.num
    def is_full(self):
        return self.num >= self.max_size


#***********************************************************
#Remove all items that are equal to element
    def dequeue_element(self , element):
        if self.num == 0:
            raise Exception("Queue empty")
            
        count=0
        for i in range(self.num):
            if self.Q[(self.first + i) % self.max_size] == element:
                self.Q.remove(element)
                count+=1
        for j in range (count):
            self.Q.insert((self.num + self.first) % self.max_size, 0)
            self.num-=1
            
        if count:
            return self.Q
        else:
            return False


#***********************************************************
#Deletes the item with i index   
    def dequeue_i(self , i):
        if self.num == 0:
            raise Exception("Queue empty")
        item=self.Q[i]
        del self.Q[i]
        index=(self.num + self.first) % self.max_size
        self.Q.insert(index,0)
        self.num-=1
        return item


            
#Example
            
q=Queue(10) # (front of queue)[](back of queue)
q.enqueue("ra'na") # ["ra'na"]
q.enqueue("vez") # ["ra'na", "vez"]
q.enqueue("Arya") # ["ra'na", "vez", "Arya"]
print("queue size is: ",q.size())
print("front of queue is:",q.front())
q.enqueue("milda") # ["ra'na", "vez", "Arya","milda"]
print("**********************************")
print(q.dequeue_i(2)) # ["ra'na", "vez","milda"]
print(q.dequeue_element("vez")) # ["ra'na","milda"]
print("It was a queue")
