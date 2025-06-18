from fastapi import FastAPI

from .meals.dinner import spam_and_eggs

app = FastAPI(title='Dinner Cafe')


@app.get('/dinner/')
def dinner() -> str:
    return spam_and_eggs()
