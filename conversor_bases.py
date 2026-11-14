# Programa: converte números entre as bases 2, 4, 8, 10 e 16, com saída formatada só com caracteres ASCII

#Autor: Eduardo Fiori

# ---------- Layout ----------
LARGURA = 46            # Largura interna das caixas (em caracteres)
SETA = "  > "           # Usado em todos os input()

# ---------- Dados da conversão ----------
DIGITOS = "0123456789ABCDEF"                   # A posição de cada caractere é o seu valor (A = 10, F = 15)
BASES_VALIDAS = ("2", "4", "8", "10", "16")    # Tupla com as bases aceitas, em texto para comparar com o input()
NOMES_BASES = ("binário", "quaternário", "octal", "decimal", "hexadecimal")  # NOMES_BASES[i] é o nome da base BASES_VALIDAS[i]
TEXTO_BASES = "2, 4, 8, 10 ou 16"              

# ---------- Cabeçalho ----------
titulo = "CONVERSOR DE BASES NUMÉRICAS".center(LARGURA)    # center() completa com espaços dos dois lados
subtitulo = "bases 2, 4, 8, 10 e 16".center(LARGURA)
print()
print("+" + "=" * LARGURA + "+")
print("|" + titulo + "|")
print("|" + subtitulo + "|")
print("+" + "=" * LARGURA + "+")

# ---------- Introdução / menu ----------
print("\nCOMO FUNCIONA")
print("  1. Escolha a base do número que vai digitar")
print("  2. Escolha a base para onde quer converter")
print("  3. Digite o número (letras A-F só na base 16)")

print("\nBASES ACEITAS")
print("  " + "Base".ljust(6) + "Nome".ljust(14) + "Dígitos")   # ljust() completa com espaços à direita
posicao = 0
for base_texto in BASES_VALIDAS:                  # Uma linha por base; 
    nome_base = NOMES_BASES[posicao]
    digitos_base = DIGITOS[:int(base_texto)]      # Mesma fatia usada na validação do número
    print("  " + base_texto.ljust(6) + nome_base.ljust(14) + digitos_base)
    posicao = posicao + 1

print("\nCOMO O RESULTADO APARECE")
print("  (número)_origem  =  (resultado)_destino")
print("  Exemplo: (26)_10  =  (11010)_2")
print("  Entre 2, 4, 8 e 16 aparece também o valor em")
print("  decimal usado na conta. Exemplo: via (26)_10")
print("  De 4, 8 ou 16 para 2, o binário mantém os")
print("  zeros do agrupamento: (1A)_16 = (00011010)_2")
print("\n  Entrada inválida mostra [ERRO] e pergunta de novo.")

numero_conversao = 1                      # Contador de quantas conversões o usuário já fez, usado no separador entre uma conversão e outra (começa no 1).
continuar = "S"  
while continuar == "S":                   # while para repetir o programa inteiro até o usuário digitar N

    # Separador numerado entre uma conversão e outra
    rotulo = f" Conversão {numero_conversao} "
    print()
    print("--" + rotulo + "-" * (LARGURA - len(rotulo)))

    # ---------- 1. Base de origem (repete até ser válida) ----------
    print(f"\n[1/3] Base do número ({TEXTO_BASES})")
    base_origem_texto = ""
    while base_origem_texto not in BASES_VALIDAS:
        base_origem_texto = input(SETA).strip()
        if base_origem_texto not in BASES_VALIDAS:
            print(f"  [ERRO] Base inválida. Escolha {TEXTO_BASES}.\n")
    base_origem = int(base_origem_texto)  # Registro da Base de Origem. Converte depois de validar, para o int() não recebe texto inválido

    # ---------- 2. Base de destino (válida e diferente da origem) ----------
    print(f"\n[2/3] Base de destino ({TEXTO_BASES})")
    base_destino_texto = ""
    while base_destino_texto not in BASES_VALIDAS or base_destino_texto == base_origem_texto:
        base_destino_texto = input(SETA).strip()
        if base_destino_texto not in BASES_VALIDAS: # Valida se é uma base válida
            print(f"  [ERRO] Base inválida. Escolha {TEXTO_BASES}.\n")
        elif base_destino_texto == base_origem_texto: #Valida se é diferente da base de origem
            print("  [ERRO] A base de destino é igual à de origem. Escolha outra.\n")
    base_destino = int(base_destino_texto) # Registro da Base de Destino. Converte depois de validar, para o int() não recebe texto inválido

    # ---------- 3. Número (cada caractere precisa existir na base de origem) ----------
    digitos_permitidos = DIGITOS[:base_origem]   # Base 2 -> "01", Base 4 -> "0123", Base 16 -> "0...F"
    print(f"\n[3/3] Número na base {base_origem} (dígitos aceitos: {digitos_permitidos})") # Exibe os dígitos permitidos
    numero_valido = False
    while not numero_valido:
        numero = input(SETA).strip().upper()     # upper() aceita "1a" como "1A"
        numero_valido = True                     # Começa como válido; vira False se algum caractere falhar
        caractere_invalido = ""
        if numero == "": # Evita que o usuário aperte Enter sem digitar nada
            numero_valido = False
            print("  [ERRO] Nenhum número foi digitado.\n")
        else:
            for caractere in numero:
                if caractere not in digitos_permitidos: # Se algum caractere não for permitido, invalida o número
                    numero_valido = False
                    caractere_invalido = caractere # Guarda o caractere inválido para mostrar na mensagem de erro
            if not numero_valido:
                print(f"  [ERRO] '{caractere_invalido}' não existe na base {base_origem}.\n")

    # ---------- 4. Origem -> decimal (soma de dígito x base^posição) ----------
    valor_decimal = 0
    expoente = 0
    for digito in numero[::-1]:                  # [::-1] inverte o texto, então o primeiro dígito lido é o da direita (posição 0)
        valor_digito = DIGITOS.index(digito)     # Ex.: "A" está na posição 10 de DIGITOS, logo vale 10
        valor_decimal = valor_decimal + valor_digito * base_origem ** expoente
        expoente = expoente + 1

    # ---------- 5. Decimal -> destino (divisões sucessivas, restos de baixo para cima) ----------
    if valor_decimal == 0:
        resultado = "0"                          
    else:
        resultado = ""
        quociente = valor_decimal
        while quociente > 0:
            resto = quociente % base_destino
            resultado = DIGITOS[resto] + resultado   # O resto novo entra à esquerda, como ler os restos de baixo para cima
            quociente = quociente // base_destino    # // é a divisão inteira

    # ---------- 5b. Zeros à esquerda no binário ----------
    # Cada dígito da base 4 vira 2 bits, da base 8 vira 3 bits e da base 16 vira 4 bits
    if base_destino == 2 and base_origem != 10: # Se a base de destino for binária e a de origem não for decimal, adiciona zeros à esquerda para completar os agrupamentos
        if base_origem == 4:
            bits_por_digito = 2                  # 4 = 2 ** 2
        elif base_origem == 8:
            bits_por_digito = 3                  # 8 = 2 ** 3
        else:
            bits_por_digito = 4                  # 16 = 2 ** 4
        tamanho_esperado = len(numero) * bits_por_digito   # Ex.: "1A" tem 2 dígitos -> 8 bits
        while len(resultado) < tamanho_esperado:
            resultado = "0" + resultado          # Zeros à esquerda não mudam o valor

    # ---------- 6. Caixa de resultado ----------
    # A base vem depois do sublinhado: (1A)_16 é o (1A) com 16 subscrito
    texto_resultado = f"({numero})_{base_origem_texto}  =  ({resultado})_{base_destino_texto}"
    texto_ponte = f"via ({valor_decimal})_10"

    largura_caixa = LARGURA
    if len(texto_resultado) + 4 > largura_caixa:  # Se o texto não couber, a caixa fica mais larga
        largura_caixa = len(texto_resultado) + 4

    print()
    print("+" + "-" * largura_caixa + "+")
    print("|" + "RESULTADO".center(largura_caixa) + "|")
    print("|" + texto_resultado.center(largura_caixa) + "|")
    if base_origem != 10 and base_destino != 10:  # Mostra o valor decimal usado entre as duas etapas
        print("|" + texto_ponte.center(largura_caixa) + "|")
    print("+" + "-" * largura_caixa + "+")

    # ---------- 7. Continuar? (S ou N) ----------
    print("\nConverter outro número? (S/N)")
    continuar = ""
    while continuar not in ("S", "N"):
        continuar = input(SETA).strip().upper()
        if continuar not in ("S", "N"): # Se o usuário digitar algo diferente de S ou N, mostra erro e pergunta de novo
            print("  [ERRO] Digite S para Sim ou N para Não.\n")
    numero_conversao = numero_conversao + 1 # Contador de quantas conversões o usuário já fez, usado no separador entre uma conversão e outra (começa no 1).

# ---------- Encerramento ----------
print()
print("=" * (LARGURA + 2))
print("Programa encerrado. Até a próxima!".center(LARGURA + 2))
print("=" * (LARGURA + 2))
print()