# fastapi-signals
Signalling for FastAPI.

# motivation
- https://stackoverflow.com/questions/62031695/how-to-use-background-tasks-with-starlette-when-theres-no-background-object
- https://spectrum.chat/ariadne/general/how-to-use-background-tasks-with-starlette~74d56970-5676-4484-8586-a9384e5f4d56
- https://github.com/encode/starlette/issues/436

# usage
### add middleware
```
from fastapi_signals import SignalMiddleware, signal
app = FastAPI()
app.add_midleware(SignalMiddleware, handler=signal)
```
### add handler
```
from fastapi_signals import signal
import asyncio

@signal.register
async def handler():
    asyncio.sleep(3)
    print('Heyy, it works!')
```
### fire signal in function
```
from fastapi_signals import initiate_signal
@app.get("/")
async def endpoint(request):
    await initiate_signal('handler',some_data="value")
    return {"status":"Success"}
```

#### package
```
python setup.py sdist
twine upload dist/*
```