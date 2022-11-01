from kakurasu import *
import math
import Util

class SearchAlgorithm:
    def solve(self, kakurasu):
        pass

class TrackNode:
    def dots_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = Kakurasu.DOT

    def nothing_at(self, row_idx, col_idx):
        self.state[row_idx][col_idx] = Kakurasu.NOTHING

    def expandnode(self):
        size = len(self.state) if self.state else 0
        for row_idx in range(size):
            for col_idx in range(size):
                if self.state[row_idx][col_idx] == Kakurasu.UNSET:
                    res = []
                    first_child = type(self)(self.state, self.row_const, self.col_const) #not enough
                    first_child.dots_at(row_idx, col_idx)
                    res += [first_child]

                    second_child = type(self)(self.state, self.row_const, self.col_const)
                    second_child.nothing_at(row_idx, col_idx)
                    
                    res += [second_child]

                    return res
        return []

    def expand_node(self):
        nodes = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_valid_cell(row, col):
                    nodes += [self.expand_at(row, col)]

        return nodes

class AStarSearch(SearchAlgorithm):
    class Node(TrackNode):
        def __init__(self,state,row_const,col_const):
            self.state = Util.deep_copy(state)
            self.size = len(row_const)
            self.row_const = [number for number in row_const]
            self.col_const = [number for number in col_const]
            self.g_value = self.cal_g_value()
            self.h_value = self.cal_h_value()
            print(self.g_value, self.h_value)
            self.total_cost = self.get_total_cost()

        
        def get_total_cost(self):
            return self.g_value + self.h_value

        def cal_g_value(self):
            countTotal = 0
            count = 0
            print(self.state)
            for row in self.state:
                count += 1
                count2 = 0
                for number in row:
                    count2 += 1
                    if number == Kakurasu.DOT:
                        countTotal += (count + count2)

            return countTotal
        
        def cal_h_value(self):
            dots_map = []
            for i in range(self.size):
                dots_map += [[0] * self.size]
            colSum = 0
            rowSum = 0
            for x in self.row_const:
                rowSum += x
            for x in self.col_const:
                colSum += x
            countTotal = rowSum + colSum
            countHave = 0
            for row_idx in range(self.size):
                for col_idx in range(self.size):
                    if self.state[row_idx][col_idx] == Kakurasu.DOT:
                        dots_map[row_idx][col_idx] = 1
                        countHave += (row_idx + col_idx + 2)
            return countTotal - countHave

    def compare(self, node_a, node_b):
        return node_a.total_cost <= node_b.total_cost

    def solve(self, kakurasu):
        open_queue = Util.PriorityQueue(self.compare)
        closed = []
        state = kakurasu.state
        rconst = kakurasu.row_const
        cconst = kakurasu.col_const

        front = AStarSearch.Node(state, rconst, cconst)

        open_queue.push(front)

        while open_queue.empty() == False:
            front = open_queue.pop()
            state = front.state
            closed += [str(state)]
            if kakurasu.is_goal_state(state):

                return state
            
            nodes = front.expandnode()

            for node in nodes:
                state1 = str(node.state)
                if kakurasu.is_legal_state(node.state) and closed.count(state1) == 0:
                    open_queue.push(node)

        return state