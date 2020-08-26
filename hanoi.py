#!/usr/bin/python

import rospy
from tower_of_hanoi_iface.client import TowerOfHanoiClient

# Default stick values
towers = {"fromTower": 0, "midTower": 1, "toTower": 2}

def execute(client):
    # Running default with 4 rings
    hanoi(client, 4, towers["fromTower"], towers["toTower"], towers["midTower"])
    return True

# Recursive function for hanoi tower, requires number of discs and the numbers of the towers
def hanoi(client, n, fromTower, toTower, midTower):
    if n == 1:
        print("Moving ring", n, "from", fromTower, "to", toTower)
        client.move_disc(fromTower, toTower)
        return
    elif n != 1:
        hanoi(client, n-1, fromTower, midTower, toTower)
        print("Moving ring", n, "from", fromTower, "to", toTower)
        client.move_disc(fromTower, toTower)
        hanoi(client, n-1, midTower, toTower, fromTower)

if __name__ == '__main__':
    rospy.init_node("tower_of_hanoi")
    c = TowerOfHanoiClient(execute)
    c.set_exception_on_any_failure(True)
    c.spin()
