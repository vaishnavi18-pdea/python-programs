class PriorityQueue:
    class Node:
        def __init__(self, data, priority):
            self.data = data  
            self.priority = priority  
            self.next = None  
    def __init__(self):
        self.head = None  
    def __del__(self):
        while self.head:
            self.dequeue()  
    def enqueue(self, data, priority):
        new_node = self.Node(data, priority)
        if not self.head or self.head.priority < priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        print(f"Added '{data}' with priority {priority}.")
    def dequeue(self):
        if not self.head:
            print("Priority Queue is empty!")
            return None
        node = self.head
        self.head = self.head.next  
        print(f"Removed '{node.data}' with priority {node.priority}.")
        return node.data
    def display(self):
        if not self.head:
            print("Priority Queue is empty!")
            return
        current = self.head
        print("Priority Queue:")
        while current:
            print(f"Data: '{current.data}', Priority: {current.priority}")
            current = current.next
def main():
    pq = PriorityQueue()
    while True:
        print("\nMenu:")
        print("1. Add Item (enqueue)")
        print("2. Remove Item (dequeue)")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter the data for the item: ")
            priority = int(input("Enter the priority (higher number means higher priority): "))
            pq.enqueue(data, priority)
        elif choice == 2:
            pq.dequeue()
        elif choice == 3:
            pq.display()
        elif choice == 4:
            print("Exiting the program.")
            del pq  
            break
        else:
            print("Invalid choice. Please try again.")
main()