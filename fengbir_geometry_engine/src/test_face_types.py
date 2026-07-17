import json

from step_reader import read_step_solids
from face_type_mapper import map_assembly_face_types

filepath = "input/arquivos_step/longarina.STEP"

solids = read_step_solids(filepath)

face_types = map_assembly_face_types(solids)

print(json.dumps(face_types, indent=4, ensure_ascii=False))
