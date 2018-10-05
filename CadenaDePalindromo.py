
__autor__='APOLINAR MARIN CAMPOS'

class Cadenas:
    def __init__(self, cadena):
        self.cadena = cadena

    def Palindrome(self):
        cadena = self.cadena
        c, i, nom, cad, x = 0, 0, '', '', ''
        i = len(cadena)
        nom = cadena.lower().replace(' ','')

        while i != c:
            for x in nom:
                cad = x + cad
                c = c + 1
            if nom == cad:
                # print (cad1, " Es Palindromo")



                return str(cadena + " Es Palindromo")
            else:
                # print (cad1, " No es Palindromo")
                return str(cadena + " No es Palindromo")
        return Palindromo(self)

cadena = input('Dame una palabra: ')
op1 = Cadenas(cadena)

# op1.Pal()#Impresion de la funcion
print(op1.Palindrome())