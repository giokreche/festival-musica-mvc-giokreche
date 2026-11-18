# Tutorial para executar — Festival de Música em MVC

Este projeto foi organizado a partir da atividade dos slides da Aula 16. A aplicação usa Flask, PostgreSQL, Flask-SQLAlchemy, Flask-Migrate e Flask-WTF.

## 1. O que a atividade pede
- Separar o projeto em Model, View e Controller.
- Colocar a criação do Flask e do banco em `app/__init__.py`.
- Criar um controller por entidade.
- Organizar os templates em pastas por entidade.
- Usar `config.py`, `.env` e `run.py`.
- Rodar migrations e conferir se as funcionalidades continuam funcionando.

## 2. Estrutura entregue
- `app/models/models.py`: tabelas e relacionamentos.
- `app/controllers/`: rotas separadas por assunto.
- `app/templates/`: páginas HTML/Jinja organizadas por entidade.
- `app/forms.py`: formulários Flask-WTF com validação.
- `app/__init__.py`: inicializa Flask, SQLAlchemy e Migrate.
- `config.py`: lê as configurações do `.env`.
- `run.py`: inicia o servidor.
- `migrations/`: será criada no seu computador na etapa de migration.

## 3. Instalar ferramentas
1. Instale Python 3.11 ou superior.
2. Instale PostgreSQL e pgAdmin.
3. Instale o Visual Studio Code.
4. Extraia o ZIP para uma pasta simples, por exemplo `C:\Projetos\Atividade_Flask_MVC_Festival`.
5. No VS Code, abra essa pasta (a pasta que contém `run.py`).

## 4. Criar o banco no PostgreSQL
1. Abra o pgAdmin e conecte ao servidor local.
2. Clique com o botão direito em **Databases > Create > Database**.
3. Nomeie o banco como `festival_mvc`.
4. Salve. Não crie tabelas manualmente: as migrations vão criá-las.

## 5. Criar e configurar o .env
1. Na pasta principal, faça uma cópia de `.env.example`.
2. Renomeie a cópia para `.env` (sem `.example`).
3. Abra `.env` e troque `SUA_SENHA` pela senha real do PostgreSQL. Se seu usuário não for `postgres`, ajuste também o usuário.
4. Exemplo: `DATABASE_URL=postgresql://postgres:minhasenha@localhost:5432/festival_mvc`
5. Troque também `SECRET_KEY` por uma frase longa e particular.
6. Não envie o arquivo `.env` para outras pessoas nem para o GitHub. Ele contém credenciais.

Se a senha tiver caracteres especiais como `@`, `#`, `/` ou `:`, a URL pode precisar de codificação desses caracteres. Para evitar esse problema no primeiro teste, use uma senha sem esses caracteres ou peça ajuda para montar a URL corretamente.

## 6. Criar ambiente virtual e instalar dependências
Abra o terminal integrado do VS Code (**Terminal > New Terminal**) na pasta principal e execute, um por vez:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Se o PowerShell bloquear a ativação, execute nesta janela:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## 7. Criar as tabelas com migrations
Confirme que o terminal está na mesma pasta de `run.py` e que o ambiente virtual está ativo. Execute:

```powershell
flask --app run db init
flask --app run db migrate -m "estrutura inicial MVC"
flask --app run db upgrade
```

`db init` é executado somente na primeira vez, para criar a pasta `migrations`. Se essa pasta já existir, não repita `db init`: execute apenas `flask --app run db migrate -m "ajustes"` quando houver mudanças nos models e depois `flask --app run db upgrade`.

## 8. Iniciar o sistema
```powershell
python run.py
```
Abra no navegador: http://127.0.0.1:5000

Para parar o servidor, volte ao terminal e pressione `Ctrl + C`.

## 9. Ordem sugerida para testar
1. Cadastre um palco.
2. Cadastre dois artistas.
3. Cadastre uma apresentação e escolha o palco e os artistas. Para escolher vários artistas, use Ctrl + clique.
4. Edite a apresentação e confira se os artistas já associados continuam selecionados.
5. Abra Artistas > Contrato e cadastre um contrato para cada artista.
6. Edite o contrato existente; o sistema atualiza o registro em vez de criar outro.
7. Teste editar e excluir registros.

## 10. Como os relacionamentos foram modelados
- **1:N:** um `Palco` possui várias `Apresentacao`; a FK `palco_id` fica em `apresentacoes`.
- **N:N:** uma `Apresentacao` pode ter vários `Artista`, e um artista pode participar de várias apresentações; a tabela intermediária é `apresentacao_artista`.
- **1:1:** um `Artista` possui no máximo um `Contrato`; `contratos.artista_id` tem `unique=True` e o relacionamento usa `uselist=False`.

## 11. Erros comuns
- **`Could not open requirements.txt`:** o terminal não está na pasta principal. Use `pwd` e `dir`; abra a pasta que contém `requirements.txt`.
- **`No module named flask`:** ambiente virtual não ativado ou dependências não instaladas. Ative `.venv` e rode `pip install -r requirements.txt`.
- **Erro de autenticação do PostgreSQL:** confira usuário, senha, porta e nome do banco no `.env`.
- **`relation ... does not exist`:** as migrations não foram aplicadas; rode `flask --app run db upgrade`.
- **`TemplateNotFound`:** confira se o arquivo está dentro de `app/templates/` e se o caminho usado no `render_template` está correto.
- **`BuildError`:** o nome usado em `url_for()` deve ser o nome da função do controller.
- **Formulário não valida / erro CSRF:** confira se `SECRET_KEY` está no `.env` e se o template inclui `{{ form.hidden_tag() }}`.

## 12. Relação com os slides
A atividade dos slides orienta rodar um exemplo, reorganizar o trabalho anterior em MVC e conferir se tudo continua funcionando. Este ZIP usa o tema Festival de Música e separa models, controllers, views/templates, formulários e configuração. A estrutura de migrations é criada localmente seguindo os comandos acima.
