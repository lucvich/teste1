def inverter_string(s):
    inverted = ""
    for i in range(len(s) - 1, -1, -1):
        inverted += s[i]
    return inverted

# Exemplo de entrada
string_original = input("Digite uma string para inverter: ")

# Invertendo a string
string_invertida = inverter_string(string_original)

# Exibindo a string invertida
print("String invertida:", string_invertida)
