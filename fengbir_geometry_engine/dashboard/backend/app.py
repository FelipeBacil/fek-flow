import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="FEK Project Manager API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


PROJECT_ROOT = Path(__file__).resolve().parents[2]

BACKLOG_FILE = (
    PROJECT_ROOT
    / "docs"
    / "management"
    / "MEB-001_Master_Engineering_Backlog.json"
)


def read_backlog() -> dict:
    if not BACKLOG_FILE.exists():
        raise FileNotFoundError(
            f"Arquivo de backlog não encontrado: {BACKLOG_FILE}"
        )

    with BACKLOG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


@app.get("/")
def root():
    return {
        "service": "FEK Project Manager API",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/api/backlog")
def get_backlog():
    try:
        return read_backlog()
    except FileNotFoundError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except json.JSONDecodeError as error:
        raise HTTPException(
            status_code=500,
            detail=f"JSON inválido: {error}",
        ) from error
