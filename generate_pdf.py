from fpdf import FPDF
from fpdf.enums import XPos, YPos
import os
rImage = 'image/LOGO-POS-GLOBAL-PNG.png'

def pdf(name,number):
    class PDF(FPDF):
        
        def header(self):
            # Arial bold 15
            self.image(rImage,x=10, y=-2, w=200, h=170)
            self.ln(22)
            self.set_font('helvetica', 'B', 10)
            # Move to the right
            self.cell(20)
            # marco
            self.set_font('helvetica','B',16)
            self.multi_cell(w=150, h=10, txt=f'"Felicidades {name}, estas participando" \n Tu número: {number}', border=0, align='C', fill=0)
            self.cell(50)
            self.set_font('helvetica','',10)
            self.ln(5)

    pdf = PDF()

    pdf.add_page()

    ruta ='pdf'
    os.makedirs(ruta,exist_ok=True)
    
    pdf.output(ruta+'\\table_with_cells.pdf')

pdf('Yoander Robles', 2543)
