# create a list of five colors
colors = ["red", "yellow", "green", "blue", "black"]

# convert them into tuple and print it
colors_tuple = tuple(colors)
print("Tuple:", colors_tuple)

# convert it back to list and add "white"
colors_list = list(colors_tuple)
colors_list.append("white")

# convert it back to tuple and print
final_tuple = tuple(colors_list)
print("Final Tuple:", final_tuple)