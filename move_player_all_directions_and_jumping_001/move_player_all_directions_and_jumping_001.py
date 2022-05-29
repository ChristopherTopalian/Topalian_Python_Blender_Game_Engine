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

wKey = keyboardEvent[bge.events.WKEY]
sKey = keyboardEvent[bge.events.SKEY]
aKey = keyboardEvent[bge.events.AKEY]
dKey = keyboardEvent[bge.events.DKEY]

spaceKey = keyboardEvent[bge.events.SPACEKEY]

shiftKey = keyboardEvent[bge.events.LEFTSHIFTKEY] or \
keyboardEvent[bge.events.RIGHTSHIFTKEY]

controlKey = keyboardEvent[bge.events.LEFTCTRLKEY] or \
keyboardEvent[bge.events.RIGHTCTRLKEY]

# W to move FORWARD
if (wKey and not controlKey):
    obj.applyMovement([0, mainSpeed, 0], 1)

# S to move BACKWARDS
if (sKey and not controlKey):
    obj.applyMovement([0, -mainSpeed, 0], 1)

# A to ROTATE LEFT
if (aKey and not controlKey):
    obj.applyRotation([0, 0, rotationSpeed], 1)

# D to ROTATE RIGHT
if (dKey and not controlKey):
    obj.applyRotation([0, 0, -rotationSpeed], 1)

# Shift + W to Boost Speed FORWARDS
if (shiftKey and wKey):
    obj.applyMovement([0, boostSpeed, 0], 1)

# Shift + S to Boost Speed BACKWARDS
if (shiftKey and sKey):
    obj.applyMovement([0, -boostSpeed, 0], 1)

# CONTROL + A to SIDE STEP LEFT
if (controlKey and aKey):
    obj.applyMovement([-mainSpeed, 0, 0], 1)

# CONTROL + D to SIDE STEP RIGHT
if (controlKey and dKey):
    obj.applyMovement([mainSpeed, 0, 0], 1)

# SHIFT + CONTROL + A to Boost Speed SIDE STEP LEFT
if (shiftKey and controlKey and aKey):
    obj.applyMovement([-boostSpeed, 0, 0], 1)

# SHIFT + CONTROL + D to Boost Speed SIDE STEP RIGHT
if (shiftKey and controlKey and dKey):
    obj.applyMovement([boostSpeed, 0, 0], 1)

# Spacebar to JUMP
if (spaceKey):
    obj.applyMovement([0, 0, jumpForce], 1)
