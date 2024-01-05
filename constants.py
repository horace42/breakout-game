# ball speed configuration
SPEED = 10  # initial speed in milliseconds
SPEED_STEP = 2  # decrease amount at defined moments

# bricks collision distance
COLLISION_DISTANCE = 25

# bricks bottom row horizontal positions
ROW_YELLOW = 285
ROW_GREEN = 305
ROW_ORANGE = 325
ROW_RED = 345

# walls horizontal position
LEFT_WALL_POS = -355
RIGHT_WALL_POS = 355

# top wall vertical position
TOP_WALL_POS = 445

# paddle vertical position
PADDLE_POS = -255

# paddle travel distance
PADDLE_STEP = 15

# paddle-ball bouncing distances (L - large paddle, S - small paddle)
MAX_DIST_L = 55
MAX_DIST_S = 31
# bounce back or exaggerate depending on direction
BOUNCE_BACK_DIST_L = 45
BOUNCE_BACK_DIST_S = 25
# reduce bouncing or normal bouncing depending on direction
BOUNCE_MOD_DIST_L = 20
BOUNCE_MOD_DIST_S = 20
