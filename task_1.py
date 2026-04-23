my_task = []
items = int(input("how many task you want to enter!"))
print("Enter items one by one")
for item in range(items):
    my_task.append(input())
print("\n" + "=" * 40)
print(f"   Your Final completed task list")
for i , task in enumerate(my_task):
    print(i , task)
