world_map = [["forest", "forest", "village", "dungeon", "forest"],
             ["forest", "plains", "plains", "plains", "plains"],
             ["village", "plains", "dungeon", "plains", "forest"],
             ["dungeon", "forest", "forest", "wasteland", "wasteland"],
             ["forest", "forest", "dungeon", "wasteland", "dragon den"]]


class Scene():
    player_x = 0
    player_y = 0
    mapSize = 5

    def navigate(self, direction):
        if direction == 'north' or direction == 'n':
            if self.player_y - 1 < 0:
                print("Your path is blocked")
                return False
            self.player_y -= 1
            print("You moved North to a " +
                  world_map[self.player_y][self.player_x])
            return True
        elif direction == 'south' or direction == 's':
            if self.player_y + 1 > self.mapSize - 1:
                print("Your path is blocked")
                return False
            self.player_y += 1
            print("You moved South to a " +
                  world_map[self.player_y][self.player_x])
            return True
        elif direction == 'east' or direction == 'e':
            if self.player_x + 1 > self.mapSize - 1:
                print("Your path is blocked")
                return False
            self.player_x += 1
            print("You moved East to a " +
                  world_map[self.player_y][self.player_x])
            return True
        elif direction == 'west' or direction == 'w':
            if self.player_x - 1 < 0:
                print("Your path is blocked")
                return False
            self.player_x -= 1
            print("You moved West to a " +
                  world_map[self.player_y][self.player_x])
            return True
        else:
            print("Invalid direction")
