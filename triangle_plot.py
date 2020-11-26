import numpy as np
import matplotlib.pyplot as plt

def transform(x):
	t0 = np.array([-(1/3)*np.cos(np.pi/6), (1/3)*(1 + np.sin(np.pi/6))])
	xp = np.array([x*np.cos(np.pi/6),-x*np.sin(np.pi/6)])
	return xp + t0

def transpt(x):
	p1,p2 = x[0],x[1]
	a = transform(p2)
	C = a[1] - (1/np.tan(np.pi/6))*a[0]
	return [(p1-C)*np.tan(np.pi/6),x[0]]

def plot_triangle(t,names):
	#Drawing the axes
	a = transform(0)
	b = transform(1)
	c = transpt([0,0])
	d = transpt([1/2,1/2])
	plt.plot([0,b[0]],[1,b[1]], c='k')
	plt.plot([c[0],b[0]],[c[1],b[1]], c='k')
	plt.plot([c[0],0],[c[1],1], c='k')
	plt.plot([a[0],b[0]],[a[1],b[1]],ls = ':',c = 'k')
	plt.plot([0,0],[0,1], ls = ':', c='k')
	plt.plot([c[0],d[0]],[c[1],d[1]], ls = ':', c='k')
	plt.text(0,1,names[0] + "\n 100%" ,fontsize = 12, horizontalalignment='center')
	plt.text(b[0],b[1],names[1] +"\n 100%",fontsize = 12, verticalalignment='center')
	plt.text(c[0],c[1],names[2]+ "\n 100%",fontsize = 12,horizontalalignment='right',verticalalignment='center')
	plt.axis('off')
	plt.gca().set_aspect('equal', adjustable='box')

	#Plotting
	tx,ty = [],[]
	for x,y in zip(t[0],t[1]):
		arr = transpt([x,y])
		tx.append(arr[0])
		ty.append(arr[1])
	plt.plot(tx,ty, c='red')
