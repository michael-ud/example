from fastapi import FastAPI

from .meals.breakfast import bacon_and_eggs

app = FastAPI(title='Breakfast Bistro')


@app.get('/breakfast/')
def breakfast(steal: bool = False) -> str:
    if steal:
        try:
            from cafe.meals.dinner import secret_sauce
        except ImportError:
            return 'Waiter arrested attempting to steal secret sauce :('
        else:
            return bacon_and_eggs() + secret_sauce()

    return bacon_and_eggs()
