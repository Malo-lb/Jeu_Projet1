# Projet 1 – Chats et souris (Game Fan-Attic)
**L1-MI – Université Gustave Eiffel – Semestre 1 – 2026**
Guide de synthèse de tous les documents fournis (CM1, sujet, règles du jeu, poly CDC, barème CDC).

---

## 0. L'essentiel en 30 secondes

- **Objectif** : développer en équipe de **3** une version logicielle du jeu *Chats et souris* pour l'association **Game Fan-Attic** (client), représentée par votre **chargé de TP**.
- **Technos imposées** : **Python** + **uniquement la librairie `fltk`** pour l'interface graphique.
- **Méthode** : cycles courts inspirés d'« Agile » : livrable → réunion client → retours → nouveau livrable.
- **Première échéance : CDC V1 à rendre sur e-learning avant le 15/11 à 23:59** (en PDF).
- **Le CDC compte pour 25 % de la note finale.**
- **Pénalités de retard** automatiques, quelle que soit la raison (voir §2).

---

## 1. Répartition de la note finale (sur 100)

| Élément | Points |
|---|---|
| CDC V1 + V2 | **25** |
| Rendu final : rapport + programme | **20** |
| Soutenance en groupe (évaluation individualisée) | **55** |

---

## 2. Planning officiel

| Période | Ce qui se passe | Échéance |
|---|---|---|
| **Semaine 1 : 09/11 → 13/11** | Constitution des équipes + déclaration sur e-learning ; TP fltk (si non terminé) ; analyse du sujet ; répartition des tâches ; début de rédaction du CDC ; **prise de RDV avec le client** ; début du développement | **CDC V1 : avant le 15/11 à 23:59** (noté) |
| **Semaine 2 : 23/11 → 27/11** | **Réunion 1 avec le client** (présence **obligatoire** de tous) : retours sur le CDC V1, **démo du programme V1**, demandes d'amélioration/évolution ; poursuite du dev ; prise de RDV suivant | **CDC V2 : avant le 04/12 à 23:59** |
| **Semaine 3 : 07/12 → 11/12** | **Réunion 2 avec le client** : retours sur le CDC V2 et évaluation, **démo du programme V2**, dernières demandes ; poursuite du dev | Horaires de soutenance publiés avant le 20/12 |
| Vacances 19/12 → 03/01 | | **Rapport + programme : avant le 02/01 à 23:59** |
| **Semaine du 04/01 → 08/01** | **Soutenances** en groupe selon le planning publié | |

### Malus de retard (rendus)
- retard de 10 min à < 3 h : **-1 point**
- de 3 h à < 24 h : **-2 points**
- au-delà : **-2 points par jour supplémentaire**
- La note de rendu ne peut pas être négative (elle peut tomber à 0).

---

## 3. Règles du jeu *Chats et souris* (à reproduire fidèlement)

### Matériel
- Cartes **carrées de couleur**, chacune avec une **face visible** (la couleur) et une **face cachée**.
- Face cachée : **vide**, **un chat** ou **une souris**.
- **Jetons** verts, gris et blancs pour « marquer » les cartes.

### But
- **2 joueurs ou plus**. À tour de rôle, chaque joueur **propose un défi** : il crée une grille en cachant des chats et des souris.
- Les autres joueurs (une seule **équipe** collaborative) doivent trouver **tous les chats et toutes les souris** en faisant **le moins d'erreurs** possible.

### Préparation d'un défi (par le créateur)
1. Il crée **plusieurs piles de cartes de couleur** : **une couleur = une pile**.
2. Dans **chaque pile** : **un seul chat** et **une seule souris**, le reste vide.
3. Il dispose les cartes **face cachée** en grille rectangulaire (plus ou moins complète) avec **3 contraintes** :
   - nombre de cartes = **(nombre de couleurs)²** ;
   - **pas deux chats** sur la même ligne ou la même colonne ;
   - **idem pour les souris** ;
   - **pas de chat et de souris de la même couleur sur deux cases adjacentes**, **diagonales comprises**.

> Exemple du sujet : 5 couleurs (rouge, orange, vert, jaune, bleu) → grille 5×5 = 25 cartes.
> Les piles de l'illustration contiennent aussi une couleur grise et plus, donc le nombre de couleurs est variable.

### Réalisation du défi
1. Le créateur **dévoile un chat ET une souris** (pas forcément de la même couleur) → indices de départ.
2. L'équipe dispose d'un **nombre limité de vies**, décidé **au début du jeu**.
3. L'équipe **désigne une carte** et **annonce** ce qu'elle contient : chat, souris ou vide.
4. La carte est **retournée**. Si elle ne correspond pas à l'annonce → **une vie perdue**. On continue.
5. Fin du défi :
   - **réussi** : tous les chats et toutes les souris trouvés ;
   - **perdu** : toutes les vies perdues.

### Scores
- **Défi gagné** : l'équipe gagne **autant de points que de vies restantes**. Le créateur ne marque **rien**.
- **Défi perdu** : le créateur marque **(vies initiales) × (nombre de joueurs de l'équipe)**. Les autres ne marquent **rien**.

### Jetons
- Aide à la réflexion uniquement : **aucune incidence** sur le défi, ce n'est **pas** une annonce.
- Exemples : **vert** = souris supposée, **gris** = chat supposé, **blanc** = « rien » supposé.
- **Plusieurs jetons possibles** sur une même carte **non retournée**.

---

## 4. Contraintes du client

- Interface : pas d'attentes précises, mais elle doit être **agréable** et **respecter la règle du jeu**.
- **Python** obligatoire, **`fltk` exclusivement** pour le graphique.
- **Code réutilisable** (évolutions futures) → code propre, structuré, lisible, commenté, fonctions/modules bien découpés.
- Les attentes du client **vont évoluer** : prévoir de s'adapter après chaque réunion.

### Règles d'intégrité (importantes)
- **Pas de sous-traitance** ni de code écrit par quelqu'un d'autre qu'un membre de l'équipe → considéré comme **plagiat**.
- **Chaque ligne de code doit être maîtrisée** par le membre qui l'a produite (vous serez interrogé en soutenance).
- **IA générative : déconseillée** (impossible de contrôler l'origine et la licence du code). À n'utiliser, au mieux, que de façon très raisonnée.
- Si vous réutilisez un fragment de code existant : **vérifier sa licence**.

### Bonnes pratiques d'équipe
- Faire équipe : être acteur, responsable, engagé ; respecter les membres, le client, le planning, ce qui a été convenu.
- Outil de partage adapté : Discord (bof), Cloud type Google Drive (mieux), **GitHub (très bien)**.
- Communiquer ses avancées **et ses difficultés**, répondre **toujours** aux collègues.
- Chacun s'investit dans **la production de code** (pas seulement des tâches annexes).
- Code **lisible**, bonnes pratiques.
- Désigner si utile un **chef de projet**.

---

## 5. Le CDC : ce qu'il doit contenir et comment le noter

Le CDC est un **document contractuel** rédigé par votre équipe, **rendu en PDF**, qui évolue (V1 → V2 → version finale annexée au rapport). La **soutenance/recette** évaluera le programme **par rapport à la version finale du CDC**.

### Plan type conseillé (couvre tout le barème)

1. **Page de garde** : titre, nom de l'équipe/startup, membres, UE, année, logo si souhaité, date, version (V1).
2. **Sommaire** (numéros de page cliquables ou non).
3. **Contexte**
   - **Client** : association *Game Fan-Attic* (jeux de plateau oubliés → logiciels jouables), représentée par le chargé de TP.
   - **Besoin** : version logicielle du jeu *Chats et souris*, code réutilisable.
4. **Équipe de développement**
   - **Nom, prénom, rôle** de chaque membre (3 membres), organisation (votre « startup » ou Université Gustave Eiffel).
   - Rôles possibles : chef de projet, responsable interface fltk, responsable logique du jeu / règles…
5. **Technologies**
   - Environnement **nécessaire au fonctionnement du programme** : Python (version), `fltk`, OS compatibles, fichiers/ressources.
   - ⚠️ Ne lister **que ce qui est requis pour faire tourner le programme**, **pas** les outils de dev (GitHub, éditeur, etc.).
   - **Licence logicielle proposée** et **conforme à l'attente du client** (code réutilisable → licence libre type MIT, GPL…, à justifier en une phrase).
6. **Planning** (voir §2)
   - Seulement les **points d'étape** : **réunion 1**, **réunion 2** et **livraison finale (recette/soutenance)**.
   - Pour chacun : date approximative, ordre du jour simplifié, livrable présenté, bilan des réunions précédentes.
   - ❌ Pas le planning de travail interne de l'équipe.
7. **Livrables** : **la partie la plus lourde (6 points)**, voir §6.
8. **Budget, idées d'amélioration, données** (1 point pour au moins un des trois)
   - Budget : aucun achat ni rémunération réels → « faire comme si » (ex. coût en heures-homme) ou mentionner la négociation de note maximale de soutenance.
   - Idées : améliorations possibles du jeu, évolutions futures (ne freinez pas votre imagination).
   - Données : si stockage (scores, pseudos…), analyse de sensibilité + **RGPD** ; sinon préciser qu'aucune donnée personnelle n'est stockée.

### Barème du CDC V1 (20 points)

| Critère | Pts |
|---|---|
| **Structure** : CDC clairement structuré en parties/sous-parties | 1 |
| Présence a minima : **contexte, équipe, technologies, planning, livrable(s)** | 2 |
| Rendu en **fichier PDF** | 1 |
| **Mise en page contractuelle** : page de garde, sommaire, titres, sous-titres, numéros de page | 1 |
| **Syntaxe/orthographe** : phrases complètes, grammaire, accords, ponctuation | 2 |
| **Contexte** correctement présenté (client + besoin) | 2 |
| **Équipe** complète (nom, prénom, rôle) | 1 |
| **Technologies** nécessaires au fonctionnement rappelées | 1 |
| **Licence** proposée et conforme à l'attente du client | 1 |
| **Planning** : les 2 réunions intermédiaires + la livraison finale | 1 |
| **Prochain livrable suffisamment explicité** | **6** |
| Mention du budget **ou** d'idées/pistes d'amélioration **ou** de la protection des données | 1 |
| **Total** | **20** |

### Barème du CDC V2 (5 pts + 2 bonus, plafonné à 5)

| Critère | Pts |
|---|---|
| Remarques de la V1 (structure, rédaction) **prises en compte** | 2 (bonus) |
| **Compte-rendu de la réunion 1** intégré, **détaillé mais synthétique** | 2 |
| **Prochain livrable** suffisamment explicité | 2 |
| **Demandes du client** (réunion 1) clairement prises en compte pour le prochain livrable | 1 |

**Note globale CDC = min(25, rendu 1 + rendu 2)**, qui compte pour 25 % de la note finale.

### Forme
- **PDF** obligatoire, non modifiable. Générer via **LaTeX**, **Markdown → PDF**, ou **LibreOffice** (OK).
- ❌ **Canvas n'est pas accepté** (pas un traitement de texte).
- Langue acceptée par les deux parties ; rédaction claire et détaillée, sans excès.

---

## 6. Rédiger la partie « Livrables » (6 points)

Le barème va de 0 pt (« simple mention d'une V1 ») à **6 pts : gameplay complet, cas particuliers explicités, illustré de maquettes**.

### À faire
- Approche **côté utilisateur** : « l'utilisateur fait ceci, le programme fait/affiche cela ».
- Détailler **les interactions** : saisies, messages, affichages, clics.
- Joindre des **maquettes** : dessins de chaque écran important, faits **avant** de coder (papier/crayon puis photo, ou logiciel). Ce ne sont **pas** des captures d'écran.
- Expliciter **les cas particuliers**.
- Rester réaliste : ni trop ambitieux, ni trop peu (client déçu).

### Livrable V1 minimal suggéré
- **Édition du plateau** (1ʳᵉ phase du jeu) plus ou moins aboutie, avec **visualisation de la grille de cartes** (et des piles).
- Interface directement en **fltk** (le mode console est possible mais déconseillé).
- ⚠️ Cela ne suffira **pas** pour le programme final.

### Écrans à maquetter (idées)
1. Menu d'accueil (nouvelle partie, nb de joueurs, nb de vies).
2. Choix du nombre de couleurs / création des piles.
3. Écran d'édition de la grille (placer les cartes, chats, souris).
4. Écran de validation (contraintes respectées ou message d'erreur).
5. Écran de défi (grille face cachée, chat et souris initiaux dévoilés, vies, jetons).
6. Écran d'annonce d'une carte (chat / souris / vide) + retournement.
7. Écran de fin de défi (gagné/perdu) + scores.

### Cas particuliers à expliciter
- Nombre de cartes ≠ (nombre de couleurs)² → refusé.
- Deux chats (ou deux souris) sur la même ligne/colonne → refusé, message clair.
- Chat et souris de même couleur adjacents (diagonales incluses) → refusé.
- Carte déjà retournée re-sélectionnée.
- Annonce erronée → perte d'une vie, la carte est retournée quand même.
- Vies à 0 → défi perdu ; tous les chats/souris trouvés → défi gagné.
- Nombre minimum/maximum de joueurs, de couleurs, de vies.
- Calcul des scores selon victoire/défaite, rotation du créateur de défi.
- Pose/retrait de jetons sur cartes non retournées (plusieurs jetons possibles, sans effet sur le défi).
- Fermeture de la fenêtre en cours de partie.

---

## 7. Questions utiles à poser au client (réunion 1)

À préparer, car les points flous des règles doivent être tranchés et consignés dans le CR de réunion (V2) :

- Taille de grille : toujours carrée ? « plus ou moins complète » → cases vides autorisées ?
- Nombre de couleurs min/max ? Quelles couleurs ?
- Nombre de vies : libre ou bornes ? Nombre de joueurs max ?
- Le créateur choisit-il lui-même les emplacements ou génération aléatoire possible ?
- Le jeu doit-il détecter/refuser automatiquement les grilles invalides ?
- Sauvegarde/chargement de grilles ? Historique des scores ?
- Les jetons : fonctionnalité obligatoire ou bonus ?
- Plusieurs manches : combien, comment le gagnant final est-il désigné ?
- Préférences d'interface (couleurs, images chat/souris, sons) ?
- Licence souhaitée pour le code ?

---

## 8. Checklist avant de rendre le CDC V1 (avant le 15/11 23:59)

- [ ] Fichier **PDF** (pas Canvas, pas .docx)
- [ ] Page de garde + sommaire + titres/sous-titres + **numéros de page**
- [ ] Orthographe/grammaire relues (relecture croisée par un 2ᵉ membre)
- [ ] Contexte : client + besoin
- [ ] Équipe : nom, prénom, rôle × 3 + organisation
- [ ] Technologies **de fonctionnement** uniquement + **licence** justifiée
- [ ] Planning : réunion 1, réunion 2, livraison finale (date approx., ordre du jour, livrable, bilan)
- [ ] Livrable V1 : gameplay détaillé + **maquettes** + cas particuliers
- [ ] 1 mention de : budget **ou** idées d'amélioration **ou** données/RGPD (idéalement les trois)
- [ ] Déposé sur e-learning **avec marge** (10 min de retard = -1 pt)
- [ ] Équipe déclarée sur e-learning, **RDV client pris**, début du dev lancé (démo V1 attendue à la réunion 1)

---

## 9. Après le CDC : ce qui vous attend

- **Réunion 1** (23–27/11) : tous présents, démo V1, retours sur le CDC.
- **CDC V2** (avant 04/12) : intégrer **compte-rendu** de la réunion 1 + nouveau livrable détaillé + prise en compte des demandes client + corrections des remarques V1.
- **Réunion 2** (07–11/12) : démo V2, dernières demandes.
- **Rapport final** (+ CDC final intégré ou annexé) et **programme** : avant le **02/01 à 23:59**.
- **Soutenance de groupe** (04–08/01), notée **individuellement** (55 pts) : le programme est évalué selon le **CDC final** ; chacun doit maîtriser son code.

---

## 10. Liens utiles (du CM1)

- Cours e-learning « Projet Informatique 1 – 26-27 » : https://elearning.univ-eiffel.fr/course/view.php?id=17803
- Discord (annonces, discussions, Q&R) : https://discord.gg/aBUjhHYTQ
