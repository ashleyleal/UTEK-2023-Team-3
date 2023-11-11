class Graph:
# make a class to store the input 

  def __init__(self):
    self.graph = {}

  def add_edge(self, start, end, cost, time):
    # keep in track of the four input and make them into dictionary
    if start not in self.graph:
      self.graph[start] = {}
    self.graph[start][end] = (cost, time)

# make the input into tuple with shape  [('a', 'b', 2, 4), ('b', 'c', 4, 6),......]
def parse_input(input_str, nodes, end):
  relationships = []

  # Split the input string based on ', ' to separate individual relationships
  relationship_strings = input_str.split('), ')
  # print(relationship_strings)

  for relationship_str in relationship_strings:
    # Split each relationship string based on '->' to extract source and rest
    source, rest = relationship_str.split('->')
    # print(source)
    # print(rest)

    # Further split the rest based on ' ($' to extract target and value_str
    target, value_str = rest.split(' ($', 1)
    # print(target)
    # print(value_str)
    value, time_str = value_str.split(', ', 1)
    # print(value)
    # print(time_str)
    time, blank = time_str.split(' min cooldown', 1)
    # Extract the numerical value and remove the closing parenthesis
    # print(time,'adsfa')
    value = int(value)
    time = int(time)
    # print(source, target, value, time)
    # return [('a', 'b', 2, 4), ('b', 'c', 4, 6)]

    # Check if there is a second part (cooldown)

    # Append the tuple to the relationships list
    relationships.append((source, target, value, time))

    for sou, tar, val, mins in relationships:
      if sou not in nodes and sou not in end:
        nodes.append(sou)
      if tar not in nodes and tar not in end:
        nodes.append(tar)

  return relationships, nodes
  # example input: "a->b ($4, 1 min cooldown), b->c ($5, 1 min cooldown), c->d ($3, 3 min cooldown), b->d ($7, 3 min cooldown), a->c ($4, 3 min cooldown), d->a ($1, 4 min cooldown)"


def find_min_cost_path(graph, nodes, max_time):
  # recursion to find the minimum path
  num_nodes = len(nodes) - 1
  min_cost = float('inf')  #initial set up cost
  min_path = None  #initial set up path
  timer = 0
  total_time = 0

  def search_paths(arr, start, end):
    nonlocal min_cost, min_path, timer, total_time

    if start == end:
      cost = 0
      for i in range(len(arr) - 1):
        start, end = arr[i], arr[i + 1]
        if end in graph.get(start, {}):
          cost += graph[start][end][0] 
          timer += graph[start][end][1]

        else:
          cost = float('inf')
          timer = float('inf')
          break

        if timer > max_time:
          cost = float('inf')
          timer = float('inf')
          break

      if (cost < min_cost
          ) and arr[0] == nodes[0] and arr[num_nodes] == nodes[num_nodes]:
            #update the minimum cost and time
        min_cost = cost
        min_path = arr
        total_time = timer
    else:
      for i in range(start, end + 1):
        arr[start], arr[i] = arr[i], arr[start]
        search_paths(arr, start + 1, end)
        arr[start], arr[i] = arr[i], arr[start]  # Backtrack here

  # Rest of the code remains unchanged

  search_paths(nodes, 0, len(nodes) - 1)

  return min_path, min_cost, total_time


# Usage of class:
my_graph = Graph()

# input
start_inter = input("Starting intersection: ")
end_inter = input("Ending intersection: ")
maxTime = int(input("maxTime = "))
# Take user input
input_string = input("Enter the relationships separated by commas: ")

# Get the result
nodes = []

nodes.insert(0, start_inter)
output, nodes = parse_input(input_string, nodes, end_inter)
nodes.append(end_inter)
#return [('a', 'b', 2), ('b', 'c', 4)]

for i, j, k, f in output:
  my_graph.add_edge(i, j, k, f)

min_path, min_path_cost, total_time = find_min_cost_path(
    my_graph.graph, nodes, maxTime)

#print out the final result
if min_path_cost == float('inf'):  # when no valid path due to time
  print("Best path:[]")
  print("Cost: -1")
  print("Time: -1")
else:
  print("bestPath:", end=' ')
  for i, path in enumerate(min_path):
    if (i == len(min_path) - 1):
      print(path)
    else:
      print(path, end="->")
  print(f"totalCost: ${min_path_cost}")
  print(f"totalTime: {total_time}min")

