import json

from step_reader import read_step_solids
from assembly_properties import calculate_assembly_properties

filepath = "input/arquivos_step/longarina.STEP"

solids = read_step_solids(filepath)

assembly = calculate_assembly_properties(solids)

print(json.dumps(assembly, indent=4, ensure_ascii=False))
