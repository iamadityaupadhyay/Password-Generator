import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password=[]
nr=int(input("Enter the numbers of numbers in your password?"))
letter=int(input("Enter the number of letters in your password?"))
sym=int(input("Enter the number of symbol in your password?"))
for char in range(1, nr+1):
  password.append(random.choice(numbers)) 
for char in range(1,letter+1):
  password.append(random.choice(letters))
for char in range(1,sym+1):
  password.append(random.choice(symbols))

random.shuffle(password)
passw=""
for char in password:
  passw= passw + char

print(f"The required password is {passw}")