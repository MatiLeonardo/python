from datetime import date

print( "Hello, Contosoville!" )
# This is a comment that won't be interpreted as a command.

# Associate variable town with the value "Contosoville"
town = "Contosoville"

# Print a message about the secret location
print( "The town I am looking for is " + town )

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )

# Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville!" )
 
print(type(town))

print(date.today())

print("Today's date is: " + str(date.today()))

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

