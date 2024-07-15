from csv import reader
import os

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_mp:
        layout = reader(level_mp, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
            
        return terrain_map

