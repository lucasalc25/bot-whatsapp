import os
from PIL import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Diretório contendo as imagens
image_directory = "./"
output_file = "contatos.txt"

# Função para extrair telefones de uma imagem
def extrair_telefones(image_path):
    # Carregar a imagem
    image = Image.open(image_path)
    
    # Extrair texto da imagem
    text = pytesseract.image_to_string(image, lang="por")
    
    # Encontrar números de telefone
    telefones = re.findall(r'\(\d{2}\)\d{4,5}-\d{4}', text)
    
     # Ajustar o DDD para "(92)" e garantir que o primeiro dígito após o DDD seja "9"
    telefones_corrigidos = []
    
    for telefone in telefones:
         # Substituir DDD de "(x2)" para "(92)" e garantir que o primeiro dígito após o DDD seja "9"
        telefone_corrigido = re.sub(r'\(\d2\)(\d)(\d{3,4})-(\d{4})', r'(92)9\2-\3', telefone)
        # Remove parênteses e mantém o DDD
        telefone_corrigido = telefone.replace("(", "").replace(")", "").replace(" ", "")
        telefones_corrigidos.append(telefone_corrigido)
        
    return telefones_corrigidos

# Processar todas as imagens no diretório
todos_telefones = set()  # Usar um conjunto para garantir que não haja duplicados

for filename in os.listdir(image_directory):
     # Verificar se o nome do arquivo começa com "Tabela" seguido de um número
    if re.match(r"tabela \d+\.(png|jpg|jpeg)$", filename, re.IGNORECASE):
        image_path = os.path.join(image_directory, filename)
        telefones = extrair_telefones(image_path)
        todos_telefones.update(telefones)  # Adicionar os números ao conjunto

# Salvar os resultados em um arquivo de texto
with open(output_file, "w") as file:
    for telefone in todos_telefones:
        file.write(telefone + "\n")

# Exibir os telefones extraídos
print("Telefones extraidos:")
for telefone in todos_telefones:
    print(telefone)

