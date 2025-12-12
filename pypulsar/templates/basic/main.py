from pypulsar.engine import Engine
engine = Engine(serve=True, webroot="web", debug=True)
engine.create_window("/index.html", "Photon APP", 900, 700)
engine.run()
