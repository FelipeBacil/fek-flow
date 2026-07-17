import json

from step_reader import read_step
from solid_properties import calculate_solid_properties

filepath = "input/arquivos_step/longarina.STEP"

solid = read_step(filepath)

properties = calculate_solid_properties(solid)

print(json.dumps(properties, indent=4, ensure_ascii=False))

