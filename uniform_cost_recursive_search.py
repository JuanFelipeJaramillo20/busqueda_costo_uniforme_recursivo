def uniform_cost_recursive_search(start_node, goal):
    nodes = []
    path = []
    current_grandparent_value = start_node.value

    if start_node is None:
        return "Invalid input. Try again"
    
    path.append(start_node.id)
    
    if start_node.value == goal:
        print("Goal found!")
        return path
    
    nodes.append(start_node.children)

    next_node = nodes[0]

    for node in nodes:
        if node.value < next_node.value:
            next_node = node

    if next_node.value == goal:
        print("Goal found!")
        path.append(next_node.id)
        return path
    
    nodes.remove(next_node)
    nodes.append(next_node.children)