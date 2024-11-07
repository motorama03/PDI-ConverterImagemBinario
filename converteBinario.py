from PIL import Image

def converter_pgm_para_pbm_binario(input_path, output_path, limiar=128):
    # Carregar a imagem PGM (escala de cinza)
    imagem = Image.open(input_path)
    imagem = imagem.convert("L")  # Garantir que esteja em escala de cinza

    # Binarização com o limiar (PBM em ASCII - P1)
    imagem_binarizada = imagem.point(lambda p: 1 if p > limiar else 0)
    
    # Salvar como PBM ASCII (P1)
    with open(output_path, 'w') as f:
        f.write("P1\n")
        f.write(f"{imagem.width} {imagem.height}\n")
        for y in range(imagem.height):
            linha = "".join(str(imagem_binarizada.getpixel((x, y))) + " " for x in range(imagem.width))
            f.write(linha.strip() + "\n")
    print(f"Arquivo PBM binário salvo em {output_path}")

def aplicar_negativo(input_path, output_path):
    # Carregar a imagem binarizada (escala de cinza)
    imagem = Image.open(input_path)
    imagem = imagem.convert("L")  # Garantir que esteja em escala de cinza

    # Aplicar o negativo
    imagem_negativa = imagem.point(lambda p: 255 - p)

    # Salvar a imagem no formato PGM ASCII (P2)
    with open(output_path, 'w') as f:
        f.write("P2\n")
        f.write(f"{imagem.width} {imagem.height}\n255\n")
        for y in range(imagem.height):
            linha = " ".join(str(imagem_negativa.getpixel((x, y))) for x in range(imagem.width))
            f.write(linha + "\n")
    print(f"Imagem negativa PGM salva em {output_path}")

# Caminhos dos arquivos de entrada e saída
caminho_pgm_entrada = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Entrada.pgm"
caminho_pbm_saida = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Saida.pbm"
caminho_pgm_negativo = "/home/matias/Documentos/BCC2024-2/PDI/converteBinario/Negativo.pgm"

# Definir o limiar e converter para PBM
limiar = 128
converter_pgm_para_pbm_binario(caminho_pgm_entrada, caminho_pbm_saida, limiar)

# Aplicar o negativo na imagem binarizada e salvar como PGM (P2)
aplicar_negativo(caminho_pgm_entrada, caminho_pgm_negativo)
