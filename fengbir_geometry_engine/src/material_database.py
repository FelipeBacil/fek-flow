"""Banco simples de materiais para o MVP do Motor Geométrico Fengbir."""

MATERIALS = {
    "ACO_CARBONO": {
        "name": "Aço carbono genérico",
        "density_kg_m3": 7850,
        "yield_strength_mpa": 250,
    },
    "S700MC": {
        "name": "S700MC",
        "density_kg_m3": 7850,
        "yield_strength_mpa": 700,
    },
    "A572_GR50": {
        "name": "ASTM A572 Gr.50",
        "density_kg_m3": 7850,
        "yield_strength_mpa": 345,
    },
}


def get_material(key: str) -> dict:
    """Retorna material pelo código. Se não encontrar, usa aço carbono genérico."""
    return MATERIALS.get(key.upper(), MATERIALS["ACO_CARBONO"])
