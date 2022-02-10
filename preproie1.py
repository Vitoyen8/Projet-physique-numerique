import numpy as np
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from scipy.integrate import odeint


y0 = [1,2] # [lapins, renards] en centaines
y1 = [1.2,3] # [lapins, renards] en centaines
y2 = [1.4,4] # [lapins, renards] en centaines
y3 = [1.6,5] # [lapins, renards] en centaines
y4 = [1.8,6] # [lapins, renards] en centaines
y5 = [2,7] # [lapins, renards] en centaines
y6 = [2.2,8] # [lapins, renards] en centaines
y7 = [2.4,9] # [lapins, renards] en centaines
y8 = [2.6,10] # [lapins, renards] en centaines
y9 = [2.8,11] # [lapins, renards] en centaines
j=y0

t = np.linspace(0,50,num=1000)

alpha = 1
# taux de reproduction lapins
beta = 1.2
# taux de mortalité lapins
delta = 1.5
# taux de reproduction renards
gamma = 1
# taux de mortalité renards
mu = alpha / gamma

# conditions initiales
# y0 = [gamma/delta , alpha/beta] # [lapins, renards] en centaines


params = [alpha, beta, delta, gamma, mu]

def sim(variables, t, params):

    # population de lapins
    x = variables[0]

    # population de renards
    y = variables[1]


    alpha = params[0]
    beta = params[1]
    delta = params[2]
    gamma = params[3]
    mu = params [4]

    dxdt = alpha * x - beta * x * y 
    dydt = delta * x * y - gamma * y
    

    return([dxdt,dydt])


f,(ax3) = plt.subplots(1)


#def trace(y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, params) :
ya = odeint(sim, y0, t, args=(params,))
yb = odeint(sim, y1, t, args=(params,))
yc = odeint(sim, y2, t, args=(params,))
yd = odeint(sim, y3, t, args=(params,))
ye = odeint(sim, y4, t, args=(params,))
yf = odeint(sim, y5, t, args=(params,))
yg = odeint(sim, y6, t, args=(params,))
yh = odeint(sim, y7, t, args=(params,))
yi = odeint(sim, y8, t, args=(params,))
yj = odeint(sim, y9, t, args=(params,))
line3a, = ax3.plot(ya[:,0],ya[:,1], color="b") 
line3b, = ax3.plot(yb[:,0],yb[:,1], color="blue")
line3c, = ax3.plot(yc[:,0],yc[:,1], color="mediumblue")
line3d, = ax3.plot(yd[:,0],yd[:,1], color="darkblue")
line3e, = ax3.plot(ye[:,0],ye[:,1], color="navy")
line3f, = ax3.plot(yf[:,0],yf[:,1], color="navy")
line3g, = ax3.plot(yg[:,0],yg[:,1], color="navy")
line3h, = ax3.plot(yh[:,0],yh[:,1], color="navy")
line3i, = ax3.plot(yi[:,0],yi[:,1], color="navy")
line3j, = ax3.plot(yj[:,0],yj[:,1], color="navy")

# line1a, = ax1.plot(t,ya[:,0], color="b")
# line1b, = ax1.plot(t,yb[:,0], color="blue")
# line1c, = ax1.plot(t,yc[:,0], color="mediumblue")
# line1d, = ax1.plot(t,yd[:,0], color="darkblue")
# line1e, = ax1.plot(t,ye[:,0], color="navy")

# line2a, = ax2.plot(t,ya[:,1], color="b")
# line2b, = ax2.plot(t,yb[:,1], color="blue")
# line2c, = ax2.plot(t,yc[:,1], color="mediumblue")
# line2d, = ax2.plot(t,yd[:,1], color="darkblue")
# line2e, = ax2.plot(t,ye[:,1], color="navy")

#line3a, = ax3.plot([y0], marker='x', linestyle='none', color='red')
#line3b, = ax3.plot([y1], marker='x', linestyle='none', color='red')
#line3c, = ax3.plot([y2], marker='x', linestyle='none', color='red')
#line3d, = ax3.plot([y3], marker='x', linestyle='none', color='red')
#line3e, = ax3.plot([y4], marker='x', linestyle='none', color='red')

ax3.plot(y0[0], y0[1], marker='x', linestyle='none', color='red')
ax3.plot(y1[0], y1[1], marker='x', linestyle='none', color='red')
ax3.plot(y2[0], y2[1], marker='x', linestyle='none', color='red')
ax3.plot(y3[0], y3[1], marker='x', linestyle='none', color='red')
ax3.plot(y4[0], y4[1], marker='x', linestyle='none', color='red')
ax3.plot(y5[0], y5[1], marker='x', linestyle='none', color='red')
ax3.plot(y6[0], y6[1], marker='x', linestyle='none', color='red')
ax3.plot(y7[0], y7[1], marker='x', linestyle='none', color='red')
ax3.plot(y8[0], y8[1], marker='x', linestyle='none', color='red')
ax3.plot(y9[0], y9[1], marker='x', linestyle='none', color='red')

#ax1.set_ylabel("Lapins (centaines)")
#ax2.set_ylabel("Renards (centaines)")
#ax2.set_xlabel("Temps (unité arbitraire)")

# Barre de glissement pour le paramètre c
axe_c = plt.axes([0.1, 0.05, 0.65, 0.03])
barre_c= Slider(axe_c, 'c', 1.0, 15, alpha)
fin = plt.axes([0.85, 0.05, 0.1, 0.04])
bouton_fin=Button(fin,'Fin')

# Mise à jour de l'image
def update(val):
  j=barre_c.val
  sim(alpha,beta,gamma,delta)

# Activation de la barre
barre_c.on_changed(update)
bouton_fin.on_clicked(quitter)

plt.show()
