import pandas as pd
import numpy as np
file_loc = "exceldata.xlsx"
Namelstt = []
Yearlstt = []
Branchlstt = []

df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols = "D")
df1 = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols = "E")
df2 = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols = "F")

Namelstt = df['Student Name'].tolist()
Branchlstt = df1['Branch'].tolist()
Yearlstt = df2['Class'].tolist()
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
for i in range(len(Namelstt)):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)
    can.setFont("Helvetica-Bold", 15)
    can.drawString(400, 262, Namelstt[i])
    can.drawString(160, 240, Yearlstt[i])
    can.drawString(360, 240, Branchlstt[i])
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("gd.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open(f'{Namelstt[i]}Certificate.pdf', "wb")
    print(f'pdf generated {Namelstt[0]}')
    output.write(outputStream)
    outputStream.close()