import os
from typing import Optional
import json
import toga
from pypulsar.engine.base_engine import BaseEngine, Hooks


class AndroidEngine(BaseEngine):
    def __init__(
        self,
        debug: bool = False,
        serve: bool = True,
        port: int = 8080,
        webroot: str = "web",
    ):
        super().__init__(debug, serve, port, webroot)
        self._app: Optional[toga.App] = None
        self._main_webview: Optional[toga.WebView] = None
        self._windows: dict[str, toga.WebView] = {}

    def run(self):
        class PyPulsarAndroidApp(toga.App):
            def startup(app_self):
                url = "file:///android_asset/web/index.html"
                self._main_webview = toga.WebView(
                    url=url, on_web_message=self._on_web_message
                )
                main_box = toga.Box(children=[self._main_webview])
                main_window = toga.MainWindow(title="PyPulsar", size=(1000, 700))
                main_window.content = main_box
                app_self.main_window = main_window
                main_window.show()
                self.emit_hook(Hooks.ON_APP_START)

        self._app = PyPulsarAndroidApp(
            formal_name="PyPulsar",
            app_id="org.pypulsar.android",
        )
        self._app.engine = self
        self._app.main_loop()

    def _on_web_message(self, widget, message: str):
        try:
            data = json.loads(message)
            self.message_queue.put_nowait(
                {
                    "event": data.get("event", "web_message"),
                    "data": data.get("data", message),
                    "window_id": "main",
                }
            )
        except Exception as e:
            print(f"[PyPulsar] Error handling web message: {e}")

    def send_to_window(self, window_id: str, js_code: str):
        webview = self._windows.get(window_id, self._main_webview)
        if webview:
            webview.evaluate_js(js_code)
        else:
            print(f"[PyPulsar] No window found with ID: {window_id}")

    def quit(self):
        if self._app:
            self._app.exit()

