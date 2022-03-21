class ganjil: 
    def __init__(n):
        n.items=[]
    def enqueue(n,item):
        n.items.insert(0,item) 
    def dequeue(n):
        return n.items.pop() 
    def semua(n):
        return n.items

q = ganjil()
q.enqueue(2)
q.enqueue(3)
print(q.semua())
print(q.dequeue(), "Bukan bilangan ganjil")
print(q.dequeue(), "Adalah Bilangan ganjil")
   



