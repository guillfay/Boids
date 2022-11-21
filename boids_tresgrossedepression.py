from typing import Iterable
import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt
from matplotlib import animation, path, cm
from tqdm import tqdm

radians=float

nombre_boids=150

# Donne la forme de flèche des boids
arrow_boid=path.Path(
    # coordonnées du schéma ci-dessous, orienté vers la droite
    vertices=np.array([[0, 0], [-100, 100], [200, 0], [-100, -100], [0, 0]]),
    codes=np.array([1, 2, 2, 2, 79], dtype=np.uint8),
)

# Rotation des boids dans leurs parcours
def rotation(arrow: path.Path,angle):
    cos,sin=np.cos(angle),np.sin(angle)
    rotation_matrix=np.array([[cos, sin], [-sin, cos]])
    new_arrow=arrow.vertices @ rotation_matrix
    return path.Path(new_arrow,arrow.codes)

class Boid:
    affichage=200
    max_voisins=20
    dispersion_vitesse=3
    angle_max=2/3*np.pi
    max_vitesse=8

    # Initialisation d'un boid avec une position et une vitesse aléatoires
    def __init__(self):
        self.x=rd.uniform(-Boid.affichage,Boid.affichage,2)
        self.dx=rd.uniform(-Boid.dispersion_vitesse,Boid.dispersion_vitesse,2)
    
    # Renvoie la vitesse d'un boid
    @property
    def vitesse(self):
        return np.linalg.norm(self.dx)

    # Modifie la vitesse du boid
    @vitesse.setter
    def vitesse(self, value):
        self.dx = self.dx * value / self.vitesse

    # Renvoie la direction d'un boid
    @property
    def direction(self):
        return np.arctan2(self.dx[1], self.dx[0])

    # Renvoie la distance entre deux boids
    def distance(self,boid2:"Boid"):
        return np.linalg.norm(self.x-boid2.x)

    # Renvoie True si le boid2 voit le boid1
    def vision(self,boid2:"Boid"):
        t1=self.dx-self.x # trajectoire du boid1
        t2=boid2.dx-boid2.x #trajectoire du boid2
        cos_angle=(t1@t2)/(np.linalg.norm(t1)*np.linalg.norm(t2))
        return np.arccos(cos_angle)<Boid.angle_max

    # Détermine si un boid peut être voisin du boid considéré et renvoit la liste des boids voisins triés par distance
    def voisins(self,group:"Iterable[Boid]",limit_distance):
            return sorted((oiseau for oiseau in group if self is not oiseau and self.vision(oiseau) and self.distance(oiseau)<limit_distance),key=self.distance)
    
    # Eloigne le boid s'il est trop proche de ses voisins
    def separation(self,group:"Iterable[Boid]"):
        return sum(self.x-oiseau.x for oiseau in self.voisins(group,20)[:Boid.max_voisins])

    # Aligne les boids dans une direciton moyenne par rapport aux voisins s'il en a
    def alignment(self,group:"Iterable[Boid]"):
        neighbors = self.voisins(group,50)
        if len(neighbors):
            return sum(oiseau.dx for oiseau in neighbors)/len(neighbors)
        else:
            return 0
    
    # Rapproche les boids trop éloignés
    def cohesion(self,group:"Iterable[Boid]"):
        neighbors = self.voisins(group,75)[: Boid.max_voisins*2]
        if len(neighbors):
            return sum(oiseau.x for oiseau in neighbors)/len(neighbors)-self.x
        else:
            return 0

    #je sais pas
    def gravity(self):
        return -self.x

    # Incertitude sur les trajectoires de boids
    def alea(self):
        return rd.uniform(-5,5,2)

    # Fait avancer le boid
    def forward(self):
        self.x+=self.dx

    # Fait rebondir le boid lorsqu'il atteint un bord, en le revoyant vers le bord opposé
    def rebound(self):
        
        if self.x[0]>=Boid.affichage:
            self.x[0]=-Boid.affichage
        if self.x[0]<-Boid.affichage:
            self.x[0]=Boid.affichage
        if self.x[1]>=Boid.affichage:
            self.x[1]=-Boid.affichage
        if self.x[1]<-Boid.affichage:
            self.x[1]=Boid.affichage

    # Permet de déplacer les boids en respectant toutes les règles d'interaction
    def movement(self,group:"Iterable[Boid]"):
        
        self.dx+=self.cohesion(group)/20+self.separation(group)/20+self.alignment(group)/20
        
        if self.vitesse > Boid.max_vitesse:
            self.vitesse = Boid.max_vitesse

        self.forward()
        self.rebound()

        return self

class Simulate:

    # Initialise la simulation en créant une liste de boids et une aire de visualisation
    def __init__(self,ax):
        self.boids=list(Boid() for oiseau in range(nombre_boids))
        self.liste=[]
        self.plot(ax)

    # Affiche les boids dans l'aire de visualisation
    def plot(self,ax):
        i=0
        cmap=cm.get_cmap('viridis')
        for i,boid in enumerate(self.boids):
            p,*_=ax.plot(*boid.x, color=cmap(rd.uniform(0,1)),markersize=10,marker=rotation(arrow_boid,boid.direction))
            self.liste.append(p)

        ax.set_xlim((-Boid.affichage,Boid.affichage))
        ax.set_ylim((-Boid.affichage,Boid.affichage))
        ax.set_aspect(1)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)    

    # Actualise la simiulation en dépalçant les boids
    def iteration(self, j):
        self.boids=list(boid.movement(self.boids) for boid in self.boids)
        for p,boid in (zip(self.liste,self.boids)):
            p.set_data(*boid.x)
            p.set_marker(rotation(arrow_boid,boid.direction))
        return self.liste

fig,ax=plt.subplots(figsize=(20,20))
simulation=Simulate(ax)  

# Crée une animation vidéo de la simulation
anim=animation.FuncAnimation(fig,simulation.iteration,frames=tqdm(range(0,300)),interval=100,blit=False,repeat=True,cache_frame_data=False)
anim.save("boids.mp4")