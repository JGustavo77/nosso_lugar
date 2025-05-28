import os
import json
from flask import Flask, render_template, url_for

app = Flask(__name__)

# Ordem desejada dos meses
ORDERED_MONTHS = [
    'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro',
    'Dezembro', 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio'
]

# Poemas para cada mês (mantidos aqui para organização)
POEMAS = {
    'Junho': "Foi em Junho que tudo floresceu... ✨",
    'Julho': "Em Julho, o amor só cresceu.",
    'Agosto': "Agosto chegou com risos e calor.",
    'Setembro': "Setembro nos trouxe sonhos e abraços.",
    'Outubro': "Outubro dançou com nossos corações.",
    'Novembro': "Novembro teve cheiro de eternidade.",
    'Dezembro': "Em Dezembro, o tempo parecia parar.",
    'Janeiro': "Janeiro começou com juras sinceras.",
    'Fevereiro': "Fevereiro foi beijo, riso e verão.",
    'Março': "Março nos uniu mais do que nunca.",
    'Abril': "Abril trouxe paz no olhar.",
    'Maio': "Maio floresceu nosso sentir."
}

def get_gallery_data():
    gallery_path = os.path.join(app.static_folder, 'img')
    gallery_data = {}
    found_months = []

    # Verifica se o diretório base existe
    if not os.path.isdir(gallery_path):
        print(f"Diretório base da galeria não encontrado: {gallery_path}")
        return {}

    # Lista os diretórios (meses) dentro de /static/img
    try:
        month_dirs = [d for d in os.listdir(gallery_path) if os.path.isdir(os.path.join(gallery_path, d))]
        found_months = [m.capitalize() for m in month_dirs] # Capitaliza para corresponder às chaves
    except OSError as e:
        print(f"Erro ao listar diretórios em {gallery_path}: {e}")
        return {}

    # Ordena os meses encontrados de acordo com ORDERED_MONTHS
    ordered_found_months = [m for m in ORDERED_MONTHS if m in found_months]
    # Adiciona meses encontrados que não estão na lista ordenada (caso existam)
    ordered_found_months.extend([m for m in found_months if m not in ORDERED_MONTHS])

    for month_name_capitalized in ordered_found_months:
        month_dir_lower = month_name_capitalized.lower()
        month_path = os.path.join(gallery_path, month_dir_lower)
        media_files = []
        try:
            # Lista arquivos e diretórios, filtra apenas arquivos
            files_in_month = [f for f in os.listdir(month_path) if os.path.isfile(os.path.join(month_path, f))]
            # Filtra extensões comuns de imagem e vídeo
            valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.avi') # Adicione outras se necessário
            media_files = sorted([f for f in files_in_month if f.lower().endswith(valid_extensions)])
        except OSError as e:
            print(f"Erro ao listar arquivos em {month_path}: {e}")
            # Continua para o próximo mês mesmo se um diretório falhar
            continue

        if media_files:
            gallery_data[month_name_capitalized] = media_files

    return gallery_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/galeria')
def galeria():
    gallery_items = get_gallery_data()
    # Passa também os poemas e a ordem dos meses para o template
    return render_template('galeria.html', galeria=gallery_items, poemas=POEMAS, meses_ordenados=list(gallery_items.keys()))

if __name__ == "__main__":
    # A configuração de porta via variável de ambiente é boa para deploy
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' permite acesso externo na rede local
    # debug=True é útil para desenvolvimento, mas desative em produção
    app.run(host="0.0.0.0", port=port, debug=True)

