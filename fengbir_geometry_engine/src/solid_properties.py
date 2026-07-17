def calculate_solid_properties(solid, density_kg_m3: float = 7850):
    """Calculate basic physical properties for a solid object.

    Expects the solid to provide Volume() in cubic millimeters,
    Area() in square millimeters, Center() with x,y,z in mm,
    and BoundingBox() with xmin,xmax,ymin,ymax,zmin,zmax,xlen,ylen,zlen in mm.
    """
    volume_mm3 = solid.Volume()
    surface_area_mm2 = solid.Area()
    center = solid.Center()
    bbox = solid.BoundingBox()

    # convert cubic millimeters to cubic meters
    volume_m3 = volume_mm3 / 1_000_000_000
    mass_kg = volume_m3 * density_kg_m3

    return {
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
    }
