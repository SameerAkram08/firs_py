import PyPDF2

def merge_pdfs(pdf_list, output_filename):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        with open(pdf, 'rb') as pdf_file:
            pdf_merger.append(pdf_file)

    with open(output_filename, 'wb') as output_file:
        pdf_merger.write(output_file)

if __name__ == "__main__":
    pdf_list = ['file1.pdf', 'file2.pdf']  # List of PDF files to merge
    output_filename = 'merged.pdf'        # Output file name

    merge_pdfs(pdf_list, output_filename)
