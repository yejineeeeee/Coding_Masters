from collections import deque
N=int(input())
dy=[-1,0,1,0]
dx=[0,1,0,-1]
queue=deque()

direct=[]
queue.append((0,0,0,0))
ans=0

def dfs(x,y,direct,count,past):
    global ans
    if count==N:
        ans+=1
        return
    past = past[:]
    past.append((x,y))
    nx=x+dx[direct]
    ny=y+dy[direct]
    if (nx,ny) not in past:
        nd1=(direct+1)%4
        nd2=(direct+3)%4
        dfs(nx,ny,nd1,count+1,past)
        dfs(nx,ny,nd2,count+1,past)
dfs(0,0,0,0,[])
print(ans//2)