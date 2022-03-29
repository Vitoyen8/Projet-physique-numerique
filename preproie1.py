from numpy import *
import numpy as np
import pylab as p
from scipy import integrate
import matplotlib.pyplot as plt


a, b, c, d = 1.0, 0.1, 1.5, 0.75

def dX_dt(X, t, a, b, c, d):
    return array([ a*X[0] - b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1] ])

X00 = [4, 2]
t3b = linspace(0, 20, 500)
values  = linspace(0.3, 0.9, 10)
vcolors = p.cm.winter_r(linspace(0.1, 1.0, len(values)))
mcolors = p.cm.winter_r(linspace(0.1, 1.0, len(values)))
betas = np.arange(0.4, 1.4, 0.1)


fig3b, ax3b = plt.subplots(2,1)
fig3b.suptitle("Proies et prédateurs en fonction de beta", size = 17 )
   
for B, col in zip(betas, vcolors):
       
    X = integrate.odeint(dX_dt, X00, t3b, args = (a,B,c,d))
    
    ax3b[0].plot(t3b, X[:,0], color = col, label= R" $\beta = $" + "%.1f" %B)
    ax3b[0].legend()
        
for B, col in zip(betas, mcolors):
        
    X = integrate.odeint(dX_dt, X00, t3b, args = (a,B,c,d))
       
    ax3b[1].plot(t3b, X[:,1], color = col, label = R" $\beta = $" + "%.1f" %B)
    ax3b[1].legend()
    fig3b.suptitle("Proies et prédateurs en fonction de beta")
       
ax3b[0].set_xlabel('Temps')
ax3b[0].set_ylabel('Prédateurs')
ax3b[1].set_xlabel('Temps')
ax3b[1].set_ylabel('Proies');

mngr = plt.get_current_fig_manager()
mngr.window.setGeometry(0,70,1438,750)
