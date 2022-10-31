
from Solver import *
from Util import *


class DepthFirstSearch(Solver):
    
    def solve(self, kakurasu):
        
        stack = Stack()
        solution = None

        start = Node(kakurasu.grid, kakurasu.row_const, kakurasu.col_const, [])
        visited = []

        stack.push(start)
        count = 0
        while stack.empty() == False:
            
            top = stack.pop()
            state = top.state
            path = top.path
            
            count += 1
            visited += [str(state)]
            if top.is_goal_state():
                solution = top
                break

            nodes = top.expand_node()

            for node in nodes:
                if visited.count(str(node.state)) == 0:
                    stack.push(node)    
        
        return solution

    