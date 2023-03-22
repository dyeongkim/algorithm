N, M = map(int,input().split()) #세로N 가로M
graph = []*N
cctv_v = [[0]*M for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input().split())))

def view(x, y, c) :
    max_cnt = -1
    if c == 1 :
        dx, dy = [-1,0,1,0],[0,1,0,-1]
        for i in range(4):
            cnt = 0
            wx = x
            wy = y
            while True :
                nx = dx[i] + wx
                ny = dy[i] + wy
         
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    break

                if graph[nx][ny] != 0:
                    break
                
                cnt += 1
                wx,wy = nx,ny
            
            if max_cnt < cnt:
                max_cnt = cnt

    return max_cnt


for i in range(N):
    for j in range(M):
        if graph[i][j] != 0:
            print(view(i,j, graph[i][j]))
