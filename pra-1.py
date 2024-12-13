def remove_duplicates(lst):
 new_lst = []
 for i in lst:
   if i not in new_lst:
     new_lst.append(i)
 return new_lst

def intersection(lst1, lst2):
 new_lst = []
 for val in lst1:
  if val in lst2:
    new_lst.append(val)
 return new_lst

def union(lst1, lst2):
  new_lst = lst1.copy()
  for val in lst2:
   if val not in new_lst:
     new_lst.append(val)
  return new_lst
 
def difference(lst1, lst2):
    new_lst = []
    for val in lst1:
      if val not in lst2:
        new_lst.append(val)
    return new_lst
  
def symmetric_difference(lst1,lst2):
 lst3=[]
 D1=difference(lst1,lst2)
 D2=difference(lst2,lst1)
 lst3=union(D1,D2)
 return lst3

def main():
 se_comp = input("Enter names of students in SE COMP (separated by space): ").split()
 cricket = remove_duplicates(input("Enter names of students who play cricket (separated by space): ").split())
 football = remove_duplicates(input("Enter names of students who play football (separated by space):").split())
 badminton = remove_duplicates(input("Enter names of students who play badminton (separated by space):").split())
 while True:
  print("\n\n--------------------MENU--------------------\n")
  print("1. List of students who play both cricket and badminton")
  print("2. List of students who play either cricket or badminton but not both")
  print("3. List of students who play neither cricket nor badminton")
  print("4. Number of students who play cricket and football but not badminton")
  print("5. Exit\n")
  choice = int(input("Enter your Choice (from 1 to 5) :"))
  if choice == 1:
   print("List of students who play both cricket and badminton: ", intersection(cricket, badminton))
  elif choice == 2:
   print("List of students who play either cricket or badminton but not both: ", symmetric_difference(cricket, badminton))
  elif choice == 3:
   print("List of students who play neither cricket nor badminton: ", difference(se_comp, union(cricket,badminton)))
  elif choice == 4:
   print("Number of students who play cricket and football but not badminton: ",len(difference(intersection(cricket, football), badminton)))
  elif choice == 5:
   print("Thanks for using this program!")
   break
  else:
   print("!!Wrong Choice!! ")
   
main()
