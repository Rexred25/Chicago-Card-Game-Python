import pygame
import sys
import pygame_menu
import random
import io
import operator


# Card class definition
class Card:
    def __init__(self, suit_type, value):
        self.suit_type = suit_type
        self.value = value
        # self.order = order

    def __repr__(self):
        return str(self.value)


# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]

# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "R"]

# The card value
cards_values = {"A": 15, "2": 5, "3": 5, "4": 5, "5": 5, "6": 5, "7": 5, "8": 5, "9": 5, "10": 10, "J": 10, "Q": 10,
                "K": 10, "R": 50}

# ordering of cards
# cards_ascending = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12,
#                    "K": 13, "R": 14}

cards_ascending = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "R"]

# print(cards_ascending['A'])
# The deck of cards - List of Objects
deck = []

# Loop for every type of suit
for suit in suits:

    # Loop for every type of card in a suit
    for card in cards:
        # Adding the card to the deck
        deck.append(Card(suit, card))
        deck.append(Card(suit, card))

deck.pop(111)
deck.pop(110)
deck.pop(83)
deck.pop(82)

rows, cols = (3, 11)
player_hand = [[0 for i in range(cols)] for j in range(rows)]
o = 0

k = 0
while k < 11:
    for o in range(3):
        current_card = random.choice(deck)
        player_hand[o][k] = current_card
        deck.remove(current_card)
        # print("player", o, "current card ", current_card, "position value ", k)
    k += 1

# print(player_hand)

# initializing the constructor
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

res = (1920, 1080)  # screen resolution

screen = pygame.display.set_mode(res)  # opens up a window

pygame.display.set_caption('Chicago')  # sets caption for the screen

color = (255, 255, 255)  # white color

color_light = (170, 170, 170)  # light shade of the button

color_dark = (100, 100, 100)  # dark shade of the button

width = screen.get_width()  # stores the width of the screen into a variable

height = screen.get_height()  # stores the height of the screen into a variable

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
#text = smallfont.render('Quit', True, color)

image1 = pygame.image.load(r'H:\Python\images\rules_main.png')
rules_img = (r'H:\Python\images\rules_main.png')

menu = pygame_menu.Menu(1000, 1000, 'Chicago',
                        theme=pygame_menu.themes.THEME_BLUE)


class player:
    def __init__(self, name, score):
        self.name = name
        self.score = score


def start_the_game():
    # Do the job here !
    menu.disable()


def game_rules():
    # adds an image
    screen.blit(image1, (440, 0))


def about():
    about_menu = pygame_menu.Menu(1000, 1000, 'Rules', theme=pygame_menu.themes.THEME_BLUE)
    about_menu.add_image(rules_img, angle=0, image_id='', scale=(1, 1), scale_smooth=False, selectable=False)
    return about_menu


def main_menu():
    about_menu = about()
    menu.add_button('Play', start_the_game)
    menu.add_button(about_menu.get_title(), about_menu)  # Open a sub-menu
    menu.add_button('Quit', pygame_menu.events.EXIT)


class button():  # code taken from online https://www.youtube.com/watch?v=4_9twnEduFA
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


player = 0
player_number = "player {}".format(player)


def change_player():
    global player
    player += 1
    if player > 2:
        player = 0


def player_turn_display():
    X = 425
    Y = 400
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    temp_player_number = player
    temp_player_number += 1
    player_number = "player {}".format(temp_player_number)
    # print(player_number)
    text2 = font.render(str(player_number), True, green)

    textRect = text2.get_rect()
    textRect.center = (X // 2, Y // 2)
    screen.blit(text2, textRect)


def display_cards():
    # player card being put onto the screen
    u = 0
    x_deg = 200
    while u < 11:
        if player == 0:
            current_card = player_hand[0][u]
            # print("1")
        if player == 1:
            current_card = player_hand[1][u]
            # print("2")
        if player == 2:
            current_card = player_hand[2][u]
            # print("3")
        # current_card = player_1[u]
        # print(current_card)
        # Load the card image
        cur_card = pygame.image.load(
            r'H:\Python\images\cards/' + current_card.value + current_card.suit_type[0] + '.png')

        # Scale the loaded card image
        cur_card = pygame.transform.scale(cur_card, (100, 160))
        x_deg = x_deg + 110
        screen.blit(cur_card, (x_deg, 800))
        u += 1


end_turn_button = button((0, 255, 0), 1625, 225, 275, 50,
                         "Change Player")  # code taken from https://www.youtube.com/watch?v=4_9twnEduFA

sort_suite_type_button = button((0, 255, 0), 1625, 300, 275, 50, "Sort by Suite Type")

sort_value_button = button((0, 255, 0), 1625, 375, 275, 50, "Sort by Value")

quit_game_button = button((0, 255, 0), 1625, 450, 275, 50, "Quit Game")

swap_card = [None, None]
swap_button = []


def build_swap_buttons():
    swap_x_coord = 335
    swap_button_number = 1
    global swap_button
    temp_y = 0

    for temp_y in range(11):
        swap_button.append(button((0, 255, 0), swap_x_coord, 1000, 50, 50, swap_button_number.__str__()))
        swap_x_coord += 110
        swap_button_number += 1


def swap_card_function():
    h = 0
    # print("player up ", player)
    global swap_card
    while h in range(11):
        if swap_button[h].isOver(pos):

            if swap_card[0] is None and player_hand[player][h] is not None:
                swap_card[0] = h
                # print("hello there ", h)
            else:
                swap_card[1] = h
                # print("hello there my boi", h)

            if (swap_card[0] or swap_card[0] == 0) and swap_card[1] is not None:
                # print("hi")
                temp_one = player_hand[player][swap_card[0]]
                player_hand[player][swap_card[0]] = player_hand[player][swap_card[1]]
                player_hand[player][swap_card[1]] = temp_one
                swap_card = [None, None]

            h = 11
        else:
            h += 1


build_swap_buttons()
main_menu()

p = 0
if __name__ == '__main__':
    while True:

        menu.mainloop(screen)

        pos = pygame.mouse.get_pos()
        screen.fill((60, 25, 60))
        player_turn_display()
        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:  #lets you quit via the red x in top right corner
                pygame.quit()

            # checks if a mouse is clicked
            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #
            #     # if the mouse is clicked on the
            #     # button the game is terminated
            #     if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
            #         pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # changes player
                if end_turn_button.isOver(pos):
                    change_player()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # descending order
                if sort_suite_type_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('suit_type'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # descending order
                if sort_value_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('value'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # swap cards
                swap_card_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:   # quit game
                if quit_game_button.isOver(pos):
                    pygame.quit()

        menu.mainloop(screen)
        end_turn_button.draw(screen)
        sort_suite_type_button.draw(screen)
        sort_value_button.draw(screen)
        quit_game_button.draw(screen)

        g = 0
        for g in range(11):
            swap_button[g].draw(screen)

        # fills the screen with a color

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        # if mouse is hovered on a button it
        # changes to lighter shade
        # if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        #     pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])
        #
        # else:
        #     pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
        #screen.blit(text, (width / 2 + 50, height / 2))

        display_cards()
        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (5, 40), (0, 25), 20000)

        # updates the frames of the game
        pygame.display.update()
