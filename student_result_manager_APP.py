student={}

while True:
  print("\n--------------STUDENT MANAGER APP----------")
  print("1. Add Student")
  print("2. View Student")
  print("3. View Result PASS OR FAIL")
  print("4. Exit")

  choice=int(input("Enter your choice==>"))

  if choice==1:
    name=input("Enter student name-->")
    marks=int(input("Enter his/her marks-->"))
    student[name]=marks
    print(f"{name} successfully Added!!")


  elif choice==2:
    if not student:
      print("Not Found")

    else:
      for name,marks in student.items():
        print(name ,":", marks)


  elif choice==3:
    name=input("Enter his name-->")
    if name in student:
      marks=student[name]
    
    if name in student:
      if marks>=33:
        print("PASS")
      else:
        print("FAIL")
    else:
      print("Who you want is not here right now.")

  elif choice==4:

    with open("main.txt","w") as file:
      file.write("-----------------FINAL STUDENT RAPORT----------------")
      if not student:
        file.write("No student records found \n")
      else:
        file.write(f"{'Name':<20} | {'Marks':<5} | {'Status':<6}\n")
        file.write("_"*40 +"\n")
        for name,marks in student.items():
          Status="PASS" if marks>=33 else "FAIL"
        file.write(f"{name:<20} | {marks:<5} | {Status:<6}\n")
    print("EXITING....")
    break

      
  else:
    print("INVALIED NUMBER!!!!!!")
