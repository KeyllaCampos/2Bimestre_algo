pacotes = (("ABC123", "Enviado"),("DEF456", "Em Trânsito"),("XYZ789", "Recebido"),("PQR987", "Em Trânsito"),("JKL321", "Enviado"),("MNO654", "Recebido"),("STU741", "Enviado"))

print(" Pacotes cadastrados: ", pacotes)

enviados = 0
recebidos = 0
em_transito = 0

for i in range(len(pacotes)):
   status = pacotes[i][1]
   if status == "Enviado":
      enviados = enviados + 1
   if status == "Recebido":
      recebidos = recebidos + 1
   if status == "Em Trânsito":
      em_transito = em_transito + 1

print("Contagem de status")
print("Enviados:", enviados)
print("Recebidos:", recebidos)
print("Em Trânsito:", em_transito)

print("Código de envio")
for i in range(len(pacotes)):
   if pacotes[i][1] == "Em Trânsito":
      print(pacotes[i][0])

def consultar_status(codigo_busca):
   i = 0
   while i < len(pacotes):
      if pacotes[i][0] == codigo_busca:
         return pacotes[i][1]
      i = i + 1
   return "Código não encontrado."

codigo_input = "XYZ789"
print("Status do pacote", codigo_input + ":", consultar_status(codigo_input))

pacotes_ordenados = tuple(sorted(pacotes))
print("Pacotes ordenados")
print(pacotes_ordenados)
