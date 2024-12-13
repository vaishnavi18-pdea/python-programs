class PizzaParlor:
    def __init__(self, size):
        self.size = size  
        self.queue = [None] * self.size  
        self.front = -1  
        self.rear = -1   
    def isFull(self):
        return self.rear == self.size - 1
    def isEmpty(self):
        return self.front == -1 or self.front > self.rear
    def addOrder(self):
        if self.isFull():
            print("Pizza parlor is full. Cannot add more orders.")
        else:
            pizza_id = input("Enter the pizza ID for the order: ")
            if self.front == -1:  
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = pizza_id
            print(f"Order for pizza ID '{pizza_id}' added.")
    def serveOrder(self):
        if self.isEmpty():
            print("No orders to serve!")
        else:
            pizza_id = self.queue[self.front]
            print(f"Serving order for pizza ID '{pizza_id}'.")
            self.front += 1
            if self.front > self.rear:  
                self.front = self.rear = -1
    def displayOrders(self):
        if self.isEmpty():
            print("No orders to display.")
        else:
            print("Current Orders in the Pizza Parlor:")
            for i in range(self.front, self.rear + 1):
                print(f"Pizza ID: {self.queue[i]}")
def menu():
    size = int(input("Enter the maximum number of orders the pizza parlor can handle: "))
    parlor = PizzaParlor(size)
    while True:
        print("\nMenu:")
        print("1. Add Order")
        print("2. Serve Order")
        print("3. Display Orders")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            parlor.addOrder()
        elif choice == 2:
            parlor.serveOrder()
        elif choice == 3:
            parlor.displayOrders()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()