import sys
from pathlib import Path


def init():
    current_file = Path(__file__)
    parent_project_path = ""
    for p in current_file.parents:
        if str(p).endswith('src'):
            print( f"parents => {p}")
            parent_project_path = str(p)
            
    sys.path.append(parent_project_path)