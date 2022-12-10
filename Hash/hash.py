from my_hash import T_Hash

hash = T_Hash(7)
hash.inserir(1)
hash.inserir(2)
hash.inserir(3)
hash.inserir(4)
hash.inserir(8)
hash.print_hash()
print(hash.buscar(1), hash.buscar(1)[1].chave)