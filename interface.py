import pygame
import sys

# === Couleurs ===
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 133, 244)
GREEN = (52, 168, 83)

# === Fonction d'affichage de la grille ===
def draw_grid(win, sudoku, top_left_x, top_left_y, label, elapsed_time, font, small_font):
    cell_size = 50

    # Titre
    label_surf = font.render(label, True, BLACK)
    win.blit(label_surf, (top_left_x, top_left_y - 40))

    time_surf = small_font.render(f"Temps : {elapsed_time:.4f} s", True, BLACK)
    win.blit(time_surf, (top_left_x, top_left_y - 15))

    # Grille
    for i in range(10):
        line_width = 3 if i % 3 == 0 else 1
        pygame.draw.line(win, BLACK, (top_left_x, top_left_y + i * cell_size), (top_left_x + 9 * cell_size, top_left_y + i * cell_size), line_width)
        pygame.draw.line(win, BLACK, (top_left_x + i * cell_size, top_left_y), (top_left_x + i * cell_size, top_left_y + 9 * cell_size), line_width)

    # Chiffres
    for i in range(9):
        for j in range(9):
            num = sudoku.grid[i][j]
            if num != 0:
                color = BLUE if sudoku.original_grid[i][j] == num else GREEN
                text = font.render(str(num), True, color)
                text_rect = text.get_rect(center=(top_left_x + j * cell_size + 25, top_left_y + i * cell_size + 25))
                win.blit(text, text_rect)

# === Fonction principale ===
def launch_interface(sudoku_bt, bt_time, sudoku_fb, fb_time, fb_success):
    pygame.init()
    WIDTH, HEIGHT = 1200, 600
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Résolution Sudoku")

    font = pygame.font.SysFont("comicsans", 30)
    small_font = pygame.font.SysFont("comicsans", 24)

    running = True
    while running:
        win.fill(WHITE)

        # Affichage des grilles
        draw_grid(win, sudoku_bt, 80, 100, "Backtracking", bt_time, font, small_font)

        if fb_success:
            draw_grid(win, sudoku_fb, 650, 100, "Force brute", fb_time, font, small_font)
        else:
            error_text = font.render("Force brute : échec", True, (200, 0, 0))
            win.blit(error_text, (700, 150))
            time_text = small_font.render(f"Temps : {fb_time:.4f} s", True, BLACK)
            win.blit(time_text, (700, 190))

        # Fermer la fenêtre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    sys.exit()
