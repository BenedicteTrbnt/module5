# Ce code a pour but de construire les tableaux de coordonnées, de calculer l'épaisseur maximale et
# et la possition de ce maximum le long de la corde et d'afficher la forme d'un profil NACA choisi

import numpy as np
import matplotlib.pyplot as plt



# demander à l'utilisateur le numéro du profil NACA à 4 chiffres symétriques
numero_profil = int(input('Quels sont les 2 derniers chiffres du profil NACA symétrique NACA00XX ?'))
corde = float(input('Quel est la corde du profil en mètres ?'))
nb_points=int(input('Combien de points veux-tu le long de la corde pour le tracé du profil ?'))
t=numero_profil/100
theta=np.linspace(0,np.pi,nb_points)
x_c = 0.5*(1-np.cos(theta))
y_t = (5*t)*(0.2969*np.sqrt(x_c)-0.1260*x_c-0.3516*np.power(x_c,2)+0.2843*np.power(x_c,3)-0.1036*np.power(x_c,4))
x_up = x_c*corde
x_down = x_c*corde
y_up = y_t*corde
y_down = -y_t*corde

# Epaisseur max et position le long de la corde
epaisseur = y_up-y_down
indice_max= np.argmax(epaisseur)
print('L\'épaisseur maximale du profil est de ',epaisseur[indice_max], ' m  et est située à ',x_up[indice_max],' m sur la corde')

# paramètres
plt.rcParams['font.size'] = 14
plt.rcParams['figure.autolayout'] = True
plt.rcParams['figure.dpi'] = 100

# figure
plt.plot(x_up,y_up,label='extrados',color='b')
plt.plot(x_down,y_down,label='intrados',color='c')
plt.xlabel('x (corde en m)')
plt.ylabel('y (épaisseur en m)')
plt.legend()
plt.grid()
numero=str(numero_profil )
titre='Profil NACA00'+numero
plt.title(titre)
plt.show()

