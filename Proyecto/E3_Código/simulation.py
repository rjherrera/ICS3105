import random
import simpy

INSTANT_UNIT = 'min'
SIM_TIME = 500
INTERVAL = 10
ORS = 3
NAME = "P{0}"
SEVERITIES = {3: 'CRÍTICO', 2: 'GRAVE', 1: 'NORMAL'}


class Surgery:

    def __init__(self, name, duration, frequency):
        self.name = name
        self.duration = duration
        self.frequency = frequency

    def __repr__(self):
        return f'{self.name} ({self.duration}{INSTANT_UNIT})'


class Pacient:

    def __init__(self, *args, **kwargs):
        self.name = kwargs['name']
        self.arrive = kwargs['arrive']
        self.number = kwargs['arrival_number']
        self.severity = kwargs['severity']

    @property
    def tolerance(self):
        return (3 - self.severity) * 30

    def __repr__(self):
        return f'{self.name} ({SEVERITIES[self.severity]})'


class Hospital:

    def __init__(self, env, capacity, surgeries):
        self.env = env
        self.ors = simpy.Resource(env, capacity=capacity)
        self.surgeries = surgeries
        self.operated = []
        self.preempted_amount = 0

    @property
    def operated_amount(self):
        return len(self.operated)

    @property
    def surgeries_weights(self):
        total = sum(s.frequency for s in self.surgeries)
        return [s.frequency / total for s in self.surgeries]

    def pick_surgery(self):
        return random.choices(self.surgeries, self.surgeries_weights)[0]

    def wait(self, pacient):
        with self.ors.request() as req:
            # lo que pase primero irá a results (que haya/se libere
            # un pabellón o que se acabe la tolerancia del paciente)
            results = yield req | self.env.timeout(pacient.tolerance)
            if req not in results:
                # si no había pabellón libre y no puede esperar más el
                # paciente, se saca a algún paciente agendado del pabellón.
                self.preempted_amount += 1
                print(f'[REAGENDAMIENTO] {pacient} esperó {pacient.tolerance}',
                      f'pero no se disponibilizó un pabellón, por lo que en',
                      f'tiempo {self.env} se reagendó a un paciente normal')
            # siempre se opera (la diferencia es si había pabellón libre o no)
            surgery = self.pick_surgery()
            self.operated.append(pacient)
            print(f'[OPERACIÓN] {pacient} entró a pabellón en tiempo {self.env} a operarse de {surgery}')
            yield self.env.timeout(surgery.duration)
            print(f'[SALIDA] {pacient} terminó su operación en tiempo {self.env}')


def pacient_generator(env, lambdat, hospital):
    count = 0
    while True:
        yield env.timeout(random.expovariate(.001736111))
        pacient = Pacient(
            name=NAME.format(count),
            arrive=int(env.now),
            arrival_number=count,
            severity=random.randint(1, 3)
        )
        print(f'[LLEGADA] {pacient} ha llegado en el instante {env}')
        count += 1
        env.process(hospital.wait(pacient))


if __name__ == '__main__':
    env = simpy.Environment()
    env.__class__.__str__ = lambda x: str(round(x.now))

    ors_amount = 1
    lambdat = 60  # INTERVAL
    time_limit = 1440  # SIM_TIME

    surgeries = [Surgery(name='Apendicitis', duration=60, frequency=0.5),  # 30-60
                 Surgery(name='Colecistitis', duration=120, frequency=0.3),  # 30-90,60-120
                 Surgery(name='Cataratas', duration=240, frequency=0.2)]

    hospital = Hospital(env, ors_amount, surgeries)
    gen = pacient_generator(env, lambdat, hospital)

    env.process(gen)
    print(f'Se inicia la simulación con {ors_amount} pabellones disponibles.')
    env.run(until=time_limit)
    print('Se operaron %d pacientes de urgencia teniendo que reagendar %d.'
          % (hospital.operated_amount, hospital.preempted_amount))
