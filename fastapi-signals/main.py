
from starlette.background import BackgroundTask
from starlette.requests import Request
from .handler import SignalHandler

signal = SignalHandler()


async def initiate_signal(
        request: Request,
        name: str,
        **kwargs: dict) -> None:
    """
    Will fire the signal. Can also be a coroutine. Long running
    background tasks will be terminated by host.

    Args:
        request (Request): Do not remove request object
        name (str): Handler name without spaces
    """
    task = BackgroundTask(signal.handlers().get(name), **kwargs)
    request.state.background = task
