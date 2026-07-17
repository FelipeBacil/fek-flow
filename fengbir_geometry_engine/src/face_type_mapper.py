def get_face_type(face):
    try:
        geom_type = face.geomType()
        return str(geom_type)
    except Exception:
        return "UNKNOWN"


def map_solid_face_types(solid):
    faces = solid.Faces()
    mapped_faces = []

    for index, face in enumerate(faces, start=1):
        bbox = face.BoundingBox()
        center = face.Center()

        mapped_faces.append({
            "face_index": index,
            "face_type": get_face_type(face),
            "area_mm2": face.Area(),
            "center_mm": {
                "x": center.x,
                "y": center.y,
                "z": center.z,
            },
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
            "edge_count": len(face.Edges()),
            "vertex_count": len(face.Vertices()),
        })

    return mapped_faces


def map_assembly_face_types(solids):
    bodies = []

    for body_index, solid in enumerate(solids, start=1):
        faces = map_solid_face_types(solid)

        type_counter = {}

        for face in faces:
            face_type = face["face_type"]
            type_counter[face_type] = type_counter.get(face_type, 0) + 1

        bodies.append({
            "body_index": body_index,
            "face_count": len(faces),
            "face_type_summary": type_counter,
            "faces": faces,
        })

    return {
        "body_count": len(solids),
        "bodies": bodies,
    }
