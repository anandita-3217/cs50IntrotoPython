from fpdf import FPDF

class Shirtificate:
    def __init__(self,name):
        self.name = name
        self.pdf = FPDF('P','mm','A4')
    def add_title(self):
        self.pdf.set_font('Helvetica','B',24)
        self.pdf.add_page()
        self.pdf.cell(0,40,'CS50 Shirtificate', align='C')
    def add_image(self):
        self.pdf.image('shirtificate.png',x=30,y=85,w=150)
    def add_name(self):
        self.pdf.set_text_color(255,255,255)
        self.pdf.set_font('Helvetica','B',24)
        self.pdf.set_xy(0,140)
        self.pdf.cell(210,10,f'{self.name} took CS50',align ='C')
    def gen_pdf(self):
        self.add_title()
        self.add_image()
        self.add_name()
        self.pdf.output('shirtificate.pdf')
def main():
    name = input("Enter name: ")
    shirt = Shirtificate(name)
    shirt.gen_pdf()
    print("Your shirt is ready!")
if __name__ == "__main__":
    main()
    