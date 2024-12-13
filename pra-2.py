def generate_Magic_Square(size):
    magic_square = [[0 for x in range(size)] for y in range(size)]
    i = size // 2
    j = size - 1
    for num in range(1, size * size + 1):  
        magic_square[i][j] = num
        new_i, new_j = (i - 1) % size, (j + 1) % size  
        if magic_square[new_i][new_j] != 0:
            new_i = (i + 1) % size  
            new_j = j  
        i, j = new_i, new_j
    magic_sum = size * (size * size + 1) // 2
    print("Sum of each row or column is:", magic_sum)
    print(f"Magic Square of size {size}x{size} is:")
    for row in magic_square:
        for num in row:
            print(f"{num}", end=" ")
        print()
while True:
    n = int(input("\nEnter the size of the MAGIC SQUARE (odd number): "))
    if n % 2 == 0:
        print("Please enter an ODD number (for example - 3, 5, 7, 9, ...)")
    else:
        generate_Magic_Square(n)
    a = input("\nDo you want to print Magic Square of some other size (y/N): ")
    if a.lower() not in ['y', 'yes']:
        break
