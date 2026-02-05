"""
Advanced example of a PyPulsar desktop application using React for the frontend.
This example demonstrates how to set up a more complex application state,
handle multiple API calls, and manage application settings and file operations.

"""

import os
from pypulsar.engine.desktop_engine import DesktopEngine
from pypulsar.acl import acl

app_state = {
    "counter": 0,
    "settings": {"theme": "light", "language": "en"},
    "files": []
}

engine = DesktopEngine(
    debug=True,
    serve=False, # if you want to use bulit frontend, set this to True
    port=3000, # if serve is False this argument is irelevant
    webroot="web/dist", # same as port if serve is False
)

acl.allow("get_app_state")
acl.allow("update_counter")
acl.allow("reset_counter")
acl.allow("save_settings")
acl.allow("load_files")
acl.allow("read_file")

def get_app_state(payload=None):
    return app_state

def update_counter(payload: dict):
    action = payload.get("action", "increment")
    step = payload.get("step", 1)
    if action == "increment":
        app_state["counter"] += step
    elif action == "decrement":
        app_state["counter"] -= step
    engine.emit_to_js("state_updated", {"counter": app_state["counter"]})
    return {"counter": app_state["counter"]}

def reset_counter(payload=None):
    app_state["counter"] = 0
    engine.emit_to_js("state_updated", {"counter": app_state["counter"]})
    return {"counter": app_state["counter"]}

def save_settings(payload: dict):
    app_state["settings"].update(payload)
    return {"settings": app_state["settings"]}

def load_files(payload: dict):
    directory = payload.get("directory", ".")
    try:
        files = os.listdir(directory)
        app_state["files"] = files
        return {"files": files}
    except Exception as e:
        return {"error": str(e)}

def read_file(payload: dict):
    file_path = payload.get("path")
    if not file_path:
        return {"error": "No path provided"}
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return {"content": content}
    except Exception as e:
        return {"error": str(e)}

engine.expose_api({
    "get_app_state": get_app_state,
    "update_counter": update_counter,
    "reset_counter": reset_counter,
    "save_settings": save_settings,
    "load_files": load_files,
    "read_file": read_file,
})

if __name__ == "__main__":
    engine.create_window(
        title="Advanced PyPulsar + React App",
        width=1400,
        height=900,
        path="http://localhost:3000/" # if serve is True and react frontend is built, write path for index.html in webroot, if serve is False write path for Vite dev server"
    )
    engine.run()