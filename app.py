from extractPDF import extract_pdf_content
from vectorDB import create_vectordb
from retriveRelevance import retrive_documents
from createTestcase import create_testcase
from exportExcel import export_to_excel

if __name__ == "main":
    pdf_file_path = "euro-ncap-aeb-c2c-test-protocol-v42.pdf"
    output_dir = "extracted_content/"
    documents = extract_pdf_content(pdf_file_path, output_dir)

    db_name = create_vectordb(documents)
    document_contents = retrive_documents(db_test=db_name, query="Test Scenarios")
    created_testcases = create_testcase()
    export_to_excel()

