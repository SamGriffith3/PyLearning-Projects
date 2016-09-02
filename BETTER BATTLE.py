import pprint


p1_matrix = [[0 for _ in range(10)] for _ in range(10)]
p2_matrix = [[0 for _ in range(10)] for _ in range(10)]


pprint.pprint(p1_matrix)

print(p1_matrix[4][4])

def new_matrix():
    return [[0 for _ in range(10)] for _ in range(10)]
