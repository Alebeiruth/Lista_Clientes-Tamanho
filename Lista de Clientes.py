### Lista de Clientes, Tamanho e Entregas ###

primeiro_nome = ["Any", "Benicio", "Charles", "Daphne"]
preferencia_tamanho = ["Pequeno", "Grande", "Medio"]

preferencia_tamanho.append("Medio")
print(preferencia_tamanho)

cliente_data = [["Any", "Pequeno", True], ["Benicio", "Grande", False], ["Charles", "Medio", True], ["Daphme", "Medio", False]]
print(cliente_data)

cliente_data[-2][-1] = False
print(cliente_data)

cliente_data[1].remove(False)
print(cliente_data)

cleinte_data_final = cliente_data + [["Adam", "Grande", True], ["Karina", "Extra Grande", False]]
print(cleinte_data_final)