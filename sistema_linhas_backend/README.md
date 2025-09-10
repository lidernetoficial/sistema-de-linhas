# Sistema de Gerenciamento de Linhas Pro - Versão 2.0

## 🚀 Instalação Automática em VPS

Sistema completo com backend Flask e persistência automática de dados em JSON.

### 📋 Pré-requisitos

- VPS com Ubuntu 18.04+ ou Debian 9+
- Acesso SSH como usuário não-root com sudo
- Conexão com internet

### ⚡ Instalação com Um Comando

```bash
curl -sSL https://raw.githubusercontent.com/seu-usuario/sistema-linhas/main/install.sh | bash
```

**OU** faça o download manual:

```bash
wget https://github.com/seu-usuario/sistema-linhas/archive/main.zip
unzip main.zip
cd sistema-linhas-main
chmod +x install.sh
./install.sh
```

### 🔧 O que a Instalação Faz

1. **Atualiza o sistema** e instala dependências
2. **Cria ambiente Python** com Flask e dependências
3. **Configura o backend** com API REST completa
4. **Instala e configura Nginx** como proxy reverso
5. **Cria serviço systemd** para inicialização automática
6. **Configura logs** e monitoramento
7. **Testa a instalação** e fornece URLs de acesso

### 🌐 Acesso ao Sistema

Após a instalação, acesse:
- **URL Principal:** `http://SEU_IP_VPS`
- **API Status:** `http://SEU_IP_VPS/api/status`
- **API Dados:** `http://SEU_IP_VPS/api/data`

### 📁 Estrutura de Arquivos

```
/home/usuario/sistema_linhas/
├── src/
│   ├── main.py              # Aplicação Flask principal
│   ├── dados/
│   │   └── dados.json       # Arquivo de dados persistente
│   └── static/
│       └── index.html       # Frontend do sistema
├── venv/                    # Ambiente virtual Python
├── logs/                    # Logs da aplicação
├── gunicorn.conf.py         # Configuração do Gunicorn
├── start.sh                 # Script para iniciar sistema
├── stop.sh                  # Script para parar sistema
├── status.sh                # Script para verificar status
└── install.sh               # Script de instalação
```

### 🎮 Comandos de Controle

```bash
# Iniciar sistema
./start.sh

# Parar sistema
./stop.sh

# Ver status
./status.sh

# Ver logs em tempo real
tail -f logs/error.log
```

### 🔧 Comandos Systemd

```bash
# Controle do serviço
sudo systemctl start sistema-linhas
sudo systemctl stop sistema-linhas
sudo systemctl restart sistema-linhas
sudo systemctl status sistema-linhas

# Habilitar/desabilitar inicialização automática
sudo systemctl enable sistema-linhas
sudo systemctl disable sistema-linhas
```

### 📊 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/api/data` | Carregar todos os dados |
| POST | `/api/data` | Salvar dados |
| GET | `/api/backup` | Criar backup dos dados |
| GET | `/api/status` | Status do servidor |

### 🔄 Funcionalidades

#### ✅ Salvamento Automático
- Dados são salvos automaticamente após qualquer modificação
- Não é necessário baixar/substituir arquivos manualmente
- Persistência garantida no arquivo `dados.json`

#### ✅ Backup Automático
- Backup com timestamp no nome do arquivo
- Download direto pelo navegador
- Estrutura JSON completa preservada

#### ✅ API REST Completa
- Endpoints para todas as operações
- Validação de dados
- Tratamento de erros
- Logs detalhados

#### ✅ Interface Web Responsiva
- Mesmo design e funcionalidades
- Comunicação transparente com API
- Indicadores visuais de status
- Notificações em tempo real

### 🛠️ Configuração Avançada

#### Alterar Porta

1. Edite `gunicorn.conf.py`:
```python
bind = "0.0.0.0:8080"  # Nova porta
```

2. Edite `/etc/nginx/sites-available/sistema-linhas`:
```nginx
proxy_pass http://127.0.0.1:8080;  # Nova porta
```

3. Reinicie os serviços:
```bash
sudo systemctl restart sistema-linhas
sudo systemctl restart nginx
```

#### Configurar HTTPS

1. Instale Certbot:
```bash
sudo apt install certbot python3-certbot-nginx
```

2. Obtenha certificado SSL:
```bash
sudo certbot --nginx -d seu-dominio.com
```

#### Backup dos Dados

```bash
# Backup manual
cp src/dados/dados.json backup_$(date +%Y%m%d_%H%M%S).json

# Backup automático (crontab)
0 2 * * * cp /home/usuario/sistema_linhas/src/dados/dados.json /home/usuario/backups/dados_$(date +\%Y\%m\%d).json
```

### 🔍 Monitoramento e Logs

#### Logs da Aplicação
```bash
# Logs de erro
tail -f logs/error.log

# Logs de acesso
tail -f logs/access.log

# Logs do systemd
sudo journalctl -u sistema-linhas -f
```

#### Monitoramento de Recursos
```bash
# Uso de CPU e memória
htop

# Espaço em disco
df -h

# Status dos serviços
sudo systemctl status sistema-linhas nginx
```

### 🚨 Solução de Problemas

#### Serviço não inicia
```bash
# Verificar logs
sudo journalctl -u sistema-linhas -n 50

# Verificar configuração
cd /home/usuario/sistema_linhas
source venv/bin/activate
python src/main.py
```

#### Nginx não funciona
```bash
# Testar configuração
sudo nginx -t

# Verificar logs
sudo tail -f /var/log/nginx/error.log
```

#### Dados não salvam
```bash
# Verificar permissões
ls -la src/dados/

# Verificar logs da aplicação
tail -f logs/error.log
```

#### Porta já em uso
```bash
# Verificar o que está usando a porta
sudo netstat -tlnp | grep :5000

# Matar processo se necessário
sudo kill -9 PID_DO_PROCESSO
```

### 🔒 Segurança

#### Firewall
```bash
# Permitir apenas HTTP/HTTPS
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

#### Atualizações
```bash
# Atualizar sistema
sudo apt update && sudo apt upgrade

# Atualizar dependências Python
cd /home/usuario/sistema_linhas
source venv/bin/activate
pip install --upgrade flask flask-cors gunicorn
```

### 📞 Suporte

Para problemas ou dúvidas:

1. **Verifique os logs** primeiro
2. **Consulte a documentação** de solução de problemas
3. **Teste em ambiente local** se possível
4. **Documente o erro** com logs e passos para reproduzir

### 📝 Changelog

#### Versão 2.0
- ✅ Backend Flask com API REST
- ✅ Persistência automática em JSON
- ✅ Instalação automatizada para VPS
- ✅ Configuração Nginx + Gunicorn
- ✅ Serviço systemd
- ✅ Scripts de controle
- ✅ Logs estruturados
- ✅ Backup automático

#### Versão 1.0
- ✅ Sistema HTML standalone
- ✅ Dados em localStorage
- ✅ Interface responsiva
- ✅ CRUD completo de usuários
- ✅ Importação de linhas

---

**Sistema de Gerenciamento de Linhas Pro v2.0**  
*Desenvolvido por Manus AI*

