from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.yaml'  # шлях до файлу swagger.yaml
swaggerui_bp = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Meteostation API"}
)
app.register_blueprint(swaggerui_bp, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(debug=True)
