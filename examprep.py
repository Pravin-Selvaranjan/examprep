# var= "James Bond"
# print(var[2::-1])
#
# {"apple,"banana","cherry"}

x = int(10)
b = float(12.8)
c = float(5.6)

print(x + b + c)

class Juice:
    def __init__(self):
        self.sweet = True
        self.sour = True


    def cool(self):
        return "ice cold juice tastes amazing"



juice_object = Juice()

print(juice_object.cool())

num = int(input("Enter a number: "))   # The % sign is like division only it checks for the remainder, so if the number divided by 2 has a remainder of 0 it's even otherwise odd.
if num % 2 == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

character_name = "Jonty "
character_fav = "Run"
print(character_name + "likes to go shopping")
print("Andy is 657 years old")
print("In the evenings, Andy likes to go for a walk")

phrase = "Sparta Global"

print(phrase[0])
print(phrase.index("G"))

name = input("Enter your name: ")
print("Hello " + name)


num1 = input("Enter a number: ")
num2 = input("Enter a number: ")
result = int(num1) + int(num2)
print(result)

colour = input("Enter a colour ")
plural_noun = input("Enter a plural noun ")
celebrity = input("Enter a celebrity ")

print("Roses are " + colour)
print(plural_noun + " are blue")
print("I love " + celebrity)


friends = ["John", "James", "Owen", "Harold", "Saron"]

print(friends[1:3])

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a tall male ")
elif is_male and not(is_tall):
    print("You are a short male ")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")

else:
    print("You are not a male and not tall ")


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print (max_num(3, 4, 5))


num1 = float(input("Enter a number: "))
operator = input("Enter operator: ")
num3 = float(input("Enter a second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1 * num2)
else:
    print("invalid")



