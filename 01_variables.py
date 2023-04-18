# Variables

my_string_variable = "My String variable"
print(my_string_variable)

my_int_variable = 25
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables de un print
print(my_string_variable, my_int_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Jorman", "Espinoza", "namroj", 33
print("Me llamo:", name, surname, ". Mi edad es:", age, "Y mi alias es:", alias)

# Inputs
first_name = input("¿Cuál es tu nombre?")
age = input("¿Cuántos años tienes?")

print(first_name)
print(age)
