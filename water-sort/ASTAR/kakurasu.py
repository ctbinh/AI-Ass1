class Kakurasu:
    UNSET = 0
    DOT = 1
    NOTHING = 2

    def __init__(self, state, row_const, col_const, size):
        self.state = state
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
            
    def accept(self, solver):
        return solver.solve(self)

    def is_goal_state(self, state):
        # Check row
        for row_idx in range(self.size):
            ans = 0
            for col_idx in range(self.size):
                if state[row_idx][col_idx] == Kakurasu.DOT:
                    ans = ans + (col_idx + 1) * state[row_idx][col_idx]
            if ans != self.row_const[row_idx]:
                return False
        # Check col
        for col_idx in range(self.size):
            ans = 0
            for row_idx in range(self.size):
                if state[row_idx][col_idx] == Kakurasu.DOT:
                    ans = ans + (row_idx + 1) * state[row_idx][col_idx]
            if ans != self.col_const[col_idx]:
                return False
        return True
    
    def can_have_dot_at(self, state, row_idx, col_idx):
        if row_idx < 0 or row_idx >= self.size or col_idx < 0 or col_idx >= self.size:
            return False
        count_row_dots_val = 0
        count_col_dots_val = 0
        for i in range(self.size):
            if state[row_idx][i] == Kakurasu.DOT:
                count_row_dots_val += (i + 1)
            if state[i][col_idx] == Kakurasu.DOT:
                count_col_dots_val += (i + 1)
        if count_col_dots_val > self.col_const[col_idx] or count_row_dots_val > self.row_const[row_idx]:
            return False
        return True
    
    
    
    def is_legal_state(self, state):
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                if state[row_idx][col_idx] == Kakurasu.DOT:
                    if self.can_have_dot_at(state, row_idx, col_idx) == False:
                        return False
        return True