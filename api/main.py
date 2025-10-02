from fastapi import FastAPI
import uvicorn, glob
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/healthz")
def healthz():
    return {"status":"ok"}

@app.get("/routes/avg-delay")
def avg_delay_route(route_id: str):
    # naive: read latest parquet files and compute; prod: Presto/Delta/Postgres
    paths = sorted(glob.glob("/data/parquet/delays/*/*/*/*"))[-10:]
    # ...load small sample w/ pyarrow/pandas...
    return JSONResponse({"route_id": route_id, "avg_delay_sec": 42})