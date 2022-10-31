
from Solver import *
from Util import *


class BreadthFirstSearch(Solver):
    
    def solve(self, kakurasu):
        
        queue = Queue()
        solution = None

        start = Node(kakurasu.grid, kakurasu.row_const, kakurasu.col_const, [])
        
        queue.push(start)

        while queue.empty() == False:
            
            front = queue.pop()
            # state = front.state
            # # path = front.path
 
            
            if front.is_goal_state():
                solution = front
                break

            nodes = front.expand_node()

            for node in nodes:
                queue.push(node)    

        return solution

    