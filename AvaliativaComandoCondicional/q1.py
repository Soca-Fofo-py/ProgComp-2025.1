# 1) Faça um programa que recebe um número de até quatro algarismos
#    (ou seja, deve ser menor do que 10000) e apresenta a soma dos algarismos.
################################################################################
# Quatro algarismos também aceitaria -9999, logo: (-10000 <var< 10000)
# Assumir que sempre será me apresentado numeros inteiros
var_1 = int(input("Digite um número menor que '10.000', para que seja apresdentado a soma de seus algarismos: "))
var_soma = 0
if var_1 >= 10000 or var_1 < 0:
    print ("Por favor, digite um número menor que 10.000 e maior que 0!")
else:
    # somar os valores em cada posição!
    unidade = var_1 % 10
    dezena = (var_1 // 10) % 10
    centena = (var_1 // 100) % 10
    milhar = (var_1 // 1000) % 10
    var_soma = unidade+dezena+centena+milhar
print("A soma dos algarismos de",var_1,"é:",var_soma)


# Não sei o que é para fazer ao certo
