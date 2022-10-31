
from Solver import *
from Util import *


class DepthFirstSearch(Solver):
    
    def solve(self, binaro):
        
        stack = Stack()
        solution = None

        start = Node(binaro.grid, None, [])

        stack.push(start)

        while stack.empty() == False:
            
            top = stack.pop()
            state = top.state
            path = top.path
            
            if binaro.is_goal_state(state):
                solution = top
                break

            nodes = top.expand_node()

            for node in nodes:
                if binaro.is_legal_state(node.state):
                    stack.push(node)    

        return solution

    