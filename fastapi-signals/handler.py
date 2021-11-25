from functools import wraps
import asyncio


class SignalHandler:

    """
    Decorator hybrid on call collects all handlers on start of server.
    All handlers are collected to registry.
    """

    def __init__(self):
        self._registry = {}

    def handlers(self):
        """
        Will return all the handlers. Helper for _registry.
        """
        return self._registry

    def register(self, _func=None):
        """
        Decorator to register the handler.
        Handler must be asynchronous.
        """
        def _wrap(func):
            if asyncio.iscoroutinefunction(func):
                self._register_handler(func)
            else:
                raise Exception("Signal handler must be async")

            @wraps(func)
            def _wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return _wrapper

        if _func is None:
            return _wrap
        else:
            return _wrap(func=_func)

    def _register_handler(self, func):

        if func.__name__ not in self._registry:
            self._registry[func.__name__] = func
