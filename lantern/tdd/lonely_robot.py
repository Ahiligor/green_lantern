class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = {"E": "N"}
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {"N": "E"}
        self.direction = turns[self.direction]

    def turn_around(self):
        turns = {"E": "W"}
        self.direction = turns[self.direction]

    # Same test of turn but with use parametrize

    def turn_param(self):
        turns = {"N": "W", "W": "S", "S": "E"}
        self.direction = turns[self.direction]

    def move_forward(self):
        move = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
        }
        if self.direction == "N":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1

    def move_backward(self):
        move = {
            "N": (0, 1),
            "E": (1, 0),
            "S": (0, -1),
            "W": (-1, 0),
        }
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "E":
            self.x -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1

    def robot_falls(self):
        if self.direction == "N":
            if self.y + 1 > self.asteroid.y:
                raise RobotFallsFromAsteroid()
        elif self.direction == "S":
            if self.y - 1 < self.asteroid.y:
                raise RobotFallsFromAsteroid()
        elif self.direction == "W":
            if self.x - 1 < self.asteroid.x:
                raise RobotFallsFromAsteroid()
        elif self.direction == "E":
            if self.x + 1 > self.asteroid.x:
                raise RobotFallsFromAsteroid()


class MissAsteroidError(Exception):
    pass


class RobotFallsFromAsteroid(Exception):
    pass
