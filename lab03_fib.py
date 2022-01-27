import pyrtl

A = pyrtl.Input(bitwidth=32, name='A')
B = pyrtl.Input(bitwidth=32, name='B')

regA = pyrtl.Register(bitwidth=32, name='regA')
regResult = pyrtl.Register(bitwidth=32, name='regResult')

count = pyrtl.Input(bitwidth=32, name='count')

result = pyrtl.Output(bitwidth=32, name='result')

with pyrtl.conditional_assignment:
    with count == 0:
        regA.next |= A
        result |= A
    with count == 1:
        regResult.next |= B
        result |= B
    with count > 1:
        regResult.next |= regA + regResult
        regA.next |= regResult
        result |= regA + regResult

sim_trace = pyrtl.SimulationTrace()
sim = pyrtl.Simulation(tracer=sim_trace)

for cycle in range(16):
    sim.step({
        'A': 1,
        'B': 2,
        'count': cycle
    })
sim_trace.render_trace()