### Assignment of Artificial Intelligent course

### Tents
Breath First Search
state: state of all trees in forests represented by an 2D array
Do all trees have a corresponding tent
Legal moves: We only can place a tent beside a tree (vertically or horizontally)
Tents never touch each other vertically or horizontally or even diagonally
Final state: All trees have a corresponding tent
We can check this if we reach out to the leaf having the highest deep

### A* Search
<h3>State:</h3>
<p>2D list</p>
<h3>Legal move:</h3>
<p>First, We choose the first empty cell</p>
<p>If we place the tent on this cell, this tent mustn't
 touch other tents vertically or horizontally or even diagonally. The cost of this action will be 1
</p>
<p>If we decide to set this cell empty, the cost of this action will be 0
</p>
<h3>Heuristic function:: </h3> <p>is the combination of the number of the used tent (the cost of the path
 from the root to this) and the number of the remaining tents we need to place to pass this game</p>
