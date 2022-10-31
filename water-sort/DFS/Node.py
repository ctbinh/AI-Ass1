from Util import *

class Node:
    def __init__(self, state, row_const, col_const, path):
        self.state = deep_copy(state)
        self.row_const = [number for number in row_const]
        self.col_const = [number for number in col_const]
        self.path = path
        self.size = len(self.row_const)
        if len(self.path) > 0:
            row = self.path[len(self.path) - 1][0]
            col = self.path[len(self.path) - 1][1]
            self.row_const[row] -= (col + 1)
            self.col_const[col] -= (row + 1)
            self.state[row][col] = 1
            
    def expand_at(self, row, col):
        node = (type(self)) (self.state, self.row_const, self.col_const, self.path + [[row, col]])
        
        return node

    def is_valid_cell(self, row, col):
        if self.state[row][col] == 1 or self.row_const[row] < (col + 1) or self.col_const[col] < (row + 1):
                return False
        return True

    def is_goal_state(self):
        for i in range(0, self.size):
            if self.row_const[i] != 0 or self.col_const[i] != 0:
                return False
        return True

    def expand_node(self):
        nodes = []
        for row in range(self.size):
            for col in range(self.size):
                if self.is_valid_cell(row, col):
                    nodes += [self.expand_at(row, col)]
        return nodes

    def generate_steps(self):
        state = create_matrix(0, self.size)
        res = []
        res += [str_matrix(state, "\n")]
        for pos in self.path:
            state[pos[0]][pos[1]] = 1
            res += [str_matrix(state, "\n")]
        return res