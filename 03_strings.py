### Strings ###

my_string = "Mi String"
my_other_string = "Mi otro String"

print(len(my_string))
print(len(my_other_string))
print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"
print(my_new_line_string)

my_tab_string = "Este es un String\tcon tabulación"
print(my_tab_string)

my_scape_string = "\\tEste es un String \\n nescapado"
print(my_scape_string)

# Formateo

name, surname, age = "Jorman", "Espinoza", 33

print("Mi nombre es Jorman Espinoza y mi edad es 33")
print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))
print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)

# División

language_slide = language[0:1]
print(language_slide)

language_slide = language[1:]
print(language_slide)

language_slide = language[-1]
print(language_slide)

language_slide = language[0:6:2]
print(language_slide)

# Reverso

reversed_language = language[::-1]
print(reversed_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count("P"))
print(language.isnumeric())
print(str(age).isnumeric())
print("25".isnumeric())
print(language.upper().isupper())
print(language.startswith("Py"))
