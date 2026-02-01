import sys
import json
import uuid
from typing import Dict, Optional, Any
from pypulsar.ipc.api import Api

IS_ANDROID = (
    "android" in sys.platform.lower()
    or "chaquopy" in sys.modules
    or getattr(sys, "getandroidapilevel", None) is not None
)
webview = None
if not IS_ANDROID:
    try:
        import webview
    except ImportError:
        webview = None
        print("[PyPulsar] pywebview is not installed. Desktop engine will not work.")

class WindowManager:
    def __init__(self, engine, hooks):
        self.engine = engine
        self.Hooks = hooks
        if IS_ANDROID:
            self.windows: Dict[str, Any] = {}
            self.main_webview: Optional[Any] = None
        else:
            self.windows: Dict[str, webview.Window] = {}
            self.main_window_id = None

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
        if IS_ANDROID:
            if is_main and hasattr(self.engine, "_main_webview"):
                self.main_webview = self.engine._main_webview
                self.windows[window_id] = self.main_webview
                print(f"[PyPulsar] Main window registered with id {window_id}")
        else:
            if webview is None:
                raise RuntimeError("pywebview is required on desktop platforms")
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
        if IS_ANDROID:
            return
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

    def get_window(self, window_id: str) -> Any:
        return self.windows.get(window_id)

    def close_window(self, window_id: str):
        window = self.get_window(window_id)
        if window and not IS_ANDROID:
            window.destroy()

    def evaluate_js(self, window_id: str, js_code: str):
        window = self.get_window(window_id)
        if window:
            if IS_ANDROID:
                window.evaluate_js(js_code)
            else:
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


