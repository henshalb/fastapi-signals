from starlette.responses import Response
from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction, RequestResponseEndpoint
from starlette.types import ASGIApp
from typing import Callable
from starlette.responses import Response


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
