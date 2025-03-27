import os
import time
from sudoku_solver import SudokuGrid
from interface import launch_interface

def main():
    print("🧩 Résolution de Sudoku")
    print("Choisissez une grille parmi :")
    print("1 - Grille 1")
    print("2 - Grille 2")
    print("3 - Grille 3")
    print("4 - Grille 4")
    print("5 - Grille 5")

    choix = input("Entrez le numéro de la grille (1 à 5) : ")
    while choix not in ["1", "2", "3", "4", "5"]:
        choix = input("Numéro invalide. Entrez un numéro entre 1 et 5 : ")

    file_path = os.path.join("examples", f"grille{choix}.txt")

    # === Backtracking ===
    sudoku_bt = SudokuGrid()
    sudoku_bt.from_file(file_path)

    start_bt = time.time()
    sudoku_bt.solve_backtracking()
    end_bt = time.time()
    bt_time = end_bt - start_bt

    print("\n✅ Grille résolue avec backtracking :\n")
    sudoku_bt.display()
    print(f"\n🕒 Temps backtracking : {bt_time:.6f} secondes")

    # === Force brute ===
    sudoku_fb = SudokuGrid()
    sudoku_fb.from_file(file_path)

    start_fb = time.time()
    solved = sudoku_fb.solve_brute_force()
    end_fb = time.time()
    fb_time = end_fb - start_fb

    if solved:
        print("\n✅ Grille résolue avec force brute :\n")
        sudoku_fb.display()
        print(f"\n🕒 Temps force brute : {fb_time:.6f} secondes")
    else:
        print("\n❌ Force brute : trop de cases vides ou échec.")
        print(f"\n🕒 Temps force brute : {fb_time:.6f} secondes")

    # === Comparaison ===
    print("\n📊 Comparatif de performance :")
    if solved and bt_time < fb_time:
        print("➡️  Le backtracking est plus rapide.")
    elif solved and fb_time < bt_time:
        print("➡️  La force brute est plus rapide.")
    else:
        print("➡️  La force brute a échoué ou temps équivalent.")

    # === Affichage graphique ===
    launch_interface(sudoku_bt, bt_time, sudoku_fb, fb_time, solved)

if __name__ == "__main__":
    main()
