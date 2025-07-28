

# arr = [1,2,3,4,5]
# print(arr[2])

# stack = []
# stack.append(10)
# stack.append(20)
# print(stack)
# print(stack.pop())


# from collections import deque

# queue = deque()
# queue.append(1)
# queue.append(2)
# print(queue.popleft())

# arr = [1,2,3,4,5,6]
# 
# 
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1
# 
# target = int(input("Введите число для поиска: "))
# 
# result = linear_search(arr, target)
# 
# if result != -1:
#     print(f"Элемент найден на позиций {result}")
# else:
#     print("Not element")

# arr = [1,2,3,4,5,6,7,8,9,11, 13]
# target = 9
# 
# def binary_search(arr, target):
#     left = 0
#     ringht = len(arr) - 1
# 
#     while left <= ringht:
#         mid = (left + ringht) // 2
#         print(f"Сравниваем с сердиной arr[{mid}] = {arr[mid]}]")
# 
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             ringht = mid - 1
# 
#     return -1
# 
# result = binary_search(arr, target)
# 
# if result != -1:
#     print(f"Элемент найден на позиций {result}")
# else:
#     print("Not element")


class SearchEngine:
    def __init__(self, data):
        self.data = data 


    def linear_search(self, target):
        print("Linear search")
        for i in range(len(self.data)):
            print(f"Проверка: data[{i}] = {self.data[i]} ")
            if self.data[i] == target:
                return 1
        return -1

    
    def binary_search(self, target):
        print("Binary Searhc")

        left = 0
        ringth = len(self.data) - 1

        while left <= ringth:
            mid = (left + ringth) // 2
            print(f"Сравниваем с сердиной data[{mid}] = {self.data[mid]}]")

            if self.data[mid] == target:
                return mid
            elif self.data[mid] < target:
                lift = mid + 1
            else:
                ringth = mid - 1

        return -1

arr = [1, 3, 5, 7, 9, 11, 13]
search_engine = SearchEngine(arr)

target = int(input("Ввдеите число для поиска: "))

res1 = search_engine.linear_search(target)
print("Результат линейного поиска: ", res1 if res1 != -1 else "Не найдено")

res2 = search_engine.binary_search(target)
print("Результат  Бинарного поиска: ", res2 if res2 != -1 else "Не найдено")
