# Класс список
class Node:
    def __init__(self, data=None, next=None):
        self.data = data  # Данные
        self.next = next  # Адрес на следующий элемент списка

class List:
    def __init__(self, head=None):
        self.head = head # Корень/начало списка

    def AddBegin(self, a): # Добавление в начало
        self.head = Node(a, self.head)

    def AddEnd(self, a): # Добавить в конец
        cur = self.head
        if cur == None:
            self.head = Node(a, self.head)
            return
        while cur.next != None:
            cur = cur.next
        cur.next = Node(a)

    def RemoveBegin(self): # Удаление из начала
        cur = self.head
        if self.head == None:
            return
        self.head = cur.next

    def RemoveEnd(self): # Удаление из конца
        cur = self.head
        if cur == None:
            return
        while cur.next.next != None:
            cur = cur.next
        cur.next = None

    def Print(self): # Печать списка
        cur = self.head
        if cur == None:
            print('List is empty!')
            return
        while cur != None:
            print(str(cur.data) + ' ', end='')
            cur = cur.next
        print('')

    def isEmpty(self): # Пустой ли список
        return self.head == None

    def Length(self): # Размер списка
        cur = self.head
        if cur == None:
            return 0
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def isExist(self, a): # Существует ли элемент
        cur = self.head
        if cur == None:
            return False
        while cur != None:
            if cur.data == a:
                return True
            cur = cur.next
        return False

    def Flip(self):
        if self.head == None:
            return
        cur = next = before = None
        cur = self.head
        while cur != None:
            next = cur.next
            cur.next = before
            before = cur
            cur = next
        self.head = before

    def Remove(self, a): # Удаление первого элемена по вхождению
        cur = self.head
        before = cur
        if cur == None:
            return
        if self.head.data == a:
            self.head = cur.next
            return
        while cur != None:
            if cur.data == a:
                before.next = cur.next
                break
            before = cur
            cur = cur.next

    def RemoveAll(self, a): # Удаление всех указаного элемента
        cur = self.head
        before = cur
        if cur == None:
            return
        while cur.data == a:
            self.head = cur.next
            cur = self.head
            before = cur
        while cur != None:
            if cur.data == a:
                before.next = cur.next
                cur = before.next
            else:
                before = cur
                cur = cur.next

    def AddAfter(self, d, a): # Добавляет элемент после указанного
        cur = self.head
        before = cur
        if cur == None:
            return
        if before.data == d: # Если элемент в начале
            before.next = Node(a, cur.next)
            return
        while cur != None: # Если элемент находится в середине
            if before.data == d:
                before.next = Node(a, cur)
                return
            else:
                before = cur
                cur = cur.next
        if before.data == d: # Если элемент находится в конце
            before.next = Node(a, cur)

    def AddNode(self, i, a):
        cur = self.head
        if i == 0: # Если в самое начало
            self.head = Node(a, cur)
        else:
            j = 0
            while j != i - 1 and cur != None:
                j += 1
                cur = cur.next
            if cur == None: # Нет элемента на такой позиции
                return
            else:
                cur.next = Node(a, cur.next)

    def Clear(self): # Удалить весь список
        while not self.isEmpty():
            self.RemoveBegin()

# Main
test_list = List()
test_list.AddBegin(1)
test_list.AddBegin(0)
test_list.AddEnd(2)
test_list.AddEnd(3)
test_list.AddEnd(5)
test_list.AddAfter(3, 4)
print(test_list.Length())
test_list.Print()
test_list.AddNode(4, 4)
test_list.AddNode(5, 4)
test_list.Print()
print(test_list.isEmpty())
print(test_list.isExist(4))
test_list.Print()
test_list.RemoveAll(4)
print(test_list.isExist(4))
test_list.Print()
test_list.Flip()
test_list.Print()
print(test_list.isEmpty())
test_list.Clear()
print(test_list.isEmpty())
