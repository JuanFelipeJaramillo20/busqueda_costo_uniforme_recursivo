class Node:
    def __init__(self, id, cost, value, best_son_value, parent, children) -> None:
        self.id = id
        self.cost = cost
        self.value = value
        self.best_son_value = best_son_value
        self.parent = parent
        self.children = children