"""Set of reusable utilities to work with AIY models."""

import os


def load_compute_graph(name):
    path = os.environ.get('VISION_BONNET_MODELS_PATH', '/opt/aiy/models')
    with open(os.path.join(path, name), 'rb') as f:
        return f.read()

def shape_tuple(shape):
    return (shape.batch, shape.height, shape.width, shape.depth)