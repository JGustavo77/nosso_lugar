import os
from flask import Flask
from views import views_blueprint

app = Flask(__name__)
app.register_blueprint(views_blueprint)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=True, host="0.0.0.0", port=port)
