# Implémentation de l'Algorithme de Shor avec Qiskit

Ce projet est une implémentation de l'algorithme de Shor en utilisant Qiskit, un framework open-source de calcul quantique développé par IBM.

## Introduction

L'algorithme de Shor est un algorithme quantique permettant de factoriser des entiers en temps polynomial, ce qui rendrait de nombreux systèmes de chiffrement actuels obsolètes.

## Installation

Pour utiliser Qiskit, commencez par créer un environnement avec Conda, puis installez les bibliothèques nécessaires :

```bash
conda create -n mon_environnement python=3.7
conda activate mon_environnement
pip install qiskit==1.0.2 qiskit-aer==0.14.0.1
```

Il est important de noter que d'autres bibliothèques que vous pourriez trouver en ligne peuvent ne pas fonctionner correctement en raison des dernières mises à jour de Qiskit. Ces deux bibliothèques sont suffisantes pour ce projet.

## Test

Trois fichiers sont fournis :
- Le premier fichier, `test_n_15_x_11.py`, permet de calculer les mesures du circuit pour \( n+15 \) avec \( x=11 \).
- Le fichier `comparaison.py` permet de tester le circuit pour plusieurs valeurs de \( x \).
- Le dernier fichier, `test_n_21.py`, permet de tester l'algorithme de Shor pour \( n=21 \).

## Circuit quantique

Pour afficher un circuit quantique, il vous suffit d'ajouter `print(circuit)` (en remplaçant "circuit" par le nom du circuit) pour afficher son intégralité.
