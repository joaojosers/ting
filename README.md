# ting

## Contexto
- O projeto requer a implementação de um programa que simule um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos TXT.
### o programa desenvolvido deverá ter dois módulos
- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT).
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.

## Habilidades a serem trabalhadas
- Manipular Pilhas, Deque, Nó & Listas Ligadas e Listas Duplamente Ligadas.

## Crie o ambiente virtual para o projeto
```
python3 -m venv .venv && source .venv/bin/activate
```
## Instalando Dependências
```
python3 -m pip install -r dev-requirements.txt
```
## Executando Testes
* executando todos os testes
 ```
 python3 -m pytest
```
* Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
## Arquivos desenvolvidos pela Trybe
* src:
  - dev-requirements.txt
  - requirements.txt