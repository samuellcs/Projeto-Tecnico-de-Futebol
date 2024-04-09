class Jogador:
    def __init__(self, nome, posicao, habilidade):
        self.nome = nome[:8].lower()
        self.posicao = posicao.lower()
        self.habilidade = habilidade

class Equipe:
    def __init__(self):
        self.jogadores = []
        self.formacao = {'goleiro': 1, 'defensor': 3, 'meia': 3, 'atacante': 4}
        self.esquema = []

    def _verificar_jogador_existente(self, nome):
        nome_lower = nome.lower()
        for nome_jogador in self.jogadores:
            if nome_lower == nome_jogador.nome:
                return True
        return False
    
    def checagem_dados(self, posicao,habilidade):
        if posicao not in ['goleiro', 'defensor', 'meia', 'atacante']:
            return "A posição informada não existe"

        if not 0 <= habilidade <= 10:
            return "A habilidade do jogador deve estar entre 0 e 10"
        return

    def contratar_jogador(self, nome, posicao, habilidade):
        nome_lower = nome.lower()[:8]
        verificador_dados = self.checagem_dados(posicao,habilidade)
        if verificador_dados != None:
            return verificador_dados
        
        verificador = self._verificar_jogador_existente(nome)
        
        if verificador:
            return "Jogador já está no time"
          
        jogador = Jogador(nome_lower, posicao, habilidade)
        self.jogadores.append(jogador)
        return
    
    def remover_jogador(self, nome):
        self.jogadores = [j for j in self.jogadores if j.nome != nome]

    def trocar_jogador(self, dados_jogador1, dados_jogador2):
        verificador_dados = self.checagem_dados(dados_jogador2[1],int(dados_jogador2[2]))

        if verificador_dados != None:
            return verificador_dados

        if not self._verificar_jogador_existente(dados_jogador1[0]) or self._posicao_jogador(dados_jogador1[0]) != dados_jogador1[1]:
            return "Jogador não está no time"
        self.remover_jogador(dados_jogador1[0])

        # Verificar se o segundo jogador já está no time
        if self._verificar_jogador_existente(dados_jogador2[0]):
            self.jogadores.append(Jogador(dados_jogador1[0], dados_jogador1[1], int(dados_jogador1[2])))  # Adiciona de volta o primeiro jogador removido
            return "Jogador já está no time"

        return self.contratar_jogador(dados_jogador2[0], dados_jogador2[1], int(dados_jogador2[2]))

    def _posicao_jogador(self, nome):
        return next((j.posicao for j in self.jogadores if j.nome == nome), None)
    
    def definir_esquema_tatico(self, qtd_defensor, qtd_meia, qtd_atacante):
        if not 2 <= qtd_defensor <= 4 or not 2 <= qtd_meia <= 4 or not 2 <= qtd_atacante <= 4:
            return "Cada posição deve conter entre 2 e 4 jogadores"

        if qtd_defensor + qtd_meia + qtd_atacante != 10:
            return "A soma das posições deve totalizar 10 jogadores"

        self.formacao['defensor'] = qtd_defensor
        self.formacao['meia'] = qtd_meia
        self.formacao['atacante'] = qtd_atacante
        self.esquema.append((qtd_defensor, qtd_meia, qtd_atacante))
        return

    def montar_time(self):
        if not self.esquema:
            return "O Esquema tático deve ser estabelecido antes de montar o time"

        time = {'goleiro': [], 'defensor': [], 'meia': [], 'atacante': []}
        faltando = []

        for posicao, qtd in self.formacao.items():
            jogadores_posicao = [j for j in self.jogadores if j.posicao == posicao]

            jogadores_posicao.sort(key=lambda x: (x.habilidade, self.jogadores.index(x)), reverse=True)
            time[posicao] = jogadores_posicao[:qtd]

            if len(jogadores_posicao) < qtd:
                if posicao == 'goleiro':
                    faltando.append(f"{qtd - len(jogadores_posicao)} {posicao}")

                elif posicao == 'defensor':
                    faltando.append(f"{qtd - len(jogadores_posicao)} {posicao}es")

                elif posicao == 'meia' or posicao == 'atacante':
                    faltando.append(f"{qtd - len(jogadores_posicao)} {posicao}s")

        if faltando:
            return "Estão faltando jogadores no time:\n" + "\n".join(faltando)       
        else:
            self.list_atacante = []
            self.list_meia = []
            self.list_defensor = []
            self.list_nome_atacante = []
            self.list_nome_meia = []
            self.list_nome_defensor = []
            self.list_nome_goleiro = []

            for jogador in self.jogadores:
                if jogador.posicao == 'atacante':
                    self.list_atacante.append(jogador)
                elif jogador.posicao == 'meia':
                    self.list_meia.append(jogador)
                elif jogador.posicao == 'defensor':
                    self.list_defensor.append(jogador)
                elif jogador.posicao == 'goleiro':
                    self.nome_goleiro = jogador.nome
                    self.list_nome_goleiro.append(self.nome_goleiro)


            self.list_atacante.sort(key=lambda jogador: jogador.habilidade, reverse=True)
            self.list_meia.sort(key=lambda jogador: jogador.habilidade, reverse=True)
            self.list_defensor.sort(key=lambda jogador: jogador.habilidade, reverse=True)
            for item,value in self.formacao.items():
                if item == "atacante":
                    self.list_atacante = self.list_atacante[:value]
                    for nome_atacante in self.list_atacante:
                        self.list_nome_atacante.append(nome_atacante.nome)
                elif item == "meia":
                    self.list_meia = self.list_meia[:value]
                    for nome_meia in self.list_meia:
                        self.list_nome_meia.append(nome_meia.nome)
                elif item == "defensor":
                    self.list_defensor = self.list_defensor[:value]
                    for nome_defensor in self.list_defensor:
                        self.list_nome_defensor.append(nome_defensor.nome)

            self._exibir_campo()

    
                                
    def _exibir_campo(self):
        print('+----------------------------------------+')
        print('|              |          |              |')
        print('|               ----------               |')
        print('|                                        |')        
        concat,bolas = self.format_print(self.list_nome_atacante)
        print(f'|{concat}|')
        print(f'{bolas}')  
        print('|                                        |')
        concat,bolas = self.format_print(self.list_nome_meia)
        print(f'|{concat}|')                                   
        print(f'{bolas}')  
        print("|                  (  )                  |")
        print('|                                        |')
        print('|                                        |')
        concat,bolas = self.format_print(self.list_nome_defensor)
        print(f'|{concat}|')
        print(f'{bolas}')  
        print("|                                        |")
        print("|               ----o-----               |")
        concat,bolas = self.format_print(self.list_nome_goleiro)
        print(f'|{concat}|') 
        print('+----------------------------------------+')

    def format_print(self,lista_nome):
        tamanho = int(40 / len(lista_nome))

        format_text = []
        for nome in lista_nome:
            if len(lista_nome) == 1:
                tamanho_nome = int(10 - len(lista_nome[0]))
                tamanho_inicial_nome = tamanho_nome // 2
                tamanho_final_nome = tamanho_nome - tamanho_inicial_nome
                tamanho_total_nome = tamanho_inicial_nome + tamanho_final_nome + len(lista_nome[0]) +2
                tamanho_inicial = int(((tamanho - tamanho_total_nome)) / 2)
                tamanho_final = tamanho - tamanho_total_nome - tamanho_inicial
                format_text.append(f"{' '*tamanho_inicial + '|' + ' '*tamanho_inicial_nome + nome + ' '*tamanho_final_nome + '|' +' '*tamanho_final}")
            else:
                tamanho_inicial = (tamanho - len(nome)) // 2
                tamanho_final = tamanho - len(nome) - tamanho_inicial
                format_text.append(f"{' '*tamanho_inicial + nome + ' '*tamanho_final}")


        concat = ''.join(format_text)
        if len(concat) < 40:
            concat += ' ' * (40 - len(concat))
        if len(lista_nome) == 3:
            bolas = f'|{5*" "}o{12*" "}o{12*" "}o{8*" "}|'
        elif len(lista_nome) == 4:
            bolas = f'|{4*" "}o{9*" "}o{9*" "}o{9*" "}o{5*" "}|'
        else:
            bolas =  ""
        return concat, bolas

    def _exibir_linha_jogadores(self, jogadores):
        colunas_disponiveis = 40
        qtd_jogadores = len(jogadores)

        if qtd_jogadores == 0:
            return " " * colunas_disponiveis

        
        espacos_por_jogador = colunas_disponiveis // qtd_jogadores
        espacos_adicionais = colunas_disponiveis % qtd_jogadores

        linha = ""
        for i in range(qtd_jogadores):
            jogador = jogadores[i]
            espacos_a_esquerda = espacos_por_jogador * i
            espacos_a_direita = espacos_por_jogador - len(jogador.nome)

            
            if len(jogador.nome) < 8:
                espacos_livres = 8 - len(jogador.nome)
                espacos_a_esquerda += espacos_livres // 2
                espacos_a_direita += espacos_livres // 2 + espacos_livres % 2

            if i == qtd_jogadores - 1:
                espacos_a_direita += espacos_adicionais

            linha += f"{espacos_a_esquerda * ' '}{jogador.nome}{espacos_a_direita * ' '}o"

        return linha[:-1]  

    def _centralizar_nome_goleiro(self, nome):
        colunas_disponiveis = 40
        espacos_a_esquerda = (colunas_disponiveis - len(nome)) // 2
        espacos_a_direita = colunas_disponiveis - len(nome) - espacos_a_esquerda

        return f"{' ' * espacos_a_esquerda}{nome}{' ' * espacos_a_direita}"



equipe = Equipe()

while True:
    try:
        opcao = input()
    except EOFError:
        opcao = '5'
    if opcao == '1':
        nome, posicao, habilidade = input().split()
        resultado = equipe.contratar_jogador(nome, posicao, int(habilidade))
        if resultado != None:
            print(resultado)
    elif opcao == '2':
        dados = input().split()
        dados = [lower.lower() for lower in dados]
        dados_jogador1 = dados[:3]
        dados_jogador1[0] = dados_jogador1[0][:8]
        dados_jogador2 = dados[4:]
        dados_jogador2[0] = dados_jogador2[0][:8]
        resultado = equipe.trocar_jogador(dados_jogador1, dados_jogador2)
        if resultado != None:
            print(resultado)
    elif opcao == '3':
        definir_esquema_tatico_input = input().split()
        qtd_defensores, qtd_meias, qtd_atacantes = map(int, definir_esquema_tatico_input)
        resultado = equipe.definir_esquema_tatico(qtd_defensores, qtd_meias, qtd_atacantes) 
        if resultado != None:   
            print(resultado)

    elif opcao == '4':
        resultado = equipe.montar_time()  
        if resultado != None:  
            print(resultado)
    elif opcao == '5':
        break
