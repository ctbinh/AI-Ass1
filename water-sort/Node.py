from Util import *

class Node_ASTAR:
    def __init__(self, state, n_tube, n_tube_empty, tube_size, g_value, path, prev_nodes):
        self.state = deep_copy(state)
        self.n_tube = n_tube
        self.n_tube_empty = n_tube_empty
        self.tube_size = tube_size
        self.path = path
        self.g_value = g_value + 1
        self.h_value = 0
        self.total_cost = 0
        self.prev_nodes = []
        if(len(prev_nodes)==0):
            self.prev_nodes += [self]
        if len(self.path) > 0:
            idx_tube_A = self.path[len(self.path) - 1][0]
            idx_tube_B = self.path[len(self.path) - 1][1]
            picked_color = self.state[idx_tube_A].top()
            for i in range(self.tube_size - self.state[idx_tube_B].length):
                if(not self.state[idx_tube_A].empty() and self.state[idx_tube_A].top() == picked_color):
                    self.state[idx_tube_B].push(self.state[idx_tube_A].pop())
            self.h_value = self.cal_h_value()
            self.total_cost = self.get_total_cost()
            self.prev_nodes = prev_nodes + [self]

    def get_total_cost(self):
        return self.g_value + self.h_value
    
    def cal_h_value(self):
        heuristic = 0
        bottomColorsCount = [0]*(self.n_tube+self.n_tube_empty)
        for tube in self.state:
            if(tube.empty()):
                continue
            heuristic += tube.colorTowers() - 1
            bottomColorsCount[tube.items[0]] += 1
        for bottomColorCount in bottomColorsCount:
            heuristic += bottomColorCount - 1
        return heuristic


    def expand_at(self, idx_tube_A, idx_tube_B):
        node = Node_ASTAR(self.state, self.n_tube, self.n_tube_empty, self.tube_size, self.g_value, [[idx_tube_A, idx_tube_B]], self.prev_nodes)
        return node

    def is_valid_cell(self, idx_tube_A, idx_tube_B):
        list_color_tube_A = self.state[idx_tube_A].items
        top_color_A = self.state[idx_tube_A].top() if (not self.state[idx_tube_A].empty()) else -1
        if(self.state[idx_tube_B].length == self.tube_size):
            return False
        elif(self.state[idx_tube_A].empty()):
            return False
        elif(not self.state[idx_tube_B].empty() and self.state[idx_tube_A].top() != self.state[idx_tube_B].top()):
            return False
        elif(list_color_tube_A.count(top_color_A) == len(list_color_tube_A) and self.state[idx_tube_B].empty()):
            return False
        return True

    def is_goal_state(self):
        for i in range(self.n_tube + self.n_tube_empty):
            if(self.state[i].empty()):
                continue
            top_color = self.state[i].top()
            list_color_tube = self.state[i].items
            if(list_color_tube.count(top_color) != self.tube_size):
                return False
        return True

    def expand_node(self):
        nodes = []
        for idx_tube_A in range(self.n_tube + self.n_tube_empty):
            for idx_tube_B in range(idx_tube_A + 1, self.n_tube + self.n_tube_empty):
                if self.is_valid_cell(idx_tube_A, idx_tube_B):
                    nodes += [self.expand_at(idx_tube_A, idx_tube_B)]
                if self.is_valid_cell(idx_tube_B, idx_tube_A):
                    nodes += [self.expand_at(idx_tube_B, idx_tube_A)]
        return nodes

    def generate_steps(self):
        step = ""
        for i in range(self.n_tube + self.n_tube_empty):
            step += (str(self.state[i]))
        return step

class Node_DFS:
    def __init__(self, state, n_tube, n_tube_empty, tube_size, path, prev_nodes):
        self.state = deep_copy(state)
        self.n_tube = n_tube
        self.n_tube_empty = n_tube_empty
        self.tube_size = tube_size
        self.path = path
        self.prev_nodes = []
        if(len(prev_nodes)==0):
            self.prev_nodes += [self]
        if len(self.path) > 0:
            idx_tube_A = self.path[len(self.path) - 1][0]
            idx_tube_B = self.path[len(self.path) - 1][1]
            picked_color = self.state[idx_tube_A].top()
            for i in range(self.tube_size - self.state[idx_tube_B].length):
                if(not self.state[idx_tube_A].empty() and self.state[idx_tube_A].top() == picked_color):
                    self.state[idx_tube_B].push(self.state[idx_tube_A].pop())
            self.prev_nodes = prev_nodes + [self]

            
    def expand_at(self, idx_tube_A, idx_tube_B):
        node = Node_DFS(self.state, self.n_tube, self.n_tube_empty, self.tube_size, [[idx_tube_A, idx_tube_B]], self.prev_nodes)
        return node

    def is_valid_cell(self, idx_tube_A, idx_tube_B):
        list_color_tube_A = self.state[idx_tube_A].items
        top_color_A = self.state[idx_tube_A].top() if (not self.state[idx_tube_A].empty()) else -1
        if(self.state[idx_tube_B].length == self.tube_size):
            return False
        elif(self.state[idx_tube_A].empty()):
            return False
        elif(not self.state[idx_tube_B].empty() and self.state[idx_tube_A].top() != self.state[idx_tube_B].top()):
            return False
        elif(list_color_tube_A.count(top_color_A) == len(list_color_tube_A) and self.state[idx_tube_B].empty()):
            return False
        return True

    def is_goal_state(self):
        for i in range(self.n_tube + self.n_tube_empty):
            if(self.state[i].empty()):
                continue
            top_color = self.state[i].top()
            list_color_tube = self.state[i].items
            if(list_color_tube.count(top_color) != self.tube_size):
                return False
        return True

    def expand_node(self):
        nodes = []
        for idx_tube_A in range(self.n_tube + self.n_tube_empty):
            for idx_tube_B in range(idx_tube_A + 1, self.n_tube + self.n_tube_empty):
                if self.is_valid_cell(idx_tube_A, idx_tube_B):
                    nodes += [self.expand_at(idx_tube_A, idx_tube_B)]
                if self.is_valid_cell(idx_tube_B, idx_tube_A):
                    nodes += [self.expand_at(idx_tube_B, idx_tube_A)]
        return nodes

    def generate_steps(self):
        step = ""
        for i in range(self.n_tube + self.n_tube_empty):
            step += (str(self.state[i]))
        return step