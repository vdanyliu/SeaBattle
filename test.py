import sys
import colorama
import termcolor
colorama.init()

termcolor.cprint('Hello, World!', 'green', 'on_red')
a = [2, 1]
b = [2, 1]
print(a)
print(a==b)
b = 4

print(-1 <= b <= 1)

print(ord('a'))

list = [2, 3, 4, 5, 6]

i = 5
while i > 0:
    list.remove(list[0])
    print(list)
    i -= 1