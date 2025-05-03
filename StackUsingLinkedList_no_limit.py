class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class StackUsingLinkedList:
    def __init__(self):
        self.top=None
        self.size=0

    def push(self,data):
        node=Node(data)
        if self.top:
            node.next=self.top
            self.top=node
        else:
            self.top=node
        self.size+=1

    def pop(self):
        if self.size == 0:
            print('Stack Underflow')
        else:
            current=self.top
            self.top=self.top.next
            self.size -=1
            return current
    def peek(self):
         if self.size == 0:
            print('Stack has no elements')
            return
         else:
            print(self.top.data)

    def traverse(self):
        if self.size == 0:
            print('Stack Underflow')
        else:
            current=self.top
            while current:
                print(current.data)
                current=current.next
         

s=StackUsingLinkedList()

while True:
    print("1. Push")
    print("2. pop")
    print("3. peek")
    print("4. Traverse")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        x = int(input("Enter element to push: "))
        s.push(x)
    elif choice == 2:
        s.pop()
    elif choice == 3:
        s.peek()
    elif choice == 4:
        s.traverse()
    elif choice == 5:
        print('Exiting...')
        break
    else:
        print("Invalid choice")
