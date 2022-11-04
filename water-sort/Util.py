def create_matrix(value, size):
    res = []
    for i in range(size):
        res += [[value] * size]
    return res

def create_list_stack(n_tube, n_tube_empty, tube_full):
    res = []
    res += tube_full
    for i in range(n_tube_empty):
        res += [Stack()]
    return res


def deep_copy(l):
    new_list = []
    for tube in l:
        new_tube = Stack()
        for i in range(tube.length):
            new_tube.push(tube.items[i])
        new_list += [new_tube]
    return new_list


def str_matrix(l, sep):
    res = ""
    for row in l:
        
        res += str(row) + sep  
    return res

def print_steps(l):
    size = len(l)
    res = ""
    for i in range(size):
        res += "Step " + str(i) + ":\n" + l[i] + "\n"
    return res

def print_steps(l):
    size = len(l)
    res = ""
    for i in range(size):
        res += "Step " + str(i) + ":\n" + l[i] + "\n"
    return res

class CustomList:
    def __init__(self):
        self.items = []
        self.length = 0
    
    def length(self):
        return self.length

    def empty(self):
        return self.length == 0
    
class Stack(CustomList):
    def top(self):
        return self.items[-1]
    
    def push(self, item):
        self.items += [item]
        self.length += 1
        
    def pop(self):
        top = self.top()
        self.items = self.items[ :-1]
        self.length -= 1
        return top
    
    def __str__(self) -> str:
        stack = 'Tube| '
        for i in range(len(self.items)):
            stack += str(self.items[i]) + ' '
        return stack

    def colorTowers(self):
        if self.empty():
            return 0
        towers = 1
        for i in range(self.length):
            if(self.items[i] != self.items[i-1]):
                towers += 1
        return towers
    


class Queue(CustomList):
    def front(self):
        return self.items[0]
    
    def empty(self):
        return self.length == 0
    
    def push(self, item):
        self.items += [item]
        self.length += 1
        
    def pop(self):
        front = self.front()
        self.items = self.items[1:]
        self.length -= 1
        return front

class PriorityQueue(CustomList):
    def __init__(self, comparator):
        super().__init__()  
        self.comparator = comparator
        
    def push(self, item):
        self.items += [item]
        self.length += 1
        self.rearrange_bottom_up(self.length - 1)

    def front(self):
        return self.items[0]

    def rearrange_bottom_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index == index or parent_index < 0:
            return
        if self.comparator(self.items[parent_index], self.items[index]) == False:
            temp = self.items[index]
            self.items[index] = self.items[parent_index]
            self.items[parent_index] = temp
            self.rearrange_bottom_up(parent_index)

    def pop(self):
        front = self.items[0]
        self.items[0] = self.items[self.length - 1]
        self.items = self.items[0 : self.length - 1]
        self.length -= 1
        self.rearrange_top_down(0)
        return front

    def rearrange_top_down(self, index):
        index_where = index
        # last item
        if index >= self.length - 1:
            return
        left = index * 2 + 1
        right = index * 2 + 2
        if left < self.length:
            if self.comparator(self.items[index_where], self.items[left]) == False:
                index_where = left
        if right < self.length:
            if self.comparator(self.items[index_where], self.items[right]) == False:
                index_where = right
        if index_where != index:
            temp = self.items[index]
            self.items[index] = self.items[index_where]
            self.items[index_where] = temp
            self.rearrange_top_down(index_where)