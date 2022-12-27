from typing import List

from src.Model.Enemy.EnemyFactory import EnemyFactory
from src.Model.Map.FileMapBuilder import FileMapBuilder
from src.Model.Map.MapController import GridCell


def test_MapBuilder1():
    height = 10
    width = 30
    max_item_health_point = 10

    world_map: List[List[GridCell]] = []
    for i in range(height):
        world_map.append([GridCell.EMPTY] * width)

    map_builder = FileMapBuilder(world_map, height, width, max_item_health_point, EnemyFactory(), './test_map.txt')
    map_builder._generate_walls()

    example = [
        '......###.#...#.#.#.###.#.#...',
        '...#..##.#..#...#..###..#.####',
        '#...#.#.#..#.#....#.##.####.#.',
        '#..##...##.##....###....##..##',
        '..#.##.#.#.#.#.#.##...#.......',
        '.##...#.##..##.#..#..#####....',
        '.##....##.#.#...#...#..#.#.##.',
        '.##..#..#...##.#.##.##.##.#...',
        '.##.##....#####......##.......',
        '.....##.###..#######.###...#..',
    ]

    for i in range(height):
        for j in range(width):
            if example[i][j] == '.':
                assert world_map[i][j] == GridCell.EMPTY
            if example[i][j] == '#':
                assert world_map[i][j] == GridCell.WALL
