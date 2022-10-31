from Tents import *
import math
import Util
# Visitor pattern is used for implementing these classes
# let_me_solve reprensents visit method

class SearchAlgo:
    # this method return solution's path
    def __init__(self):
        self.visited = []
            
    def solve(self, tents):
        pass
    def let_me_solve(self, tents):
        return tents.accept(self)

class TrackNode:
    def tents_at(self,row_idx, col_idx):
            self.state[row_idx][col_idx] = Tents.TENT
        
    def nothing_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = Tents.NOTHING

    def expand_node(self):

            #find first UNSET cell
            size = len(self.state) if self.state else 0
            for row_idx in range(size):
                for col_idx in range(size):
                    if self.state[row_idx][col_idx] == Tents.UNSET:

                        res = []
                        # type(self) = constructor of subtype
                        first_child = type(self)(self.state, self.trees)
                        first_child.tents_at(row_idx, col_idx)  
                        res += [first_child]
                    
                        second_child = type(self)(self.state, self.trees)
                        second_child.nothing_at(row_idx, col_idx)
                        
                        res += [second_child]

                        return res
            
            return []



class AStarSearch(SearchAlgo):
    
    class Node(TrackNode):

        def __init__(self, state, trees):
            
            self.state = Util.deep_copy(state)
            self.trees = trees
            self.size = len(self.state)
            self.g_value = self.cal_g_value() # number of used tents
            self.h_value = self.cal_h_value() # number of tents need to be placed
            self.totcal_cost = self.g_value + self.h_value


        def get_total_cost(self):
            return self.g_value + self.h_value

        def cal_g_value(self):
            count = 0
            
            for row in self.state:
                for number in row:
                    if number == Tents.TENT:
                        count += 1
            
            return count
        
        def cal_h_value(self):
            
            """One tent can not be used for two tree
                so we need to track corresponding tree of tent
            """
            tents_map = []

            for i in range(self.size):
                tents_map += [[0] * self.size]

            count = 0
        
            for tree in self.trees:
                row_idx = tree[0]
                col_idx = tree[1]
                count += 1
                if row_idx > 0 and self.state[row_idx - 1][col_idx] == Tents.TENT and tents_map[row_idx - 1][col_idx] != 1:
                    tents_map[row_idx - 1][col_idx] = 1
                elif row_idx < self.size - 1 and self.state[row_idx + 1][col_idx] == Tents.TENT and tents_map[row_idx + 1][col_idx] != 1:
                    tents_map[row_idx + 1][col_idx] = 1
                elif col_idx > 0 and self.state[row_idx][col_idx - 1] == Tents.TENT and tents_map[row_idx][col_idx - 1] != 1:
                    tents_map[row_idx][col_idx - 1] = 1
                elif col_idx < self.size - 1 and self.state[row_idx][col_idx + 1] == Tents.TENT and tents_map[row_idx][col_idx + 1] != 1:
                    tents_map[row_idx][col_idx + 1] = 1
                else:
                    count -= 1
            
            return len(self.trees) - count


    
          
    def compare(self, node_a, node_b):
        return node_a.totcal_cost < node_b.totcal_cost
        # return node_a.totcal_cost <= node_b.totcal_cost

    def solve(self, tents):
        
        # use compare function to sort queue
        open_queue = Util.PriorityQueue(self.compare)
        
        # track visited nodes
        closed = []
        solution = []
        state = tents.state
        trees = tents.trees

        frontier = AStarSearch.Node(state, trees)

        open_queue.push(frontier)
        count = 0
        while open_queue.empty() == False:
            
            frontier = open_queue.pop()
            state = frontier.state

            # add this node to visited list
            closed += [str(state)]
            
            if tents.is_goal_state(state):
               solution = state
               break
            
            nodes = frontier.expand_node()
            
            for node in nodes:
                # str_state = str(node.state)
                if tents.is_legal_state(node.state) and closed.count(node.state) == 0:
                    open_queue.push(node)
                    # closed += [str_state]
                # because we are using priority queue built by Heap,
                # so we don't need to carry about whether this node is in open_queue
                    
                
    
        return solution




class BreadthFirstSearch(SearchAlgo):

    class Node(TrackNode):

        def __init__(self, state, trees):
            self.state = Util.deep_copy(state)
            self.trees = trees

     
    
    def solve(self, tents):
        
        queue = Util.Queue()
        state = tents.state
        size = tents.size
        frontier = BreadthFirstSearch.Node(tents.state, tents.trees)
        solution = []
        queue.push(frontier)

        while queue.empty() == False:
            
            frontier = queue.pop()
            state = frontier.state
            
            if tents.is_goal_state(state):
                solution = state
                break
            
            nodes = frontier.expand_node()

            for node in nodes:
                if tents.is_legal_state(node.state):
                    queue.push(node)
            
        
        return solution
                           
