# Nucomp API👩‍💻💻

Esta é a API do site de computação. Nela você encontrara os cruds das seguintes entidades:

- Professor
- Aluno
- Coordenador
- Artigo
- Evento
- Notícia 

Além das funções de login e reset de senha.
# Guia de Uso da Aplicação

Este guia fornece informações sobre como iniciar a aplicação usando Docker Compose e Poetry.

## Docker Compose

Para executar a aplicação usando Docker Compose, siga os passos abaixo:

1. Certifique-se de que você possui o Docker e o Docker Compose instalados em sua máquina.

3. Execute o seguinte comando para construir e iniciar os contêineres da aplicação:

   ```bash
   docker-compose up -d
   ```

Caso queria excutar a aplicação de outra forma, execute os comandos abaixo em sequência:

    export $(cat .env | xargs)

    python3 main.py

Porém, antes disso, certifique-se de ter a virtualenv ou poetry com as dependencias ja instaladas. Caso use o poetry execute o comando abaixo:

    poetry run python main.py
