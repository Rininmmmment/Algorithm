'''
Union-Find 

---- example ----
uf = unionfind(N)
for i in range(M):
    uf.unite(A[i], B[i])
'''
class unionfind:
	def __init__(self, n):
		self.n = n
		self.par = [ -1 ] * (n + 1)
		self.size = [ 1 ] * (n + 1)
	
	# 頂点 x の根を返す関数
	def root(self, x):
		while self.par[x] != -1:
			x = self.par[x]
		return x
	
	# 要素 u, v をつなげる関数
	def unite(self, u, v):
		rootu = self.root(u)
		rootv = self.root(v)
		if rootu != rootv:
			if self.size[rootu] < self.size[rootv]:
				self.par[rootu] = rootv
				self.size[rootv] += self.size[rootu]
			else:
				self.par[rootv] = rootu
				self.size[rootu] += self.size[rootv]
	
	#  要素 u と v が同一のグループかどうかを返す関数
	def same(self, u, v):
		return self.root(u) == self.root(v)



'''
DFS

---- example ----
dfs(1, G, visited)
for i in range(1, N + 1):
	if visited[i] == False:
		answer = False
'''
import sys
sys.setrecursionlimit(120000)

G = [ list() for i in range(N + 1) ]
visited = [ False ] * (N + 1)

# pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値
def dfs(pos, G, visited):
	visited[pos] = True
	for i in G[pos]:
		if visited[i] == False:
			dfs(i, G, visited)



'''
BFS

---- example ----
最短距離出力
for i in range(1, N + 1):
	print(dist[i])
'''
from collections import deque

dist = [ -1 ] * (N + 1) # 頂点までの距離
dist[1] = 0
Q = deque()
Q.append(1)

while len(Q) >= 1:
	pos = Q.popleft()
	for nex in G[pos]:
		if dist[nex] == -1:
			dist[nex] = dist[pos] + 1
			Q.append(nex)


'''
有向グラフサイクル検出(ABC285 D参照)

---- example ----
N, M = map(int, input().split())
G = [[] for _ in range(N)]  # グラフを表現する隣接リスト (終点のインデックスから、始点の番号を取り出す)
deg = [0 for _ in range(N)] # deg[v]：頂点 v の出次数
for i in range(M):
    a, b = map(int, input().split())
    # 通常のグラフとは逆で、G[b] に a を入れる
    G[b].append(a)
    # 頂点 a の出次数を 1 増やす
    deg[a] += 1

isCycle(N, G, deg)
'''
def isCycle(N, G, deg):

    """
    N: 頂点の数
    M: 辺の数
    G: グラフ(終点のインデックスから、始点の番号を取り出す)
    deg: 頂点 v の出次数
    """

    # 問題文の指示より、隣接リストの中身をソートしておく
    for i in range(N):
        G[i].sort()

    que = deque([]) # 探索候補の頂点番号を入れるキュー
    # 頂点 v = 0, 1, …, N-1 の順に
    for v in range(N):
        # 頂点 v の出次数が最初の時点で 0 ならば、キューに v を入れる
        if deg[v] == 0: que.append(v)

    order = []  # トポロジカルソート順を格納するための配列

    # キューに要素が残っている限り
    while len(que) > 0:
        # キューの先頭要素 v を取り出し、配列 order に挿入する
        v = que.popleft()
        order.append(v)
        
        # 頂点 v に隣接している頂点 v2 について、
        for v2 in G[v]:
            # v2 の出次数を 1 減らして、もし出次数が 0 になったらキューに v2 を入れる
            deg[v2] -= 1
            if deg[v2] == 0: que.append(v2)

    # 全ての頂点が order に含まれているかによって、答えを変える
    if len(order) != N:
        # order の要素数が N でなければ、order に含まれていない頂点があるので Yes
        return True
    else:
        # order の要素数が N であれば、すべての頂点が order に含まれているので No
        return False