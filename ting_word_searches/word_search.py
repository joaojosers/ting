from typing import List

from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue) -> List[dict]:
    results = []

    for i in range(len(instance)):
        file_info = instance.search(i)
        print("aqui está", file_info)
        # Caso a palavra seja encontrada no arquivo, armazena as informações
        occurrences = []
        for line_num, line in enumerate(
            file_info["linhas_do_arquivo"], start=1
        ):
            if word.lower() in line.lower():
                occurrences.append({"linha": line_num})

        if occurrences:
            result_entry = {
                "palavra": word,
                "arquivo": file_info["nome_do_arquivo"],
                "ocorrencias": occurrences,
            }
            results.append(result_entry)

    # print('aqui',results)
    return results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
