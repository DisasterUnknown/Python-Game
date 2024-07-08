# game setUp
WIDTH = 1280
HEIGHT = 720
FPS = 120
TILESIZE = 16
ZOOMSIZE = TILESIZE * 4

# Game map 
WORLD_MAP = [
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ','x','x','x','x','x',' ','x',' ','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ','x',' ',' ','x','x',' ','p',' ','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ','x','x','x','x',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x',' ',' ',' ','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ','x',' ',' ',' ',' ',' ',' ',' ','x','x','x','x','x',' ',' ',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
]

WORLD_MAP2 = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x'],     
    ['x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'p', 'x', 'p', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', 'x', 'x'],     
    ['x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', 'x'],     
    ['x', 'x', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', 'x'],     
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x'],     
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],     
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],   
]