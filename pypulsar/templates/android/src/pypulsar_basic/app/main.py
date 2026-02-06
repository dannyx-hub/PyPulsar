import os
from pypulsar.engine.android_engine import AndroidEngine

def app():
    engine = AndroidEngine(
        debug=True,
        serve=False  # Parametr dla kompatybilności z BaseEngine
    )
    
    print("[App] Starting PyPulsar on Android with Asset Manager")
    
    engine.run()