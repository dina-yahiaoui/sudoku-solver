Bienvenue dans notre Sudoku Solver !!!
Ce projet a pour but de créer un algorithme qui résout les sudoku.
Pour ce faire, on peut utiliser 2 méthodes: -> la force brute
                                            -> le backtracking 
                                            
Dans un premier temps faut comprendre le concepte des 2 méthodes : 

1. Méthode de la Force Brute
  Principe: La force brute consiste à essayer toutes les combinaisons possibles de chiffres pour remplir la grille jusqu'à ce que la solution correcte soit     
trouvée. Cette méthode ne fait pas de vérification intelligente des solutions, mais teste simplement toutes les possibilités.
  Avantage: C'est une méthode très simple à implémenter.
  Inconvénient: La méthode est extrêmement inefficace car elle teste toutes les combinaisons possibles, ce qui conduit à une complexité exponentielle. Pour une 
grille 9x9, le nombre de combinaisons possibles est énorme, ce qui rend cette méthode très lente.
  Complexité de la force brute: La complexité de la méthode de force brute pour un Sudoku de taille 9×9 (n = 9) est approximativement O(9n²). Cela signifie qu'à 
chaque étape, l'algorithme pourrait essayer jusqu'à 9 chiffres pour chaque case vide, et pour une grille de 81 cases, cela mène à un nombre de tentatives très 
élevé.

2. Méthode du Backtracking
  Principe: Le backtracking est une méthode plus intelligente et plus efficace que la force brute. Elle repose sur l'idée d'explorer les solutions possibles de 
manière récursive, tout en revenant en arrière dès qu'une solution partielle est invalide. L'idée est de remplir progressivement la grille, et si à un moment 
donné, une configuration ne peut pas mener à une solution valide, on revient en arrière (d'où le terme "backtracking") et on essaie une autre option.
  Avantage: Le backtracking est plus efficace que la force brute. Il permet de réduire l'espace de recherche en abandonnant des solutions qui mènent à des 
contradictions dès que possible. Cela rend le programme plus rapide. Il est beaucoup plus rapide que la force brute pour des grilles de Sudoku complexes.
  Inconvénient: Il peut être plus complexe à implémenter que la force brute, car il nécessite de gérer la récursivité et de revenir en arrière.
  Complexité du Backtracking: La complexité du backtracking pour un Sudoku classique est plus difficile à évaluer de manière précise, mais elle est généralement 
bien meilleure que la force brute. En moyenne, la complexité peut être approximée par O(n!), où 𝑛 est le nombre de cases vides dans la grille. Cela signifie que 
l'algorithme explore moins d'options et revient plus tôt lorsqu'il rencontre des conflits.
