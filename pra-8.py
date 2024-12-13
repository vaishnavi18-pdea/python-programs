
class Node:
    def __init__(self, bit):
        self.bit = bit
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_bit(self, bit):
        new_node = Node(bit)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
    def display(self):
        current = self.head
        binary_number = ""
        while current:
            binary_number += str(current.bit)
            current = current.next
        print("Binary Number:", binary_number)
    def ones_complement(self):
        current = self.head
        while current:
            current.bit = 1 if current.bit == 0 else 0  
            current = current.next
    def twos_complement(self):
        self.ones_complement()  
        current = self.tail
        carry = 1
        while current and carry:
            if current.bit == 0:
                current.bit = 1
                carry = 0
            else:
                current.bit = 0
                current = current.prev
        if carry:  
            new_node = Node(1)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def add_binary(self, other):
        result = DoublyLinkedList()
        carry = 0
        a = self.tail
        b = other.tail
        while a or b or carry:
            bit_a = a.bit if a else 0
            bit_b = b.bit if b else 0
            sum_bits = bit_a + bit_b + carry
            result.insert_bit_front(sum_bits % 2)
            carry = sum_bits // 2
            if a: a = a.prev
            if b: b = b.prev
        return result
    def insert_bit_front(self, bit):
        new_node = Node(bit)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
def main():
    binary1 = DoublyLinkedList()
    binary2 = DoublyLinkedList()
    bits1 = [1, 1, 0, 1]
    bits2 = [1, 0, 1, 1]
    for bit in bits1:
        binary1.insert_bit(bit)
    for bit in bits2:
        binary2.insert_bit(bit)
    print("Binary Number 1:")
    binary1.display()
    print("Binary Number 2:")
    binary2.display()
    print("\n1's Complement of Binary Number 1:")
    binary1.ones_complement()
    binary1.display()
    print("\n2's Complement of Binary Number 2:")
    binary2.twos_complement()
    binary2.display()
    print("\nAddition of Binary Number 1 and Binary Number 2:")
    result = binary1.add_binary(binary2)
    result.display()
main()