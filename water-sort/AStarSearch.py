


from Solver import *
from Util import *


class AStarSearch(Solver):
    
    class CustomNode(Node):

        def __init__(self, state, row_const, col_const, path):
            super().__init__(state, row_const, col_const, path)
            self.g_value = self.calc_cost_root_to_current()
            self.h_value = self.calc_cost_current_to_goal()
            self.total_cost = self.g_value + self.h_value
        def calc_cost_root_to_current(self):
            
            return len(self.path)
        def calc_cost_current_to_goal(self):
            h_value = 0

            for i in range(self.size):
                h_value += self.row_const[i]
                h_value += self.col_const[i]

            return h_value

        def is_goal_state(self):
            return self.h_value == 0

    def compare(self, node_a, node_b):
        return node_a.total_cost <= node_b.total_cost
        # return node_a.totcal_cost <= node_b.totcal_cost


    def solve(self, kakurasu):
        
        open_queue = PriorityQueue(self.compare)
        solution = None

        start = AStarSearch.CustomNode(kakurasu.grid, kakurasu.row_const, kakurasu.col_const, [])
        visited = []

        open_queue.push(start)
        
        while open_queue.empty() == False:
            
            front = open_queue.pop()
            state = front.state
            # path = front.path
            visited += [str(state)]

            if front.is_goal_state():
                solution = front
                break

            nodes = front.expand_node()

            for node in nodes:
                if visited.count(str(node.state)) == 0:
                    open_queue.push(node)    
        
        return solution

    