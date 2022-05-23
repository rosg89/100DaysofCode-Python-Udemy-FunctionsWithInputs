# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")
  print(f"{name}, isn't the weather nice today?")

#Call the function
greet("Rocio")
greet("Lucas")

#funcion (parametros)
#parametros = argumentos
#Name es un parametro
#Rocio o Lucas son argumentos

#Multiple inputs
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"What is it like in {location}")

greet_with("Rocio", "Ushuaia")

#Keyword Arguments
greet_with(location = "Somewhere", name="Somebody")