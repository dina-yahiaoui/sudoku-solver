import time
from colorama import Fore, Style, init
init(autoreset=True)
from itertools import product
import copy

class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.original_grid = [[0 for _ in range(9)] for _ in range(9)]

    def from_file(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            row = []
            for char in line.strip():
                if char == '_':
                    row.append(0)
                elif char.isdigit():
                    row.append(int(char))
            self.grid[i] = row
            self.original_grid[i] = row.copy()

    def display(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")

                num = self.grid[i][j]
                original = self.original_grid[i][j]

                if num == 0:
                    print(".", end=" ")
                elif num == original:
                    print(Fore.BLUE + str(num), end=" ")
                else:
                    print(Fore.GREEN + str(num), end=" ")
            print()  # nouvelle ligne

    def solve_brute_force(self, time_limit=10): #ajout d'une limite de temps en secondes que l'on peut modifier
        # Enregistrer l'heure de début
        start_time = time.time()

        # Trouver toutes les positions vides
        empty_positions = [(i, j) for i in range(9) for j in range(9) if self.grid[i][j] == 0]

        # Générer toutes les combinaisons possibles de chiffres 1 à 9
        for values in product(range(1, 10), repeat=len(empty_positions)):
            # Vérifier si le temps écoulé dépasse la limite
            if time.time() - start_time > time_limit:
                print(f"⏱️ Limite de temps atteinte après {time_limit} secondes.")
                return False  # Temps écoulé, arrêt de l'algorithme

            test_grid = copy.deepcopy(self.grid)
            for (row, col), val in zip(empty_positions, values):
                test_grid[row][col] = val

            if self.is_full_and_valid(test_grid):
                self.grid = test_grid
                return True

        return False  # Aucune combinaison n’a fonctionné    

    def is_full_and_valid(self, grid):
        # Vérifie lignes, colonnes et blocs
        for i in range(9):
            if not self.is_unique(grid[i]):  # lignes
                return False
            if not self.is_unique([grid[j][i] for j in range(9)]):  # colonnes
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                block = [
                    grid[i][j]
                    for i in range(box_row, box_row + 3)
                    for j in range(box_col, box_col + 3)
                ]
                if not self.is_unique(block):
                    return False

        return True

    def is_unique(self, group):
        nums = [num for num in group if num != 0]
        return len(nums) == len(set(nums))

    def solve_backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, row, col):
                            self.grid[row][col] = num
                            if self.solve_backtracking():
                                return True
                            self.grid[row][col] = 0  # Backtrack
                    return False  # Aucun chiffre possible ici → échec
        return True  # Tout est rempli

    def is_valid(self, num, row, col):
        # Vérifier la ligne
        if num in self.grid[row]:
            return False

        # Vérifier la colonne
        for i in range(9):
            if self.grid[i][col] == num:
                return False

        # Vérifier la sous-grille 3x3
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False

        return True

    def is_complete(self):
        pass
