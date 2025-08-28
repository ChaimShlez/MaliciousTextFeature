import uvicorn
from fastapi import FastAPI
import logging

from fetcher import Fetcher

app=FastAPI()
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)

@app.get("/getDataAntisemitic")
def display_data():
    try:
        fetcher=Fetcher()
        return fetcher.get_data('antisemitic')

    except Exception as e:
       return {"don't success", "error", e}


@app.get("/getDataNotAntisemitic")
def display_data():
    try:
        fetcher=Fetcher()
        return fetcher.get_data('not_antisemitic')

    except Exception as e:
       return {"dont success", "error", e}


if __name__=="__main__":
    uvicorn.run(app)
