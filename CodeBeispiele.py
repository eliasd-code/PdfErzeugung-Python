from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4

canvas = Canvas(filename="Beispiel.pdf", pagesize=A4)

canvas.drawString(x=50, y=650, text="Überschrift")


canvas.drawImage(image="./images/el-gato.jpg", x= 50,y= 500, width=120, height=130)

canvas.acroForm.textfield(x=50, y=400, width=150, height=30, name="textfiled1")


canvas.save()


