from pagent import agent

def run():
    print("Running")
    agent_count = 100
    agents = []
    for i in range(agent_count):
        x = agent.Agent()
        print(i, ": ", x.name, x.uid)
        agents.append(x)