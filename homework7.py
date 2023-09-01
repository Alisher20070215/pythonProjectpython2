import random

a = random.random()
print(a)

def bubble_sort(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            return a

a = ()

print(bubble_sort(a))

def selection(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            return a

a = ()

print(selection(a))

def insertion(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            return a

a = ()

print(insertion(a))

def merge(a):
    for i in range(0, len(a)-1):
        for j in range(len(a)-1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
            return a

a = ()

print(merge(a))
