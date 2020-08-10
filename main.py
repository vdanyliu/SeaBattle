import colorama
import termcolor
from sys import exit

from Ships import Ships, Ship

colorama.init()


class SeaBattleGame:
    def __init__(self):
        w, h = 10, 10
        # Matrix[h][w]
        # Matrix s(1) - ship, x(2) - ship hit, o(3) - miss, 0 - nothing
        self.seaMatrix = [[0 for x in range(w)] for y in range(h)]
        self.ships = Ships()
        self.__add_ships_in_matrix_field()
        self.__print_matrix(self.seaMatrix)
        self.command = None
        self.turn = 0

    @classmethod
    def __print_matrix(cls, matrix: list):
        """
        Print matrix of sea
        """
        n = 3
        char = 65
        print(' ' * n, end='')
        for i in range(10):
            print(('{: ^' + str(n) + '}').format(chr(char)), end='')
            char += 1
        print()
        k = 0
        for y in matrix:
            print(('{: ^' + str(n) + '}').format(k), end='')
            k += 1
            for x in y:
                # Matrix 0 - nothing, s(1) - ship, x(2) - ship hit, o(3) - miss
                if x == 0:
                    termcolor.cprint(' ' * n, 'red', 'on_blue', end='')
                elif x == 1:
                    termcolor.cprint(' ' * n, 'blue', 'on_blue', end='')
                elif x == 2:
                    strPrint = ('{: ^' + str(n) + '}').format('X')
                    termcolor.cprint(strPrint, 'blue', 'on_red', end='')
                elif x == 3:
                    strPrint = ('{: ^' + str(n) + '}').format('X')
                    termcolor.cprint(strPrint, 'red', 'on_blue', end='')
            print("")
        print('\n')

    def __add_ships_in_matrix_field(self):
        for ship in self.ships.shipList:
            for coord in ship.coord:
                self.seaMatrix[coord[0]][coord[1]] = 1

    def __controller(self):
        validatorActionList = [exit, self.__help, self.__fire]
        validatorActionList[self.__validator()]()

    def __validator(self) -> int:
        if self.command == '/exit':
            return 0
        elif self.command == '/help' or len(self.command) != 2:
            return 1
        str_list = list(self.command)
        if ('a' <= str_list[0] <= 'j') and (0 <= int(str_list[1]) <= 9):
            return 2
        else:
            return 1

    def __help(self, **shame):
        print("try 'H5', or type '/exit' for exit")

    def __fire(self):
        x = ord(self.command[0]) - ord('a')
        y = int(self.command[1])
        # Matrix s(1) - ship, x(2) - ship hit, o(3) - miss, 0 - nothing
        coord_node = self.seaMatrix[y][x]
        if coord_node == 0:
            self.__missShot(x, y)
        if coord_node == 1:
            self.__shipShot(x, y)
        if coord_node == 2 or coord_node == 3:
            self.__unavailableShot(x, y)

    def __missShot(self, x, y):
        self.seaMatrix[y][x] = 3
        print('miss')

    def __shipShot(self, x, y):
        self.seaMatrix[y][x] = 2
        destroyedShip = self.ships.eventShot(x, y)
        if destroyedShip:
            self.addBlowInMatrix(destroyedShip)  # X mark around ship
        if self.__check_end_game_state():
            self.__game_over()

    def addBlowInMatrix(self, ship: Ship):
        for coord in ship.blowCoord:
            print(coord)
            x = coord[0]
            y = coord[1]
            hitList = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1],
                       [x + 1, y + 1]]
            self.modyfiMatrixByhitList(hitList)

    def modyfiMatrixByhitList(self, hitList):
        print(hitList)
        for cord in hitList:
            y = cord[0]
            x = cord[1]
            # Matrix s(1) - ship, x(2) - ship hit, o(3) - miss, 0 - nothing
            if (0 <= x <= 9) and (0 <= y <= 9):
                if self.seaMatrix[y][x] != 2:
                    self.seaMatrix[y][x] = 3

    def __check_end_game_state(self):
        for Ship in self.ships.shipList:
            if Ship.alive == 1:
                return False
        return True

    def __game_over(self):
        print("all ships destroyed")
        print(f"You finish game for {self.turn} turns")
        exit()

    def __unavailableShot(self, x, y):
        print(f'u cant shoot x = {x}, y = {y}')

    def run(self):
        self.__print_matrix(self.seaMatrix)
        while True:
            self.command = input("Print fire coord or '/exit': ").lower()
            self.__controller()
            self.__print_matrix(self.seaMatrix)
            self.turn += 1
            # self.__print_matrix(self.seaMatrix)


game = SeaBattleGame()
game.run()
