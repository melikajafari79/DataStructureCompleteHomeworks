class Node:

#*********************************
#Edited constructor to receive polynomial input
    def __init__(self, poly):
        if poly is None:
            self.len = 0
            self.poly = None
        else:
            self.len = len(poly)
            self.poly = poly
        self.next = None
        self.prev = None


class List:
    def __init__(self):        
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
        self.n = 0
        
    def get(self,ind):
        if ind >=  self.size() : 
            raise Exception('Out of list')
        x = self.head.next
        for i in range(ind) :
            x=x.next
        return x
    
    def insert_after(self, x, poly):
        y = Node(poly)
        self.n += 1
        y.prev = x
        y.next = x.next
        x.next = y
        y.next.prev = y
        return y
        
    def delete(self, x):
        if self.size()==0:
            raise Exception('List is empty')
        self.n -= 1
        x.prev.next = x.next
        x.next.prev = x.prev
        return x
        
    def find(self, val):
        x = self.head.next
        for i in range(self.size()) :
            if x.poly == val :
                return x
            x=x.next
        return None
    
    def size(self):
        return self.n
      
    def is_empty(self):
        return self.n==0

#**********************************
#Addition of two polynomials
    
    def add_polynomials(self, poly1, poly2):
   
        if poly2.len > poly1.len:
            poly1, poly2 = poly2, poly1

        poly2_poly = [0] * ((poly1.len) - (poly2.len)) + poly2.poly
    
        result = []
        for i , j in zip(poly1.poly, poly2_poly):
            result.append(i+j)
        
        return result
    
#Example
l=List()
l.insert_after(l.head,[2, 3, 4])
l.insert_after(l.get(0),[5, -1])
print(l.add_polynomials(l.get(0),l.get(1)))