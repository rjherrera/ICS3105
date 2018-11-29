# coding: utf-8
from prettytable import PrettyTable
from scipy.stats import poisson, binom, expon
from math import factorial, exp, inf
import numpy as np


optimal_policy = [(0, 0), (0, 2), (0, 0), (0, 1), (0, 3), (1, 0), (0, 1), (1, 0), (0, 3),(1, 0), (0, 1), (3, 0), (0, 0), (0, 2), (0, 1), (0, 1), (0, 0), (0, 3), (0, 0), (0, 0), (0, 1), (0, 0), (0, 4), (0, 3), (0, 0), (0, 0), (0, 1), (0, 4), (0, 1), (4, 0), (3, 1), (0, 0), (0, 1), (0, 0), (1, 0), (0, 0), (0, 1), (1, 0), (0, 3), (0, 3), (0, 1), (0, 1), (0, 1), (1, 1), (0, 2), (0,0), (0, 1), (3, 0), (1, 0), (0, 0), (0, 2), (1, 0), (0, 0), (0, 3), (0, 0), (0, 1), (0, 0), (2, 0), (0, 2), (1, 0), (4, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 3), (4, 0), (2, 1), (0, 0), (2, 0), (1, 2), (0, 1), (0, 2), (0, 4), (0, 0), (0, 2), (0, 3), (0, 0), (1, 0), (0, 0), (0, 0),(0, 0), (1, 2), (0, 0), (0, 4), (0, 0), (0, 0), (4, 0), (0, 4), (0, 2), (0, 2), (1, 1), (0, 3), (0, 0), (0, 0), (0, 0), (0, 3), (1, 1), (1, 0), (0, 1), (0, 0), (0, 0), (1, 0), (2, 0), (0, 1), (2, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 1), (0, 1), (0, 0), (0, 1), (0, 1), (1, 1), (2, 0), (0,2), (0, 0), (0, 1), (0, 2), (2, 1), (0, 0), (0, 2), (0, 1), (0, 0), (1, 1), (0, 0), (0, 0), (1, 1), (0, 0), (0, 0), (1, 0), (0, 3), (1, 0), (4, 0), (0, 0), (0, 0), (0, 1), (1, 0), (0, 3), (0, 1), (0, 3), (0, 1), (2, 0), (0, 0), (3, 0), (0, 2), (0, 2), (0, 2), (0, 0), (1, 1), (0, 0), (0, 3),(2, 0), (0, 1), (0, 0), (3, 0), (0, 1), (0, 0), (2, 0), (2, 0), (1, 1), (0, 2), (1, 1), (1, 0), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (3, 0), (0, 3), (0, 0), (1, 0), (0, 1), (0, 1), (2, 0), (0, 0), (1, 0), (3, 0), (1, 2), (0, 0), (0, 3), (0, 2), (4, 0), (0, 1), (0, 1), (0,0), (1, 2), (2, 1), (0, 0), (2, 0), (0, 2), (0, 0), (0, 0), (3, 0), (0, 0), (1, 0), (1, 0), (2, 0), (0, 0), (0, 1), (0, 1), (0, 2), (1, 1), (0, 0), (0, 0), (1, 0), (0, 0), (0, 2), (0, 2), (0, 1), (0, 3), (0, 0), (0, 1), (0, 0), (4, 0), (0, 0), (0, 2), (0, 0), (0, 1), (0, 1), (2, 1), (0, 1),(1, 0), (0, 1), (0, 2), (0, 0), (0, 0), (0, 0), (0, 2), (0, 0), (0, 2), (0, 1), (2, 0), (0, 0), (0, 0), (0, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 4), (0, 2), (0, 0), (0, 3), (0, 1), (0, 1), (0, 4), (0, 1), (0, 2), (1, 1), (1, 1), (0, 0), (0, 2), (4, 0), (0, 0), (1, 0), (1, 0), (1, 0), (2,0), (0, 0), (0, 0), (0, 2), (0, 2), (2, 0), (0, 0), (0, 0), (0, 4), (0, 0), (1, 1), (2, 0), (0, 0), (1, 1), (1, 0), (0, 3), (0, 0), (0, 1), (1, 1), (0, 1), (0, 0), (0, 0), (0, 0), (1, 3), (1, 0), (3, 1), (0, 0), (0, 0), (0, 0), (0, 1), (4, 0), (0, 0), (3, 0), (0, 0), (0, 0), (2, 0), (0, 2),(1, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 1), (2, 1), (0, 0), (0, 2), (2, 0), (0, 0), (0, 0), (0, 1), (3, 0), (0, 1), (1, 0), (1, 0), (0, 4), (0, 1), (0, 0), (4, 0), (1, 0), (1, 0), (2, 0), (3, 0), (0, 1), (0, 3), (0, 1), (1, 0), (0, 0), (0, 1), (0, 1), (2, 2), (0, 1), (0, 0), (3, 0), (0,1), (0, 0), (0, 0), (0, 1), (0, 0), (0, 1), (2, 0), (0, 1), (0, 0), (1, 1), (0, 0), (0, 4), (0, 0), (0, 0), (0, 3), (0, 0), (0, 1), (3, 0), (0, 0), (0, 0), (0, 0), (0, 3), (0, 0), (1, 2), (1, 2), (2, 0), (0, 1), (2, 0), (0, 0), (0, 0), (0, 3), (0, 3), (1, 0), (0, 2), (2, 1), (1, 2), (0, 0),(0, 2), (1, 0), (0, 1), (0, 1), (0, 0), (2, 0), (2, 0), (0, 0), (0, 0), (0, 1), (2, 0), (0, 0), (0, 2), (0, 0), (0, 0), (0, 0), (1, 0), (0, 3), (0, 3), (0, 3), (0, 0), (1, 1), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 2), (1, 0), (0, 3), (0, 0), (0, 1), (1, 0), (2, 0), (0, 1), (1, 0), (3,0), (1, 3), (0, 2), (1, 0), (2, 0), (0, 1), (0, 0), (1, 0), (0, 1), (2, 1), (0, 0), (0, 2), (2, 0), (3, 0), (2, 0), (0, 0), (0, 2), (0, 1), (0, 0), (0, 0), (3, 0), (0, 1), (0, 3), (0, 0), (0, 1), (0, 0), (1, 1), (2, 0), (0, 2), (1, 0), (0, 1), (0, 0), (0, 0), (0, 3), (0, 0), (0, 1), (0, 0),(0, 1), (1, 0), (0, 2), (0, 2), (1, 3), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 4), (0, 1), (0, 3), (0, 1), (0, 1), (0, 1), (0, 0), (3, 0), (0, 0), (1, 1), (0, 0), (0, 2), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 1), (0, 1), (0, 2), (0, 2), (0, 1), (3, 0), (0,0), (0, 1), (0, 1), (0, 1), (0, 2), (1, 3), (0, 2), (0, 1), (0, 1), (0, 1), (0, 3), (0, 0), (0, 0), (3, 0), (0, 0), (0, 0), (1, 0), (0, 1), (0, 4), (1, 0), (0, 1), (0, 1), (1, 1), (0, 2), (0, 1), (0, 3), (0, 0), (2, 0), (1, 0), (2, 0), (0, 1), (0, 0), (0, 1), (0, 0), (0, 1), (0, 1), (0, 0),(1, 0), (0, 3), (3, 0), (0, 0), (0, 0), (0, 0), (1, 0), (0, 2), (3, 0), (0, 4), (0, 3), (0, 0), (0, 0), (2, 1), (1, 2), (0, 1), (2, 0), (1, 0), (0, 0), (0, 0), (2, 2), (0, 0), (0, 0), (0, 0), (1, 0), (0, 1), (0, 0), (0, 1), (0, 1), (0, 2), (1, 1), (0, 2), (0, 0), (0, 0), (0, 0), (1, 0), (0,1), (0, 0), (0, 0), (0, 2), (1, 0), (2, 0), (0, 0), (1, 0), (0, 0), (0, 1), (1, 0), (0, 1), (3, 1), (2, 0), (1, 0), (0, 0), (0, 1), (2, 0), (1, 2), (0, 2), (0, 0), (0, 0), (0, 2), (2, 0), (2, 1), (0, 2), (1, 0), (0, 3), (0, 0), (1, 0), (2, 0), (0, 4), (0, 0), (0, 0), (1, 0), (0, 1), (0, 0),(1, 0), (0, 0), (1, 1), (1, 0), (1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (1, 1), (0, 2), (0, 2), (1, 0), (0, 1), (0, 3), (0, 0), (0, 2), (0, 2), (1, 0), (0, 0), (1, 0), (0, 0), (0, 0), (0, 2), (0, 0), (0, 4), (0, 3), (1, 0), (2, 0), (0, 0), (0, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0,2), (0, 0), (1, 0), (0, 0), (0, 0), (0, 2), (0, 1), (1, 0), (1, 2), (1, 0), (2, 0), (0, 0), (0, 0), (0, 2), (0, 2), (1, 2), (0, 0), (0, 0), (1, 0), (1, 0), (0, 0), (1, 1), (0, 0), (0, 1), (0, 2), (0, 0), (0, 3), (2, 0), (2, 1), (2, 0), (0, 2), (1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),(2, 2), (0, 0), (0, 2), (0, 0), (0, 0), (0, 0), (0, 1), (0, 0), (0, 2)]
# 5,1 3,1

I = 2  # tipos de cirugías
E = 7  # cantidad de pabellones
MAX_CAP = E * 2


def h(i, x):
    # if i == 1:
    #     return 2 * x
    return x


def rec(assigns, total, i=0):
    if i >= len(assigns):
        yield tuple(assigns)
    else:
        for j in range(0, total+1):
            yield from rec(assigns[:i] + [j] + assigns[i+1:], total-j, i+1)


def state_generator():
    # returns ((u_u, u_nu, w)_i, ...) \forall i
    states = set()
    max_length_queue = MAX_CAP
    urgs_gen = rec([0 for i in range(I)], max_length_queue)
    occupied_gen = list(rec([0 for i in range(I)], E))
    for urgs in urgs_gen:
        for w in occupied_gen:
            states.add((urgs, w))
    return list(states)


def x(s):
    # returns ((urgent, no-urgent), ...)
    accs = set()
    total = E - sum(s[1])

    nagns = I
    gen = rec([i for i in range(nagns)], total)
    for options in gen:
        # if sum(options) < total:
            # we dont consider the ones that left beds empty
            # continue
        acc = tuple(min(options[i], s[0][i]) for i in range(I))
        accs.add(acc)
    return accs


def c(s, x):
    if sum(s[0]) - sum(x) < 0:
        print(s[0])
        print(x)
        # print(list(zip(*x))[0], 'blabla')
        raise Exception
    # cost = 0
    # cost += k(lengths[0] - sum(x_trasp[0]))
    # cost += h(lengths[1] - sum(x_trasp[1]))
    c = 0
    for i in range(I):
        c += h(i, s[0][i] - x[i])
    return c
    # return k(lengths[0] - sum(x_trasp[0])) + h(lengths[1] - sum(x_trasp[1]))


def simulate_exponential(scale, T):
    realization = expon.rvs
    time = 0
    amount = 0
    while time < T:
        time += realization(scale=scale)
        amount += 1
    return amount - 1


def simulate_capped_joined_exponential(scale1, scale2, T, capacity1, capacity2):
    realization = expon.rvs
    time1 = 0
    time2 = 0

    rs1 = []
    rs2 = []
    rs3 = []
    rs4 = []
    tt = []
    while time1 < T or time2 < T:
        r1 = realization(scale=scale1)
        r2 = realization(scale=scale2)
        time1 += r1
        time2 += r2
        rs1.append(time1)
        rs3.append(time1)
        rs2.append(time2)
        rs4.append(time2)
        if time1 < time2:
            tt += [1, 2]
        else:
            tt += [2, 1]

    time1 = 0
    time2 = 0
    amount1 = 0
    amount2 = 0
    while capacity1 > 0 and (time1 < T or time2 < T):
        r1 = rs1.pop(0)
        r2 = rs2.pop(0)
        time1 += r1
        time2 += r2
        if time1 < time2:
            amount1 += 1
            capacity1 -= 1
            if time2 < T and capacity1 > 0:
                amount2 += 1
                capacity1 -= 1
        else:
            amount2 += 1
            capacity1 -= 1
            if time1 < T and capacity1 > 0:
                amount1 += 1
                capacity1 -= 1

    time1 = 0
    time2 = 0
    amount3 = 0
    amount4 = 0
    while capacity2 > 0 and (time1 < T or time2 < T):
        r1 = rs3.pop(0)
        r2 = rs4.pop(0)
        time1 += r1
        time2 += r2
        if time1 < time2:
            amount3 += 1
            capacity2 -= 1
            if time2 < T and capacity2 > 0:
                amount4 += 1
                capacity2 -= 1
        else:
            amount4 += 1
            capacity2 -= 1
            if time1 < T and capacity2 > 0:
                amount3 += 1
                capacity2 -= 1
    return (amount1, amount2), (amount3, amount4), tt

# print(simulate_capped_joined_exponential(24/5, 24/3, 24, 8))


def simulation(T):
    def update_state(old, assigned, left, arrived):
        old_queue = old[0]
        old_occupied = old[1]
        new_queue = (old_queue[0] + arrived[0] - assigned[0],
                     old_queue[1] + arrived[1] - assigned[1])
        new_occupied = (old_occupied[0] + assigned[0] - left[0],
                        old_occupied[1] + assigned[1] - left[1])
        new_occupied = (max(0, new_occupied[0]), max(0, new_occupied[1]))
        return (new_queue, new_occupied)

    DAY = 24  # necesario para saber la cantidad de arrivals/departures q hay
    # la tasa debería estar en función de esto
    ARRIVAL_RATE_PER_DAY = [0.1, 0.1]  # llegadas al día por tipo
    DEPARTURE_RATE_PER_DAY = [3, 1]  # salidas al día por tipo

    def naive_choice(state, tt):
        # beds = state[1]
        # available = E - beds[0] - beds[1]
        # type1, type2 = state[0]
        # a = min(type1, available)
        # available -= a
        # b = min(type2, available)
        # return (a, b)
        res = [0, 0]
        beds = state[1]
        queue = state[0]
        el = 0
        while (beds[0] + res[0] + beds[1] + res[1]) < E and len(tt):
            el = tt.pop(0)
            if queue[el - 1] > 0:
                res[el - 1] += 1
        res[el - 1] -= 1
        return tuple(res)

    def optimal_choice(state):
        return optimal_choice_dict[state]

    def simulate_events(rate):
        lambda_hour = rate / DAY
        scale = 1 / lambda_hour
        return simulate_exponential(scale, DAY)

    def simulate_joined_events(rate1, rate2, state1, state2):
        lambda_hour1 = rate1 / DAY
        lambda_hour2 = rate2 / DAY
        scale1 = 1 / lambda_hour1
        scale2 = 1 / lambda_hour2
        capacity = MAX_CAP
        return simulate_capped_joined_exponential(scale1, scale2, DAY, capacity - sum(state1[0]), capacity - sum(state2[0]))

    current_state_naive = ((0, 0), (0, 0))
    current_state_optimal = ((0, 0), (0, 0))
    # print('INICIAL:', S[0])
    total_cost_naive = 0
    total_cost_optimal = 0

    tt = []

    for i in range(T):
        # actual state
        # x_of_current_state = x(current_state_naive)
        # print(x_of_current_state)
        # x_naive = list(x_of_current_state)[0]  # choose 1st decision (policy)
        x_naive = naive_choice(current_state_naive, tt)
        print(current_state_naive, x_naive)
        x_optimal = optimal_choice(current_state_optimal)
        total_cost_naive += c(current_state_naive, x_naive)
        total_cost_optimal += c(current_state_optimal, x_optimal)

        # randomness
        assigned_naive = x_naive
        assigned_optimal = x_optimal
        left = (simulate_events(DEPARTURE_RATE_PER_DAY[0]),
                simulate_events(DEPARTURE_RATE_PER_DAY[1]))

        arrived_naive, arrived_optimal, tt = simulate_joined_events(
            ARRIVAL_RATE_PER_DAY[0],
            ARRIVAL_RATE_PER_DAY[1],
            current_state_naive,
            current_state_optimal
        )

        # update actual state with randomness
        current_state_naive = update_state(current_state_naive, assigned_naive, left, arrived_naive)

        current_state_optimal = update_state(current_state_optimal, assigned_optimal, left, arrived_optimal)

    return total_cost_naive, total_cost_optimal


s = [
    tuple([10 for i in range(I)]),
    tuple([0 for i in range(I)])
]

print('beds:', E)
print('patient types:', I)

S = state_generator()

optimal_choice_dict = {}
for i in range(len(S)):
    optimal_choice_dict[S[i]] = optimal_policy[i]

sims = []
for i in range(100):
    T = 50  # días
    results = simulation(T)
    sims.append(results)

avg_cost_naive = sum(i[0] for i in sims) / len(sims)
avg_cost_optimal = sum(i[1] for i in sims) / len(sims)
print(avg_cost_naive, avg_cost_optimal, 100*avg_cost_naive/avg_cost_optimal)
