import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#selected_letters = random.choice(letters) jangan taruh diluar karena dia random cuman sekali jadiny satu jenis
#selected_symbols = random.choice(symbols)
#selected_numbers = random.choice(numbers)
password = [] #kl gk random urutan pake password = ""
for x in range(1,nr_letters+1):# jika tidak ingin 1,x+1 ubah jd 0,x
    password += random.choice(letters)

for y in range(1,nr_numbers+1):
    password += random.choice(numbers)

for z in range(1,nr_symbols+1):
    password += random.choice(symbols)

random.shuffle(password)
final = ""

final_password = final.join(password)#seperator cuman masalahny harus pake dictionary []
print(final_password)
# 1,2,3(1,4)
# 0,1,2,3(0,4)




