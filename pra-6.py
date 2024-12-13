def input_percentage():
    n = int(input("Enter the number of students: "))
    perc = []
    for i in range(n):
        percentage = float(input(f"Enter percentage for student {i + 1}: "))
        perc.append(percentage)
    return perc
def percentage_partition(perc, start, end):
    pivot = perc[end]  
    i = start - 1
    for j in range(start, end):
        if perc[j] <= pivot:
            i += 1
            perc[i], perc[j] = perc[j], perc[i]  
    perc[i + 1], perc[end] = perc[end], perc[i + 1]
    return i + 1
def quick_sort(perc, start, end):
    if start < end:
        pi = percentage_partition(perc, start, end)
        quick_sort(perc, start, pi - 1)
        quick_sort(perc, pi + 1, end)
def display_top_five(perc):
    top_perc = sorted(perc, reverse=True)[:5]
    print("Top Five Percentages:", top_perc)
def main():
    perc = input_percentage()
    while True:
        print("\nChoose an option:")
        print("1. Sort percentages using Quick Sort")
        print("2. Display Top Five Percentages")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            quick_sort(perc, 0, len(perc) - 1)
            print("Sorted Percentages using Quick Sort:", perc)
        elif choice == 2:
            display_top_five(perc)
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")
main()