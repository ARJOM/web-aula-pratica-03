# Prática colaborativa
Para este exercício você deve fazer um fork deste repositório, clonar em sua máquina e executar as tarefas a seguir:
- Incremente o modelo `Student` com campos que considere pertinentes
- Crie a tela de cadastro, bem como sua view
- Modifique a tela de listagem para fazer o que se pede nos comentários

Ao finalizar, crie uma pull request para o repositório original. Você deve solicitar a revisão do estudante à sua frente na chamada.
### Executando Django

1. Crie um ambiente virtual
```
python -m venv venv
```
2. Ative o ambiente virtual
```
source venv/bin/activate
```
3. Instale as dependências do projeto
```
pip install -r requirements.txt
```
4. Execute as migrações
```
python manage.py migrate
```

5. Crie um super usuário
```
python manage.py createsuperuser
```

6. Execute o projeto
```
python manage.py runserver