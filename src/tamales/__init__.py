from flask import Flask

__version__ = '0.1.2'

app = Flask(__name__)
app.config.from_object('tamales.default_settings')
app.config.from_envvar('TAMALES_SETTINGS', silent=True)

import tamales.views
