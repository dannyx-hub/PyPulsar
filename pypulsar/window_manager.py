import uuid
from typing import Dict
from pypulsar.ipc.api import Api
import webview


class WindowManager:
    def __init__(self, engine, hooks):
        self.engine = engine
        self.windows: Dict[str, webview.Window] = {}
        self.main_window_id = None
        self.Hooks = hooks

    def create_window(
            self,
            is_main: bool = True,
            url=None,
            title="PyPulsar",
            width=1000,
            height=700,
            resizable=True
    ) -> str:
        window_id = "main" if is_main else str(uuid.uuid4())

        api = Api(self.engine, window_id)

        window = webview.create_window(
            js_api=api,
            text_select=True,
            url=url,
            width=width,
            height=height,
            resizable=resizable,
            title=title,
        )

        self.windows[window_id] = window
        if is_main:
            self.main_window_id = window_id

        window.events.closed += lambda: self._on_window_closed(window_id)
        window.events.resized += lambda w, h: self.engine.emit_hook(
            "on_window_resized", window_id, w, h
        )

        self.engine.emit_hook(self.Hooks.ON_WINDOW_CREATE, window_id, window)
        return window_id

    def _on_window_closed(self, window_id):
        if not window_id in self.windows:
            return
        is_main = (window_id == self.main_window_id)
        del self.windows[window_id]
        self.engine.emit_hook("on_window_closed", window_id)
        if is_main:
            for wid, window in list(self.windows.items()):
                try:
                    window.destroy()
                except Exception:
                    pass

            self.windows.clear()
            self.engine.quit()

    def get_window(self, window_id: str) -> webview.Window:
        return self.windows.get(window_id)

    def close_window(self, window_id: str):
        window = self.get_window(window_id)
        if window:
            window.destroy()

    def evaluate_js(self, window_id: str, js_code: str):
        window = self.get_window(window_id)
        if window:
            window.evaluate_js(js_code)

    def broadcast_event(self, event: str, data: dict):
        payload = json.dumps({
            "event": event,
            "data": data
        })

        for window_id in self.windows:
            self.evaluate_js(
                window_id,
                f"window.dispatchEvent(new CustomEvent('pypulsar', {{ detail: {payload} }}));"
            )


