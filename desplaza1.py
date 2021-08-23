from time import time
from random import randint
from math import log, sqrt
# dados n y m nos devuelve el cociente de la division entre n y m.

def cociente(n, m):
    return n//m
# dados n y m nos devuelve el resto de la division entre n y m.

def resto(n, m):
    return n % m

# Calcula el primer divisor de n, aun es lento

def p_d(n):
    for i in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29):
        if n % i == 0:
            n = i
    k = 30  # Aqui fijo los saltos de 30 en 30 aunque tiene que hacer 8 if si no se cumple ninguno. Un poco mas rapido que antes
    L = int(sqrt(n))
    for i in range(k, L, k):
        for p in (i+1, i+7, i+11, i+13, i+17, i+19, i+23, i+29):
            if n % p == 0:
                n = p
                break
        if n == p:
            break
    return n


def primiun(n):  # Es impar pero no es primo, lo hace mal Lucas, pero da un divisor de 2**n-1
    return n != p_d(n) and n % 2 == 1
# print(primiun(n))


def Lucas_Lehmer(n):  # Se da el numero pequeño.El lo eleva a 2**n-1
    M = (1 << n)-1
    S = 4
    for _ in range(n-2):
        S = (S*S-2) % M
    return S == 0  # Si S es cero, entonces 2**n-1(M) es primo


def Millar(n):  # Para que sea fiable k>5, yo le doy k=7
    if n < 2:
        return False
    if n == 2 or n == 3:  # si no añado esto, da error en estos numeros, por el modulo random.py
        return True
    if n % 2 == 0:
        return False
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d >>= 1
    for _ in range(7):#Aqui he fijado en 7 a k que en principio tiene la función (n,k) si k crece tambien la precision, con 7 no he visto fallos. 
        rand = randint(2, n - 2)
        x = pow(rand, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s):
            toReturn = True
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n - 1:
                toReturn = False
                break
        if toReturn:
            return False
    return True
    
def sigup(n):
    if n < 2:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        n -= 1
    i = n+2
    while not Millar(i):
        i += 2
    return i


# Como saber si un numero es generado por 2**p-1
def esMer(n):
    N = int(log(n+1)/log(2))
    return n == (1 << N)-1

# Ver si un numero es primo
def primo(n):
    if esMer(n):
        N = int(log(n+1)/log(2))
        return Lucas_Lehmer(N)
    else:
        return Millar(n)

def primer_divisor(n):
	if primo(n):
		return n
	N=int(log(n+1)/log(2))
	i=2
	while i <=2*N:
		if n%i==0:
			n=i
			break
		i=sigup(i)
	if esMer(n):
		for j in range(2*N+1, int(n**0.5)+1,2*N):
			if n%j==0:
				n=j
				break
		return n
	else:
		return p_d(n)
# definir una funcion que nos da los primeros r factores primos con sus exponentes [(p,exp)]


def f_pj(n, r):
    l = []
    j = 0
    while n > 1 and j < r:
        k = primer_divisor(n)
        ex = 1
        n = n//k
        while k == primer_divisor(n):
            ex += 1
            n = n//k
        l.append((k, ex))
        j += 1
    return tuple(l)


def ultimo_divisor(n):
    if primo(n):
        return n
    else:
        return n//primer_divisor(n) # Si n es primo, el ultimodivisor es 1 (n//n=1, podría hacer que en este caso dijera que es n en vez de 1)
 
def ultimo_divisor_primo(n):
    ult=ultimo_divisor(n)
    n=ult
    while not primo(ult):
        ult = ultimo_divisor(ult)
        n=ult
    return n

def factores_primos(n):
    l = []
    while n > 1:
        k = primer_divisor(n)
        ex = 1
        n = n//k
        while k == primer_divisor(n):
            ex += 1
            n = n//k
        l.append((k, ex))
    return l
# Definimos primi solo por estetica en la respuesta


def primi(n):
    if primo(n):
        return "El número " + str(n) + " ES PRIMO"
    else:
        return "El número " + str(n) + " NO ES PRIMO"

# Definir la función que encuentra el siguiente numero  X que hará perfecto al 2**(X-1)*(2**X -1)
def sigMp(n):
    n = sigup(n)
    if Lucas_Lehmer(n):
        return n
    else:
        return sigMp(n)
    
def n_divisores(n):
    l = factores_primos(n)
    k = 1
    for i in l:
        k = k*(i[1]+1)
    return k


def listal(n):  # n es un par (primo,exponente)
    a = n[0]
    p = n[1]
    l = []
    for i in range(0, p+1):
        l.append(a**i)
    return l
 
# Multiplica dos listas de números.
def mult(l1, l2):
    l = []
    for i in l1:
        for j in l2:
            l.append(i*j)
    return l

# Aprovechando las dos anteriores calcular los divisores de un numero. (Es muy rápida)
def divisores(n):
    k = factores_primos(n)
    i = 0
    l = []
    l1 = [1]
    while i < len(k):
        l2 = listal(k[i])
        l = mult(l1, l2)
        i += 1
        l1 = l
    return tuple(l)
# Calcular una lista de numeros primos a partir de uno dado. Aunque éste no sea primo o incluso si es par.

def listp(p, q):
    if q <= 2:
        lista = [2]
    else:
        lista = [q]
    if not primo(q):
        lista = [sigup(q)]
        i = sigup(q)
    else:
        lista = [q]
        i = q
    while len(lista) < p:
        lista.append(sigup(i))
        i = sigup(i)
    yield tuple(lista)
