import asyncio
from pypulsar.acl import acl

class Api:
    def __init__(self, engine, window_id):
        self.engine = engine
        self.window_id = window_id

    def send(self, event, data):
        if not acl.validate(event, data):
            return

        message = {
            "event": event,
            "data": data,
            "window_id": self.window_id
        }

        asyncio.run_coroutine_threadsafe(
            self.engine.message_queue.put(message),
            self.engine.loop
        )
