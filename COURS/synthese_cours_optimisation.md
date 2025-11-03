# Synthèse des Méthodes d'Optimisation - Aide à la Décision

## 1. La Programmation Linéaire (PL)

### Concept
C'est une technique mathématique pour trouver le meilleur résultat (profit max, coût min...) dans un modèle où toutes les relations sont des droites (linéaires).

> **Analogie :** C'est comme trouver le point le plus haut (ou le plus bas) d'une région montagneuse aux facettes parfaitement planes.

### Pourquoi est-ce si important ?
La PL est la base de tout. Savoir "poser" un problème en langage PL (le modéliser), c'est 90% du travail. C'est la compétence humaine essentielle. La résolution est ensuite confiée à l'ordinateur.

### Procédure de Modélisation (pas-à-pas)
1.  **Lire et Comprendre :** Lisez attentivement l'énoncé pour identifier l'objectif principal et les différentes limitations.
2.  **Identifier les Variables de Décision :** Posez-vous la question : "Sur quoi puis-je agir ? Quelles sont les quantités que je dois déterminer ?". Ce seront vos `x_i`. Nommez-les explicitement (ex: `x_A` = nombre de produits A à fabriquer).
3.  **Formuler la Fonction Objectif :** Traduisez le but principal en une équation mathématique impliquant vos variables. Est-ce une maximisation (profit, rendement) ou une minimisation (coût, risque) ?
4.  **Lister et Formuler les Contraintes :** Pour chaque limitation, ressource, ou règle de l'énoncé (ex: "pas plus de 120h de travail", "au moins 10 unités de B"), écrivez une inéquation.
5.  **Ajouter les Contraintes de Non-Négativité :** Ne jamais oublier d'écrire que vos variables doivent être positives ou nulles (`x_i >= 0`), sauf cas exceptionnel.
6.  **Assembler le Modèle Final :** Présentez proprement le modèle complet avec la fonction objectif en premier, suivie de la liste des contraintes.

---

## 2. La Méthode du Simplexe

### Concept
C'est l'algorithme ("recette de calcul") qui résout un problème de PL. La méthode graphique est pédagogique mais limitée à 2 variables. Le simplexe peut naviguer dans un espace à des milliers de dimensions.

### Comment ça marche (vulgarisé) ?
1.  La zone des solutions réalisables est un **polyèdre** (un volume à facettes planes).
2.  La solution optimale se trouve FORCÉMENT sur un des **sommets**.
3.  L'algorithme du simplexe est un "alpiniste" qui se déplace de sommet en sommet, en choisissant toujours l'arête qui "monte" le plus, jusqu'à atteindre le point culminant (l'optimum).

### Procédure de Résolution Graphique (pour 2 variables)
1.  **Tracer les Axes :** Dessinez un repère avec vos deux variables (`x1` en abscisse, `x2` en ordonnée).
2.  **Tracer chaque Contrainte :** Pour chaque inéquation, tracez la droite frontière (en remplaçant `≤` ou `≥` par `=`). Trouvez deux points pour tracer la droite (ex: si `x1=0`, que vaut `x2` ? et vice-versa).
3.  **Identifier la Zone Valide :** Pour chaque contrainte, déterminez de quel côté de la droite se trouve la zone autorisée (souvent en testant le point (0,0)). Hachurez la zone *interdite*.
4.  **Délimiter la Zone Réalisable :** La zone laissée vierge après avoir tracé toutes les contraintes est le polygone des solutions réalisables.
5.  **Calculer les Coordonnées des Sommets :** Chaque sommet est à l'intersection de deux droites-frontières. Résolvez les systèmes d'équations `2x2` pour trouver leurs coordonnées exactes.
6.  **Évaluer l'Objectif :** Calculez la valeur de la fonction objectif `Z` pour chaque sommet.
7.  **Conclure :** Le sommet qui donne la plus grande valeur de `Z` (pour une maximisation) ou la plus petite (pour une minimisation) est la solution optimale.

---

## 3. La Dualité en Programmation Linéaire

### Concept
Chaque problème Primal possède un problème "miroir", le Dual. Ils représentent deux facettes (économiques) du même problème. Le Primal est souvent le point de vue du producteur (maximiser profit), le Dual celui d'un acheteur de ressources (minimiser coût d'achat).

### L'Interprétation Économique
Les variables du dual (`y_i`) sont les **"prix marginaux"** (ou "shadow prices"). `y_machine = 5€` signifie qu'une heure de machine supplémentaire augmenterait le profit maximal de 5€.

### Théorème Fondamental
À l'optimum, **Profit max du Primal = Coût min du Dual**.

### Procédure pour Construire le Dual (d'un Primal de Max)
1.  **Associer les Variables :** Créez une variable duale `y_i` pour chaque contrainte `i` du primal.
2.  **Construire l'Objectif Dual :**
    *   L'objectif devient une **Minimisation**.
    *   Les coefficients de cet objectif sont les seconds membres (les valeurs à droite) des contraintes du primal.
3.  **Construire les Contraintes Duales :**
    *   Il y aura autant de contraintes duales qu'il y avait de variables `x_j` dans le primal.
    *   La matrice des coefficients est la **transposée** de la matrice primale.
    *   Le signe des contraintes duales est `≥`.
    *   Les seconds membres de ces contraintes sont les coefficients de l'objectif primal.
4.  **Définir le Signe des Variables Duales :** Toutes les variables duales `y_i` doivent être `≥ 0`.

---

## 4. L'Optimisation Multi-Objectifs

### Concept
Gérer des problèmes réels avec des objectifs contradictoires (ex: Maximiser la performance ET Minimiser le coût). Il n'y a plus UNE solution optimale, mais un **ENSEMBLE de bons compromis**.

### Le Front de Pareto
C'est l'ensemble de toutes les solutions "non-dominées".

> **Analogie :** Le Front de Pareto, c'est **l'élite des champions**. Aucun champion sur le front ne peut être battu dans toutes les disciplines à la fois par un autre.

### Procédure pour Identifier le Front de Pareto
1.  **Prendre une solution** S_i dans la liste.
2.  **La comparer à toutes les autres solutions** S_j.
3.  **Vérifier la Dominance :** Est-ce que S_j est meilleure ou égale à S_i sur tous les objectifs, et strictement meilleure sur au moins un ?
    *   Si **OUI**, alors S_i est dominée. On peut la barrer de la liste des candidats au front.
    *   Si **NON**, on continue la comparaison avec les autres S_j.
4.  **Répéter :** Faire ce processus pour chaque solution S_i.
5.  **Conclure :** Les solutions qui n'ont jamais été barrées (jamais dominées) forment le Front de Pareto.

### Méthodes pour Choisir sur le Front

#### a) Méthode de la Somme Pondérée
*   **Philosophie :** "Transformer plusieurs objectifs en un seul super-score."
*   **Procédure :**
    1.  **Isoler les solutions** du Front de Pareto.
    2.  Pour chaque critère (objectif), **trouver la valeur `min` et la valeur `max`** parmi ces solutions.
    3.  **Normaliser les scores :** Pour chaque solution et chaque critère, calculer la valeur normalisée (entre 0 et 1).
        *   Pour un critère à **maximiser** : `(valeur - min) / (max - min)`
        *   Pour un critère à **minimiser** : `1 - (valeur - min) / (max - min)`
    4.  **Définir les Poids :** Attribuer un poids `w_i` à chaque critère selon son importance (la somme des poids doit faire 1).
    5.  **Calculer le Score Global :** Pour chaque solution, calculer `Score = w1 * score_norm_1 + w2 * score_norm_2 + ...`
    6.  **Classer les solutions :** La solution avec le score global le plus élevé est la meilleure selon cette pondération.

#### b) Méthodes de Sur-classement (ex: ELECTRE)
*   **Philosophie :** "Organiser un tournoi entre les solutions pour les classer."
*   **Procédure Conceptuelle :**
    1.  **Comparer les solutions deux à deux** (A vs B) sur chaque critère.
    2.  **Calculer un "indice de concordance" :** Somme des poids des critères où A est meilleure que B. Cela mesure la force de l'affirmation "A est préférable à B".
    3.  **Calculer un "indice de non-discordance" :** Vérifier si sur un critère, B n'écrase pas complètement A (dépasse un "seuil de veto").
    4.  **Établir la Relation de Sur-classement :** Si l'indice de concordance est assez haut ET qu'il n'y a pas de veto, on déclare que "A surclasse B".
    5.  **Construire le Classement Final :** À partir de toutes les relations de sur-classement, on déduit un classement (parfois partiel) des solutions.
