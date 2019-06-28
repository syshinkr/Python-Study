f = open('C:/Users/admin/Desktop/a.txt', 'r')
print(f.read())

with open('C:/Users/admin/Desktop/a.txt') as f:
    print(f.read())