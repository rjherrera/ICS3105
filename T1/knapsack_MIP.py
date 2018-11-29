from parser import Parser

from gurobipy import *


def knapsack(n, B, volumes, values, binary=True):
    n = [i for i in range(n)]
    model = Model('Knapsack')
    model.params.output_flag = False

    x = model.addVars(n, vtype=GRB.BINARY if binary else GRB.INTEGER, name='x')

    model.addConstr(quicksum(volumes[p] * x[p] for p in n) <= B)
    obj = quicksum(values[p] * x[p] for p in n)

    model.setObjective(obj, GRB.MAXIMIZE)
    model.optimize()

    return [i.X for i in model.getVars()]


if __name__ == '__main__':
    from datetime import datetime
    file = 'InstanciasKnapsackSinSolucionFixed.xlsx'
    p = Parser(file)

    for instance in p.instances:
        n, B, vol, val = p.parameters_from_sheet_name(instance)
        start = datetime.now()
        out = knapsack(n, B, vol, val)
        print(f'Instancia {instance}:')
        print('\tTime', datetime.now() - start)
        print(f'\tVolumen mochila (B): {B}')
        print(f'\tCantidad de objetos (n): {n}')
        print('\tÓptimo:')
        print(f'\t  Volumen óptimo: {sum([i * j for i, j in zip(out, vol)])}')
        print(f'\t  Valor óptimo: {sum([i * j for i, j in zip(out, val)])}')

    file = 'InstanciasKnapsackSinSolucionFixed.xlsx'
    p = Parser(file)

    print('\nKnapsack Entero\n')

    for instance in p.instances:
        n, B, vol, val = p.parameters_from_sheet_name(instance)
        start = datetime.now()
        out = knapsack(n, B, vol, val, binary=False)
        print(f'Instancia {instance}:')
        print('\tTime', datetime.now() - start)
        print(f'\tVolumen mochila (B): {B}')
        print(f'\tCantidad de objetos (n): {n}')
        print('\tÓptimo:')
        print(f'\t  Volumen óptimo: {sum([i * j for i, j in zip(out, vol)])}')
        print(f'\t  Valor óptimo: {sum([i * j for i, j in zip(out, val)])}')
