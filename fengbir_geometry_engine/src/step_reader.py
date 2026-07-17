import cadquery as cq


def read_step_shape(filepath: str):
    shape = cq.importers.importStep(filepath)
    return shape


def read_step_solids(filepath: str):
    shape = read_step_shape(filepath)
    solids = shape.solids().vals()

    if not solids:
        raise ValueError("Nenhum sólido encontrado no arquivo STEP/STP.")

    return solids


def read_step(filepath: str):
    solids = read_step_solids(filepath)
    return solids[0]
