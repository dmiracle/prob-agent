import agent


def init_population(size, printing=False):
    agents = []
    for i in range(size):
        x = agent.Agent()
        if printing:
            print(i, ": ", x.name, x.uid)
        agents.append(x)
    return agents