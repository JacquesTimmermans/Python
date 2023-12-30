#
# Cálculo Do Determinante De Uma Matriz
# Quadrada De Terceira Ordem
# Pelo
# Teorema De Saoirse Una Ronan
# 
# by Timmermans, Jacques
#
Matriz = [ [ 2, 3, 5 ] , [ 7, 11, 13 ], [ 17, 19, 23 ] ]
def theta(t,varpi):
	if (t<varpi): sinal=0
	else: sinal=1
	return sinal
def pot(entrada):
	if (entrada==0): ptt=1
	else: ptt=-1
	return ptt
det = 0
for t in range(6) :
	prod = 1
	for p in range(3) :
		l = p + 1
		i = (t+2+l) % 3 + 1
		j = l + (4-2*l)*theta(t,3)
		print("μ[",i,",",j,"] =", Matriz[i -1][j -1])
		prod = prod*Matriz[i-1][j-1]
	det = det + pot(theta(t,3))*prod
	print(pot(theta(t,3))*prod)
print('@@@@@')
print('Determinante = ',det)
# Fim