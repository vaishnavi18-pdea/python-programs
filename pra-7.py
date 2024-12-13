
class Node:
    def __init__(self, prn, name):
        self.prn = prn  
        self.name = name  
        self.next = None  
class Club:
    def __init__(self):
        self.head = None  
    def add_at_beginning(self, prn, name):
        new_node = Node(prn, name)
        new_node.next = self.head
        self.head = new_node
    def add_at_end(self, prn, name):
        new_node = Node(prn, name)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def add_after_node(self, prn, name, after_prn):
        new_node = Node(prn, name)
        current = self.head
        while current:
            if current.prn == after_prn:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with PRN {after_prn} not found.")
    def delete_from_beginning(self):
        if not self.head:
            print("List is empty!")
            return
        self.head = self.head.next
    def delete_from_end(self):
        if not self.head:
            print("List is empty!")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next and current.next.next:
            current = current.next
        current.next = None
    def delete_by_value(self, prn):
        if not self.head:
            print("List is empty!")
            return
        if self.head.prn == prn:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.prn == prn:
                current.next = current.next.next
                return
            current = current.next
        print(f"Node with PRN {prn} not found.")
    def total_members(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    def display_members(self):
        if not self.head:
            print("No members to display.")
            return
        current = self.head
        while current:
            print(f"PRN: {current.prn}, Name: {current.name}")
            current = current.next
    def concatenate(self, other_club):
        if not other_club.head:
            print("The other list is empty.")
            return
        if not self.head:
            self.head = other_club.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = other_club.head
def main():
    club = Club()
    while True:
        print("\nClub Member Management System:")
        print("1. Add member at the beginning")
        print("2. Add member at the end")
        print("3. Add member after a specific member")
        print("4. Delete member from the beginning")
        print("5. Delete member from the end")
        print("6. Delete member by PRN")
        print("7. Display all members")
        print("8. Concatenate another club")
        print("9. Show total number of members")
        print("10. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            prn = input("Enter PRN: ")
            name = input("Enter name: ")
            club.add_at_beginning(prn, name)
        elif choice == 2:
            prn = input("Enter PRN: ")
            name = input("Enter name: ")
            club.add_at_end(prn, name)
        elif choice == 3:
            prn = input("Enter PRN: ")
            name = input("Enter name: ")
            after_prn = input("Enter the PRN after which to add: ")
            club.add_after_node(prn, name, after_prn)
        elif choice == 4:
            club.delete_from_beginning()
        elif choice == 5:
            club.delete_from_end()
        elif choice == 6:
            prn = input("Enter PRN of member to delete: ")
            club.delete_by_value(prn)
        elif choice == 7:
            club.display_members()
        elif choice == 8:
            other_club = Club()
            print("Enter members for the second club.")
            n = int(input("How many members in the second club? "))
            for _ in range(n):
                prn = input("Enter PRN: ")
                name = input("Enter name: ")
                other_club.add_at_end(prn, name)
            club.concatenate(other_club)
            print("Clubs concatenated successfully!")
        elif choice == 9:
            print(f"Total members: {club.total_members()}")
        elif choice == 10:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please try again.")
main()