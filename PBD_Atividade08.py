from matplotlib import pyplot as plt
import random
from collections import Counter
import math

users = [
    {"id": 0, "name": "Hero","gender":"m","age":18, 'interest in': 'n'},    
    {"id": 1, "name": "Dunn","gender":"m","age":20, 'interest in': 'b'},    
    {"id": 2, "name": "Sue","gender":"f","age":14, 'interest in': 'm'},    
    {"id": 3, "name": "Chi","gender":"f","age":16, 'interest in': 'm'},      
    {"id": 4, "name": "Thor","gender":"m","age":18, 'interest in': 'f'},      
    {"id": 5, "name": "Clive","gender":"m","age":24, 'interest in': 'f'},
    {"id": 6, "name": "Hicks","gender":"m","age":22, 'interest in': 'f'},   
    {"id": 7, "name": "Devin","gender":"m","age":17, 'interest in': 'm'},       
    {"id": 8, "name": "Kate","gender":"f","age":19, 'interest in': 'm'},        
    {"id": 9, "name": "Klein","gender":"m","age":20, 'interest in': 'f'},
]

for user in users:
    user["friends"] = []

def quantidade_de_usuarios_na_rede():
    return len(users)

def numero_de_conexoes():
    return 25

def gera_amizades(numero_conexoes_desejado, qtde_usuarios_na_rede): #Gera tuplas de conexoes
    for i in range(numero_conexoes_desejado):
        while True:
            u1 = random.randint(0, qtde_usuarios_na_rede - 1)
            u2 = random.randint(0, qtde_usuarios_na_rede - 1)
            if u1 != u2:
                users[u1]['friends'].append(users[u2])
                users[u2]['friends'].append(users[u1])
                break

gera_amizades(numero_de_conexoes(), quantidade_de_usuarios_na_rede())
 
def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip (v, w))

def sum_of_squares (v):
     return dot (v, v)

def variance (v):
    mean = sum(v) / len(v)
    return [v_i - mean for v_i in v]

def covariance (x, y):
    n = len (x)
    return dot(variance(x), variance(y)) / (n - 1)

def correlation (x, y):
    desvio_padrao_x = math.sqrt(sum_of_squares(variance(x)) / (len(x) - 1))
    desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))
    if desvio_padrao_x > 0 and desvio_padrao_y > 0:
        return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
    else:
        return 0


def ex1_e_ex2():    
    idades = []
    num_amigos = []
    for user in users:
        idades.append(user['age'])
        num_amigos.append(len(user['friends']))
    
    print('- Exercicio 1 e 2:')
    print('Covariância:', covariance(idades, num_amigos))
    print('Correlação:', correlation(idades, num_amigos))

def retorna_tupla_de_duas_listas(n, correlacao):
    qtd_amigos = []
    qtd_min = []

    rand_num = random.randint(0, quantidade_de_usuarios_na_rede() - 1)

    for i in range(n):

        if correlacao == 1:
            val = random.randint(0, quantidade_de_usuarios_na_rede() - 1)
            qtd_amigos.append(val)
            qtd_min.append(val) 
        elif correlacao == 0:
            qtd_amigos.append(rand_num)
            qtd_min.append(rand_num)
        else:
            val = random.randint(0, quantidade_de_usuarios_na_rede() - 1)
            qtd_amigos.append(val)
            qtd_min.append(val*-1) 
    return (qtd_amigos, qtd_min)

def ex3_e_ex4():
    tuplas = retorna_tupla_de_duas_listas(10, 1)
    print("\n- EXERCICIO 3.1:\nLista 1:",tuplas[0],"\nLista 2:", tuplas[1], "\nCorrelação:", correlation(tuplas[0], tuplas[1]))
    tuplas = retorna_tupla_de_duas_listas(10, -1)
    print("\n- EXERCICIO 3.2:\nLista 1:",tuplas[0],"\nLista 2:", tuplas[1], "\nCorrelação:", correlation(tuplas[0], tuplas[1]))
    tuplas = retorna_tupla_de_duas_listas(10, 0)
    print("\n- EXERCICIO 3.3:\nLista 1:",tuplas[0],"\nLista 2:", tuplas[1], "\nCorrelação:", correlation(tuplas[0], tuplas[1]))

ex1_e_ex2()
ex3_e_ex4()