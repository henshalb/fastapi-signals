from setuptools import setup
setup(
    name='fastapi-signals',
    packages=['fastapi_signals'],
    version='0.1.1',
    license='MIT',
    description='Signalling for FastAPI.',
    long_description="""# fastapi-signals
Signalling for FastAPI.

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
```""",
    long_description_content_type="text/markdown",
    author='Henshal B',
    author_email='henshalb@gmail.com',
    url='https://github.com/henshalb/fastapi-signals.git',
    download_url='https://github.com/henshalb/fastapi-signals/archive/refs/tags/v0.1.1.tar.gz',
    keywords=['fastapi', 'signals', 'fastapi-signals', 'background task'],
    install_requires=[
        'starlette',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
