from Util import *
from Node import *

class DepthFirstSearch:

    def solve(self, watersort):
        
        stack = Stack()
        solution = None
        start = Node(watersort.state, watersort.n_tube, watersort.n_tube_empty, watersort.tube_size, [])
        visited = []

        stack.push(start)
        count = 0
        while stack.empty() == False:
            
            top = stack.pop()
            watersort.steps += [top]
            visited += [top.generate_steps()]
            count += 1
            if top.is_goal_state():
                solution = top
                break

            nodes = top.expand_node()
            
            for node in nodes:
                if visited.count(node.generate_steps()) == 0:
                    stack.push(node)
        return solution