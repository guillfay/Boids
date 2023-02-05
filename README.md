# Boids

## Introduction

Les boids sont un algorithme de simulation d'essaims d'oiseaux ou de poissons. Ils modélisent le comportement collectif d'une multitude d'individus en utilisant une approche de programmation basée sur les règles. Chaque boid suit trois règles simples pour déterminer sa direction : alignment (alignement avec les autres boids), cohesion (tendance à rester groupé) et séparation (tendance à éviter les collisions avec les autres boids). En combinant ces trois règles, les boids peuvent simuler un comportement cohérent et réaliste d'essaim en mouvement.

## Histoire

Les boids ont été développés pour la première fois par Craig Reynolds en 1986. Le terme "boid" est un acronyme pour "bird-oid object", qui signifie "objet semblable à un oiseau". Cela reflète l'origine de ce concept en tant que simulation du comportement d'essaims d'oiseaux. Ce terme est par la suite devenu générique pour décrire ce type de simulation de comportement collectif. Craig Reynolds voulait créer une simulation réaliste du comportement collectif d'essaims d'oiseaux ou de poissons pour des applications en animation et en infographie. Il a conçu un algorithme basé sur des règles simples pour déterminer la direction de chaque boid individuel en fonction de sa position et de la position des autres boids. Ce concept a été largement utilisé dans de nombreux domaines, notamment la production cinématographique, les jeux vidéo, la robotique et la modélisation environnementale. Les boids sont considérés comme l'un des premiers exemples de systèmes complexes en simulation informatique, et ont contribué à établir les fondements de la recherche sur les systèmes multi-agents.

## Modélisation

Chaque boid possède un champ de vision, ici à 240° vers l'avant. Dans ce champ de vision, il est à même de d'assimiler les boids les plus proches de sa position à des voisins. Il va alors se comporter en fonction du comportement de son entourage.

On note $V$ l'ensemble des boids suffisamment proche du boid considérés. On les nomme "voisins" de celui-ci.

Les boids suivent généralement trois règles pour déterminer leur direction. Ces trois règles donne trois poids eux-mêmes coefficientés et sommés pour donner la position itérée des boids:

- Alignement : les boids cherchent à se déplacer dans la même direction que les autres boids proches. Cela simule le fait que les oiseaux d'un essaim tendent à voler dans la même direction.

$$\forall v \in V, w_{A} = \frac{1}{card(V)}\sum_{v \in V}
\begin{pmatrix}
dx_v \\
dy_v \\
\end{pmatrix}$$

- Cohésion : les boids cherchent à se rapprocher les uns des autres pour former un groupe serré. Cela simule le fait que les oiseaux d'un essaim cherchent à rester ensemble pour se protéger.

$$\forall v \in V, w_{C} = \frac{1}{card(V)}\sum_{v \in V}
\begin{pmatrix}
x_v \\
y_v \\
\end{pmatrix} -\begin{pmatrix}
x \\
y \\
\end{pmatrix}$$

- Séparation : les boids cherchent à éviter les collisions avec les autres boids. Cela simule le fait que les oiseaux d'un essaim cherchent à maintenir une certaine distance les uns des autres pour éviter les collisions.

$$\forall v \in V, w_{S} = \sum_{v \in V}\left(
\begin{pmatrix}
x \\
y \\
\end{pmatrix}-\begin{pmatrix}
x_v \\
y_v \\
\end{pmatrix}\right)$$

En combinant ces trois règles, les boids peuvent simuler un comportement collectif réaliste d'essaim en mouvement. Les algorithmes de boids peuvent être ajustés en modifiant les poids de chaque règle pour obtenir des comportements différents. Les règles peuvent également être ajoutées ou modifiées pour simuler des comportements plus complexes.

Pour une modélisation plus fidèle à la réalité, les boids ne sont pas confinés dans le cadre d'affichage, mais disposent d'un cadre infini. Par exemple, lorsqu'un boid sort du cadre à droite, il revient à la même hauteur depuis le cadre gauche et dans lamême direction.

## Perspectives et applications

Les boids ont de nombreuses applications dans différents domaines, notamment :
- Animation et effets spéciaux : les boids sont souvent utilisés pour créer des simulations réalistes d'essaims d'oiseaux ou de poissons pour les films, les séries télévisées et les jeux vidéo.
- Modélisation environnementale : les boids peuvent être utilisés pour simuler le comportement de différents animaux dans leur environnement, comme les oiseaux migrateurs ou les poissons dans les rivières.
- Robotique : les algorithmes de boids peuvent être utilisés pour contrôler le comportement collectif de robots, comme les drones en essaim.
- Recherche sur les systèmes multi-agents : les boids sont un exemple de systèmes complexes en simulation informatique et peuvent être utilisés pour étudier les comportements collectifs dans différents contextes.
- Optimisation : les algorithmes de boids peuvent être utilisés pour résoudre des problèmes d'optimisation en utilisant des approches inspirées de la nature.

En particulier, la simulation de boids peut avoir des applications biomédicales
Les boids peuvent en effet aider la médecine dans certaines situations. Par exemple :
- Modélisation de l'épidémiologie : les boids peuvent être utilisés pour simuler la propagation des maladies infectieuses dans une population, en utilisant les règles d'interaction sociale pour modéliser la transmission d'une maladie de personne à personne.
- Planification de la chirurgie : les algorithmes de boids peuvent être utilisés pour planifier la chirurgie en utilisant des méthodes inspirées de la nature pour trouver les meilleures solutions.
- Modélisation des systèmes circulatoires : les boids peuvent être utilisés pour simuler le comportement des fluides dans le corps, comme le sang, pour comprendre comment les maladies affectent le système circulatoire.

Cependant, il convient de noter que les boids ne sont qu'un outil parmi d'autres dans la médecine, et que leur utilisation dépend des besoins spécifiques de chaque situation. Il est important de combiner les approches informatiques avec d'autres méthodes pour obtenir les meilleurs résultats en médecine et en recherche biomédicale.
