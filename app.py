
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
            
            
            
            pdf_pass = st.text_input("PDF Password")
        
        unlock = st.button("Unlock PDF")
        if unlock:

            pdf = pikepdf.open(uploaded_file, password=pdf_pass)
            pdf.save(uploaded_file.name)
            st.write("File successfully unlocked - Please subscribe to download")
            
            
            with open(uploaded_file.name, "rb") as f:
                PDFbyte = f.read()

                st.download_button(label="Download",
                data=PDFbyte,
                file_name=uploaded_file.name,
                mime='application/octet-stream')
        
        

                
        components.html("""<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="learnapplybuild" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>""", 
                            height=200)
    elif option == 'Merge PDF':
        
        uploaded_files = st.file_uploader("Choose a PDF file", accept_multiple_files=True)
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            st.write("filename:", uploaded_file.name)
            
        
        
        merge = st.button("Merge")  
        if merge:  
            merger = PdfFileMerger()
            for pdf in uploaded_files:
                merger.append(pdf)

                merger.write("result.pdf")
                
                
            with open("result.pdf", "rb") as f:
                PDFbyte = f.read()

            st.download_button(label="Download PDF",
                                data=PDFbyte,
                                file_name="result.pdf",
                                mime='application/octet-stream')
            
        components.html("""<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="learnapplybuild" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" ></script>""", 
                            height=200)
                
        
        
        
        
                
            
    
if __name__ == '__main__':
    main()