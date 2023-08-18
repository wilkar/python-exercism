class Alien:
    total_aliens_created = 0

    def __init__(
        self,
        x: int,
        y: int,
    ):
        self.__class__.total_aliens_created += 1
        self.health = 3
        self.x_coordinate = x
        self.y_coordinate = y

    def hit(self):
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other):
        pass


def new_aliens_collection(pos):
    return [Alien(x, y) for (x, y) in pos]
