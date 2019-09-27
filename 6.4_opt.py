import numpy as np
import matplotlib.pyplot as plt


l = 100
r1 = np.sqrt(5)
theta = np.linspace(0,2*np.pi,l)
x_circ1 = np.zeros((2,l))
x_circ2 = np.zeros((2,l))
x_circ3 = np.zeros((2,l))
#Given
c1 = np.array([1,0])
c2 = np.array([2,-1])
#from KKT condition 1
lam = 1 - (np.linalg.norm(c1-c2))/r1
# from KKT condition 2
X = (c1 - lam*c2)/(1 - lam)
print(lam)
print(X)
# raidus of the optimum cricle
r2 = np.linalg.norm(c1 - X)

for r in range(0,10): 
      r = r/5 
      x_circ1[0,:] = r*np.cos(theta)
      x_circ1[1,:] = r*np.sin(theta)
      x_circ1 = (x_circ1.T + c1).T
      x = 'cricles'
      #plt.plot(x_circ1[0,:],x_circ1[1,:])
#Constrained cricle
x_circ2[0,:] = r1*np.cos(theta)
x_circ2[1,:] = r1*np.sin(theta)
x_circ2 = (x_circ2.T + c2).T

#Optimum cricle
x_circ3[0,:] = r2*np.cos(theta)
x_circ3[1,:] = r2*np.sin(theta)
x_circ3 = (x_circ3.T + c1).T
plt.plot(x_circ3[0,:],x_circ3[1,:],label = 'O_cricle3')
plt.plot(x_circ2[0,:],x_circ2[1,:],label = 'cricle2')
print(r2)
#Optimum point
plt.plot(X[0],X[1],'o')
plt.text(X[0]*(1.01),X[1]*(1.01), 'A')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.grid() 
plt.axis('equal')
plt.title("gvv_linalg_2d_circle\nQuestion 1")


plt.show()
