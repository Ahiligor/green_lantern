import pytest

from lonely_robot import Robot, Asteroid, MissAsteroidError, RobotFallsFromAsteroid


@pytest.fixture
def standard_robot():
    x, y = 3, 3
    asteroid = Asteroid(x, y)
    return Robot(x, y, asteroid, "N")


@pytest.fixture
def standard_asteroid():
    x, y = 5, 5
    return Asteroid(x, y)


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestTurns:

    def test_turn_left(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        robot.turn_left()
        assert robot.direction == "N"

    def test_turn_right(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        direction = "N"
        robot = Robot(x, y, asteroid, direction)
        robot.turn_right()
        assert robot.direction == "E"

    def test_turn_around(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        direction = "E"
        robot = Robot(x, y, asteroid, direction)
        robot.turn_around()
        assert robot.direction == "W"


class TestTurnsParam:

    # Same test of turn but with use parametrize

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
        )
    )
    def test_turn_param(self, current_direction, expected_direction):
        x, y = 10, 15
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, "N")
        robot.direction = current_direction
        robot.turn_param()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        'direction, expected_x, expected_y',
        [
            ('N', 3, 4),
            ('E', 4, 3),
            ('S', 3, 2),
            ('W', 2, 3),
        ]
    )
    def test_move_forward(self, standard_robot, direction, expected_x, expected_y):
        standard_robot.direction = direction
        standard_robot.move_forward()

        assert standard_robot.x == expected_x
        assert standard_robot.y == expected_y

    @pytest.mark.parametrize(
        'direction, expected_x, expected_y',
        [
            ('N', 3, 2),
            ('E', 2, 3),
            ('S', 3, 4),
            ('W', 4, 3),
        ]
    )
    def test_move_backward(self, standard_robot, direction, expected_x, expected_y):
        standard_robot.direction = direction
        standard_robot.move_backward()

        assert standard_robot.x == expected_x
        assert standard_robot.y == expected_y

    @pytest.mark.parametrize(
        'direction,robot_coordinates',
        [
            ('N', (3, 6)),
            ('E', (6, 3)),
            ('S', (3, -1)),
            ('W', (-1, 3)),
        ]
    )
    def test_robot_falls(self, standard_robot, direction, robot_coordinates):
        with pytest.raises(RobotFallsFromAsteroid):
            standard_robot.robot_falls()
