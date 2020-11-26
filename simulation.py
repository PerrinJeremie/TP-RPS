import numpy as np
import numpy.random as rd
import copy as cp
import scipy.stats as st
import matplotlib.pyplot as plt

N = 5000
C = 5	
T = 500
eps = -0.2
mu = 0

dist = [4000,500,500] # Has to be sum N

lCeps = st.poisson(C+eps)
lCm1 = st.poisson(C-1)
lCp1 = st.poisson(C+1)



M = [[lCeps,lCp1,lCm1],[lCm1,lCeps,lCp1],[lCp1,lCm1,lCeps]]

pts = [[],[],[]]

def nchilds(law,nparents):
	return np.sum(law.rvs(nparents))

def selectOffsprings(childs):
	NC = sum(childs)
	h = st.hypergeom(NC,childs[0],N)
	dist[0] = h.rvs()
	if dist[0] != N :
		h = st.hypergeom(childs[1]+childs[2],childs[1],N-dist[0])
		dist[1] = h.rvs()
		dist[2] = N - dist[0] - dist[1]
	else:
		dist[1], dist[2] = 0,0

def mutatechilds(childs):
	tmp = [0,0,0]
	for i in range(3):
		nm = rd.binomial(childs[i],mu)
		tmp[i] -= nm
		tmp[(i+1)%3] += nm//2
		tmp[(i+2)%3] += nm - nm//2
	for i in range(3):
		childs[i] += tmp[i]

for t in range(T):
	childs = [0,0,0]
	while sum(childs) < N : 
		for i in range(3):
			for j in range(3):
				tmp = dist[j]
				if i == j:
					tmp -= 1
				tmp = tmp/(N-1)
				childs[i] += nchilds(M[j][i],int(dist[i]*tmp))	
	mutatechilds(childs)
	selectOffsprings(childs)
	for i in range(3):
		pts[i].append(dist[i])

plt.plot(range(T),pts[0], label = "Rock")
plt.plot(range(T),pts[1], label = "Scissors")
plt.plot(range(T),pts[2], label = "Scissors")
plt.legend()
plt.title("Simulating RPS with C = " + str(C) + ", eps = " + str(eps) + ", N = " + str(N) + ", mu = " + str(mu))
plt.show()

'''
for t in range(T):
	childs = [0,0,0]
	t = [0 for _ in range(dist[0])]+\
		[1 for _ in range(dist[1])]+\
		[2 for _ in range(dist[2])]
	rd.shuffle(t)
	L = [[0,0,0],[0,0,0],[0,0,0]]
	for k in range(N//2):
		i,j = t[k],t[N//2 + k]
		L[j][i] += 1
		L[i][j] += 1
	for i in range(3):
		for j in range(3):
			childs[i] += nchilds(M[j][i],L[j][i])
	selectOffsprings(childs)
	print(dist)
'''