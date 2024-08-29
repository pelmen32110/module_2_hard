import random
items = []
for i in range(1,21):
    items.append(i)
random_item = random.choice(items)
print('Наше случайное число: ', random_item)
print('Парами чисел для него являются: ')
x=1
while random_item-x >= x:
    if random_item-x == x:
        break
    else:
        print(random_item-x,x)
        x+=1


