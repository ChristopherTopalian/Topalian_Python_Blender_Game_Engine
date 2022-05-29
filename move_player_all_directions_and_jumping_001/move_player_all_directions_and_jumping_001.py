# Dedicated to God the Father
# All Rights Reserved Christopher Topalian Copyright 2000-2022
# https://github.com/ChristopherTopalian
# move_player_all_directions_and_jumping_001.py
# WASD to move
# Shift to boost speed
# Control to Side Step
# Spacebar to jump

# this script requires these logic bricks:
# Keyboard sensor, w, pulse true, connected to Python controller
# Keyboard sensor, s, pulse true, connected to Python controller
# Keyboard sensor, a, pulse true, connected to Python controller
# Keyboard sensor, d, pulse true, connected to Python controller
# Keyboard sensor, space, pulse true, connected to Python controller

# optional logic bricks
# Always sensor, connected to Or controller,
# connected to Contraint actuator, location constraint, locZ, max 10.0

import bge

mainSpeed = 0.1
rotationSpeed = 0.03
jumpForce = 0.7
boostSpeed = 0.2

controller = bge.logic.getCurrentController()
obj = controller.owner
kb = bge.logic.keyboard
keyboardEvent = kb.events

wkey = keyboardEvent[bge.events.WKEY]
skey = keyboardEvent[bge.events.SKEY]
akey = keyboardEvent[bge.events.AKEY]
dkey = keyboardEvent[bge.events.DKEY]

spacekey = keyboardEvent[bge.events.SPACEKEY]

shiftkey = keyboardEvent[bge.events.LEFTSHIFTKEY] or \
keyboardEvent[bge.events.RIGHTSHIFTKEY]

controlKey = keyboardEvent[bge.events.LEFTCTRLKEY] or \
keyboardEvent[bge.events.RIGHTCTRLKEY]

# CONTROL + A to SIDE STEP LEFT
if (controlKey and akey):
    obj.applyMovement([-mainSpeed, 0, 0], 1)

# CONTROL + D to SIDE STEP RIGHT
if (controlKey and dkey):
    obj.applyMovement([mainSpeed, 0, 0], 1)

# W to move FORWARD
if (wkey and not controlKey):
    obj.applyMovement([0, mainSpeed, 0], 1)

# S to move BACKWARDS
if (skey and not controlKey):
    obj.applyMovement([0, -mainSpeed, 0], 1)

# A to move ROTATE LEFT
if (akey and not controlKey):
    obj.applyRotation([0, 0, rotationSpeed], 1)

# D to ROTATE RIGHT
if (dkey and not controlKey):
    obj.applyRotation([0, 0, -rotationSpeed], 1)

# Spacebar to JUMP
if (spacekey):
    obj.applyMovement([0, 0, jumpForce], 1)

# Shift + W to Boost Speed FORWARDS
if (shiftkey and wkey):
    obj.applyMovement([0, boostSpeed, 0], 1)

# Shift + S to Boost Speed BACKWARDS
if (shiftkey and skey):
    obj.applyMovement([0, -boostSpeed, 0], 1)
