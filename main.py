def adicionar_paciente(fila, nome, numero_carteirinha, prioridade):
    fila.append((prioridade, nome, numero_carteirinha))
    fila.sort()  # Ordena a fila para garantir prioridade

def chamar_proximo(fila):
    if fila:
        _, nome, numero_carteirinha = fila.pop(0)
        return f"{nome} ({numero_carteirinha})"
    return None

def listar_fila(fila):
    return [f"{nome} ({numero_carteirinha}) - Prioridade: {prioridade}" for prioridade, nome, numero_carteirinha in fila]

# Exemplo de uso
fila = []
adicionar_paciente(fila, "Ana", "12345", 2)  # Agendado
adicionar_paciente(fila, "Carlos", "67890", 1)  # Urgência
adicionar_paciente(fila, "Bruna", "54321", 2)  # Agendado

print("Ordem de chamada:")
while (paciente := chamar_proximo(fila)) is not None:
    print(paciente)
