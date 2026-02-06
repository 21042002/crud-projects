# python-crud

Documentação de uso do arquivo `CadastroUsuario.py` e o banco de dados local.

Descrição
- O diretório contém um projeto CRUD em Python. O arquivo `CadastroUsuario.py` implementa operações básicas de cadastro e leitura de usuários.

Banco de dados
- O banco de dados foi criado localmente para este projeto (simulado por um arquivo local). Não há dependência de um servidor externo; os dados são persistidos localmente no diretório do projeto.

Dependências
- Se o projeto utiliza apenas bibliotecas padrão do Python (por exemplo, `sqlite3`), não é necessário instalar pacotes adicionais. Basta importar as bibliotecas no código.
- Caso o projeto exija bibliotecas externas, instale-as com `pip install -r requirements.txt`. Verifique o `requirements.txt` no diretório do projeto quando presente.

Uso
1. Recomenda-se criar um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Se houver `requirements.txt`, instale dependências:

```bash
pip install -r requirements.txt
```

3. Executar o script de cadastro de usuário:

```bash
python3 CadastroUsuario.py
```

Observações
- O arquivo que originalmente continha exemplos de como conectar a um banco de dados foi manipulado localmente para simular o comportamento de um banco de dados; ele serve apenas para demonstração e não substitui um banco real em produção.
- Antes de abrir PRs, documente alterações e inclua instruções claras no README do subprojeto.
