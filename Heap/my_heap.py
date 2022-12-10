
class Entidade:
    def __init__(self, prioridade):
        self.prioridade = prioridade

class Heap:
    def __init__(self, vetor):
        self.elementos = []
        vetors = sorted(vetor, key = int, reverse = True)
        for i in range(0, len(vetor)):
            self.inserir(vetors[i])

    def subir(self, pos):
        metade_pos = pos // 2
        if (metade_pos) >= 0:
            if self.elementos[pos].prioridade > self.elementos[metade_pos].prioridade:
                self.elementos[pos], self.elementos[metade_pos] = self.elementos[metade_pos], self.elementos[pos]
                self.subir(metade_pos)

    def descer(self, pos, tamanho):
        if 2*pos == tamanho:
            filho = 2*pos - 1
        elif 2*pos == 0:
            filho = 0
        else:
            filho = 2*pos
        if filho <= tamanho:
            if filho < tamanho - 1:
                if self.elementos[filho + 1].prioridade > self.elementos[filho].prioridade:
                    filho = filho + 1
            if self.elementos[pos].prioridade < self.elementos[filho].prioridade:
                self.elementos[pos].prioridade, self.elementos[filho].prioridade = self.elementos[filho].prioridade, self.elementos[pos].prioridade
                self.descer(filho, tamanho)

    def inserir(self,chave):
        self.elementos.append(Entidade(chave))
        self.subir(len(self.elementos) - 1)

    def remover(self):
        if len(self.elementos) == 1:
            removido = self.elementos[0].prioridade
            self.elementos.clear()
            return removido
        removido = self.elementos[0].prioridade
        self.elementos[0].prioridade = self.elementos[-1].prioridade
        self.elementos.pop()
        if len(self.elementos) > 0:
            self.descer(0, len(self.elementos))
        return removido

    def print_heap(self):
        if len(self.elementos) == 0:
            print("Heap vazio")
        else:
            print("[", end = '')
            for i in range(len(self.elementos)):
                print(self.elementos[i].prioridade, end = ',')
            print("]")

def heap_sort(vetor):
    vetorHS = []
    heap = Heap(vetor)
    m = len(heap.elementos)
    while m > 0:
        aux = heap.remover()
        vetorHS.insert(0,aux)
        m -= 1
    return vetorHS



