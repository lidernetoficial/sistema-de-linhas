import os
import sys
import json
from datetime import datetime
# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'sistema_linhas_secret_key_2024'

# Habilitar CORS para permitir requisições do frontend
CORS(app)

# Caminho para o arquivo de dados
DATA_FILE = os.path.join(os.path.dirname(__file__), 'dados', 'dados.json')
DATA_DIR = os.path.dirname(DATA_FILE)

# Criar diretório de dados se não existir
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# Dados padrão do sistema
DEFAULT_DATA = {
    "users": [
        {
            "id": 1,
            "name": "Oliveira",
            "type": "revendedor",
            "lines": [
                {"servidor": "3", "telefone": "(11) 94120-6749", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91618-9662", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 97478-4488", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 97118-9376", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91020-6118", "vencimento": ""},
                {"servidor": "3", "telefone": "(21) 96742-8641", "vencimento": ""},
                {"servidor": "3", "telefone": "(21) 97261-1187", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 99761-9679", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 96199-7231", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 91965-7531", "vencimento": ""}
            ]
        },
        {
            "id": 2,
            "name": "Ernando",
            "type": "revendedor",
            "lines": [
                {"servidor": "3", "telefone": "(11) 91764-0520", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 92069-0507", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 93718-5417", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 93389-4112", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 94359-5771", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 91195-8075", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 96418-0027", "vencimento": ""},
                {"servidor": "2", "telefone": "(16) 99608-3100", "vencimento": ""},
                {"servidor": "2", "telefone": "(61) 99682-4421", "vencimento": ""},
                {"servidor": "2", "telefone": "(61) 99885-6803", "vencimento": ""},
                {"servidor": "2", "telefone": "(61) 99987-2491", "vencimento": ""},
                {"servidor": "2", "telefone": "(61) 99624-9465", "vencimento": ""},
                {"servidor": "4", "telefone": "(11) 97356-2305", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99872-1390", "vencimento": ""}
            ]
        },
        {
            "id": 3,
            "name": "Flauber",
            "type": "revendedor",
            "lines": [
                {"servidor": "3", "telefone": "(11) 95592-6103", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91614-9214", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 91893-1137", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99971-2986", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99840-6849", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99970-0595", "vencimento": ""}
            ]
        },
        {
            "id": 4,
            "name": "Kennidy",
            "type": "revendedor",
            "lines": [
                {"servidor": "2", "telefone": "(11) 99786-5380", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 95052-2086", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91831-1846", "vencimento": ""},
                {"servidor": "4", "telefone": "(11) 91709-9456", "vencimento": ""}
            ]
        },
        {
            "id": 5,
            "name": "Josefa",
            "type": "revendedor",
            "lines": [
                {"servidor": "3", "telefone": "(11) 93374-0099", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 92069-0158", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 93397-8147", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 97220-8714", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 97591-3562", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99822-2355", "vencimento": ""},
                {"servidor": "lig", "telefone": "(75) 99904-8826", "vencimento": ""}
            ]
        },
        {
            "id": 6,
            "name": "Luiz Paulo Souza",
            "type": "revendedor",
            "lines": [
                {"servidor": "Direto", "telefone": "(11) 91229-7233", "vencimento": ""},
                {"servidor": "Direto", "telefone": "(11) 93399-0328", "vencimento": ""},
                {"servidor": "Direto", "telefone": "(11) 92069-0564", "vencimento": ""},
                {"servidor": "Direto", "telefone": "(11) 91221-2006", "vencimento": ""},
                {"servidor": "Direto", "telefone": "(11) 92069-0605", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91031-7202", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 93060-6716", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91560-3564", "vencimento": ""},
                {"servidor": "3", "telefone": "(11) 91715-4361", "vencimento": ""},
                {"servidor": "3", "telefone": "(21) 99809-3606", "vencimento": ""},
                {"servidor": "2", "telefone": "(11) 97318-1011", "vencimento": ""},
                {"servidor": "T", "telefone": "11 98718-0239", "vencimento": ""},
                {"servidor": "T", "telefone": "11 98718-0998", "vencimento": ""}
            ]
        }
    ],
    "freeLines": [
        {"servidor": "3", "telefone": "(21) 97107-0149", "vencimento": ""},
        {"servidor": "3", "telefone": "(21) 99958-8099", "vencimento": ""},
        {"servidor": "4", "telefone": "(11) 95770-0337", "vencimento": ""},
        {"servidor": "4", "telefone": "(11) 96189-3504", "vencimento": ""},
        {"servidor": "T", "telefone": "11 98718-0073", "vencimento": ""},
        {"servidor": "T", "telefone": "11 98718-0923", "vencimento": ""},
        {"servidor": "T", "telefone": "11 98718-1193", "vencimento": ""}
    ],
    "servers": [
        {"id": 1, "name": "2", "description": "Servidor principal 2", "status": "ativo"},
        {"id": 2, "name": "3", "description": "Servidor principal 3", "status": "ativo"},
        {"id": 3, "name": "4", "description": "Servidor secundário 4", "status": "ativo"},
        {"id": 4, "name": "lig", "description": "Servidor Lig", "status": "ativo"},
        {"id": 5, "name": "T", "description": "Servidor T", "status": "ativo"},
        {"id": 6, "name": "Direto", "description": "Servidor Direto", "status": "ativo"}
    ],
    "timestamp": datetime.now().isoformat(),
    "version": "2.0"
}

def load_data():
    """Carrega dados do arquivo JSON ou retorna dados padrão"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                print(f"Dados carregados do arquivo: {len(data.get('users', []))} usuários")
                return data
        else:
            print("Arquivo de dados não encontrado, usando dados padrão")
            save_data(DEFAULT_DATA)
            return DEFAULT_DATA
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return DEFAULT_DATA

def save_data(data):
    """Salva dados no arquivo JSON"""
    try:
        data['timestamp'] = datetime.now().isoformat()
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Dados salvos com sucesso: {len(data.get('users', []))} usuários")
        return True
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")
        return False

@app.route('/api/data', methods=['GET'])
def get_data():
    """Endpoint para carregar dados"""
    try:
        data = load_data()
        return jsonify({
            'success': True,
            'data': data,
            'message': 'Dados carregados com sucesso'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Erro ao carregar dados'
        }), 500

@app.route('/api/data', methods=['POST'])
def save_data_endpoint():
    """Endpoint para salvar dados"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'message': 'Nenhum dado fornecido'
            }), 400
        
        # Validar estrutura básica dos dados
        required_keys = ['users', 'freeLines', 'servers']
        for key in required_keys:
            if key not in data:
                return jsonify({
                    'success': False,
                    'message': f'Campo obrigatório ausente: {key}'
                }), 400
        
        success = save_data(data)
        
        if success:
            return jsonify({
                'success': True,
                'message': 'Dados salvos com sucesso',
                'timestamp': data.get('timestamp')
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Erro ao salvar dados'
            }), 500
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Erro interno do servidor'
        }), 500

@app.route('/api/backup', methods=['GET'])
def create_backup():
    """Endpoint para criar backup dos dados"""
    try:
        data = load_data()
        filename = f"sistema_linhas_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        return jsonify({
            'success': True,
            'data': data,
            'filename': filename,
            'message': 'Backup criado com sucesso'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Erro ao criar backup'
        }), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Endpoint para verificar status do servidor"""
    try:
        data_exists = os.path.exists(DATA_FILE)
        data = load_data() if data_exists else None
        
        return jsonify({
            'success': True,
            'status': 'online',
            'data_file_exists': data_exists,
            'data_file_path': DATA_FILE,
            'users_count': len(data.get('users', [])) if data else 0,
            'free_lines_count': len(data.get('freeLines', [])) if data else 0,
            'servers_count': len(data.get('servers', [])) if data else 0,
            'last_update': data.get('timestamp') if data else None,
            'version': data.get('version', '2.0') if data else '2.0'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Erro ao verificar status'
        }), 500

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Servir arquivos estáticos"""
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return jsonify({
                'message': 'Sistema de Gerenciamento de Linhas - Backend API',
                'version': '2.0',
                'endpoints': {
                    'GET /api/data': 'Carregar dados',
                    'POST /api/data': 'Salvar dados',
                    'GET /api/backup': 'Criar backup',
                    'GET /api/status': 'Status do servidor'
                }
            })

if __name__ == '__main__':
    print("=== Sistema de Gerenciamento de Linhas - Backend ===")
    print(f"Diretório de dados: {DATA_DIR}")
    print(f"Arquivo de dados: {DATA_FILE}")
    print("Iniciando servidor...")
    
    # Carregar dados iniciais
    load_data()
    
    app.run(host='0.0.0.0', port=5000, debug=False)

