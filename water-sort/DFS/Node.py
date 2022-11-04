from Util import *

class Node:
    def __init__(self, state, n_tube, n_tube_empty, tube_size, path):
        self.state = deep_copy(state)
        self.n_tube = n_tube
        self.n_tube_empty = n_tube_empty
        self.tube_size = tube_size
        self.path = path
        if len(self.path) > 0:
            idx_tube_A = self.path[len(self.path) - 1][0]
            idx_tube_B = self.path[len(self.path) - 1][1]
            picked_color = self.state[idx_tube_A].top()
            for i in range(self.tube_size - self.state[idx_tube_B].length):
                if(not self.state[idx_tube_A].empty() and self.state[idx_tube_A].top() == picked_color):
                    self.state[idx_tube_B].push(self.state[idx_tube_A].pop())

            
    def expand_at(self, idx_tube_A, idx_tube_B):
        node = Node(self.state, self.n_tube, self.n_tube_empty, self.tube_size, [[idx_tube_A, idx_tube_B]])
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