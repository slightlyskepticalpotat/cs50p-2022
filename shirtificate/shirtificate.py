from fpdf import FPDF, Align

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.cell(40, 0, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", Align.C)

pdf.set_text_color(255, 255, 255)
pdf.cell(40, -100, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
