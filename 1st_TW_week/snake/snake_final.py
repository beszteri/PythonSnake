import curses
from termcolor import colored, cprint
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint  # koordináták miatt
import os  # clear parancs miatt
import pickle
from operator import itemgetter

points = 0  # Variable that defines the default score
name = " "


def cool_Snake():   # falon átmenős kigyó

    win = curses.initscr()  # Initializing curses module
    win = curses.newwin(24, 80, 0, 0)  # Defines the size of the window
    win.keypad(True)  # Allows to use special keys with curses

    curses.noecho()  # Allows the app to react to keys instantly (without pressing enter)
    curses.curs_set(False)  # Turns off the blinking cursor

    key = KEY_RIGHT  # Variable that refers to the key pressed

    food = [10, 20]  # Where the first food appears
    snake = [[4, 10], [4, 9], [4, 8]]  # Starting point of the snake
    # Places the FIRST food, and gives a symbol
    win.addch(food[0], food[1], snake_food)
    valid_keys = [
        KEY_LEFT,
        KEY_RIGHT,
        KEY_UP,
        KEY_DOWN,
        27]  # List of valid keys

    while key != 27:  # The loop goes on until ESC is pressed
        global points
        win.border()  # Draws the borderline for the game area
        # Prints the points on the border area
        win.addstr(23, 35, ' Points: ' + str(points) + ' ')
        win.addstr(0, 34, ' COOL Snake ')  # Prints the name of the ontop

        win.timeout(int((150 - (len(snake) / 5 + len(snake) / 10) % 120)))

        prevKey = key  # Variable that refers to the last key pressed

        x = win.getch()
        key = key if x == -1 else x

        if key not in valid_keys:  # Only valid keys can be pressed
            key = prevKey

        if key == KEY_LEFT:
            valid_keys = [KEY_LEFT, KEY_UP, KEY_DOWN, 27]
        elif key == KEY_RIGHT:
            valid_keys = [KEY_RIGHT, KEY_UP, KEY_DOWN, 27]
        elif key == KEY_UP:
            valid_keys = [KEY_LEFT, KEY_UP, KEY_RIGHT, 27]
        elif key == KEY_DOWN:
            valid_keys = [KEY_LEFT, KEY_RIGHT, KEY_DOWN, 27]

        snake.insert(0, [snake[0][0] +
                         (key == KEY_DOWN and 1) +
                         (key == KEY_UP and -
                          1), snake[0][1] +
                         (key == KEY_LEFT and -
                          1) +
                         (key == KEY_RIGHT and 1)])

        if snake[0][0] == 0:
            snake[0][0] = 22
        if snake[0][1] == 0:
            snake[0][1] = 78
        if snake[0][0] == 23:
            snake[0][0] = 1
        if snake[0][1] == 79:
            snake[0][1] = 1  # Snake reaches the wall and enters on the other side

        if snake[0] in snake[1:]:
            break  # In case snake eats itself, app terminates

        if snake[0] == food:  # The snake eats the food

            food = []
            points = points + 1

            while food == []:
                food = [randint(1, 22), randint(1, 78)]
                if food in snake:
                    food = []

            win.addch(food[0], food[1], snake_food)
        else:
            # [1] If it does not eat the food, length decreases
            last = snake.pop()
            win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], '0')

    curses.endwin()


def classic_Snake():  # falba ütköző kígyó

    win = curses.initscr()  # Initializing curses module
    win = curses.newwin(24, 80, 0, 0)  # Defines the size of the window
    win.border()
    win.keypad(True)  # Allows to use special keys with curses

    curses.noecho()  # Allows the app to react to keys instantly (without pressing enter)
    curses.curs_set(False)  # Turns off the blinking cursor

    key = KEY_RIGHT  # Variable that refers to the key pressed

    food = [10, 20]  # Where the first food appears
    snake = [[4, 10], [4, 9], [4, 8]]  # Starting point of the snake
    # Places the FIRST food, and gives a symbol
    win.addch(food[0], food[1], snake_food)
    valid_keys = [
        KEY_LEFT,
        KEY_RIGHT,
        KEY_UP,
        KEY_DOWN,
        27]  # List of valid keys

    while key != 27:  # The loop goes on until ESC is pressed
        global points
        win.border()  # Draws the borderline for the game area
        # Prints the points on the border area
        win.addstr(23, 35, ' Points: ' + str(points) + ' ')
        win.addstr(0, 33, ' CLASSIC SNAKE ')  # Prints the name of the ontop

        win.timeout(int((150 - (len(snake) / 5 + len(snake) / 10) % 120)))

        prevKey = key  # Variable that refers to the last key pressed

        if key == KEY_LEFT:
            valid_keys = [KEY_LEFT, KEY_UP, KEY_DOWN, 27]
        elif key == KEY_RIGHT:
            valid_keys = [KEY_RIGHT, KEY_UP, KEY_DOWN, 27]
        elif key == KEY_UP:
            valid_keys = [KEY_LEFT, KEY_UP, KEY_RIGHT, 27]
        elif key == KEY_DOWN:
            valid_keys = [KEY_LEFT, KEY_RIGHT, KEY_DOWN, 27]

        x = win.getch()
        key = key if x == -1 else x

        if key not in valid_keys:  # Only valid keys can be pressed
            key = prevKey

        snake.insert(0, [snake[0][0] +
                         (key == KEY_DOWN and 1) +
                         (key == KEY_UP and -
                          1), snake[0][1] +
                         (key == KEY_LEFT and -
                          1) +
                         (key == KEY_RIGHT and 1)])

        if snake[0][0] == 0 or snake[0][0] == 23 or snake[0][1] == 0 or snake[0][1] == 79:
            break

        if snake[0] in snake[1:]:
            break  # In case snake eats itself, app terminates

        if snake[0] == food:  # The snake eats the food

            food = []
            points = points + 1

            while food == []:
                food = [randint(1, 22), randint(1, 78)]
                if food in snake:
                    food = []

            win.addch(food[0], food[1], snake_food)
        else:
            last = snake.pop()
            win.addch(last[0], last[1], ' ')

        win.addch(snake[0][0], snake[0][1], "O")

    curses.endwin()


snake_food = "x"


def customize():

    os.system("clear")

    win = curses.initscr()  # Initializing curses module
    win.keypad(True)  # Allows to use special keys with curses
    curses.noecho()  # nem jeleniti meg a leutott billenytűt
    curses.curs_set(False)  # Turns off the blinking cursor

    key = KEY_RIGHT  # Variable that refers to the key pressed
    prevKey = KEY_RIGHT

    win.addstr(2, 15, "        Select a character for food")
    win.addstr(10, 32, " 1:  X")
    win.addstr(12, 32, ' 2:  # ')
    win.addstr(14, 32, ' 3:  @ ')
    win.addstr(16, 32, ' 4:  random ch. ')

    x = win.getch()
    key = key if x == -1 else x
    valid_keys = [49, 50, 51, 52]

    if key not in valid_keys:
        key = prevKey

    global snake_food

    random_food = ["*", "+", "#", "@", "&", "$", "ß"]

    if key == 49:
        snake_food = "X"
    elif key == 50:
        snake_food = "#"
    elif key == 51:
        snake_food = "@"
    elif key == 52:
        snake_food = random_food[randint(0, 6)]

    os.system('clear')

    curses.endwin()

    os.system('clear')

    options()


def menu():

    os.system('clear')

    print('''

        CODECOOL SNAKE v1.0
    ________         _________
  /         \       /         \   
 /  /~~~~~\  \     /  /~~~~~\  \ 
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |         /
 |  |     |  |     |  |     |  |       //
(o  o)    \  \_____/  /     \  \_____/ /
 \__/      \         /       \        /
  |         ~~~~~~~~~         ~~~~~~~~       ''')

    cprint('  ^', 'red', attrs=['blink'])

    print('  by Lajos Beszteri & Adam Konyari')
    cprint('     -Hit ENTER to continue!-', 'white', attrs=['blink'])

    input()
    os.system('clear')


def read_score():

    os.system('clear')
    high_scores = []
    with open('highscores.txt', 'rb') as f:
        high_scores = pickle.load(f)

    high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

    '''
    for i in high_scores:
        for j in range(0, 40):
            print(" ", end="")
        print(i[0], i[1])


    '''
    cprint('                                  HIGH SCORE ', 'green', attrs=['blink'])
    print('-' * 80)

    for i in high_scores:
        print(i[0].rjust(38), str(i[1]).rjust(5))

    print('-' * 80)

    input()
    os.system('clear')


def score():

    os.system('clear')
    high_scores = []
    with open('highscores.txt', 'rb') as f:
        high_scores = pickle.load(f)

    high_scores.append((name, points))
    high_scores = sorted(high_scores, key=itemgetter(1), reverse=True)[:10]

    with open('highscores.txt', 'wb') as f:
        pickle.dump(high_scores, f)


def player_Name():
    global name
    name = input('Player name: ')


def options():

    os.system('clear')
    win = curses.initscr()  # Initializing curses module
    win.keypad(True)  # Allows to use special keys with curses
    curses.noecho()  # nem jeleniti meg a leutott billenytűt
    curses.curs_set(False)  # Turns off the blinking cursor

    key = KEY_RIGHT  # Variable that refers to the key pressed
    prevKey = KEY_RIGHT

    while key != 27:
        win.clear()
        win.addstr(3, 16, 'Select an option with a corresponding number!')
        win.addstr(8, 32, '1. Classic Mode ')
        win.addstr(10, 32, '2. COOL Mode ')
        win.addstr(12, 32, '3. Customize')
        win.addstr(14, 32, '4. High Score                               ')
        win.addstr(20, 30, 'Or hit ESC to exit.')
        x = win.getch()
        key = key if x == -1 else x
        valid_keys = [27, 49, 50, 51, 52]

        if key not in valid_keys:
            key = prevKey

        if key == 49:
            classic_Snake()
            score()
        elif key == 50:
            cool_Snake()
            score()
        elif key == 51:
            customize()
        elif key == 52:
            curses.endwin()
            read_score()

    curses.endwin()


def main():
    menu()
    player_Name()
    options()
    #print(f'Well done {name}! You scored {points} points.')


if __name__ == '__main__':
    main()
