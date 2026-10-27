
# EXERCISE 1: TABLE-DRIVEN AGENT

table = {
    ('A', 'Dirty'): 'Suck',
    ('A', 'Clean'): 'Right',
    ('B', 'Dirty'): 'Suck',
    ('B', 'Clean'): 'Right',
    ('C', 'Dirty'): 'Suck',
    ('C', 'Clean'): 'Left'
}


def table_driven_agent(percept):
    action = table[percept]
    return action


print("===== TABLE-DRIVEN AGENT =====")

percept = ('A', 'Dirty')
print("Perception:", percept)
print("Action:", table_driven_agent(percept))


# EXERCISE 2: SIMPLE REFLEX AGENT

def simple_reflex_agent(percept):
    location, status = percept

    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'C':
        return 'Left'
    else:
        # At B, move towards C.
        return 'Right'


print("\n===== SIMPLE REFLEX AGENT =====")

percept = ('B', 'Dirty')
print("Perception:", percept)
print("Action:", simple_reflex_agent(percept))

# EXERCISE 3: MODEL-BASED AGENT

# The agent remembers the condition of all locations.
model = {
    'A': 'Unknown',
    'B': 'Unknown',
    'C': 'Unknown'
}

# Actual environment
environment = {
    'A': 'Dirty',
    'B': 'Clean',
    'C': 'Dirty'
}

Location = 'A'


def model_based_agent(location, status):
    # Update the model using the current perception.
    model[location] = status

    # If the current location is dirty, clean it.
    if status == 'Dirty':
        return 'Suck'

    # Find locations that are unknown or dirty.
    targets = [
        loc for loc in ['A', 'B', 'C']
        if model[loc] in ['Unknown', 'Dirty']
        and loc != location
    ]

    # If every location is clean, stop the simulation.
    if not targets:
        return 'Stop'

    # Choose the nearest target.
    target = min(
        targets,
        key=lambda loc: abs(
            ord(loc) - ord(location)
        )
    )

    # Move one step towards the target.
    if ord(target) > ord(location):
        return 'Right'
    else:
        return 'Left'


print("\n===== MODEL-BASED AGENT =====")

max_steps = 20

for step in range(max_steps):
    status = environment[Location]

    print("\nStep:", step + 1)
    print("Perception:", (Location, status))

    action = model_based_agent(Location, status)
    print("Action:", action)
    print("Model:", model)

    if action == 'Stop':
        print("\nAll locations are clean!")
        break

    elif action == 'Suck':
        environment[Location] = 'Clean'

    elif action == 'Right':
        if Location in ['A', 'B']:
            Location = chr(ord(Location) + 1)

    elif action == 'Left':
        if Location in ['B', 'C']:
            Location = chr(ord(Location) - 1)

else:
    print("\nMaximum steps reached.")