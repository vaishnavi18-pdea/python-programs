
def Selection_Sort(marks):
    n = len(marks)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if marks[j] < marks[min_index]:
                min_index = j
        marks[i], marks[min_index] = marks[min_index], marks[i]
def Bubble_Sort(marks):
    n = len(marks)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if marks[j] > marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
def top_five_marks(marks):
    top_marks = sorted(marks, reverse=True)[:5]
    print("Top Five Scores:", top_marks)
def main():
    n = int(input("Enter the number of students: "))
    marks = []
    for i in range(n):
        mark = float(input(f"Enter percentage for student {i + 1}: "))
        marks.append(mark)
    while True:
        print("\nChoose a sorting method:")
        print("1. Selection Sort")
        print("2. Bubble Sort")
        print("3. Display Top Five Scores")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            Selection_Sort(marks)
            print("Sorted list using Selection Sort:", marks)
        elif choice == 2:
            Bubble_Sort(marks)
            print("Sorted list using Bubble Sort:", marks)
        elif choice == 3:
            top_five_marks(marks)
        elif choice == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
main()