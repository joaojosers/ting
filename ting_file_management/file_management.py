import sys


def txt_importer(path_file):
    try:
        # Verifica se a extensão do arquivo é .txt
        if not path_file.lower().endswith(".txt"):
            raise ValueError("Formato inválido")

        # Abre o arquivo para leitura
        with open(path_file, "r") as file:
            # Lê linhas file, retorna lista, remove caracteres quebra linha
            return [line.rstrip("\n") for line in file.readlines()]

    except FileNotFoundError:
        # Caso o arquivo não seja encontrado, exibe a mensagem de erro
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return None

    except ValueError:
        # Caso a extensão do arquivo seja inválida, exibe a mensagem de erro
        print("Formato inválido", file=sys.stderr)
        return None
