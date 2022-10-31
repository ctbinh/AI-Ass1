from SearchAlgo import *


class TrackNode:

    def __init__(self, state, row_const, col_const, parent, tree_index):
        self.state = Util.deep_copy(state)
        self.row_const = row_const + []
        self.col_const = col_const + []
        self.parent = parent
        self.tree_index = tree_index + 0
        self.count = 0

    def tents_at(self,row_idx, col_idx):
        self.state[row_idx][col_idx] = Tents.TENT
        self.row_const[row_idx] -= 1
        self.col_const[col_idx] -= 1
        self.count += self.check(row_idx, col_idx)
    
    def check(self, row_idx, col_idx):
        if row_idx > 0 and self.state[row_idx - 1][col_idx] == Tents.TREE:
            return 1
        if row_idx < len(self.state) - 1 and self.state[row_idx + 1][col_idx] == Tents.TREE:
            return 1
        if col_idx > 0 and self.state[row_idx][col_idx - 1] == Tents.TREE:
            return 1
        if col_idx < len(self.state) - 1 and self.state[row_idx][col_idx + 1] == Tents.TREE:
            return 1

        return 0


class HeuristicSearch(SearchAlgo):

    def solve(self, tents):

        state = tents.state
        row_const = tents.row_const
        col_const = tents.col_const
        size = tents.size
        trees = tents.generate_list_tree()

        queue = Util.Queue()

        front_node = TrackNode(state, row_const, col_const, None, 0)

        queue.push(front_node)

        while queue.empty() == False:
            
            tree = queue.pop()
            tree_index = tree.tree_index
            
            state = tree.state
            if tree_index >= len(trees):
                return state
            row_idx = trees[tree_index][0]
            col_idx = trees[tree_index][1]
            row_const = tree.row_const
            col_const = tree.col_const
            
            

            if Tents.can_have_tents_at(state, row_const, col_const, row_idx - 1, col_idx, size):
                new_tent = TrackNode(state, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx - 1, col_idx)
                queue.push(new_tent)
                
            if Tents.can_have_tents_at(state, row_const, col_const, row_idx + 1, col_idx, size):
                
                new_tent = TrackNode(state, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx + 1, col_idx)
                queue.push(new_tent)
                
            if Tents.can_have_tents_at(state, row_const, col_const, row_idx, col_idx - 1, size):
               
                new_tent = TrackNode(state, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx, col_idx - 1)
                queue.push(new_tent)
                

            if Tents.can_have_tents_at(state, row_const, col_const, row_idx, col_idx + 1, size):
                
                new_tent = TrackNode(state, row_const, col_const, tree, tree_index + 1)
                new_tent.tents_at(row_idx, col_idx + 1)
                queue.push(new_tent)
                
        return []
    

    