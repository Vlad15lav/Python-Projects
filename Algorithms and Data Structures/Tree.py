# Класс дерева
class Node:
    def __init__(self, data):
        self.data = data # Данные узла
        self.left = None # Адрес на левый узел
        self.right = None # Адрес на правый узел

class Tree:
    def __init__(self, main_root=None):
        self.main_root = main_root # Корень дерева

#  Вызовы рекурсивных функций
    def Add(self, i): # Добавление в дерево
        if(self.main_root == None):
            self.main_root = Node(i)
        else:
            self.__Add(self.main_root, i)

    def PrintLTR(self): # Вызов рекурсивной печати ЛКП
        self.__PrintLTR(self.main_root)
        print('')
    def PrintRTL(self): # Вызов рекурсивной печати ПКЛ
        self.__PrintRTL(self.main_root)
        print('')
    def PrintTLR(self): # Вызов рекурсивной печати КЛП
        self.__PrintTLR(self.main_root)
        print('')
    def PrintLRT(self): # Вызов рекурсивной печати ЛПК
        self.__PrintLRT(self.main_root)
        print('')

    def PrintLVL(self): # Вызов печати по уровням
        self.__PrintLVL(self.main_root, 0, True)

    def Height(self): # Вызов рекурсии подсчета высоты дерева
        return self.__Height(self.main_root)

    def Delete(self): # Удалить дерево
        self.main_root = None

    def isExist(self, i): # Есть ли элемент в дереве
        if self.main_root == None:
            return False
        else:
            return self.__isExist(self.main_root, i)

    def FindNode(self, i): # Вернуть узел с указыным элементом
        if self.main_root == None:
            return None
        else:
            return self.__FindNode(self.main_root, i)
# Рекурсивные функции
    def __Add(self, root, i): # Добавление в дерево(рекурсивно)
        if i < root.data:
            if root.left != None:
                self.__Add(root.left, i)
            else:
                root.left = Node(i)
        else:
            if root.right != None:
                self.__Add(root.right, i)
            else:
                root.right = Node(i)

    def __PrintLTR(self, root): # Рекурсия ЛКП
        if root != None:
            self.__PrintLTR(root.left)
            print(root.data, end=' ')
            self.__PrintLTR(root.right)
    def __PrintRTL(self, root): # Рекурсия ПКЛ
        if root != None:
            self.__PrintRTL(root.right)
            print(root.data, end=' ')
            self.__PrintRTL(root.left)
    def __PrintTLR(self, root): # Рекурсия КЛП
        if root != None:
            print(root.data, end=' ')
            self.__PrintTLR(root.left)
            self.__PrintTLR(root.right)
    def __PrintLRT(self, root): # Рекурсия ЛПК
        if root != None:
            self.__PrintLRT(root.left)
            self.__PrintLRT(root.right)
            print(root.data, end=' ')

    def __PrintLVL(self, root, level, isRight): # Печать по уровням(рекурси)
        if root != None:
            self.__PrintLVL(root.right, level + 1, True)
            for i in range(level):
                print('   ', end='')
            if self.main_root.data == root.data:
                print('-' + str(root.data))
            else:
                if isRight:
                    print('/ ' + str(root.data))
                else:
                    print('\\ ' + str(root.data))
            self.__PrintLVL(root.left, level + 1, False)

    def __Height(self, root): # Подсчет высоты дерева(рекурсия)
        if root == None:
            return 0
        h_left = self.__Height(root.left)
        h_right = self.__Height(root.right)
        if h_left > h_right:
            return h_left + 1
        else:
            return h_right + 1

    def __isExist(self, root, i): # Поиска элемента в дереве(рекурсия)
        if i == root.data:
            return True
        elif i < root.data and root.left != None:
            return self.__isExist(root.left, i)
        elif i > root.data and root.right != None:
            return self.__isExist(root.right, i)

    def __FindNode(self, root, i): # Найти узел по значению(рекурсия)
        if i == root.data:
            return root
        elif i < root.data and root.left != None:
            return self.__FindNode(root.left, i)
        elif i > root.data and root.right != None:
            return self.__FindNode(root.right, i)

# Main
test = Tree()
test.Add(59)
test.Add(98)
test.Add(30)
test.Add(76)
test.Add(125)
test.Add(16)
test.Add(45)
print('ЛКП - ', end='')
test.PrintLTR()
print('ПКЛ - ', end='')
test.PrintRTL()
print('КЛП - ', end='')
test.PrintTLR()
print('ЛПК - ', end='')
test.PrintLRT()
test.PrintLVL()
print(test.Height())
print(test.isExist(31))
print(test.isExist(30))
test2 = Tree(test.FindNode(98))
test2.PrintLVL()
test.Delete()
test2.Delete()