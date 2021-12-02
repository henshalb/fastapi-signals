import asyncio
from threading import Thread
from starlette.responses import Response
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.types import ASGIApp, Receive, Scope, Send
from typing import Callable, Iterable, List, Tuple
from starlette.responses import Response
from .main import task

class SignalMiddleware(BaseHTTPMiddleware):

    """Middleware to dispatch modified response"""

    def __init__(self, app: ASGIApp,
                 dispatch: DispatchFunction = None,
                 handler: Callable = None) -> None:
        super().__init__(app, dispatch=dispatch)
        self.handler = handler

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint) -> Response:
        request.state.background = None
        response = await call_next(request)
        if request.state.background:
            response.background = request.state.background
        return response


class TaskMiddleware(BaseHTTPMiddleware):

    """Middleware that updates queue with new task and initiate runner"""

    async def dispatch(
            self,
            request: Request,
            call_next: RequestResponseEndpoint) -> Response:
        response = await call_next(request)
        asyncio.run_coroutine_threadsafe(task.handler(), task.loop)
        return response
