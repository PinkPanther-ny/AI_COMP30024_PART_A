# SETTINGS
# ------------ Booleans ------------
BEST_FIRST_SEARCH_ON = True
# if WEIGHT_ON_COST==0, then a* turns to be Best first search,
# which equivalent to BEST_FIRST_SEARCH_ON == True
WEIGHT_ON_COST = 0.7

CAN_SWING_ONTO_FRIENDLY_TOKEN = True
BFS_DEBUG = False
SINGLE_TOKEN_SHOW_ROUTE = False
GET_CHILD_STATES_DEBUG = False
CHILD_STATES_SHOW_COMBINATIONS = False

VISUALIZE_RESULT = True
SHOW_SOLVE_TIME = True

# ------------ Heuristic value calculation ------------
H_SINGLE_BFS_MAX_DISTANCE = 1
H_SINGLE_MAX_ABSOLUTE_DISTANCE = 2

HEURISTIC_MODE = H_SINGLE_BFS_MAX_DISTANCE

# ------------ Global variables ------------
# Maximum distance from the centre hex
BOARD_SIZE = 4
UPPER_SIGN = "()"
LOWER_SIGN = "  "
BLOCK_SIGN = "#####"
