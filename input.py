#Primer ejemplo
print("Welcome to the greeter program")
name = input("Enter your name: ")
print("Greetings " + name)

#Segundo ejemplo
print("calculator program")
first_number = input("first number: ")
second_number = input("second number: ")
print(first_number + second_number)
print(int(first_number) + int(second_number))

#Tercer ejemplo
parsecs_input = input("Input number of parsecs:")
parsecs = int(parsecs_input)
lightyears = 3.26156 * parsecs

print(parsecs_input + " parsecs is " + str(lightyears) + " lightyears")
