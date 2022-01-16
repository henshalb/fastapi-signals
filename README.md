[![Downloads](https://pepy.tech/badge/fastapi-signals)](https://pepy.tech/project/fastapi-signals)
# fastapi-signals
Signalling for FastAPI. Run background task without hurting the function. fastapi-signals is trying not to work like Django Signals. Instead, it tries to stay as a background task runner. Mostly similiar to Celery, but feathery.

# Usage - SignalMiddleware
NB: Only one signal per function, must take request object
### Add middleware
```
from fastapi_signals import SignalMiddleware, signal
app = FastAPI()
app.add_midleware(SignalMiddleware, handler=signal)
```
### Add handler
Specify how the fired signal should work.
```
from fastapi_signals import signal
import asyncio

@signal.register
async def handler():
    await asyncio.sleep(3)
    print('Heyy, it works!')
```
### Fire signal in function
Note that only one signal call is allowed using backgroud task.
```
from fastapi_signals import initiate_signal
@app.get("/")
async def endpoint(request):
    await initiate_signal('handler',some_data="value")
    return {"status":"Success"}
```
# Usage - TaskMiddleware
Any number of tasks, no request object needed.
### Add middleware
```
from fastapi_signals import TaskMiddleware
app = FastAPI()
app.add_midleware(TaskMiddleware)
```
### Write handler
Specify how the fired task should work.
```
async def handler():
    await asyncio.sleep(3)
    print('Heyy, it works!')
```
### Fire task in function
```
from fastapi_signals import initiate_task
@app.get("/")
async def endpoint():
    await initiate_task(handler,some_data="value")
    return {"status":"Success"}
```
