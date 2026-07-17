def map_solid_topology(solid):
    faces = solid.Faces()
    edges = solid.Edges()
    vertices = solid.Vertices()
    bbox = solid.BoundingBox()

    return {
        "face_count": len(faces),
        "edge_count": len(edges),
        "vertex_count": len(vertices),
        "volume_mm3": solid.Volume(),
        "surface_area_mm2": solid.Area(),
        "bounding_box_mm": {
            "x_min": bbox.xmin,
            "x_max": bbox.xmax,
            "y_min": bbox.ymin,
            "y_max": bbox.ymax,
            "z_min": bbox.zmin,
            "z_max": bbox.zmax,
            "length_x": bbox.xlen,
            "width_y": bbox.ylen,
            "height_z": bbox.zlen,
        },
    }


def map_assembly_topology(solids):
    mapped_bodies = []

    total_faces = 0
    total_edges = 0
    total_vertices = 0

    for index, solid in enumerate(solids, start=1):
        topology = map_solid_topology(solid)

        total_faces += topology["face_count"]
        total_edges += topology["edge_count"]
        total_vertices += topology["vertex_count"]

        mapped_bodies.append({
            "body_index": index,
            **topology,
        })

    return {
        "body_count": len(solids),
        "total_faces": total_faces,
        "total_edges": total_edges,
        "total_vertices": total_vertices,
        "bodies": mapped_bodies,
    }
