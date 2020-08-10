import random


class Ships:
    def __init__(self):
        self.aliveShips = 0
        self.shipList = list()
        self.__arrange_ships()

    def __arrange_ships(self):
        stop = 0
        n = 4
        for size in range(n, 0, -1):
            for count in range(0, 5 - size):
                while True:
                    x = random.randrange(0, 10)
                    y = random.randrange(0, 10)
                    direction = random.randrange(0, 2)
                    if self.__field_check(size, x, y, direction) and self.__ship_check(size, x, y, direction):
                        self.shipList.append(Ship(size, x, y, direction))
                        self.aliveShips += 1
                        break
                    stop += 1
                    if stop >= 100: exit(0)

    @classmethod
    def __field_check(cls, size, x, y, direction) -> bool:  # check occlusion with field
        if direction == 0:
            if (x + size - 1) > 9:
                return False
        if direction == 1:
            if (y + size - 1) > 9:
                return False
        return True

    def __ship_check(self, size, x, y, direction) -> bool:  # check occlusion with already created ship
        coord_list = list()
        for i in range(0, size):
            coord_list.append([y, x])
            if direction:
                y += 1
            else:
                x += 1
        for ship in self.shipList:
            for trueShipCoordList in ship.coord:
                for i in coord_list:
                    deltaX = int(trueShipCoordList[0]) - int(i[0])
                    deltaY = int(trueShipCoordList[1]) - int(i[1])
                    if (-1 <= deltaX <= 1) and (-1 <= deltaY <= 1):
                        return False
        return True

    def eventShot(self, x, y):
        coord = [y, x]
        for ship in self.shipList:
            test = ship
            for shipCoord in ship.coord:
                if shipCoord == coord:
                    print(shipCoord)
                    print('hit')
                    ship.coord.remove(shipCoord)
                    if len(ship.coord) == 0:
                        ship.alive = 0
                        print("ship destroyed")
                        return ship


class Ship:
    def __init__(self, size, x, y, direction):
        self.size = size
        self.coord = list()
        self.__create_ship_coord(x, y, direction)
        self.blowCoord = self.coord[:]
        self.alive = True

    def __create_ship_coord(self, x, y, direction):
        for i in range(0, self.size):
            self.coord.append([y, x])
            if direction:
                y += 1
            else:
                x += 1
