
class Entidade:
    def __init__(self, chave):
        self.chave = chave

class T_Hash:
    def __init__(self, tamanho):
        self.elementos = [[]]
        self.tamanho = tamanho
        for i in range(tamanho - 1):
            self.elementos.append([])


    def fun_hash(self, chave):
        hash_key = chave % (self.tamanho - 1)
        return hash_key

    def inserir(self, chave):
        if self.buscar(chave)[0] != 1:
            hash_key = self.fun_hash(chave)
            self.elementos[hash_key].append(Entidade(chave))
        else:
            print("chave já inserida na tabela")
            return None

    def print_hash(self):
        for i in range(len(self.elementos)):
            print("[", i, "] ", end='[ ')
            for j in range(0, len(self.elementos[i])):
                print(self.elementos[i][j].chave, end=',')
            print("]")





    def buscar(self, chave):
        hash_key = self.fun_hash(chave)
        for i in range(len(self.elementos[hash_key])):
            if chave == self.elementos[hash_key][i].chave:
               return[1, self.elementos[hash_key][i]]
            else:
                return[0, self.elementos[hash_key][-1]]
        return[0, None]

    def remover(self, chave):
        removido = self.buscar(chave)
        hash_key = self.fun_hash(chave)
        if removido[0] == 1:
            self.elementos[hash_key].remove(removido[0])
        else:
            print("chave não inserida na tabela")

