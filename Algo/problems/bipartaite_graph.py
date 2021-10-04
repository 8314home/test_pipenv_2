from collections import deque

# -1 - white
# 0 - red
# 1 - blue


def bipartaite_check_node(node, input_input_matrix, input_list_of_colours):

    bfs_queue = deque()
    bfs_queue.append(node)  # add 1st node to queue
    input_list_of_colours[node] = 0 # mark 1st node colour to red=0 to show it is visited

    while bfs_queue:
        print(f"-----------------------")

        # take out item from queue
        u = bfs_queue.popleft()
        print(f"poped item - {u}")

        # check FOR evry neighbour in of item
        #          if not visited
        #          change color to alternative of item
        #          push to queue
        #          check against color if the item with it's neighbour after above colouring
        for v in range(len(input_input_matrix[u])):
            # Below is signifying that node should not have a cyclic link to itself
            if input_input_matrix[u][u] == 1:
                return False
            # Below mean a connection from u to v present and v is still not visited/coloured
            if input_input_matrix[u][v] == 1 and input_list_of_colours[v] == -1:
                input_list_of_colours[v] = 1 - input_list_of_colours[u]
                bfs_queue.append(v)
            # If does not go into above if condition, for a case when node already have a colour but u to v conn present
            if input_input_matrix[u][v] == 1 and input_list_of_colours[u] == input_list_of_colours[v]:
                print(f"input_list_of_colours[{u}] - {input_list_of_colours[u] }")
                print(f"input_list_of_colours[{v}] - {input_list_of_colours[v] }")
                return False
        print(f"bfe_queue - {bfs_queue}")
        print(f"input_list_of_colours - {input_list_of_colours}")
    return True


if __name__ == "__main__":
    print("Bipartaite graph check")

    # Adjacency matrix

    G = [
        [0,1,1,0],
       [1,0,0,1],
       [1,0,0,1],
       [0,1,1,0]
       ]

    G2 = [
        [0,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,0]
    ]
    # Nodes

    V = [0,1,2,3]  # these are nodes which we can access using index values of G
    colour_matrix = [-1, -1, -1, -1]

    bipartaite_flag_1 = bipartaite_check_node(0, G, colour_matrix)
    print(f"bipartaite_flag_1 - {bipartaite_flag_1}")

    print("\n#################\n")
    colour_matrix = [-1, -1, -1, -1]

    bipartaite_flag_2 = bipartaite_check_node(0, G2, colour_matrix)
    print(f"bipartaite_flag_2 - {bipartaite_flag_2}")
