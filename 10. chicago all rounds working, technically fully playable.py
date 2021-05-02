import pygame
import os
import sys
import pygame_menu
import random
import io
import operator
from pygame import FULLSCREEN
from pygame.rect import Rect

clock = pygame.time.Clock()


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

cards_ascending = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "R"]

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


# all variables declared outside

player = 0
turn = 0
player_number = "player {}".format(player)

# dark_green = (0, 138, 7)
grey = (211, 227, 212)
green = (0, 255, 0)
# end_turn_button = button(grey, 1625, 225, 275, 50,
# "Change Player")  # code taken from https://www.youtube.com/watch?v=4_9twnEduFA

build_button = False
y_deg = 100

may_i_button = []

# approve put down buttons

put_down_button = []

validate_card_down_button = []

round_type = [["Set 1", "Set 2", "Null"], ["Run 1", "Run 2", "Null"], ["Set 1", "Set 2", "Run 1"],
              ["Run 1", "Run 2", "Set 1"], ["Set 1", "Set 2", "Set 3"], ["Run 1", "Run 2", "Run 3"]]

confirm_put_down = [False, False, False]
# confirm_put_down = [True, True, True]

player_x_coords = [[25, 75, 125], [550, 600, 650], [1075, 1125, 1175]]
player_y_coords = [[300, 500, 700], [300, 500, 700], [300, 500, 700]]

swap_card = [None, None]
swap_button = []
multi_use_button = []
player_card_range = 0

player_may_i = [3, 3, 3]

discard_pile = []

set_pile = []

player1_hand_put_down = [[], [], []]

player2_hand_put_down = [[], [], []]

player3_hand_put_down = [[], [], []]

player_hand_put_down = [[[], [], []], [[], [], []], [[], [], []]]

build_set = []

put_down_array_counter = 0

confirm_player_put_down = [False, False, False]

swap_x_coord = 335
swap_button_number = 1

player1_put_down = [[], [], []]
player2_put_down = [[], [], []]
player3_put_down = [[], [], []]

may_i_request = 0

p = 0
potato1 = 0
run_build_swap = False
notOver = False

round_counter = 1

# end of variables

# initializing the constructor
pygame.init()

FPS = 144
FramePerSec = pygame.time.Clock()

res = (1920, 1080)  # screen resolution

screen = pygame.display.set_mode(res)  # opens up a window
# screen = pygame.display.set_mode((0, 0), pygame.HWSURFACE | pygame.DOUBLEBUF)  # opens up a window
# game_surface = pygame.Surface((game_height, game_height))

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
# text = smallfont.render('Quit', True, color)

image1 = pygame.image.load(r'H:\Python\images\rules_main.png')
rules_img = r'H:\Python\images\rules_main.png'

wood_background = pygame.image.load(r'H:\Python\images\wood2.jpg').convert()

menu = pygame_menu.Menu(1000, 1000, 'Chicago',
                        theme=pygame_menu.themes.THEME_BLUE)


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


def change_player():
    global player
    global turn
    h = 0
    while h < player_card_range:
        multi_use_button[h].color = (136, 3, 252)
        h += 1
    swap_card = [None, None]

    player += 1
    turn += 1
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
    player_number = "Player {}".format(temp_player_number)
    # print(player_number)
    text2 = font.render(str(player_number), True, green)

    textRect = text2.get_rect()
    # textRect.center = (X // 2, Y // 2)
    textRect.x = 1700
    textRect.y = 50
    screen.blit(text2, textRect)


def round_display():
    X = 100
    Y = 200
    green = (0, 255, 0)
    blue = (0, 0, 128)
    font = pygame.font.Font('freesansbold.ttf', 32)
    round_number = "Round {}".format(round_counter)
    # print(player_number)
    text3 = font.render(str(round_number), True, green)

    textRect2 = text3.get_rect()
    # textRect.center = (X // 2, Y // 2)
    textRect2.x = 1500
    textRect2.y = 50
    screen.blit(text3, textRect2)


def display_cards():
    # player card being put onto the screen
    u = 0
    x_deg = -75
    while u < len(player_hand[player]):
        current_card = player_hand[player][u]
        # Load the card image
        cur_card = pygame.image.load(
            r'H:\Python\images\cards/' + current_card.value + current_card.suit_type[0] + '.png').convert_alpha()

        # Scale the loaded card image
        cur_card = pygame.transform.scale(cur_card, (80, 140))
        x_deg = x_deg + 100
        screen.blit(cur_card, (x_deg, 875))
        u += 1


while not build_button:
    sort_suite_type_button = button(grey, 1625, y_deg, 275, 50, "Sort by Suite Type")
    y_deg += 75

    sort_value_button = button(grey, 1625, y_deg, 275, 50, "Sort by Value")
    y_deg += 75

    quit_game_button = button(grey, 1625, y_deg, 275, 50, "Quit Game")
    y_deg += 75

    discard_button = button(grey, 1625, y_deg, 275, 50, "Discard Card")
    y_deg += 75

    draw_card_button = button(grey, 1625, y_deg, 275, 50, "Draw Card")
    y_deg += 75

    pickup_from_discard_button = button(grey, 1625, y_deg, 275, 50, "Pick Discard Card")
    y_deg += 75

    # swap_card_button = button(grey, 1625, y_deg, 275, 50, "Pick Discard Card22")
    # y_deg += 75

    # may_i_button = button(grey, 1625, y_deg, 275, 50, "May I")
    # y_deg += 75

    p = 1
    may_i_x_deg = 850
    validate_card_x_deg = 700
    while p != 4:
        may_i_button.append(button(grey, may_i_x_deg, 125, 25, 25, p.__str__()))
        validate_card_down_button.append(button(grey, 1775, validate_card_x_deg, 125, 30, "Approve"))
        validate_card_x_deg += 45
        may_i_x_deg += 50
        p += 1

    confirm_put_down_button = button((255, 0, 0), 1625, 835, 110, 30, "Confirm")

    cancel_put_down_button = button(grey, 1775, 835, 110, 30, "Cancel")

    new_may_i_button = button(grey, 875, 60, 75, 50, "May I")  # literal button you press to activate it

    put_down = button(grey, 1625, y_deg, 275, 50, "Put Down")
    y_deg += 75

    next_round_button = button(grey, 1625, y_deg, 275, 50, "Next Round")
    y_deg += 75

    build_button = True

# #round 1
put_down_button.append(button(grey, 1625, 700, 80, 30, round_type[0][0]))
put_down_button.append(button(grey, 1625, 745, 80, 30, round_type[0][1]))
put_down_button.append(button(grey, 1625, 790, 80, 30, round_type[0][2]))




def display_set_player1():
    lop = 0
    x_deg = -25  # for showing only one card
    while lop < len(player1_hand_put_down[0]):
        x_deg += 50  # for showing all cards
        screen.blit(player1_hand_put_down[0][lop], (x_deg, 300))
        lop += 1

    lop = 0
    x_deg = -25  # for showing only one card
    while lop < len(player1_hand_put_down[1]):
        x_deg += 50  # for showing all cards
        screen.blit(player1_hand_put_down[1][lop], (x_deg, 500))
        lop += 1

    lop = 0
    x_deg = -25  # for showing only one card
    while lop < len(player1_hand_put_down[2]):
        x_deg += 50  # for showing all cards
        screen.blit(player1_hand_put_down[2][lop], (x_deg, 700))
        lop += 1


def display_set_player2():
    lop = 0
    x_deg = 500  # for showing only one card
    while lop < len(player2_hand_put_down[0]):
        x_deg += 50  # for showing all cards
        screen.blit(player2_hand_put_down[0][lop], (x_deg, 300))
        lop += 1

    lop = 0
    x_deg = 500  # for showing only one card
    while lop < len(player2_hand_put_down[1]):
        x_deg += 50  # for showing all cards
        screen.blit(player2_hand_put_down[1][lop], (x_deg, 500))
        lop += 1

    lop = 0
    x_deg = 500  # for showing only one card
    while lop < len(player2_hand_put_down[2]):
        x_deg += 50  # for showing all cards
        screen.blit(player2_hand_put_down[2][lop], (x_deg, 700))
        lop += 1


def display_set_player3():
    lop = 0
    x_deg = 1025  # for showing only one card
    while lop < len(player3_hand_put_down[0]):
        x_deg += 50  # for showing all cards
        screen.blit(player3_hand_put_down[0][lop], (x_deg, 300))
        lop += 1

    lop = 0
    x_deg = 1025  # for showing only one card
    while lop < len(player3_hand_put_down[1]):
        x_deg += 50  # for showing all cards
        screen.blit(player3_hand_put_down[1][lop], (x_deg, 500))
        lop += 1

    lop = 0
    x_deg = 1025  # for showing only one card
    while lop < len(player3_hand_put_down[2]):
        x_deg += 50  # for showing all cards
        screen.blit(player3_hand_put_down[2][lop], (x_deg, 700))
        lop += 1


def build_display_set2():
    if player == 0:
        global set_pile
        discard_current = player1_put_down[put_down_array_counter][-1]
        # disc_current = pygame.image.load(
        # r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert()

        player1_hand_put_down[put_down_array_counter].append(pygame.image.load(
            r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert_alpha())

        player1_hand_put_down[put_down_array_counter][-1] = pygame.transform.scale(
            player1_hand_put_down[put_down_array_counter][-1], (80, 140)).convert_alpha()

    if player == 1:
        global set_pile
        discard_current = player2_put_down[put_down_array_counter][-1]
        # disc_current = pygame.image.load(
        # r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert()

        player2_hand_put_down[put_down_array_counter].append(pygame.image.load(
            r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert_alpha())

        player2_hand_put_down[put_down_array_counter][-1] = pygame.transform.scale(
            player2_hand_put_down[put_down_array_counter][-1], (80, 140)).convert_alpha()

    if player == 2:
        global set_pile
        discard_current = player3_put_down[put_down_array_counter][-1]
        # disc_current = pygame.image.load(
        # r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert()

        player3_hand_put_down[put_down_array_counter].append(pygame.image.load(
            r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert_alpha())

        player3_hand_put_down[put_down_array_counter][-1] = pygame.transform.scale(
            player3_hand_put_down[put_down_array_counter][-1], (80, 140)).convert_alpha()


def display_discard_pile():
    global discard_pile
    lop = 0
    # x_deg = 100        for showing all cards
    x_deg = 100  # for showing only one card
    while lop < len(discard_pile):
        discard_current = discard_pile[lop]
        disc_current = pygame.image.load(
            r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png').convert_alpha()

        # Scale the loaded card image
        # x_deg += 50 for showing all cards
        disc_current = pygame.transform.scale(disc_current, (80, 140))
        screen.blit(disc_current, (x_deg, 50))
        lop += 1


def remove_card(h):
    discard_pile.append(player_hand[player][h])
    player_hand[player].pop(h)


def pickup_from_discard():
    global player_hand
    global may_i_request
    if (len(player_hand[player]) % 2) != 0:
        if len(discard_pile) != 0 and may_i_button[may_i_request].color != (255, 0, 0):
            temp_card = discard_pile.pop()
            if new_may_i_button.color == (0, 255, 0):
                player_hand[may_i_request].append(temp_card)
                # print("this works")

            else:
                player_hand[player].append(temp_card)
                # print("failure")
    else:
        pickup_from_discard_button.color = (255, 0, 0)


def build_multi_button():
    # swap_x_coord = 45          #buttons underneath card
    swap_x_coord = 26.5  # buttons behind card
    global swap_button_number
    swap_button_number = 1
    global multi_use_button
    temp_y = 0
    player_card_range = len(player_hand[player])
    # print("build swap function: ", player_card_range)

    # for temp_y in range(len(player_hand[player])):
    while temp_y < 18:
        # multi_use_button.append(button((0, 255, 0), swap_x_coord, 1025, 40, 40, swap_button_number.__str__()))         #buttons underneath card
        multi_use_button.append(
            button((136, 3, 252), swap_x_coord, 880, 75, 135, swap_button_number.__str__()))  # buttons behind card
        swap_x_coord += 100
        swap_button_number += 1
        temp_y += 1
        # print(swap_x_coord)
        # print("temp y ", temp_y)
    # print(swap_button_number)


def display_multi_button():
    # print(len(player_hand[player]))
    g = 0
    player_card_range = len(player_hand[player])
    # print("display swap function: ", player_card_range)
    while g < player_card_range:
        multi_use_button[g].draw(screen, (0, 0, 0))
        # print(g)
        g += 1
    player_card_range = len(player_hand[player]) - 1


def multi_button_function():
    global disc
    global TESTSET
    global swap_bool
    h = 0
    press_button = False
    # print("player up ", player)
    global multi_use_button
    # print("Swap ", len(player_hand[player]))
    global player_card_range
    player_card_range = len(player_hand[player])
    # print("player card range: ", player_card_range)
    if discard_button.color == (255, 0, 0):
        pass
        # print("Hello there")

    if TESTSET == True:
        pass
        global put_down_array_counter
        h = 0
        press_button2 = False
        while h < player_card_range:
            if put_down_button[0].isOver(pos):
                put_down_button[0].color = green
                put_down_array_counter = 0

            if put_down_button[1].isOver(pos):
                put_down_button[1].color = green
                put_down_array_counter = 1

            if put_down_button[2].isOver(pos):
                put_down_button[2].color = green
                put_down_array_counter = 2

            if multi_use_button[h].isOver(pos) and put_down_button[put_down_array_counter].color == green:
                multi_use_button[h].color = (255, 0, 0)
                if player == 0:
                    player1_put_down[put_down_array_counter].append(player_hand[player][h])
                    build_display_set2()

                if player == 1:
                    player2_put_down[put_down_array_counter].append(player_hand[player][h])
                    build_display_set2()

                if player == 2:
                    player3_put_down[put_down_array_counter].append(player_hand[player][h])
                    build_display_set2()

                # set_pile.append(player_hand[player][h])
                # player_hand[player].pop(h)
                # TESTSET = False

                h = 21

            else:

                h += 1

        # if test_button.color == (0, 0, 255):
        #     TESTSET = False

        if press_button:
            h = 0
            while h < player_card_range:
                multi_use_button[h].color = (136, 3, 252)
                h += 1
            press_button = False
            swap_bool == True
            TESTSET = False

    if disc == True:
        # print("hello my guy")
        while h < player_card_range:
            if multi_use_button[h].isOver(pos):
                if (len(player_hand[player]) % 2) == 0:
                    multi_use_button[h].color = (255, 0, 0)

                    # if multi_use_button[0] is None and player_hand[player][h] is not None:
                    remove_card(h)
                    change_player()

                    disc = False
                    press_button = True
                    # print("hello there boi", h)

                h = 21

            else:
                h += 1

        if press_button:
            h = 0
            while h < player_card_range:
                multi_use_button[h].color = (136, 3, 252)
                h += 1
            # press_button = False
    if swap_bool == True:
        # print("heyo poision")
        h = 0
        press_button = False
        # print("player up ", player)
        global swap_card
        # print("Swap ", len(player_hand[player]))
        player_card_range = len(player_hand[player])
        # print("player card range: ", player_card_range)
        while h < player_card_range:
            if multi_use_button[h].isOver(pos):
                multi_use_button[h].color = (255, 0, 0)
                if swap_card[0] is None and player_hand[player][h] is not None and multi_use_button[h].color == (
                255, 0, 0):
                    swap_card[0] = h
                    multi_use_button[h].color = (255, 0, 0)
                    # print("hello there 1551 ", h)
                else:
                    swap_card[1] = h
                    multi_use_button[h].color = (255, 0, 0)
                    # print("hello there my boi", h)

                if (swap_card[0] or swap_card[0] == 0) and swap_card[1] is not None and multi_use_button[h].color == (
                255, 0, 0):
                    # print("hi")
                    # swap_button[h].color = (255, 0, 0)
                    temp_one = player_hand[player][swap_card[0]]
                    player_hand[player][swap_card[0]] = player_hand[player][swap_card[1]]
                    player_hand[player][swap_card[1]] = temp_one
                    swap_card = [None, None]
                    press_button = True

                h = 21

            else:
                h += 1

        if press_button:
            h = 0
            while h < player_card_range:
                multi_use_button[h].color = (136, 3, 252)
                h += 1
            press_button = False


def valid_put_down():
    set_counter = 2  # round 1
    run_counter = 2
    set_valid = False
    set1 = [3, 3, 3]
    run1 = [11, 3, 4]
    h = 1
    j = 1

    x = 1
    while x <= set_counter:
        while j < len(set1):
            c1 = set1[j]
            c2 = set1[j - 1]

            if (c1 != c2) and (c1 != 50) and (c2 != 50):
                h = 1
            else:
                h = 0
            j += 1
        x += 1

    if h == 0:
        print("set success")
    else:
        print("set failure")

    x = 1
    j = 1
    h = 1
    while x <= run_counter:
        while j < len(run1):
            c1 = run1[j]
            c2 = run1[j - 1]
            if c1 != (c2 + 1):
                h = 1
            else:
                h = 0
            j += 1
        x += 1

    if h == 0:
        print("run success")
    else:
        print("run failure")


def draw_card():
    global player_hand
    if (len(player_hand[player]) % 2) != 0:
        new_card = random.choice(deck)
        player_hand[player].append(new_card)
        draw_card_button.color = (255, 0, 0)

    # else:
    #     pass
    # # swap_x_coord += 110
    # # swap_button.append(button((0, 255, 0), swap_x_coord, 1000, 50, 50, swap_button_number.__str__()))
    # # print(player_hand[player])


def may_i_function():
    if len(discard_pile) != 0 and may_i_button[may_i_request].color != (255, 0, 0):
        if player_may_i[may_i_request] != 0:
            pickup_from_discard()
            new_may_i_button.color = grey
            # draw_card()
            global player_hand
            new_card = random.choice(deck)
            player_hand[may_i_request].append(new_card)
            draw_card_button.color = (255, 0, 0)
            player_may_i[may_i_request] -= 1
            pass


def next_round():
    global notOver, player1_hand_put_down, player2_hand_put_down, player3_hand_put_down, deck, suit, card, rows, cols, player_hand, current_card, player_may_i, round_counter
    notOver = False
    player1_hand_put_down = [[], [], []]

    player2_hand_put_down = [[], [], []]

    player3_hand_put_down = [[], [], []]

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

    player_may_i = [3, 3, 3]
    round_counter += 1

    if round_counter == 2:
        # round 2
        put_down_button[0] = (button(grey, 1625, 700, 80, 30, round_type[1][0]))
        put_down_button[1] = (button(grey, 1625, 745, 80, 30, round_type[1][1]))
        put_down_button[2] = (button(grey, 1625, 790, 80, 30, round_type[1][2]))

    if round_counter == 3:
        # round 3
        put_down_button[0] = (button(grey, 1625, 700, 80, 30, round_type[2][0]))
        put_down_button[1] = (button(grey, 1625, 745, 80, 30, round_type[2][1]))
        put_down_button[2] = (button(grey, 1625, 790, 80, 30, round_type[2][2]))

    if round_counter == 4:
        # round 4
        put_down_button[0] = (button(grey, 1625, 700, 80, 30, round_type[3][0]))
        put_down_button[1] = (button(grey, 1625, 745, 80, 30, round_type[3][1]))
        put_down_button[2] = (button(grey, 1625, 790, 80, 30, round_type[3][2]))

    if round_counter == 5:
        # round 5
        put_down_button[0] = (button(grey, 1625, 700, 80, 30, round_type[4][0]))
        put_down_button[1] = (button(grey, 1625, 745, 80, 30, round_type[4][1]))
        put_down_button[2] = (button(grey, 1625, 790, 80, 30, round_type[4][2]))

    if round_counter == 6:
        # round 6
        put_down_button[0] = (button(grey, 1625, 700, 80, 30, round_type[5][0]))
        put_down_button[1] = (button(grey, 1625, 745, 80, 30, round_type[5][1]))
        put_down_button[2] = (button(grey, 1625, 790, 80, 30, round_type[5][2]))

    if round_counter == 7:
        pygame.quit()

while not notOver:
    disc = False
    TESTSET = False
    swap_bool = True
    del_card = False
    build_multi_button()
    main_menu()
    while True:

        menu.mainloop(screen)

        # Copy the text surface to the main surface

        pos = pygame.mouse.get_pos()
        # screen.fill((60, 25, 60))
        screen.blit(wood_background, (0, 0))
        player_turn_display()
        round_display()

        # determining which player cannot may I

        if player == 0:
            may_i_button[0].color = (255, 0, 0)

            may_i_button[1].color = grey
            may_i_button[2].color = grey

        if player == 1:
            may_i_button[1].color = (255, 0, 0)

            may_i_button[0].color = grey
            may_i_button[2].color = grey

        if player == 2:
            may_i_button[2].color = (255, 0, 0)

            may_i_button[0].color = grey
            may_i_button[1].color = grey

        # end

        if (len(player_hand[player]) % 2) != 0:
            draw_card_button.color = (0, 255, 0)
            if len(discard_pile) == 0:
                pickup_from_discard_button.color = (255, 0, 0)
            else:
                pickup_from_discard_button.color = (0, 255, 0)
            discard_button.color = (255, 0, 0)
        else:
            if disc == True:
                discard_button.color = (0, 0, 255)
            else:
                discard_button.color = (0, 255, 0)
            draw_card_button.color = (255, 0, 0)
            pickup_from_discard_button.color = (255, 0, 0)

        # resetting the colors for put down for new player

        if confirm_player_put_down[player] is True and confirm_put_down_button.color == green:
            for i in range(len(put_down_button)):
                put_down_button[i].color = (255, 0, 0)
                validate_card_down_button[i].color = (255, 0, 0)
            confirm_put_down_button.color = (255, 0, 0)
            put_down.color = (255, 0, 0)

        if confirm_player_put_down[player] is False and put_down.color == (255, 0, 0):
            for i in range(len(put_down_button)):
                put_down_button[i].color = grey
                validate_card_down_button[i].color = grey
            confirm_put_down_button.color = (255, 0, 0)
            put_down.color = grey

        # end of resetting the colors

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:  # lets you quit via the red x in top right corner
                notOver = True
                pygame.quit()

            # if ev.type == pygame.MOUSEBUTTONDOWN:  # changes player
            #     if end_turn_button.isOver(pos):
            #         change_player()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # suite type
                if sort_suite_type_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('suit_type'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # value
                if sort_value_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('value'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # swap cards
                # build_player_1_put_down()
                multi_button_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # quit game
                if quit_game_button.isOver(pos):
                    notOver = True
                    pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if discard_button.isOver(pos):
                    discard_button.color = (0, 0, 255)
                    disc = True

            if ev.type == pygame.MOUSEBUTTONDOWN and disc == True:  # discard button does stuff
                multi_button_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if draw_card_button.isOver(pos):
                    draw_card()
                    build_multi_button()
                    # pygame.display.update(draw_card(), build_multi_button())

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pickup_from_discard_button.isOver(pos):
                    pickup_from_discard()

            # if ev.type == pygame.MOUSEBUTTONDOWN:
            #     if may_i_button.isOver(pos):
            #         may_i_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if put_down.isOver(pos):
                    if put_down.color != (255, 0, 0):
                        # build_player_1_put_down()
                        put_down.color = (0, 0, 255)
                        # build_display_set2()
                        TESTSET = True
                        swap_bool = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if next_round_button.isOver(pos):
                    notOver = True
                    next_round()
                # if approve_button.isOver(pos):
                #     del_card = True
                #     TESTSET = False
                #     swap_bool = True
                #     run_build_swap = True

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if new_may_i_button.isOver(pos):
                    if len(discard_pile) != 0:
                        new_may_i_button.color = (0, 255, 0)

            if ev.type == pygame.MOUSEBUTTONDOWN and (new_may_i_button.color == (0, 255, 0)):
                if may_i_button[0].isOver(pos):
                    may_i_request = 0
                    may_i_function()

                if may_i_button[1].isOver(pos):
                    may_i_request = 1
                    may_i_function()

                if may_i_button[2].isOver(pos):
                    may_i_request = 2
                    may_i_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if validate_card_down_button[0].isOver(pos):
                    validate_card_down_button[0].color = green
                    confirm_put_down[0] = True
                    put_down_button[0].color = (255, 0, 0)

                if validate_card_down_button[1].isOver(pos):
                    validate_card_down_button[1].color = green
                    confirm_put_down[1] = True
                    put_down_button[1].color = (255, 0, 0)

                if validate_card_down_button[2].isOver(pos) or put_down_button[2].text == "Null":
                    # print("test")
                    validate_card_down_button[2].color = green
                    confirm_put_down[2] = True
                    put_down_button[2].color = (255, 0, 0)

                    confirm_true = all(ele == True for ele in confirm_put_down)
                    if confirm_true == True:
                        # print("success")
                        confirm_put_down_button.color = green
                        confirm_put_down = [False, False, False]

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if confirm_put_down_button.color == green and confirm_put_down_button.isOver(pos):
                    del_card = True
                    TESTSET = False
                    swap_bool = True
                    run_build_swap = True

                    # build_display_set()
                    display_set_player1()
                    # TESTSET = True
                    # swap_bool = False
                    confirm_put_down_button.color = (255, 0, 0)
                    put_down.color = (255, 0, 0)
                    for i in range(len(put_down_button)):
                        put_down_button[i].color = (255, 0, 0)
                        validate_card_down_button[i].color = (255, 0, 0)
                    confirm_player_put_down[player] = True
                    # TESTSET = False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if cancel_put_down_button.isOver(pos) and confirm_put_down_button.color != (255, 0, 0):
                    if player == 0:
                        player1_hand_put_down = [[], [], []]

                    if player == 1:
                        player2_hand_put_down = [[], [], []]

                    if player == 2:
                        player3_hand_put_down = [[], [], []]

                    confirm_put_down_button.color = (255, 0, 0)
                    h = 0
                    while h < player_card_range:
                        multi_use_button[h].color = (136, 3, 252)
                        h += 1

                    for i in range(len(put_down_button)):
                        put_down_button[i].color = grey
                        validate_card_down_button[i].color = grey
                    TESTSET = False
                    swap_bool = True
                    run_build_swap = True
                    put_down.color = grey

                    display_set_player1()
                    display_set_player2()
                    display_set_player3()
                    # potato1 = 1

        if del_card == True:

            if player == 0:
                for i in player1_put_down[0]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player1_put_down[1]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player1_put_down[2]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

            if player == 1:
                for i in player2_put_down[0]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player2_put_down[1]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player2_put_down[2]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

            if player == 2:
                for i in player3_put_down[0]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player3_put_down[1]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

                for i in player3_put_down[2]:
                    if i in player_hand[player]:
                        player_hand[player].remove(i)

            del_card = False

        # end_turn_button.draw(screen, (0, 0, 0))
        sort_suite_type_button.draw(screen, (0, 0, 0))
        sort_value_button.draw(screen, (0, 0, 0))
        quit_game_button.draw(screen, (0, 0, 0))
        discard_button.draw(screen, (0, 0, 0))
        draw_card_button.draw(screen, (0, 0, 0))
        pickup_from_discard_button.draw(screen, (0, 0, 0))
        # may_i_button.draw(screen, (0, 0, 0))
        put_down.draw(screen, (0, 0, 0))
        next_round_button.draw(screen, (0, 0, 0))

        # building may i button area

        orange = (237, 98, 5)
        pygame.draw.rect(screen, orange, (843, 55, 140, 100))

        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(843, 55, 140, 100), 2)

        may_i_button[0].draw(screen, (0, 0, 0))
        may_i_button[1].draw(screen, (0, 0, 0))
        may_i_button[2].draw(screen, (0, 0, 0))

        new_may_i_button.draw(screen, (0, 0, 0))

        # end of building may i button area

        # building of the put down button area

        for i in range(len(put_down_button)):
            put_down_button[i].draw(screen, (0, 0, 0))
            validate_card_down_button[i].draw(screen, (0, 0, 0))

        confirm_put_down_button.draw(screen, (0, 0, 0))
        cancel_put_down_button.draw(screen, (0, 0, 0))

        # end of building put down button area

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        display_multi_button()
        display_cards()

        if run_build_swap == True:
            h = 0
            while h < player_card_range:
                multi_use_button[h].color = (136, 3, 252)
                h += 1
            # pygame.display.update(multi_use_button)
            run_build_swap = False

        display_card_img = pygame.image.load(r'H:\Python\images\cards\red_back.png')
        display_card_img = pygame.transform.scale(display_card_img, (80, 140))
        screen.blit(display_card_img, (10, 50))

        display_discard_pile()

        potato1 = 1
        if potato1 == 1:
            # print("run")
            display_set_player1()
            display_set_player2()
            display_set_player3()
            potato1 = 2

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (5, 40), (0, 25), 20000)

        # updates the frames of the game
        pygame.display.update()
        clock.tick(144)
