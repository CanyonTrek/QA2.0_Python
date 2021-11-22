#! /usr/bin/python
# Author: QA2.0 LIVE, V1.0
# Description: This is an ultra realistic computer game with Tanks!
"""
    Game of Tanks!
"""

import sys
import tank

def main():
    """ Main game """
    # Instantiate 3 new Tank objects.
    lancelot_tank = tank.Tank("German", "Tiger")
    arthur_tank = tank.Tank("British", "Churchill")
    robin_tank = tank.Tank("American", "Sherman")

    # .. and the game begins.
    lancelot_tank.accel(41)
    arthur_tank.accel(33)

    robin_tank.rotate_left(385)
    robin_tank.accel(15)
    robin_tank.shoot()

    # ..and success!
    lancelot_tank.take_damage(40)
    arthur_tank.take_damage(62)

    # And now for some game visuals! Well at least a print statement!
    print(f"Health of Lancelot's Tank = {lancelot_tank._health}") # Why is this POOR Code?

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)