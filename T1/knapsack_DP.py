from parser import Parser
from datetime import datetime

def elapsed(start, label=''):
    print(label, datetime.now() - start)


def binary_knapsack(n, B, volumes, values):
    start = datetime.now()
    V = [[0 for _ in range(B + 1)] for _ in range(n)]
    for i in range(B + 1):
        V[n - 1][i] = values[n - 1] if volumes[n - 1] <= i else 0

    elapsed(start, '\tSetup time:')
    for k in range(n - 2, -1, -1):
        vol_k = volumes[k]
        val_k = values[k]
        next_k = k + 1
        for j in range(0, min(vol_k, B + 1)):
            V[k][j] = V[next_k][j]
        for i in range(vol_k, B + 1):
            V[k][i] = max(V[next_k][i], val_k + V[next_k][i - vol_k])
    elapsed(start, '\tTotal time:')
    return V


def integer_knapsack(n, B, volumes, values):
    start = datetime.now()
    V = [0 for _ in range(B + 1)]
    for i in range(B + 1):
        V[i] = values[n - 1] if volumes[n - 1] <= i else 0

    elapsed(start, '\tSetup time:')
    for i in range(B + 1):
        V[i] = max(values[k] + V[i - volumes[k]] if volumes[k] <= i else 0
                   for k in range(n))
        if i % 1000 == 0:
            print(f'\t\tProgreso: {(i / B) * 100}%')
            elapsed(start, '\t\t\t')

    elapsed(start, '\tTotal time:')
    return V


def solution_from_matrix(n, B, volumes, values, V):
    objects = []
    value = V[0][B]
    for i in range(n - 1):
        if value <= 0:
            break
        if value != V[i + 1][B]:
            objects.append(i)
            value = value - values[i]
            B = B - volumes[i]
    return objects


if __name__ == '__main__':
    file = 'InstanciasKnapsackSinSolucionFixed.xlsx'
    p = Parser(file)

    for instance in p.instances[0:0]:
        print(f'Instancia {instance}:')
        n, B, vol, val = p.parameters_from_sheet_name(instance)
        out = binary_knapsack(n, B, vol, val)
        obj = solution_from_matrix(n, B, vol, val, out)
        print(f'\tVolumen mochila (B): {B}')
        print(f'\tCantidad de objetos (n): {n}')
        print('\tÓptimo:')
        print(f'\t  Volumen óptimo: {sum(vol[i] for i in obj)}')
        print(f'\t  Valor óptimo: {out[0][B]}')

    for instance in p.instances[3:4]:
        print(f'Instancia {instance}:')
        n, B, vol, val = p.parameters_from_sheet_name(instance)
        out = integer_knapsack(n, B, vol, val)
        # obj = solution_from_matrix(n, B, vol, val, out)
        print(f'\tVolumen mochila (B): {B}')
        print(f'\tCantidad de objetos (n): {n}')
        print('\tÓptimo:')
        # print(f'\t  Volumen óptimo: {sum(vol[i] for i in obj)}')
        print(f'\t  Valor óptimo: {out[B]}')
