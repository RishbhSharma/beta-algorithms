''' The following program does the following:
    Takes a Graph/Tree as input, creates its adjacency list,
    Calculates number of nodes at a level [BFS Traversal]
'''
# INPUT FORMAT
# LINE 1 : Number of Nodes (N)
# N-1 Lines : "1 Indexed" End-points of edge (S,D) where S->D and D->S
# Nth Line : Query of number of elements "0 Indexed" X'th level

# IMPORT DOUBLE_ENDED_QUEUE
from collections import deque
# INPUT NO. OF NODES
n=input()
# CREATE ADJACENCY LIST
adj=[[1]]+[[] for i in range(n)]
# INPUT S,D and add Edges ( S->D and D->S )
for i in range(n-1):
    s,d=map(int,raw_input().split())
    adj[s].append(d)
    adj[d].append(s)
# BOOLEAN ARRAY FOR VISITED NODES (initially False)
visited=[False]*(n+1)
# INITIALISE D-E-QUEUE W/ HYPOTHETICAL ROOT NODE '0'
q=deque([0]) 
# LEV IS THE INDEX FOR "NO. OF ELEMENTS AT i'th LEVEL"
lev=[1]
# ELE IS THE LIST OF DISTINCT ADJACENT NODES IN A LEVEL"
ele=[0]

''' BREADTH-FIRST-SEARCH STARTS HERE! '''
while len(q):
    # c KEEPS ALL THE 'NODES' ADJACENT TO 'NODES IN ELE'
    c=[]
    # POP CURRENT ELEMENT FROM QUEUE 
    curr=q.popleft()
    # MARK AS VISITED
    visited[curr]=True

    ''' THE LOOP CAN BE EXPLAINED AS FOLLOWS:
        FOR EACH NODE IN 'ELE', ADD ITS ADJACENT NODES IN C '''
    for x in ele:
        c+=adj[x]
    '''FILTER THE DISTINCT ELEMENTS OUT OF C'''
    ele=list(set(c))
    # EAL == ELEMENTS IN LEVEL (NOT YET VISITED)
    eal=0
    for x in ele:
        if not visited[x]:
            eal+=1
    # ADD NODES AT LEVEL IN LIST
    lev.append(eal)
    ''' REMAINING PART OF BFS '''
    for x in adj[curr]:
        if not visited[x]:
            q.append(x)
#PRINT ELEMENTS AT INPUT() LEVEL (0 INDEXED)
print lev[input()]
