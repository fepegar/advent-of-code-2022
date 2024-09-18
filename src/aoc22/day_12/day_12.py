import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
from scipy import ndimage

from aoc22 import get_logger


_logger = get_logger(__name__)


def dijkstra(graph: np.ndarray, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    max_value = 1_000_000_000
    distances = np.full_like(graph, max_value)  # not working with np.inf (why?)
    shape = *graph.shape, 2
    previous = np.full(shape, -1)
    unvisited = np.ones_like(graph, dtype=bool)
    distances[start] = 0
    while unvisited.any():
        # print(np.count_nonzero(unvisited))
        # print()
        # print('distances')
        # print(distances)
        visited = np.logical_not(unvisited)
        # print('visited')
        # print(visited)
        distances_masked = np.ma.masked_array(distances, mask=visited)
        current = np.unravel_index(np.argmin(distances_masked), graph.shape)
        current_graph = np.zeros_like(graph).astype(bool)
        current_graph[current] = True
        # print('current')
        # print(current)
        if current == (0, 2):
            pass
        # print('current_graph')
        # print(current_graph)
        if current == end:
            break
        unvisited[current] = False
        # Neighbors are only pixels that are one more or any less than the current value
        height_difference = graph - graph[current]
        # print('height_difference')
        # print(height_difference)
        neighbors = ndimage.binary_dilation(current_graph)
        # Remove the current pixel from the neighbors
        neighbors[current] = False
        # Remove any pixels that have already been visited
        neighbors = neighbors * (height_difference <= 1) * unvisited
        # print('neighbors')
        # print(neighbors)
        for neighbor in np.argwhere(neighbors):
            neighbor = tuple(neighbor)
            new_distance = distances[current] + 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
    path = []
    current = end
    while current != start:
        path.append(current)
        current = tuple(previous[current])
    path.append(start)
    path.reverse()
    distances[distances == max_value] = 0
    plt.imshow(distances)
    plt.axis('off')
    plt.savefig('distances.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    return path


def dijkstra_2(graph: np.ndarray, start: tuple[int, int]) -> list[tuple[int, int]]:
    max_value = 1_000_000_000
    distances = np.full_like(graph, max_value)  # not working with np.inf (why?)
    shape = *graph.shape, 2
    previous = np.full(shape, -1)
    unvisited = np.ones_like(graph, dtype=bool)
    distances[start] = 0
    while unvisited.any():
        # print(np.count_nonzero(unvisited))
        # print()
        # print('distances')
        # print(distances)
        visited = np.logical_not(unvisited)
        # print('visited')
        # print(visited)
        distances_masked = np.ma.masked_array(distances, mask=visited)
        current = np.unravel_index(np.argmin(distances_masked), graph.shape)
        current_graph = np.zeros_like(graph).astype(bool)
        current_graph[current] = True
        # print('current')
        # print(current)
        if current == (0, 2):
            pass
        # print('current_graph')
        # print(current_graph)
        unvisited[current] = False
        # Neighbors are only pixels that are one more or any less than the current value
        height_difference = graph - graph[current]
        # print('height_difference')
        # print(height_difference)
        neighbors = ndimage.binary_dilation(current_graph)
        # Remove the current pixel from the neighbors
        neighbors[current] = False
        # Remove any pixels that have already been visited
        neighbors = neighbors * (height_difference >= -1) * unvisited
        # print('neighbors')
        # print(neighbors)
        for neighbor in np.argwhere(neighbors):
            neighbor = tuple(neighbor)
            new_distance = distances[current] + 1
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current
    distances[distances == max_value] = 0
    plt.imshow(distances)
    plt.axis('off')
    plt.savefig('distances_2.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    paths = []
    all_as = np.argwhere(graph == graph.min())
    from tqdm.auto import tqdm
    for end in tqdm(all_as):
        path = []
        current = tuple(end)
        while current != start:
            path.append(current)
            if len(path) > 10000:  # kind of cheating
                break
            current = tuple(previous[current])
        path.append(start)
        path.reverse()
        paths.append(path)
    return paths


def part_1(data: str) -> int:
    offset = 1
    data = data.replace('S', chr(ord('a') - offset))
    data = data.replace('E', chr(ord('z') + offset))
    lines = []
    for line in data.splitlines():
        values = [ord(char) for char in line]
        lines.append(values)
    image = np.array(lines)
    start = np.unravel_index(np.argmin(image, axis=None), image.shape)
    end = np.unravel_index(np.argmax(image, axis=None), image.shape)
    path = dijkstra(image, start, end)
    plt.imshow(image)
    for i, second in enumerate(path[1:], start=1):
        first = path[i - 1]
        # Draw line between first and second
        x = [first[1], second[1]]
        y = [first[0], second[0]]
        plt.plot(x, y, color='red')
    plt.axis('off')
    plt.savefig('part_1.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    return len(path) - 1


def part_2(data: str) -> int:
    offset = 1
    data = data.replace('S', 'a')
    data = data.replace('E', chr(ord('z') + offset))
    lines = []
    for line in data.splitlines():
        values = [ord(char) for char in line]
        lines.append(values)
    image = np.array(lines)
    start = np.unravel_index(np.argmax(image, axis=None), image.shape)
    paths = dijkstra_2(image, start)
    lengths = np.array([len(path) for path in paths])
    path = paths[np.argmin(lengths)]
    plt.imshow(image)
    for i, second in enumerate(path[1:], start=1):
        first = path[i - 1]
        # Draw line between first and second
        x = [first[1], second[1]]
        y = [first[0], second[0]]
        plt.plot(x, y, color='red')
    plt.axis('off')
    plt.savefig('path_2.png', dpi=300, bbox_inches='tight', pad_inches=0)
    plt.close()
    return len(path) - 1


if __name__ == '__main__':
    from pathlib import Path
    with open(Path(__file__).parent / 'input.txt') as f:
        data = f.read()
    print(part_2(data))
