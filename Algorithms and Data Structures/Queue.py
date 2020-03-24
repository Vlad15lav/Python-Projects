# Класс очердь
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Данные
        self.next = next  # Адрес на следующий элемент очереди

class Queue:
    def __init__(self, head=None):
        self.head = head # Корень/начало очереди

    def push(self, a): # Добавить в очередь
        cur = self.head
        if cur == None:
            self.head = Node(a, self.head)
            return
        while cur.next != None:
            cur = cur.next
        cur.next = Node(a)

    def pop(self): # Удалить из очереди
        cur = self.head
        if self.head == None:
            return
        self.head = cur.next

    def front(self): # Доступ к первому элементу
        cur = self.head
        if cur == None:
            return
        return cur.data

    def back(self): # Доступ к последнему элементу
        cur = self.head
        if cur == None:
            return
        while cur.next != None:
            cur = cur.next
        return cur.data

    def print(self): # Печать всех элементов в очереди
        cur = self.head
        if cur == None:
            print('Queue is empty!')
            return
        while cur != None:
            print(str(cur.data) + ' ', end='')
            cur = cur.next
        print('')

    def isEmpty(self): # Пустая ли очередь
        return self.head == None

    def size(self): # Размер очереди
        cur = self.head
        if cur == None:
            return 0
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def isExist(self, a): # Существует ли элемент из очереди
        cur = self.head
        if cur == None:
            return False
        while cur != None:
            if cur.data == a:
                return True
            cur = cur.next
        return False

    def clear(self): # Удалить всю очередь
        while not self.isEmpty():
            self.pop()

# Main
q = Queue()
for i in range(1, 6):
    q.push(i)
q.print()
q.pop()
q.push(6)
q.print()
print(q.front())
print(q.back())
print(q.size())
print(q.isExist(7))
q.push(7)
print(q.isExist(7))
q.print()
print(q.isEmpty())
q.clear()
print(q.isEmpty())