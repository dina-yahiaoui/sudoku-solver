import os
import time
from sudoku_solver import SudokuGrid
from interface import launch_interface

def main():
    print("🧩 Résolution de Sudoku")
    print("Choisissez une grille parmi :")
    for i in range(1, 6):
        print(f"{i} - Grille {i}")

    choix = input("Entrez le numéro de la grille (1 à 5) : ")
    while choix not in ["1", "2", "3", "4", "5"]:
        choix = input("Numéro invalide. Entrez un numéro entre 1 et 5 : ")

    file_path = os.path.join("examples", f"grille{choix}.txt")

    print("\nMéthode de résolution :")
    print("1 - Backtracking")
    print("2 - Force brute")

    method = input("Entrez le numéro de la méthode : ")
    while method not in ["1", "2"]:
        method = input("Numéro invalide. Choisissez 1 ou 2 : ")

    sudoku = SudokuGrid()
    sudoku.from_file(file_path)

    print("\n⏳ Résolution en cours...\n")

    start = time.time()
    solved = False

    if method == "1":
        solved = sudoku.solve_backtracking()
        method_name = "Backtracking"
    elif method == "2":
        solved = sudoku.solve_brute_force()
        method_name = "Force brute"
    
    end = time.time()
    elapsed = end - start

    if solved:
        print(f"\n✅ Grille résolue avec {method_name} :\n")
        sudoku.display()
        print(f"\n🕒 Temps {method_name.lower()} : {elapsed:.6f} secondes")
    else:
        print(f"\n❌ Résolution impossible avec {method_name}")
        print(f"\n🕒 Temps écoulé : {elapsed:.6f} secondes")

    # Affichage dans l'interface graphique
    launch_interface(sudoku, elapsed, method_name, solved)


if __name__ == "__main__":
    main()