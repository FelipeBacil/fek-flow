# Fengbir Geometry Engine - MVP 01.1

Motor geométrico 2D com dois modos:

- `section`: seção transversal, para cálculo de propriedades estruturais da seção.
- `plate`: vista lateral/chapa plana, para cálculo de área plana, volume e massa total.

## Instalação

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Rodar seção transversal

```powershell
py src/main.py input/arquivos_dxf/secao.dxf --component longarina --material S700MC --mode section --output output
```

## Rodar chapa/vista lateral

```powershell
py src/main.py input/arquivos_dxf/longarina.dxf --component longarina --material S700MC --mode plate --thickness 6.35 --output output
```

## Observação técnica

Use `section` quando o DXF representar o perfil/seção da peça.
Use `plate` quando o DXF representar a vista lateral ou contorno plano da peça.
