class Tents:
    UNSET = 0
    TREE = 1
    TENT = 2
    NOTHING = 3
    
    def get_icon(self, value):
        
        if value == Tents.TENT:
            # return "⛺"
            return "TENT"
        if value == Tents.TREE:
            # return "🌳"
            return "TREE"
        if value == Tents.NOTHING:
            return "NOT"

        return ""

    def get_all_icon(self, state):
        res = []
        for row in state:
            cur = []
            for number in row:
                cur += [self.get_icon(number)]
            
            res += [cur]
        
        return res
        
    def __init__(self, state, row_const, col_const, size):
        self.state = state
        self.row_const = row_const
        self.col_const = col_const
        self.size = size
        self.trees = self.generate_list_tree()
        self.title = "Tents puzzle"

    def accept(self, solver):
        return solver.solve(self)
    
    def generate_list_tree(self):
        self.trees = []
        
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                number = self.state[row_idx][col_idx]
                if number == Tents.TREE:
                    self.trees += [[row_idx, col_idx]]
        
        return self.trees

    def can_have_tent_at(self, state, row_idx, col_idx):
        
        
        if row_idx < 0 or row_idx >= self.size or col_idx < 0 or col_idx >= self.size:
            return False

        count_row_tents = 0
        count_col_tents = 0
        for i in range(self.size):
            if state[row_idx][i] == Tents.TENT:
                count_row_tents += 1
            if state[i][col_idx] == Tents.TENT:
                count_col_tents += 1

        if count_col_tents > self.col_const[col_idx] or count_row_tents > self.row_const[row_idx]:
            return False

        # check tent in horizontal, vertical direction
        if row_idx > 0 and state[row_idx - 1][col_idx] == Tents.TENT:
            return False
        if col_idx > 0 and state[row_idx][col_idx - 1] == Tents.TENT:
            return False
        if row_idx < self.size - 1 and state[row_idx + 1][col_idx] == Tents.TENT:
            return False
        if col_idx < self.size - 1 and state[row_idx][col_idx + 1] == Tents.TENT:
            return False

        # check diagonally
        if row_idx > 0 and col_idx > 0 and state[row_idx - 1][col_idx - 1] == Tents.TENT:
            return False
        if row_idx > 0 and col_idx < self.size - 1 and state[row_idx - 1][col_idx + 1] == Tents.TENT:
            return False
        
        if row_idx < self.size - 1 and col_idx > 0 and state[row_idx + 1][col_idx - 1] == Tents.TENT:
            return False

        
        if row_idx > 0 and row_idx < self.size - 1 and col_idx < self.size - 1 and state[row_idx + 1][col_idx + 1] == Tents.TENT:
            return False

        return True

    def is_legal_state(self, state):

        
        for row_idx in range(self.size):
            for col_idx in range(self.size):
                if state[row_idx][col_idx] == Tents.TENT:
                    if self.can_have_tent_at(state, row_idx, col_idx) == False:
                        return False
        
        return True

    def have_tents_beside(self, state, row_idx, col_idx):
        if row_idx > 0 and state[row_idx - 1][col_idx] == Tents.TENT:
            return True
        if row_idx < self.size - 1 and state[row_idx + 1][col_idx] == Tents.TENT:
            return True
        if col_idx > 0 and state[row_idx][col_idx - 1] == Tents.TENT:
            return True
        if col_idx < self.size - 1 and state[row_idx][col_idx + 1] == Tents.TENT:
            return True

        return False

    def is_goal_state(self, state):
        
        tents_map = []

        for i in range(self.size):
            tents_map += [[0] * self.size]
        flag = True
       
        for tree in self.trees:
            row_idx = tree[0]
            col_idx = tree[1]
            if row_idx > 0 and state[row_idx - 1][col_idx] == Tents.TENT and tents_map[row_idx - 1][col_idx] != 1:
                tents_map[row_idx - 1][col_idx] = 1
            elif row_idx < self.size - 1 and state[row_idx + 1][col_idx] == Tents.TENT and tents_map[row_idx + 1][col_idx] != 1:
                tents_map[row_idx + 1][col_idx] = 1
            elif col_idx > 0 and state[row_idx][col_idx - 1] == Tents.TENT and tents_map[row_idx][col_idx - 1] != 1:
                tents_map[row_idx][col_idx - 1] = 1
            elif col_idx < self.size - 1 and state[row_idx][col_idx + 1] == Tents.TENT and tents_map[row_idx][col_idx + 1] != 1:
                tents_map[row_idx][col_idx + 1] = 1
            else:
                flag = False
           
       
        
        return flag
 
    @staticmethod
    def can_have_tents_at(state, row_const, col_const ,row_idx, col_idx, size):
        
        
        if row_idx < 0 or row_idx >= size or col_idx < 0 or col_idx >= size:
            return False

        if state[row_idx][col_idx] != Tents.UNSET:
            return False
        

        # check constraint
        if row_const[row_idx] <= 0 or col_const[col_idx] <= 0:
            return False

        # check tent in horizontal, vertical direction
        if row_idx > 0 and state[row_idx - 1][col_idx] == Tents.TENT:
            return False
        if col_idx > 0 and state[row_idx][col_idx - 1] == Tents.TENT:
            return False
        if row_idx < size - 1 and state[row_idx + 1][col_idx] == Tents.TENT:
            return False
        if col_idx < size - 1 and state[row_idx][col_idx + 1] == Tents.TENT:
            return False

        # check diagonally
        if row_idx > 0 and col_idx > 0 and state[row_idx - 1][col_idx - 1] == Tents.TENT:
            return False
        if row_idx > 0 and col_idx < size - 1 and state[row_idx - 1][col_idx + 1] == Tents.TENT:
            return False
        
        if row_idx < size - 1 and col_idx > 0 and state[row_idx + 1][col_idx - 1] == Tents.TENT:
            return False

        
        if row_idx > 0 and row_idx < size - 1 and col_idx < size - 1 and state[row_idx + 1][col_idx + 1] == Tents.TENT:
            return False

        return True
    
   
