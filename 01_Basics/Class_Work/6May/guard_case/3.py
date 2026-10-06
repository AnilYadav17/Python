while True:
  print("Menu : ")
  print("1. Add Two Numbers ")
  print("2. Check Even or Odd ")
  print("3. Find Square ")
  print("4. Exit")

  choice=int(input("Enter the Choice = "))
  match choice:
    case 1:
      num1 =int(input("Enter First Number = "))
      num2 = int(input("Enter Second Number = "))
      print("Result =",(a+b))
    case 4:
      print("Exitted!\n")
      break
    case 2:
       num1 =int(input("Enter A Number = "))
       if num%2==0:
         print("Even")
       else:
         print("Odd")
    case 3:
        num1 =int(input("Enter A Number = "))
        print("Square =",num1**2)
