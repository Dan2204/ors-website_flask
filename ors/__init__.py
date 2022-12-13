from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "Don'ttrythisathomefolks!@!@!£$"


# <== IMPORT BLUEPRINTS <==
from ors.core import bp as core_bp

# <== REGISTER BLUEPRINTS <==
app.register_blueprint(core_bp)
