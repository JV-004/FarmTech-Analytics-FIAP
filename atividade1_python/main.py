import os
import csv
os.system('cls')
# Lista para armazenar os dados de plantio
plantio = []

# Loop principal do programa
while True:
    # Exibe o menu principal
    print("\n==MENU PLANTIO==")
    print("1. Adicionar dados")
    print("2. Mostrar dados")
    print("3. Atualizar dados")
    print("4. Excluir dados")
    print("5. Cálculo de Manejo")
    print("6. Sair")
    
    # Recebe a opção do usuário
    opcao = int(input("Digite a opção desejada: "))
    
    # Define códigos para formatação colorida no terminal
    cor_abre = '\033[1;33m'  # Amarelo em negrito
    cor_fecha = '\033[m'  # Reset da cor
    
    # Opção 1: Adicionar novos dados de plantio
    if opcao == 1:
        # Solicita informações básicas
        cultura = input("Digite a cultura (café/milho): ").lower()
        insumo = input("Digite o insumo (ex: fosfato): ").lower()
        
        # Calcula a área de acordo com o tipo de cultura
        if cultura == "café" or cultura == "cafe":
            # Para café, calcula área retangular
            largura = float(input("Largura (M): "))
            comprimento = float(input("Comprimento (m): "))
            area = largura * comprimento
        elif cultura == "milho":
            # Para milho, calcula área circular
            raio = float(input("Raio (M): "))
            area = 3.14 * (raio ** 2)
        else:
            # Trata cultura inválida
            print("Cultura inválida")
            continue
        
        # Adiciona os dados à lista de plantio
        plantio.append({
            "cultura": cultura, "area": area, "insumo": insumo
        })
        print("Dados adicionados com sucesso")
    
    # Opção 2: Visualizar dados existentes
    elif opcao == 2:
        # Verifica se existem dados para mostrar
        if not plantio:
            print("Nenhum dado encontrado")
        else:
            # Exibe todos os dados em formato tabular
            print("\n== DADOS ==")
            for contador in range(len(plantio)):
                print(contador, end=' | ')
                print(f'{cor_abre}Cultura:{cor_fecha} {plantio[contador]["cultura"]:>15} |', end=' ')
                print(f'{cor_abre}Área: {cor_fecha} {plantio[contador]["area"]:>15.2f}m² |', end=' ')
                print(f'{cor_abre}Insumo: {cor_fecha} {plantio[contador]["insumo"]:>15}')
    
    # Opção 3: Atualizar dados existentes
    elif opcao == 3:
        # Verifica se existem dados para atualizar
        if not plantio:
            print("Nenhum dado para atualização")
            continue
        
        # Exibe todos os dados para que o usuário escolha qual atualizar
        for contador in range(len(plantio)):
            print(contador, end=' | ')
            print(f'{cor_abre}Cultura:{cor_fecha} {plantio[contador]["cultura"]:>15} |', end=' ')
            print(f'{cor_abre}Área: {cor_fecha} {plantio[contador]["area"]:>15.2f}m² |', end=' ')
            print(f'{cor_abre}Insumo: {cor_fecha} {plantio[contador]["insumo"]:>15}')
        
        # Solicita a posição do dado a ser atualizado
        posicao = int(input("Digite a posição do dado que deseja atualizar: "))
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= len(plantio):
            print("Posição inválida")
            continue
        
        # Mostra o dado atual antes da atualização
        print(f"Dado atual: {plantio[posicao]}")
        
        # Solicita novas informações
        cultura = input("Digite a nova cultura (café/milho): ").lower()
        insumo = input("Digite o novo insumo (ex: fosfato): ").lower()
        
        # Recalcula a área baseada no tipo de cultura
        if cultura == "café" or cultura == "cafe":
            largura = float(input("Largura (M): "))
            comprimento = float(input("Comprimento (m): "))
            area = largura * comprimento
        elif cultura == "milho":
            raio = float(input("Raio (M): "))
            area = 3.14 * (raio ** 2)
        else:
            print("Cultura inválida")
            continue
        
        # Atualiza o registro na posição especificada
        plantio[posicao] = {
            "cultura": cultura, "area": area, "insumo": insumo
        }
        print("Dados atualizados com sucesso")
    
    # Opção 4: Excluir dados existentes
    elif opcao == 4:
        # Verifica se existem dados para excluir
        if not plantio:
            print("Nenhum dado para exclusão")
            continue
        
        # Exibe todos os dados para que o usuário escolha qual excluir
        for contador in range(len(plantio)):
            print(contador, end=' | ')
            print(f'{cor_abre}Cultura:{cor_fecha} {plantio[contador]["cultura"]:>15} |', end=' ')
            print(f'{cor_abre}Área: {cor_fecha} {plantio[contador]["area"]:>15.2f}m² |', end=' ')
            print(f'{cor_abre}Insumo: {cor_fecha} {plantio[contador]["insumo"]:>15}')
        
        # Solicita a posição do dado a ser excluído
        posicao = int(input("Digite a posição do dado que deseja excluir: "))
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= len(plantio):
            print("Posição inválida")
            continue
        
        # Remove o item da lista
        plantio.pop(posicao)
        print("Dado excluído com sucesso")
    
    # Opção 5: Calcular o manejo de insumos
    elif opcao == 5:
        # Verifica se existem dados para calcular
        if not plantio:
            print("Nenhum dado encontrado para cálculo de manejo")
            continue
        
        # Exibe todos os dados para que o usuário escolha qual calcular
        for contador in range(len(plantio)):
            print(contador, end=' | ')
            print(f'{cor_abre}Cultura:{cor_fecha} {plantio[contador]["cultura"]:>15} |', end=' ')
            print(f'{cor_abre}Área: {cor_fecha} {plantio[contador]["area"]:>15.2f}m² |', end=' ')
            print(f'{cor_abre}Insumo: {cor_fecha} {plantio[contador]["insumo"]:>15}')
        
        # Solicita a posição do dado para calcular o manejo
        posicao = int(input("Digite a posição do dado para calcular o manejo: "))
        # Verifica se a posição é válida
        if posicao < 0 or posicao >= len(plantio):
            print("Posição inválida")
            continue
        
        # Obtém os dados do plantio selecionado
        cultura = plantio[posicao]["cultura"]
        area = plantio[posicao]["area"]
        insumo = plantio[posicao]["insumo"]
        
        # Exibe cabeçalho formatado para o cálculo de manejo
        print(f"\n{cor_abre}╔══════════════════════════════════════╗{cor_fecha}")
        print(f"{cor_abre}║        CÁLCULO DE MANEJO              ║{cor_fecha}")
        print(f"{cor_abre}╚══════════════════════════════════════╝{cor_fecha}")
        
        # Cálculos específicos para cada tipo de cultura
        if cultura == "café" or cultura == "cafe":
            # Para café, o cálculo é baseado na área total
            tamanho_ruas_somadas = area
            quantidade_insumos = tamanho_ruas_somadas * 0.5
            
            # Exibe os resultados formatados para café
            print(f"\n{cor_abre}▶ Informações do plantio de café:{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Cada metro de rua plantada deverá receber {cor_abre}500ml{cor_fecha} de {cor_abre}{insumo}{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Área total: {cor_abre}{area:.2f}m²{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Total de insumo necessário: {cor_abre}{quantidade_insumos:.2f}L{cor_fecha}")
        
        elif cultura == "milho":
            # Para milho, calcula baseado nos perímetros das ruas concêntricas
            ruas_somadas = 0
            raio_original = (area / 3.14) ** 0.5  # Recalcula o raio a partir da área armazenada
            raio_rua = raio_original
            
            # Soma os perímetros de todas as ruas concêntricas
            for i in range(int(raio_original), 0, -1):
                ruas_somadas = (2 * 3.14 * raio_rua) + ruas_somadas
                raio_rua -= 1

            # Calcula a quantidade de insumos (0.5L por metro de rua)
            quantidade_insumos = ruas_somadas * 0.5
            
            # Exibe os resultados formatados para milho
            print(f"\n{cor_abre}▶ Informações do plantio de milho:{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Área total do plantio: {cor_abre}{area:.2f}m²{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Soma dos perímetros das ruas: {cor_abre}{ruas_somadas:.2f}m{cor_fecha}")
            print(f"  {cor_abre}→{cor_fecha} Total de insumo necessário: {cor_abre}{quantidade_insumos:.2f}L{cor_fecha} de {cor_abre}{insumo}{cor_fecha}")
            
        # Linha decorativa para encerrar a seção de cálculo
        print(f"\n{cor_abre}═══════════════════════════════════════{cor_fecha}")
    
    # Opção 6: Encerrar o programa
    elif opcao == 6:
        # Salvar dados em CSV  
        with open('plantio.csv', 'w', newline='') as arquivo:  
            campos = ['cultura', 'area', 'insumo']  
            escritor = csv.DictWriter(arquivo, fieldnames=campos)  
            escritor.writeheader()  
            escritor.writerows(plantio)  
        print("Dados salvos em plantio.csv. Saindo...")  
        break
    
    # Tratamento para opções inválidas
    else:
        print(f"\n{cor_abre}Opção inválida!{cor_fecha}")
        print("Por favor, escolha uma opção entre 1 e 6.")