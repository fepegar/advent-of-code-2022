"""
Convert the input of day 12 of Advent of Code 2022 to an STL file.

To install requirements, run:
pip install scikit-image numpy-stl

Usage:
python input_to_mesh.py input.txt output.stl

Example content of input.txt:
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

import argparse
from pathlib import Path

import numpy as np
from skimage import measure
import stl
from stl import mesh


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_path', type=Path)
    parser.add_argument('output_path')
    args = parser.parse_args()
    input_path = Path(args.input_path)
    data = input_path.read_text()

    offset = 1
    data = data.replace('S', chr(ord('a') - offset))
    data = data.replace('E', chr(ord('z') + offset))
    lines = []
    for line in data.splitlines():
        values = [ord(char) for char in line]
        lines.append(values)
    image = np.array(lines)
    image -= image.min()

    height, width = image.shape
    volume = np.zeros((height + 2, width + 2, image.max() + 2), dtype=np.uint8)
    for row in range(height):
        for col in range(width):
            value = image[row, col]
            volume[row + 1, col + 1, 1:value + 1] = 1

    # https://scikit-image.org/docs/stable/auto_examples/edges/plot_marching_cubes.html
    vertices, faces, _, _ = measure.marching_cubes(volume, 0)

    # https://pypi.org/project/numpy-stl/
    my_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for face_index, face in enumerate(faces):
        for i, vertex_idx in enumerate(face):
            my_mesh.vectors[face_index][i] = vertices[vertex_idx]
    my_mesh.save(args.output_path, mode=stl.Mode.ASCII)


if __name__ == '__main__':
    main()
