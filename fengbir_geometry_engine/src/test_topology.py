import json

from step_reader import read_step_solids
from topology_mapper import map_assembly_topology

filepath = "input/arquivos_step/longarina.STEP"

solids = read_step_solids(filepath)

topology = map_assembly_topology(solids)

print(json.dumps(topology, indent=4, ensure_ascii=False))
