from fpdf import FPDF

name = input("Name: ")
name = name + "took CS50"
pdf = FPDF()
pdf.add_page()
pdf.image("https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png", 0, 60, 210, 140)
pdf.set_font("helvetica", style="B", size=24)
#pdf.set_text_color(128)
pdf.set_y(40)
pdf.set_x(0)
pdf.cell(210, 10, "CS50 Shirtificate" , 0 , 0 , "C")

pdf.set_font("helvetica", style="B", size=40)
pdf.set_text_color(128)
pdf.set_y(120)
pdf.set_x(0)
pdf.cell(210, 50, name , 0 , 0 , "C")
pdf.output("shirtificate.pdf")
