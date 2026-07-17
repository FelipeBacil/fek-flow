from step_reader import read_step_solids

filepath = "input/arquivos_step/longarina.STEP"

solids = read_step_solids(filepath)

print(f"Quantidade de sólidos encontrados: {len(solids)}")

for index, solid in enumerate(solids, start=1):
    volume_mm3 = solid.Volume()
    bbox = solid.BoundingBox()

    print("-" * 60)
    print(f"Sólido {index}")
    print(f"Volume mm³: {volume_mm3:.3f}")
    print(f"Comprimento X mm: {bbox.xlen:.3f}")
    print(f"Largura Y mm: {bbox.ylen:.3f}")
    print(f"Altura Z mm: {bbox.zlen:.3f}")
