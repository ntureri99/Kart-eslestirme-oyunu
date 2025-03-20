import pygame
import random
import time

pygame.init()

# Oyun ekranı ayarları
WIDTH, HEIGHT = 800, 600
CARD_SIZE = (100, 150)
GRID_COLS, GRID_ROWS = 4, 4
PADDING = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Kart Eşleştirme Oyunu")

# Renkler ve kart arkası
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)

# Kartları oluşturma
symbols = [i for i in range((GRID_COLS * GRID_ROWS) // 2)] * 2
random.shuffle(symbols)
cards = []
for row in range(GRID_ROWS):
    for col in range(GRID_COLS):
        rect = pygame.Rect(
            col * (CARD_SIZE[0] + PADDING) + PADDING,
            row * (CARD_SIZE[1] + PADDING) + PADDING,
            CARD_SIZE[0], CARD_SIZE[1],
        )
        cards.append({"rect": rect, "symbol": symbols.pop(), "revealed": False})

# Oyun döngüsü değişkenleri
running = True
selected_cards = []
matched_pairs = 0
font = pygame.font.Font(None, 50)

def draw_cards():
    screen.fill(WHITE)
    for card in cards:
        if card["revealed"]:
            pygame.draw.rect(screen, WHITE, card["rect"])
            text = font.render(str(card["symbol"]), True, (0, 0, 0))
            screen.blit(text, (card["rect"].x + 35, card["rect"].y + 50))
        else:
            pygame.draw.rect(screen, BLUE, card["rect"])
    pygame.display.flip()

while running:
    draw_cards()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for card in cards:
                if card["rect"].collidepoint(event.pos) and not card["revealed"]:
                    card["revealed"] = True
                    selected_cards.append(card)
                    if len(selected_cards) == 2:
                        if selected_cards[0]["symbol"] == selected_cards[1]["symbol"]:
                            matched_pairs += 1
                        else:
                            pygame.display.flip()
                            time.sleep(1)
                            selected_cards[0]["revealed"] = False
                            selected_cards[1]["revealed"] = False
                        selected_cards = []
    if matched_pairs == (GRID_COLS * GRID_ROWS) // 2:
        print("Tebrikler! Tüm kartları eşleştirdiniz!")
        running = False
    pygame.time.delay(100)

pygame.quit()