# def process(path_file, instance):
#     """Aqui irá sua implementação"""


# def remove(instance):
#     """Aqui irá sua implementação"""


# def file_metadata(instance, position):
#     """Aqui irá sua implementação"""

from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    # Obtém o nome do arquivo a partir do caminho completo
    file_name = path_file

    # Verifica se o arquivo já foi processado anteriormente
    if file_name in instance._data:
        print(
            f"Arquivo {file_name} já foi processado anteriormente. Ignorando."
        )
        return

    # Importa as linhas do arquivo usando a função txt_importer
    file_lines = txt_importer(path_file)

    if file_lines is not None:
        # Cria um dicionário com as informações solicitadas
        file_info = {
            "nome_do_arquivo": file_name,
            "qtd_linhas": len(file_lines),
            "linhas_do_arquivo": file_lines,
        }

        # Adiciona o nome do arquivo à fila
        instance.enqueue(file_name)

        # Mostra os dados processados via stdout
        print(file_info)


# Exemplo de uso
if __name__ == "__main__":
    # Crie uma instância da fila
    my_queue = Queue()

    # Substitua "caminho/do/arquivo.txt" pelo caminho do arquivo desejado
    arquivo = "statics/arquivo_teste.txt"

    # Execute a função process
    process(arquivo, my_queue)

# def remove(instance):
#     """Aqui irá sua implementação"""

# def file_metadata(instance, position):
#     """Aqui irá sua implementação"""


# Implemente a função remove
def remove(instance):
    # print(instance)
    # try:
    #     instance.dequeue()
    # except IndexError:
    #     print('Não há elementos')
    inst = instance.dequeue()
    if inst is None:
        print("Não há elementos")


# Implemente a função file_metadata
def file_metadata(instance, position):
    if 0 <= position < len(instance):
        file_name = instance.search(position)
        file_lines = txt_importer(file_name)

        if file_lines is not None:
            metadata = {
                "nome_do_arquivo": file_name,
                "qtd_linhas": len(file_lines),
                "linhas_do_arquivo": file_lines,
            }
            return metadata
    else:
        raise IndexError("Posição Inválida")


# def process(path_file, instance):
#     # Obtém o nome do arquivo a partir do caminho completo
#     file_name = path_file

#     # Verifica se o arquivo já foi processado anteriormente
#     if file_name in instance:
#         print(f"Arquivo {file_name} já foi processado anteriormente. Ignorando.")
#         return

#     # Importa as linhas do arquivo usando a função txt_importer
#     file_lines = txt_importer(path_file)

#     if file_lines is not None:
#         # Cria um dicionário com as informações solicitadas
#         file_info = {
#             "nome_do_arquivo": file_name,
#             "qtd_linhas": len(file_lines),
#             "linhas_do_arquivo": file_lines
#         }

#         # Adiciona o nome do arquivo à fila
#         instance.enqueue(file_name)

#         # Mostra os dados processados via stdout
#         print(file_info)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""


# Exemplo de uso
if __name__ == "__main__":
    # Crie uma instância da fila
    my_queue = Queue()

    # Substitua "caminho/do/arquivo.txt" pelo caminho do arquivo desejado
    arquivo = "statics/arquivo_teste.txt"

    # Execute a função process
    process(arquivo, my_queue)


# def process(path_file, instance):
#      def __init__(self) -> None:
#         self.jobs_list = list()
#     # Obtém o nome do arquivo a partir do caminho completo
#     file_name = path_file

#     # Verifica se o arquivo já foi processado anteriormente
#         if file_name in file_queue:
#             print(f"Arquivo {file_name} já foi processado anteriormente. Ignorando.")
#         return

#     # Importa as linhas do arquivo usando a função txt_importer
#         ile_lines = txt_importer(file_path)

#         if file_lines is not None:
#         # Cria um dicionário com as informações solicitadas
#         file_info = {
#             "nome_do_arquivo": file_name,
#             "qtd_linhas": len(file_lines),
#             "linhas_do_arquivo": file_lines
#         }

#         # Adiciona o nome do arquivo à fila
#         file_queue.enqueue(file_name)

#         # Mostra os dados processados via stdout
#         print(file_info)

# # Exemplo de uso
# if __name__ == "__main__":
#     # Crie uma instância da fila
#     my_queue = Queue()

#     # Substitua "caminho/do/arquivo.txt" pelo caminho do arquivo desejado
#     arquivo = "statics/arquivo_teste.txt"

#     # Execute a função process
#     process(my_queue, arquivo)
