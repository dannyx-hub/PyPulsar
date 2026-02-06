"""
Basic example of a PyPulsar desktop application using React for the frontend.
"""

from pypulsar.engine.desktop_engine import DesktopEngine

engine = DesktopEngine(
    debug=True,
    serve=True, # if you want to use Vite dev server, set this to False
    port=3000,   # if serve is False this argument is irelevant       
    webroot="web/dist", # same as port if serve is False
)


if __name__ == "__main__":
    engine.create_window(
        title="PyPulsar + React",
        width=1200,
        height=800,
        path="/index.html" # if serve is False, write path for vite dev server e.g. "http://localhost:3000"
    )
    engine.run()