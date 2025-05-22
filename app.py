from flask import Flask
import views  # importa o arquivo, NÃO uma variável ou objeto

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)
