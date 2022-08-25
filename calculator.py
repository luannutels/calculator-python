import random

letrasmin = "abcdefghijklmnopqrstuvwxyz"
letrasmay = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%&*()_+-=;:.,?/[]{}"

todos = letrasmin + letrasmay + numeros + simbolos

senha= "".join(random.sample(todos, 10))
print("The generated password is:"+senha)