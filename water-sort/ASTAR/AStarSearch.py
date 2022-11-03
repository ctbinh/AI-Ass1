from Util import *
from Node import *

class AStarSearch:

    def compare(self, node_a, node_b):
        return node_a.total_cost <= node_b.total_cost

    def solve(self, watersort):
        
        open_queue = PriorityQueue(self.compare)
        closed = []
        solution = None
        start = Node(watersort.state, watersort.n_tube, watersort.n_tube_empty, watersort.tube_size, -1, [], [])
        visited = []

        open_queue.push(start)
        count = 0
        while open_queue.empty() == False:
            
            top = open_queue.pop()
            watersort.steps += [top]
            closed += [top.generate_steps()]
            count += 1
            if top.is_goal_state():
                solution = top
                break

            nodes = top.expand_node()
            
            for node in nodes:
                if visited.count(node.generate_steps()) == 0:
                    open_queue.push(node)
        return solution