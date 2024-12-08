from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

canvas = canvas.Canvas("Blabla.pdf", pagesize=A4)

seitenabstand_links = 55

canvas.setFont("Helvetica-Bold", 18)
canvas.drawString(x=seitenabstand_links + 5, y=780, text="Projektantrag 2023")

image_path = "images/gsog-logo.jpg"
canvas.drawImage(image_path, x=seitenabstand_links + 280, y=760, width=200, height=50)

canvas.setFont("Helvetica", 14)
canvas.drawString(x=seitenabstand_links, y=710, text="1. Angabe zur Schule")


def draw_textfield_with_heading(x, y, heading, width=240, height=30):
    # Setzte Standarttextgröße für Heading
    canvas.setFont("Helvetica", 12)
    # Label
    canvas.drawString(x=x, y=y + height + 5, text=heading)
    # Textfeld
    canvas.acroForm.textfield(name=heading, x=x, y=y, width=width, height=height)


# Name der Schule
draw_textfield_with_heading(x=seitenabstand_links, y=645, heading="Name der Schule*")

# Schulart
draw_textfield_with_heading(x=seitenabstand_links + 250, y=645, heading="Schulart*")

# Schulanschrift
draw_textfield_with_heading(x=seitenabstand_links, y=580, heading="Schulanschrift*")

# Schulnummer
draw_textfield_with_heading(x=seitenabstand_links + 250, y=580, heading="Schulnummer*")

# Schülerin/Schüler
draw_textfield_with_heading(x=seitenabstand_links, y=515, heading="Schülerin/Schüler*")

# Homepage
draw_textfield_with_heading(x=seitenabstand_links + 250, y=515, heading="Homepage*")

# Telefon
draw_textfield_with_heading(x=seitenabstand_links, y=450, heading="Telefon*")

# E-Mail
draw_textfield_with_heading(x=seitenabstand_links + 250, y=450, heading="E-Mail*")

# Angaben Zum Entwicklungsvorhaben
canvas.setFont("Helvetica", 14)
canvas.drawString(x=seitenabstand_links + 5, y=420, text="2. Angaben zur Projektarbeit")

draw_textfield_with_heading(seitenabstand_links, 355, "2.1 Titel", 490)

# Kurzbeschreibung
draw_textfield_with_heading(seitenabstand_links, 270 - 60, "2.2 Kurzbeschreibung", 490, 60 + 60)

# 2.3
canvas.setFont("Helvetica", 14)
canvas.drawString(x=seitenabstand_links + 5, y=240 - 60,
                  text="2.3. Ausführliche Beschreibung mit Bezug zu den 4 Kriterien*")

link_x = 50
link_y = 50
link_width = 50  # 20
link_height = 50  # 8
link_url = "https://www.gs-offenburg.de/"
canvas.linkURL(link_url, (link_x, link_y, link_x + link_width, link_y + link_height))

canvas.acroForm.checkbox(x=seitenabstand_links + 5, y=224 - 60, size=10, checked=False, buttonStyle='check',
                         name="sperate_doc")
canvas.setFont("Helvetica", 8)
canvas.drawString(x=seitenabstand_links + 20, y=226 - 60, text="Separates Dokument wird als Anhang (pdf-, doc-, oder "
                                                               "docx-Datei) beigefügt.")

# Setze die Linienbreite auf 1 (dünnere Linie)
canvas.setLineWidth(1)
y_linie = 100
canvas.line(seitenabstand_links, y_linie, 250, y_linie)

canvas.drawString(x=seitenabstand_links + 5, y=90, text="Unterschrift")

canvas.save()
