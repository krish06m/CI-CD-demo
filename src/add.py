import sys 
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent[1]))

from src.add import add, sub

def test_add():
    assert add(2, 3) == 5
    