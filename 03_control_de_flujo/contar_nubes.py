# -- coding: utf-8 --

string = "Una nube es un hidrometeoro consistente en diminutas partículas de agua líquida o hielo, o de ambos, suspendidas en la atmósfera y que, por lo general, no tocan el suelo."

j=0
for  c in string :
    if c in "aeiou" : 
        j += 1

print("Contiene ", j, " vocales, de un total de ", len(string), " letras.")
