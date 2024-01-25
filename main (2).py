#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
sum=""
for i in range(0,nr_letters):
  char=random.choice(letters)
  sum+=char
for i in range(0,nr_numbers):
  char=random.choice(numbers)
  sum+=char
for i in range(0,nr_symbols):
  char=random.choice(symbols)
  sum+=char
print(f"Easy Level - Order of characters randomised:{sum}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for i in range(0,len(sum)):
  sum=list(sum)
  char=random.shuffle(sum)
num=""
for n in range(0,len(sum)):
  num+=sum[n]
print(f"Hard Level - Order of characters randomised:{num}")