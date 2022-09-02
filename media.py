"""temperatura = int (input("tempura "))
dor_cabeça = input ( "tem dor de cabeça = ")
coriza = input ("tem coriza: ")
print ("\ntemperatura =" , temperatura)
print ("\ndor_cabeça = ", dor_cabeça)
print ("\ncoriza = " , coriza)
gripe = temperatura > 37 and dor_cabeça or coriza
print("o paciente tem gripe = ", gripe)

nome = "Anderson"
sobrenome = "Portes"
média = 0.0
português = 6.5
matemática = 9.0
história = 4.0
geografia = 4
educação_física = 5.5
print ("nome do aluno: ", nome, sobrenome)
print ("valor da média = /t/t/t/t/t/t" , média)
média = (português + matemática + história + geografia + educação_física)/5
print ("valor da média atualizada = \t" , média) """

nome = input("Nome do aluno: ")
sobrenome = input("Sobrenome do aluno: ")

português = float(input("digite a nota de português: "))
matemática = float (input ("digite a nota de matemática: "))
história  = float (input ("digite a nota de história: "))
geográfia = float (input ("digite a nota de geográfia: "))
educação_física = float (input ("digite a nota de educação física: "))

média = (português + matemática + história + geográfia + educação_física)/5

print ("o aluno ", nome, sobrenome, "foi ")
print (" a média é: ", média)

if (média >= 6):
    print("aprovado")
else:
    print("reprovado") 
