class Node(object):

    def __init__(self, name):
        self.name = name
        self.adjacency_list = []
        self.visited = False
        self.prdecessor = None


class DFS(object):
    def dfs(self, current_node: Node):
        print(f"{current_node.name}")
        current_node.visited = True
        for n in current_node.adjacency_list:
            if not n.visited:
                self.dfs(n)



if __name__ == "__main__":

    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")
    node_g = Node("G")
    node_h = Node("H")

    node_a.adjacency_list=[node_b, node_d]
    node_b.adjacency_list=[node_e, node_f, node_c]
    node_f.adjacency_list=[node_g, node_h]
    node_c.adjacency_list=[node_h]

    print("DFS")

    dfs = DFS()
    dfs.dfs(node_a)
