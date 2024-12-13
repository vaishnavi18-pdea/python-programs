class Queue:
    def __init__(self, size):
        self.size = size  
        self.queue = [None] * self.size  
        self.front = -1  
        self.rear = -1   
    def is_empty(self):
        return self.front == -1
    def is_full(self):
        return self.rear == self.size - 1
    def enqueue(self, job):
        if self.is_full():
            print("Queue is full. Cannot add more jobs.")
        else:
            if self.front == -1:  
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = job
            print(f"Job '{job}' added to the queue.")
    def del_queue(self):
        if self.is_empty():
            print("Queue is empty. No jobs to remove.")
            return None
        else:
            job = self.queue[self.front]
            if self.front == self.rear:  
                self.front = self.rear = -1
            else:
                self.front += 1
            print(f"Job '{job}' removed from the queue.")
            return job
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Jobs in the queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i])
def main():
    size = int(input("Enter the size of the queue: "))
    queue = Queue(size)
    while True:
        print("\nMenu:")
        print("1. Add Job (enqueue)")
        print("2. Remove Job (dequeue)")
        print("3. Display Queue")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            job = input("Enter the job name to add to the queue: ")
            queue.enqueue(job)
        elif choice == 2:
            queue.del_queue()
        elif choice == 3:
            queue.display()
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()