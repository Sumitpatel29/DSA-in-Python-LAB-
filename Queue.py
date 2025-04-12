size=4
item = [0]*size
front = rear = 0

def enqueue(x):
    global rear
    if rear >= size:
        print("Queue overflow")
    else:
        item[rear] = x
        rear = rear+1

def dequeue():
    global front
    if rear == 0:
        print("Queue is empty")
    else:
        print(item[front])
        while front != rear-1:
            item[front] = item[front+1]
            front = front+1
        front=0
        rear=rear-1

def traverse():
    print(item[front:rear])

while True:
    print("1. Enqueue")
    print("2. Dequque")
    print("3. Traverse")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Enter element to push: "))
        enqueue(x)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        traverse()
    elif choice == 4:
        print('Exiting...')
        break
    else:
        print("Invalid choice")
