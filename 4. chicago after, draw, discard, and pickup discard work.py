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
# text = smallfont.render('Quit', True, color)

image1 = pygame.image.load(r'H:\Python\images\rules_main.png')
rules_img = r'H:\Python\images\rules_main.png'

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


player = 0
turn = 0
player_number = "player {}".format(player)


def change_player():
    global player
    global turn

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
    player_number = "player {}".format(temp_player_number)
    # print(player_number)
    text2 = font.render(str(player_number), True, green)

    textRect = text2.get_rect()
    # textRect.center = (X // 2, Y // 2)
    textRect.x = 1625
    textRect.y = 150
    screen.blit(text2, textRect)


def display_cards():
    # player card being put onto the screen
    u = 0
    x_deg = -75
    while u < len(player_hand[player]):
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
        cur_card = pygame.transform.scale(cur_card, (80, 140))
        x_deg = x_deg + 100
        screen.blit(cur_card, (x_deg, 875))
        u += 1


end_turn_button = button((0, 255, 0), 1625, 225, 275, 50,
                         "Change Player")  # code taken from https://www.youtube.com/watch?v=4_9twnEduFA

sort_suite_type_button = button((0, 255, 0), 1625, 300, 275, 50, "Sort by Suite Type")

sort_value_button = button((0, 255, 0), 1625, 375, 275, 50, "Sort by Value")

quit_game_button = button((0, 255, 0), 1625, 450, 275, 50, "Quit Game")

discard_button = button((0, 255, 0), 1625, 525, 275, 50, "Discard Card")

draw_card_button = button((0, 255, 0), 1625, 600, 275, 50, "Draw Card")

pickup_from_discard_button = button((0, 255, 0), 1625, 675, 275, 50, "Pick Discard Card")

swap_card = [None, None]
swap_button = []
multi_use_button = []
player_card_range = 0


def swap_card_function():
    h = 0
    press_button = False
    # print("player up ", player)
    global swap_card
    # print("Swap ", len(player_hand[player]))
    global player_card_range
    player_card_range = len(player_hand[player])
    # print("player card range: ", player_card_range)
    while h < player_card_range:
        if swap_button[h].isOver(pos):
            swap_button[h].color = (255, 0, 0)
            if swap_card[0] is None and player_hand[player][h] is not None:
                swap_card[0] = h
                swap_button[h].color = (255, 0, 0)
                # print("hello there ", h)
            else:
                swap_card[1] = h
                swap_button[h].color = (255, 0, 0)
                # print("hello there my boi", h)

            if (swap_card[0] or swap_card[0] == 0) and swap_card[1] is not None:
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
            swap_button[h].color = (0, 255, 0)
            h += 1
        press_button = False


discard_pile = []


# u = 0
# for u in range(7):
#     discard_current = random.choice(deck)
#     discard_pile.append(discard_current)
#     # print("discard card: ", discard_pile)
#     deck.remove(discard_current)
#     u += 1


def display_discard_pile():
    global discard_pile
    lop = 0
    # x_deg = 100        for showing all cards
    x_deg = 150  # for showing only one card
    while lop < len(discard_pile):
        discard_current = discard_pile[lop]
        disc_current = pygame.image.load(
            r'H:\Python\images\cards/' + discard_current.value + discard_current.suit_type[0] + '.png')

        # Scale the loaded card image
        # x_deg += 50 for showing all cards
        disc_current = pygame.transform.scale(disc_current, (100, 160))
        screen.blit(disc_current, (x_deg, 50))
        lop += 1


def remove_card(h):
    discard_pile.append(player_hand[player][h])
    player_hand[player].pop(h)


swap_x_coord = 335
swap_button_number = 1


def pickup_from_discard():
    global player_hand
    if (len(player_hand[player]) % 2) != 0:
        if len(discard_pile) != 0:
            temp_card = discard_pile.pop()
            player_hand[player].append(temp_card)
    else:
        pickup_from_discard_button.color = (255, 0, 0)

def build_swap_buttons():
    global swap_x_coord
    swap_x_coord = 45
    global swap_button_number
    swap_button_number = 1
    global swap_button
    temp_y = 0
    player_card_range = len(player_hand[player])
    # print("build swap function: ", player_card_range)

    # for temp_y in range(len(player_hand[player])):
    while temp_y < 18:
        swap_button.append(button((0, 255, 0), swap_x_coord, 1025, 40, 40, swap_button_number.__str__()))
        swap_x_coord += 100
        swap_button_number += 1
        temp_y += 1
        # print(swap_x_coord)
        # print("temp y ", temp_y)
    # print(swap_button_number)


def display_swap_buttons():
    # print(len(player_hand[player]))
    g = 0
    player_card_range = len(player_hand[player])
    # print("display swap function: ", player_card_range)
    while g < player_card_range:
        swap_button[g].draw(screen, (0, 0, 0))
        # print(g)
        g += 1
    player_card_range = len(player_hand[player]) - 1


def build_multi_button():
    swap_x_coord = 45
    global swap_button_number
    swap_button_number = 1
    global multi_use_button
    temp_y = 0
    player_card_range = len(player_hand[player])
    # print("build swap function: ", player_card_range)

    # for temp_y in range(len(player_hand[player])):
    while temp_y < 18:
        multi_use_button.append(button((0, 255, 0), swap_x_coord, 825, 40, 40, swap_button_number.__str__()))
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
    h = 0
    press_button = False
    # print("player up ", player)
    global multi_use_button
    # print("Swap ", len(player_hand[player]))
    global player_card_range
    player_card_range = len(player_hand[player])
    # print("player card range: ", player_card_range)

    while h < player_card_range:
        if multi_use_button[h].isOver(pos):
            if (len(player_hand[player]) % 2) == 0:
                multi_use_button[h].color = (255, 0, 0)

                # if multi_use_button[0] is None and player_hand[player][h] is not None:
                remove_card(h)
                global disc
                disc = False
                press_button = True
                # print("hello there boi", h)

            h = 21

        else:
            h += 1

    if press_button:
        h = 0
        while h < player_card_range:
            multi_use_button[h].color = (0, 255, 0)
            h += 1
        press_button = False


def draw_card():
    global player_hand
    if (len(player_hand[player]) % 2) != 0:
        new_card = random.choice(deck)
        player_hand[player].append(new_card)
        draw_card_button.color = (255, 0, 0)

    else:
        pass
    # swap_x_coord += 110
    # swap_button.append(button((0, 255, 0), swap_x_coord, 1000, 50, 50, swap_button_number.__str__()))
    # print(player_hand[player])


build_swap_buttons()
build_multi_button()
main_menu()

p = 0
run_build_swap = False
if __name__ == '__main__':
    disc = False
    while True:

        menu.mainloop(screen)

        pos = pygame.mouse.get_pos()
        screen.fill((60, 25, 60))
        player_turn_display()

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

        for ev in pygame.event.get():

            if ev.type == pygame.QUIT:  # lets you quit via the red x in top right corner
                pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # changes player
                if end_turn_button.isOver(pos):
                    change_player()

            if ev.type == pygame.MOUSEBUTTONDOWN:  # suite type
                if sort_suite_type_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('suit_type'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # value
                if sort_value_button.isOver(pos):
                    player_hand[player].sort(key=operator.attrgetter('value'))

            if ev.type == pygame.MOUSEBUTTONDOWN:  # swap cards
                swap_card_function()
                # print("gi")
                # run_build_swap = True

            if ev.type == pygame.MOUSEBUTTONDOWN:  # quit game
                if quit_game_button.isOver(pos):
                    pygame.quit()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if discard_button.isOver(pos):
                    discard_button.color = (0, 0, 255)
                    disc = True
                    # multi_button_function()
                    pass
                    # remove_card()

            if ev.type == pygame.MOUSEBUTTONDOWN and disc == True:
                multi_button_function()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if draw_card_button.isOver(pos):
                    draw_card()
                    build_swap_buttons()
                    build_multi_button()
                    # display_swap_buttons()

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if pickup_from_discard_button.isOver(pos):
                    pickup_from_discard()
                    pass

        menu.mainloop(screen)
        end_turn_button.draw(screen, (0, 0, 0))
        sort_suite_type_button.draw(screen, (0, 0, 0))
        sort_value_button.draw(screen, (0, 0, 0))
        quit_game_button.draw(screen, (0, 0, 0))
        discard_button.draw(screen, (0, 0, 0))
        draw_card_button.draw(screen, (0, 0, 0))
        pickup_from_discard_button.draw(screen, (0, 0, 0))

        # fills the screen with a color

        # stores the (x,y) coordinates into
        # the variable as a tuple
        mouse = pygame.mouse.get_pos()

        display_cards()
        display_swap_buttons()
        display_multi_button()

        if run_build_swap == True:
            h = 0
            while h < player_card_range:
                swap_button[h].color = (0, 255, 0)
                h += 1
            run_build_swap = False

        display_card_img = pygame.image.load(r'H:\Python\images\cards\red_back.png')
        display_card_img = pygame.transform.scale(display_card_img, (100, 160))
        screen.blit(display_card_img, (50, 50))

        display_discard_pile()

        color = pygame.Color(255, 255, 255)
        pygame.draw.line(screen, color, (5, 40), (0, 25), 20000)

        # updates the frames of the game
        pygame.display.update()
