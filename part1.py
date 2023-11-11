""" 
UTEK 2024
Part 1: Graph Construction
By Team 3: Ashley Leal, Danelle D'Souza, Zuha Mujib, Winnie Hsiang
"""

def print_and_count_unique_strings(input_string):
  # Split the input string based on '->' and ',' to extract individual strings
  strings = [s.strip() for s in input_string.split('->')]
  strings = [s.strip() for string in strings for s in string.split(',')]
  num = 1
  totallen = 0
  count = 0

  # Use a list to store unique strings
  unique_strings = list()

  # Iterate through the strings, print each unique string without newline, and add it to the list
  for string in strings:
      if(len(string)>num):
          num = len(string)
      if string not in unique_strings:
          count = count +1
          totallen = totallen + len(string)
          unique_strings.append(string)

  print(" " * (num + 1), end='|')
  for string in unique_strings:
    print(string, end='|')

  print()
  print('-'* (totallen + count + 1 + num + 1))

  # Return the count of unique strings
  return num, len(unique_strings), unique_strings

def parse_input(input_string):

  # Create a 2x2 matrix initialized with zeros
  number, result, nodeList = print_and_count_unique_strings(input_string)

  matrix = []
  for i in range(result):
      row = []
      for j in range(result):
          row.append(0)
      matrix.append(row)

  relationships = input_string.strip().split(', ')

  first_index = -1
  second_index = -2

  # Process each relationship
  for relationship in relationships:
    start, end = relationship.split('->') 

    for j, node in enumerate(nodeList):
        if(node==start):
          first_index = j
        if(node==end):
          second_index = j
    matrix[first_index][second_index] = 1
  for row in range(len(matrix)):
    print(nodeList[row], end='')
    print(' '*(number-(len(nodeList[row]))), end = ' |')
    for col in range(len(matrix[row])):
      length = len(nodeList[col])-1
      if(length<0):
        length = 0
      
      print(matrix[row][col],end='')
      print(' '*(length),end = '|' )
    print()

  return result


# Take user input
input_string = input("Enter the relationships separated by commas: ")

# Get the result
output = parse_input(input_string)
