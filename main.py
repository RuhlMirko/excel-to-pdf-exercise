import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob('files/*.txt')

print(filepaths)
pdf = FPDF(orientation="P", unit="mm", format="A4")
for file in filepaths:
    pdf.add_page()

    filename = Path(file).stem.capitalize()
    print(filename)

    pdf.set_font(family="Helvetica", size=16, style='B')
    pdf.cell(w=50, h=8, text=filename)


pdf.output('output.pdf')
