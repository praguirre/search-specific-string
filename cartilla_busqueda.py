import PyPDF2

def search_string_in_pdf(search_string, pdf_path='cartillamed.pdf'):
    """Search for a string in the PDF and print the pages where it appears"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.is_encrypted:
                reader.decrypt('')
            
            pages_with_string = []
            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if search_string in text:
                    pages_with_string.append(page_num)
            
            if pages_with_string:
                print(f"La cadena '{search_string}' se encontró en las siguientes páginas: {pages_with_string}")
            else:
                print(f"La cadena '{search_string}' no se encontró en el documento.")
                
    except Exception as e:
        print(f"Ocurrió un error al procesar el PDF: {e}")

if __name__ == "__main__":
    search_string = "CUERPO MÉDICO"
    search_string_in_pdf(search_string)
