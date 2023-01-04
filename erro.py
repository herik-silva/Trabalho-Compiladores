class Erro:
    codigo_status: int
    linha_erro: int

    def __init__(self, codigo: int, linha: int):
        self.codigo_status = codigo
        self.linha_erro = linha

    def _encontrarErro(self) -> str:
        """Encontra e retorna o erro de acordo com o código"""
        dicionario = {
            0: "Descrição do Erro",
            1: "Ou sô"
        }

        try:
            return dicionario[self.codigo_status]
        except:
            raise "Erro não encontrado"

    def exibirErro(self):
        """Exibe o erro"""
        try:
            print("Erro na linha {}: {} - {}".format(self.linha_erro, self._encontrarErro(), self.codigo_status))
        except:
            print("Erro no erro!! F")