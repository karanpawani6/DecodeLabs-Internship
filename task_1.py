my_task = []
items = int(input("how many task you want to enter!"))
print("Enter items one by one")
for item in range(items):
    my_task.append(input())

for i , task in enumerate(my_task):
    print(i , task)
