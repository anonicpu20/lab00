import queue

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8, 9],
    5: [10, 11],
    6: [12, 13],
    7: [14, 15]
}

tree = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F', 'G'],
'D': ['H'],
'E': [],
'F': ['I'],
'G': [],
'H': [],
'I': []
}
def bfs(graph, start, goal):
    visited= []
    que = []

    visited.append(start)
    que.append(start)
    while que:
        node = que.pop(0)
        print(node, end=" ") 
        if node == goal:
            print ("goal found")
            break
        for neig in graph[node]:
            if neig not in visited:
                visited.append(neig)
                que.append(neig)
           
# bfs(tree, "A", "I")
# bfs (graph, 1, 7)





# dfs(graph, 1, 7)
# dfs (tree, "A", "I")



# start = goal = None
# for i in range(len(grid)):
#     for j in range(len(grid[0])):
#         if grid[i][j] == 'S':
#             start = (i, j)
#         elif grid[i][j] == 'K':
#             goal = (i, j)

# print(create_graph(grid), end = " ")
# newgraph = create_graph(grid)
# dfs(newgraph, start, goal)
# bfs(newgraph, start, goal)

def dfs(graph, start, goal):
    visited = []
    stack = []
    path = []
    visited.append(start)
    stack.append(start)
    while stack:
        node = stack.pop()
        path.append(node)
        print (node , end=" ")
        if node == goal:
            print ("goal found")
            return path
        for n in graph[node]:
            if n not in visited:
                visited.append(n)
                stack.append(n)
    return path

class GoalbasedAgent:
    def __init__(self, start, goal, graph):
        self.start = start
        self.goal = goal
        self.graph= graph
    def act(self):
        result = dfs(self.graph, self.start, self.goal)
        return result

class envir:
    def __init__(self, grid):
        self.grid = grid
        self.graph = create_graph(grid)
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = self.find_position('S')
        self.goal = self.find_position('K')

    def find_position(self, element):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == element:
                    return (i, j)
        return None

def create_graph(maze):
    graph = {}
    rows = len(maze)
    cols = len(maze[0])
    # print (rows, cols)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != '#' and maze[i][j] != 'F':
                neig = []
                for dx, dy in (directions):
                    nx, ny = i+dx, j+dy
                    if (0<=nx<rows and 0<=ny< cols and maze[nx][ny]!='#' and maze[i][j] != 'F'):
                        neig.append((nx, ny))
                graph[(i,j)]= neig
    return graph

grid = [
    ['S', '.', '#', '.', 'K'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.'],
    ['#', '.', '#', '.', '#'],
    ['.', '.', '.', '.', '.']
]


env = envir(grid)
agent = GoalbasedAgent(env.start, env.goal, env.graph)
result = agent.act()
print("Result:", result)