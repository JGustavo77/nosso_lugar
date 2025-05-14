from flask import Flask

app = Flask(__name__)

# Importa as rotas
import views

if __name__ == "__main__":
    app.run(debug=True)
