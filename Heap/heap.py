from my_heap import *

vetor = [10, 5, 1000, 113, 7, 1000000]
heap = Heap(vetor)
heap.print_heap()
heap.inserir(1)
heap.print_heap()
heap.remover()
heap.print_heap()
vetor = heap_sort(vetor)
print(vetor)