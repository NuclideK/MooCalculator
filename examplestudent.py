import LogicHandler
LogicHandler.indicateLoading("Loading " + __name__)
import random
import string
def mockStudent():
    c = []
    for i in range(14):
        c.append(random.randint(0,10))
    return {
        "name": [''.join(random.choice(string.ascii_lowercase) for i in range(10)),''.join(random.choice(string.ascii_uppercase) for i in range(10))],
        "id": random.randint(0,1000),
        "courses": c.copy(),
        "total_score": sum(c),
        "organization": "",
        "email": f"{''.join(random.choice(string.ascii_lowercase) for i in range(10))}@example.com"
    }

LogicHandler.indicateSuccess(f"{__name__} loaded [S]")