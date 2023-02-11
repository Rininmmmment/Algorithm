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