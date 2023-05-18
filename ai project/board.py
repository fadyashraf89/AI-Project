import pyautogui
from PIL import ImageGrab

# These are the coordinates of the rectangle that defines the region of the screen where the Connect Four game is located.
LEFT = 570
TOP = 200
RIGHT = 1350
BOTTOM = 875

# These are constants that are used to represent the state of a cell on the Connect Four board.
EMPTY = 0
RED = 1
BLUE = 2


class Board:
    # This is the constructor of the class. It initializes the board as a 6x7 grid of empty cells.
    def __init__(self) -> None:
        self.board = [[EMPTY for i in range(7)] for j in range(6)]

    # This function is used to print the current state of the board to the console in a user-friendly way.
    def print_grid(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY:
                    print("*", end=" \t")
                elif grid[i][j] == RED:
                    print("R", end=" \t")
                elif grid[i][j] == BLUE:
                    print("B", end=" \t")
            print("\n")
        print("##################\n")

    # This function takes a grid of RGB values and converts it to a grid of integer values representing the state of each cell on the board.
    def _convert_grid_to_color(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == (255, 255, 255):
                    grid[i][j] = EMPTY
                elif grid[i][j][0] > 200:
                    grid[i][j] = RED
                elif grid[i][j][0] > 50:
                    grid[i][j] = BLUE
        return grid

    # This function generates a list of coordinates that correspond to the center of each cell on the Connect Four board.
    def _get_grid_cordinates(self):
        startCord = (50, 55)
        cordArr = []
        for i in range(0, 7):
            for j in range(0, 6):
                x = startCord[0] + i * 115
                y = startCord[1] + j * 112
                cordArr.append((x, y))
        return cordArr

    # This function transposes the grid so that the rows become columns and vice versa.
    def _transpose_grid(self, grid):
        return [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]

    #  This function captures an image of the Connect Four game board from the screen.
    def _capture_image(self):
        image = ImageGrab.grab()
        cropedImage = image.crop((LEFT, TOP, RIGHT, BOTTOM))
        return cropedImage

    # This function takes an image of the Connect Four game board and converts it to a grid of RGB values representing the state of each cell on the board.
    def _convert_image_to_grid(self, image):
        pixels = [[] for i in range(7)]
        i = 0
        for index, cord in enumerate(self._get_grid_cordinates()):
            pixel = image.getpixel(cord)
            if index % 6 == 0 and index != 0:
                i += 1
            pixels[i].append(pixel)
        return pixels

    # This function captures an image of the Connect Four game board, converts it to a grid of RGB values, and transposes it to match the internal representation of the board.
    def _get_grid(self):
        cropedImage = self._capture_image()
        pixels = self._convert_image_to_grid(cropedImage)
        # cropedImage.show()
        grid = self._transpose_grid(pixels)
        return grid

    # This function checks if the game has ended by comparing the current state of the board with the previous state. If any cell has changed from empty to non-empty, the game is considered to have ended.
    def _check_if_game_end(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == EMPTY and self.board[i][j] != EMPTY:
                    return True
        return False

    #  This function returns the current state of the Connect Four game board as a 2D list of integers, and a boolean indicating whether the game has ended.
    def get_game_grid(self):
        game_grid = self._get_grid()
        new_grid = self._convert_grid_to_color(game_grid)
        is_game_end = self._check_if_game_end(new_grid)
        self.board = new_grid
        return (self.board, is_game_end)

    # This function simulates a mouse click on the center of the specified column on the Connect Four game board. This is used to make a move in the game.
    def select_column(self, column):
        pyautogui.click(
            self._get_grid_cordinates()[column][1] + LEFT,
            self._get_grid_cordinates()[column][0] + TOP,
        )
