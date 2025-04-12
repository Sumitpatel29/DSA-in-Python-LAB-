size = 4
data = [0]*size
top = -1

def push(x):
    global top
    if top >= size-1:
        print("Stack Overflow")
    else:
        top = top+1
        data[top]=x

def pop():
    global top
    if top == -1:
        print('Stack underflow')
    else:
        top= top-1
        return data[top+1]

def peek():
    if top == -1:
        print('Stack is empty')
    else:
        print(data[top])

def traverse():
    if top == -1:
        print('Stack is empty')
    else:
        print(data[0:top+1])


while True:
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Traverse")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Enter element to push: "))
        push(x)
    elif choice == 2:
        pop()
    elif choice == 3 :
        peek()
    elif choice == 4:
        traverse()
    elif choice == 5:
        break
    else:
        print("Invalid choice")
