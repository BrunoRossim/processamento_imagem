from PIL import Image

class Processamento_imagem:

  def __init__(self, image_path):

    self.image = Image.open(image_path)

  def resize(self, width, height):

    """Redimensiona a imagem para o tamanho especificado."""

    self.image = self.image.resize((width, height))

    return self

  def convert(self, mode):

    """Converte a imagem para o modo especificado (ex: 'L', 'RGB')."""

    self.image = self.image.convert(mode)

    return self

  def save(self, output_path):

    """Salva a imagem em um novo arquivo."""

    self.image.save(output_path)