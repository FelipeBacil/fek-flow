def calculate_assembly_properties(solids, density_kg_m3: float = 7850):
    bodies = []

    total_volume_mm3 = 0
    total_mass_kg = 0

    for index, solid in enumerate(solids, start=1):
        volume_mm3 = solid.Volume()
        surface_area_mm2 = solid.Area()
        center = solid.Center()
        bbox = solid.BoundingBox()

        volume_m3 = volume_mm3 / 1_000_000_000
        mass_kg = volume_m3 * density_kg_m3

        total_volume_mm3 += volume_mm3
        total_mass_kg += mass_kg

        bodies.append({
            "body_index": index,
            "volume_mm3": volume_mm3,
            "surface_area_mm2": surface_area_mm2,
            "mass_kg": mass_kg,
            "center_of_mass_mm": {
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
        })

    return {
        "body_count": len(solids),
        "total_volume_mm3": total_volume_mm3,
        "total_volume_m3": total_volume_mm3 / 1_000_000_000,
        "total_mass_kg": total_mass_kg,
        "bodies": bodies,
    }
