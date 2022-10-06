
import pikepdf
import streamlit as st
from PyPDF2 import PdfFileMerger
import streamlit.components.v1 as components


st.title("PDF Unlocker")

def  main():
    
    option = st.selectbox(
    'Working with PDFs',
    ('Unlock PDF', 'Merge PDF'))
    if option == 'Unlock PDF':
        

                          
        uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            st.write(bytes_data)
        pdf_pass = st.text_input("PDF Password")
        
        unlock = st.button("Unlock PDF")
        if unlock:

            pdf = pikepdf.open(uploaded_file.name, password=pdf_pass)
            pdf_save = st.text_input("Save file as: ")
            if pdf_save:


                pdf.save(pdf_save)
                st.write("File successfully unlocked - Please subscribe to download")
                Subscribe = st.button("Subscribe")
                if Subscribe:
                    with open(pdf_save, "rb") as f:
                        PDFbyte = f.read()

                    st.download_button(label="Download PDF",
                                data=PDFbyte,
                                file_name=pdf_save,
                                mime='application/octet-stream')
                    
                    

                    st.write("The password successfully removed from the PDF")
                
                
                components.html("""<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="learnapplybuild" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>""", 
                            height=200)
    elif option == 'Merge PDF':
        pdfs = []
        pdf1 = st.text_input("First PDF File Location")
        pdfs.append(pdf1)
        pdf2 = st.text_input("Second PDF File Location")
        pdfs.append(pdf2)
        
        add = st.button("Add PDF")
        if add:
            pdf3 = st.text_input("Third PDF File Location")
            pdfs.append(pdf3)
            pdf4 = st.text_input("Fourth PDF File Location")
            pdfs.append(pdf4)
            
        
            merge = st.button("Merge")
            if merge:
                merger = PdfFileMerger()
                for pdf in pdfs:
                    merger.append(pdf)

                    merger.write("result.pdf")
                    merger.close()
            with open("result.pdf", "rb") as f:
                        PDFbyte = f.read()

            st.download_button(label="Download PDF",
                                data=PDFbyte,
                                file_name="result.pdf",
                                mime='application/octet-stream')
        else:
            merge = st.button("Merge")
            if merge:
            
                merger = PdfFileMerger()
                for pdf in pdfs:
                    merger.append(pdf)

                    merger.write("result.pdf")
                    
                with open("result.pdf", "rb") as f:
                    PDFbyte = f.read()

                st.download_button(label="Download PDF",
                                    data=PDFbyte,
                                    file_name="result.pdf",
                                    mime='application/octet-stream')
                
        
        
        
        
                
            
    
if __name__ == '__main__':
    main()