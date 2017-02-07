
import sys
import time

# Algorithm for IDA search
def IDA(root,goal,N,filename):
    size = N
    threshold = manhattan(root,goal,size) # Setting the depth bound as heuristic value
    while(1):
        temp = search(root,0,threshold,goal,size,filename,visited=None,paths=None)
        if(temp ==1):
            return threshold
        if(temp==float('inf')):
            return
        threshold = temp

# recursive search algorithm
def search(root,g,threshold,goal,size,filename,visited,paths):
    if paths is None:
        paths = []
    if visited is None:
        visited = []

    f=g+manhattan(root,goal,size)
    if(f>threshold):
        return f
    if(root ==goal):
        file = open(filename, 'w')
        file.write(",".join(paths))
        print(paths)
        return 1
    min = sys.maxsize

    child,p = children_IDA(root,size) # Generation of child nodes
    for tempnode,t in zip(child,p):
        visited.append(tempnode)
        paths.append(t)

        temp = search(tempnode,g + 1,threshold,goal,size,filename,visited,paths) # Recursive call to search till bound exceeded
        if temp==1:
            return 1
        if(temp<min):
            min = temp

        del(visited[-1])
        del(paths[-1])

    return min


def calcheuristic(node, goal): # Number of misplaced tiles heuristic(not used in this code)
        if node == goal:
            return 0
        dist = 0
        for x, y in zip(goal, node):
            if x != y:
                dist += 1

        if node.index(0)!= goal.index(0):
            dist = dist-1

        return dist

def manhattan(A,goal,N): # Manhattan distance heuristic
    misplaced = 0
    for x in A:
        if x==0:
            continue
        own = A.index(x)
        index = goal.index(x)
        if own ==index:
            continue

        else:
            i = int(own/N)
            j = own%N

            k = int(index/N)
            l = index%N

            misplaced+= abs(i-k)+abs(j-l)
    return misplaced


def children_IDA(node,size): # function to generate children in IDA algorithm
        child = []
        p=[]
        n = node.index(0)
        i = int(n / size)
        j = n % size

        if i > 0:
            a = i - 1
            index = a * size + j
            A1 = node[:]
            A1[n], A1[index] = A1[index], A1[n]
            child.append(A1)
            p.append('U')


        if j > 0:
            b = j - 1
            index = i * size + b
            A2 = node[:]
            A2[n], A2[index] = A2[index], A2[n]
            child.append(A2)
            p.append('L')

        if i < size-1:
            c = i + 1
            index = c * size + j
            A3 = node[:]
            A3[n], A3[index] = A3[index], A3[n]
            child.append(A3)
            p.append('D')

        if j < size-1:
            d = j + 1
            index = i * size + d
            A4 = node[:]
            A4[n], A4[index] = A4[index], A4[n]
            child.append(A4)
            p.append('R')

        return child,p

# A Star Algorithm starts here

class Node:
    def __init__(self,value,H,G,path):
        self.value = value
        self.H = H
        self.G = G
        self.F = self.G + self.H
        self.path = path
        self.parent= None




def sub2index(a,b,N):
    return a*N + b


def children_Astar(node,goal,N): # function to generate children
    #size = N
    child = []
    n = node.value.index(0)
    i = int(n / N)
    j = n % N

    if i > 0:
        a = i - 1
        index = sub2index(a,j,N) #a * N + j
        A1 = node.value[:]
        A1[n], A1[index] = A1[index], A1[n]
        N1 = Node(A1,manhattan(A1, goal,N), node.G +1, 'U')
        child.append(N1)



    if j > 0:
        b = j - 1
        index = sub2index(i,b,N) #i * N + b
        A2 = node.value[:]
        A2[n], A2[index] = A2[index], A2[n]
        N2 = Node(A2,manhattan(A2,goal,N),node.G+1, 'L')
        child.append(N2)

    if i < N-1:
        c = i + 1
        index = sub2index(c,j,N) #c * N + j
        A3 = node.value[:]
        A3[n], A3[index] = A3[index], A3[n]
        N3 = Node(A3,manhattan(A3,goal,N),node.G+1,'D')
        child.append(N3)


    if j < N-1:
        d = j + 1
        index = sub2index(i,d,N) #i * N + d
        A4 = node.value[:]
        A4[n], A4[index] = A4[index], A4[n]
        N4 = Node(A4,manhattan(A4,goal,N), node.G+1,'R')
        child.append(N4)


    return child


def astar(start, goal,numstatesexplored,N):
    openset = [] # Initialize frontier to empty

    closedset = [] # Initialize explored set to empty
    current = start
    openset.append(current) # Add starting node to openset



    while openset:  # While the frontier has elements
        openset.sort(key=lambda x:x.F, reverse=False) # Extract node with least F value
        current = openset[0]
        numstatesexplored += 1

        if current.value == goal: # Check if goal
            path = []
            while current.parent:
                path.append(current.path)
                current = current.parent # If goal, retrace and return path
            print ("States explored: " + str(numstatesexplored))
            return path[::-1]

        openset.remove(current)  # Remove item from frontier
        closedset.append(current) # Add item to explored



        for node in children_Astar(current,goal,N):

            if node in closedset: # If child node in explored, ignore
                continue
            if node in openset: # If child node in frontier, update frontier node with lower of the two G values
                new_g = current.G + 1
                if node.G > new_g:
                    node.G = new_g
                    node.parent=current

            else:
                openset.append(node) # Else add child to frontier
                node.parent = current



    raise ValueError('No Path Found')





if __name__ == "__main__":


    if len(sys.argv) == 5:
        Algorithm = int(sys.argv[1])
        N = int(sys.argv[2])
        in_file = sys.argv[3]
        out_file = sys.argv[4]

    else:
        print('Wrong number of arguments.')


    d = []
    with open(in_file, 'r') as f:
        for line in f:
            data = line.splitlines()
            for i in data:
                d.extend(i.split(','))

        k = [0 if x is '' else int(x) for x in d]
        print(k)

    if N == 3:
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    elif N == 4:
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]


    #Algorithm =1

    if Algorithm == 1:
        numstatesexplored = 0
        start1 = Node(k, 0, 0, [])
        print ("starting...")

        start = time.time()
        a = astar(start1, goal, numstatesexplored, N)
        end = time.time()
        elapsed = 1000*(end-start)
        print("Time in milliseconds: " + str(elapsed))
        print(a)
        print("Depth: " + str(len(a)))
        file = open(out_file, 'w')
        file.write(",".join(a))

    if Algorithm == 2:
        s = IDA(k, goal, N, out_file)
        print(s)





