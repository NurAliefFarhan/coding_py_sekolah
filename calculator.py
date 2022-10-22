def Pertambahan(x, y):
    return x + y

def Pengurangan(x, y):
    return x - y

def Perkalian(x, y):
    return x * y

def Pembagian(x, y):
    return x / y

print("Select Operation.")
print("1. Pertambahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

choice = input("Pilih dengan angka (1/2/3/4) : ")

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))

if choice == '1':
    print("Hasil=>",num1,"+",num2,"=", (num1 + num2))

elif choice == '2':
    print("Hasil =>",num1,"-",num2,"=", (num1 - num2))

elif choice == '3':
    print("Hasil =>",num1,"*",num2,"=", (num1 * num2))

elif choice == '4':
    print("Hasil =>",num1,"/",num2,"=", (num1 / num2))

else:
    print("Invalid Input")

    