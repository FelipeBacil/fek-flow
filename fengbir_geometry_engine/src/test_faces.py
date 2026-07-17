import json

from step_reader import read_step_solids
from face_mapper import map_assembly_faces

filepath = "input/arquivos_step/longarina.STEP"

solids = read_step_solids(filepath)

faces = map_assembly_faces(solids)

print(json.dumps(faces, indent=4, ensure_ascii=False))