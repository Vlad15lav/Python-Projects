import numpy as np

# Класс Граф
class Graph:
    def __init__(self, n):
        self.__n = n # Количество точек
        self.__m = 0 # Количество рёбр
        self.__Map = np.zeros((n, n)) # Матрица смежности

    def GetMap(self): # Вернуть матрицу смежности
        return self.__Map

    def GetSize(self): # Вернуть количество точек
        return self.__n

    def GetRoads(self): # Вернуть количество рёбр
        return self.__m

    def Input(self): # Ввод дорог
        print('Укажите количество рёбер:', end=' ')
        m = int(input())
        self.__m = m
        begin = end = length = 0
        for i in range(m):
            print('Начало: ', end='')
            begin = int(input())
            print('Конец: ', end='')
            end = int(input())
            print('Длина: ', end='')
            length = int(input())
            print('Двухсторонний (y/n)?: ', end='')
            if input() == 'y':
                self.__Map[begin - 1][end - 1] = self.__Map[end - 1][begin - 1] = length
            else:
                self.__Map[begin - 1][end - 1] = length

    def PathOnWidth(self): # Обход в ширину
        labels = list();
        for i in range(self.__m):
            labels.append(False)
        queue = list();
        res = list()
        v = 0
        queue.append(v)
        labels[v] = True
        while len(queue) != 0:
            queue.reverse()
            v = queue.pop()
            queue.reverse()
            res.append(v + 1)
            for i in range(self.__n):
                if self.__Map[v][i] != 0 and not labels[i]:
                    queue.append(i)
                    labels[i] = True
        print(res)

    def PathOnHeight(self): # Обход в глубину
        labels = list();
        for i in range(self.__m):
            labels.append(False)
        stack = list();
        res = list()
        v = 0
        stack.append(v)
        labels[v] = True
        while len(stack) != 0:
            v = stack.pop()
            res.append(v + 1)
            for i in range(self.__n):
                if self.__Map[v][i] != 0 and not labels[i]:
                    stack.append(i)
                    labels[i] = True
        print(res)

    def ShortestPath(self, begin, end): # Поиск кратчайшего пути между двумя вершинами (алгоритм Дейекстра)
        labels = list()
        prev = list()
        len_paths = list()
        res = list()
        for i in range(self.__n):
            labels.append(False)
            len_paths.append(pow(2, 1000))
            prev.append(-1)
        labels[begin - 1] = True
        len_paths[begin - 1] = 0
        prev[begin - 1] = -1
        v = begin - 1
        flag = False
        while 1:
            for i in range(self.__n):
                if self.__Map[v][i] != 0:
                    if not labels[i] and len_paths[i] > len_paths[v] + self.__Map[v][i]:
                        len_paths[i] = len_paths[v] + self.__Map[v][i]
                        prev[i] = v
            min_len = pow(2, 1000)
            imin = -1
            for i in range(self.__n):
                if not labels[i] and len_paths[i] < min_len:
                    min_len = len_paths[i]
                    imin = i
            if imin == end - 1:
                break
            labels[imin] = True
            v = imin
        stack = list()
        stack.append(end)
        v = end - 1
        while v != begin - 1:
            v = prev[v]
            stack.append(v + 1)
        while len(stack) != 0:
            res.append(stack.pop())
        print(res)

    def ShortestPaths(self): # Поиск всех кратчайших путей в графе (алгоритм Флойда)
        paths = self.GetMap()
        for i in range(self.__n):
            for j in range(self.__n):
                for k in range(self.__n):
                    if j != k and i != j and i != k:
                        if paths[j][k] > paths[j][i] + paths[i][k]:
                            paths[j][k] = paths[j][i] + paths[i][k]
        return paths

    def Carcas(self): # Поиск каркаса минимального веса (алгоритм Прима)
        labels = list()
        res = Graph(self.__n)
        alpha = list()
        beta = list()
        for i in range(self.__n):
            labels.append(False)
            alpha.append(0)
            beta.append(pow(2, 1000))
        labels[0] = True
        for i in range(1, self.__n):
            if self.__Map[0][i] != 0:
                alpha[i] = 0
                beta[i] = self.__Map[0][i]
        for i in range(self.__n - 1):
            min = pow(2, 1000)
            imin = -1
            for j in range(self.__n):
                if not labels[j] and beta[j] < min:
                    min = beta[j]
                    imin = j
            labels[imin] = imin
            res.__Map[imin][alpha[imin]] = res.__Map[alpha[imin]][imin] = min
            res.__m += 1
            for i in range(self.__n):
                if not labels[j] and self.__Map[imin][j] != 0:
                    if beta[j] > self.__Map[imin][j]:
                        beta[j] = self.__Map[imin][j]
                        alpha[j] = imin
        return res

# Main
g = Graph(5)
g.Input()
g.PathOnWidth()
g.PathOnHeight()
g.ShortestPath(1, 5)
paths = g.ShortestPaths()
print(paths)
Carcas_t = g.Carcas()
print(Carcas_t.GetMap())
