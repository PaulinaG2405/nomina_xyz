my_list = ["Lucas", "Sara", "Ana"]

salaries = [1300000, 2400000, 1200000]

for i in my_list:
    print(i)

for j in range(len(my_list)):
    print(my_list[j])

age = []
i = [0, 1, 2, 3]
k = 0


for k in i:
    item = input("Ingrese la edad")
    age.append(item)
    k += 1

limit = 4
l = 0
for l in range(limit):
    item = input("Ingrese la edad ")
    age.append(item)
    k += 1
