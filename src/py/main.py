# * Author: Malika Xasanboyeva
# * Date:


# Problem 1: Shortest Path
n, m, k = map(int, input().split())
roads = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    roads[a-1].append(b-1)
    roads[b-1].append(a-1)
forbidden = set()
for i in range(k):
    a, b, c = map(int, input().split())
    forbidden.add((a-1, b-1, c-1))
    forbidden.add((a-1, c-1, b-1))
    forbidden.add((b-1, a-1, c-1))
    forbidden.add((b-1, c-1, a-1))
    forbidden.add((c-1, a-1, b-1))
    forbidden.add((c-1, b-1, a-1))

# Finding the shortest path using breadth-first search
start = 0
end = n-1
visited = set()
queue = [(start, [])]
while queue:
    node, path = queue.pop(0)
    if node == end:
        print(len(path))
        print(" ".join(str(x+1) for x in path+[node]))
        break
    if node not in visited:
        visited.add(node)
        for neighbor in roads[node]:
            if (node, neighbor, end) not in forbidden:
                queue.append((neighbor, path+[node]))
else:
    print(-1)





# Problem 2: SPIKES - Spiky Mazes
n, m, j = map(int, input().split())
maze = []
for i in range(n):
    row = input().strip()
    maze.append(row)

# Finding the start and end points
start = None
end = None
for i in range(n):
    for j in range(m):
        if maze[i][j] == '@':
            start = (i, j)
        elif maze[i][j] == 'x':
            end = (i, j)

# Defining the possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Defining the BFS function
def bfs(start, end, j):
    queue = [(start, j)]
    visited = set()
    while queue:
        current, remaining_jumps = queue.pop(0)
        if current == end:
            return "SUCCESS"
        if current in visited:
            continue
        visited.add(current)
        i, j = current
        if maze[i][j] == 's':
            if remaining_jumps == 0:
                continue
            else:
                remaining_jumps -= 1
        for move in moves:
            new_i, new_j = i + move[0], j + move[1]
            if maze[new_i][new_j] != '#':
                queue.append(((new_i, new_j), remaining_jumps))
    return "IMPOSSIBLE"

# Running the BFS function
result = bfs(start, end, j)
print(result)





# Problem 3: Transformation from A to B
a = int(input())
b = int(input())

results = []

while b >= a:
  results.append(b)
  if b % 10 == 1:
    b = (b-1) // 10
  elif b % 2 == 0:
    b = b // 2
  else:
    break

if results[-1] != a:
  print('NO')
else:
  print('YES')
  print(len(results))

print(results[::-1])





# Problem 4: Making Genome in Berland 
n = int(input())
fragments = []
for i in range(n):
    fragments.append(input())

# Creating a set of all distinct nucleotides
nucleotides = set()
for fragment in fragments:
    for nucleotide in fragment:
        nucleotides.add(nucleotide)

# Creating a graph where each nucleotide is a node
# and each fragment is an edge connecting the corresponding nodes
graph = {}
for nucleotide in nucleotides:
    graph[nucleotide] = set()
for fragment in fragments:
    for i in range(len(fragment)):
        if i == 0:
            graph[fragment[i]].add(fragment[i+1])
        elif i == len(fragment)-1:
            graph[fragment[i]].add(fragment[i-1])
        else:
            graph[fragment[i]].add(fragment[i-1])
            graph[fragment[i]].add(fragment[i+1])

# Finding the shortest path that visits all nodes
# using breadth-first search
start_node = list(nucleotides)[0]
visited = set()
queue = [(start_node, "")]
while queue:
    node, path = queue.pop(0)
    if node not in visited:
        visited.add(node)
        path += node
        if len(visited) == len(nucleotides):
            print(path)
            break
        for neighbor in graph[node]:
            queue.append((neighbor, path))


