# fastapi-signals
Signalling for FastAPI.

# motivation
- https://stackoverflow.com/questions/62031695/how-to-use-background-tasks-with-starlette-when-theres-no-background-object
- https://spectrum.chat/ariadne/general/how-to-use-background-tasks-with-starlette~74d56970-5676-4484-8586-a9384e5f4d56
- https://github.com/encode/starlette/issues/436

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
Specify how the fired signal should work.
```
async def handler():
    await asyncio.sleep(3)
    print('Heyy, it works!')
```
### Fire signal in function
Note that only one signal call is allowed using backgroud task.
```
from fastapi_signals import initiate_task
@app.get("/")
async def endpoint():
    await initiate_task(handler,some_data="value")
    return {"status":"Success"}
```