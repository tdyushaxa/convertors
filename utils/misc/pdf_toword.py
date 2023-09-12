from pdf2docx import Converter


async def pdf_to_word(pdf_file, docx_file):
    convertor = Converter(pdf_file)
    convertor.convert(docx_file)
    convertor.close()
