# Класс стэк
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Данные
        self.next = next  # Адрес на следующий элемент стэка

class Stack:
    def __init__(self, head=None):
        self.head = head # Корень/начало стэка

    def push(self, a): # Добавить в стэк
        self.head = Node(a, self.head)

    def pop(self): # Удалить из стэка
        cur = self.head
        if cur == None:
            return
        self.head = cur.next

    def top(self): # Доступ к верхнему элементу
        cur = self.head
        if cur == None:
            return
        return cur.data

    def print(self): # Печать всех элементов стэка
        cur = self.head
        if cur == None:
            print('Stack is empty!')
            return
        while cur != None:
            print(str(cur.data) + ' ', end='')
            cur = cur.next
        print('')

    def isEmpty(self): # Пустой ли стэк
        return self.head == None

    def size(self): # Размер стэка
        cur = self.head
        if cur == None:
            return 0
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def isExist(self, a): # Существует ли элемент в стэке
        cur = self.head
        if cur == None:
            return False
        while cur != None:
            if cur.data == a:
                return True
            cur = cur.next
        return False

    def clear(self): # Удалить весь стэк
        while not self.isEmpty():
            self.pop()

# Main
q = Stack()
for i in range(6, 0, -1):
    q.push(i)
q.print()
q.pop()
q.push(0)
q.print()
print(q.top())
print(q.size())
print(q.isExist(-1))
q.push(-1)
print(q.isExist(-1))
q.print()
print(q.isEmpty())
q.clear()
print(q.isEmpty())