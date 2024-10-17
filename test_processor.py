import unittest

from imagem_processor.processor import Processamento_imagem

class TestProcessamento_imagem(unittest.TestCase):

  def test_resize(self):

    processor = Processamento_imagem('test_image.jpg')

    original_size = processor.image.size

    processor.resize(100, 100)

    self.assertEqual(processor.image.size, (100, 100))

  def test_convert(self):

    processor = Processamento_imagem('test_image.jpg')

    processor.convert('L')

    self.assertEqual(processor.image.mode, 'L')

if __name__ == '__main__':

  unittest.main()