class Graph:

  def __init__(self):
    self.graph = {}

  def add_edge(self, start, end, cost):
    if start not in self.graph:
      self.graph[start] = {}
    self.graph[start][end] = cost


def parse_input(input, nodes, end):
  # Split the input string based on '->' and ',' to extract individual strings
  relationships = []
  # Split the input string based on ', ' to separate individual relationships
  relationship_strings = input.split(', ')
  #print(relationship_strings)

  for relationship_str in relationship_strings:
    # Split each relationship string based on '->' to extract source and rest
    source, rest = relationship_str.split('->')

    # Further split the rest based on '($' to extract target and value_str
    target, value_str = rest.split(' ($', 1)

    # Extract the numerical value and remove the closing parenthesis
    #print(target, value_str)
    value = int(value_str.rstrip(')'))
    #print(value)

    # Append the tuple to the relationships list
    relationships.append((source, target, value))

    for sou, tar, val in relationships:
      if sou not in nodes and sou not in end:
        nodes.append(sou)
      if tar not in nodes and tar not in end:
        nodes.append(tar)

  return relationships, nodes


def find_min_cost_path(graph, nodes):
  cha = nodes[0]
  lengthads = len(nodes)-1
  endcha = nodes[lengthads]
  min_cost = float('inf')  #initial set up cost
  min_path = None  #initial set up path

  def search_paths(arr, start, end):
      nonlocal min_cost, min_path

      if start == end:
          cost = 0
          for i in range(len(arr) - 1):
              start, end = arr[i], arr[i + 1]
              if end in graph.get(start, {}):
                  cost += graph[start][end]
              else:
                  cost = float('inf')
                  break

          if (cost < min_cost) and arr[0]==cha and arr[lengthads]==endcha:
              min_cost = cost
              min_path = arr
              #print(min_cost, min_path)

      else:
          for i in range(start, end + 1):
              arr[start], arr[i] = arr[i], arr[start]
              search_paths(arr, start + 1, end)
              arr[start], arr[i] = arr[i], arr[start]  # Backtrack here

  # Rest of the code remains unchanged


  search_paths(nodes, 0, len(nodes) - 1)

  return min_path, min_cost


# Example usage:
my_graph = Graph()

#input
start_inter = input("Starting intersection: ")
end_inter = input("Ending intersection: ")
# Take user input
input_string = input("Enter the relationships separated by commas: ")

# Get the result
nodes = []

nodes.insert(0, start_inter)
output, nodes = parse_input(input_string, nodes, end_inter)
nodes.append(end_inter)
#return [('a', 'b', 2), ('b', 'c', 4)]

for i, j, k in output:
  my_graph.add_edge(i, j, k)

#print(my_graph.graph)

min_path, min_path_cost = find_min_cost_path(my_graph.graph, nodes)

if min_path_cost == float('inf'):
  print(f"No valid path found.")
else:
  print(f"The minimum cost path is: {min_path} with cost {min_path_cost}")
