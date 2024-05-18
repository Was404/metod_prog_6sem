def process_particles(n, sequence, actions):
    particles = list(sequence)
    for action in actions:
        if action[0] == 'a':
            i, j = action[1], action[2]
            particles.insert(j-1, particles.pop(i-1))
        elif action[0] == 'q':
            k = action[1]
            print(particles[k-1])

n, m = map(int, input().split())
sequence = input().strip()
actions = []
for _ in range(m):
    action = input().strip().split()
    if action[0] == 'a':
        action[1], action[2] = map(int, action[1:3])
    else:
        action[1] = int(action[1])
    actions.append(action)

process_particles(n, sequence, actions)
