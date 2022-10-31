def deep_copy(l):
    new_list = []

    for row in l:
        new_list += [[number for number in row]]
    
    return new_list


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