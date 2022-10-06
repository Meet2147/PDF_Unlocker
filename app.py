
import pikepdf
import streamlit as st

import streamlit.components.v1 as components


st.title("PDF Unlocker")

def  main():
#  pdf_loc = input("PDF location: ")
    pdf_loc = st.text_input("PDF File Location")

    # pdf_pass = "31829427157"
    pdf_pass = st.text_input("PDF Password")
    
    unlock = st.button("Unlock PDF")
    if unlock:

        pdf = pikepdf.open(pdf_loc, password=pdf_pass)
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
            
            
    
if __name__ == '__main__':
    main()