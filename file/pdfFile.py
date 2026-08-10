from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm


# ==========================================
# PDF SETTINGS
# ==========================================

doc = SimpleDocTemplate(
    "Python_File_Handling_Notes.pdf",
    pagesize=A4,
    rightMargin=16 * mm,
    leftMargin=16 * mm,
    topMargin=14 * mm,
    bottomMargin=14 * mm
)


# ==========================================
# STYLES
# ==========================================

styles = getSampleStyleSheet()

title = ParagraphStyle(
    "TitleCustom",
    parent=styles["Title"],
    fontSize=20,
    leading=24,
    alignment=TA_CENTER,
    spaceAfter=8
)

subtitle = ParagraphStyle(
    "Subtitle",
    parent=styles["Normal"],
    fontSize=9,
    leading=12,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#555555"),
    spaceAfter=14
)

heading = ParagraphStyle(
    "HeadingCustom",
    parent=styles["Heading2"],
    fontSize=12,
    leading=15,
    spaceBefore=7,
    spaceAfter=5,
    textColor=colors.HexColor("#1f4e79")
)

body = ParagraphStyle(
    "BodyCustom",
    parent=styles["BodyText"],
    fontSize=8.5,
    leading=11,
    spaceAfter=4
)

code_style = ParagraphStyle(
    "Code",
    parent=styles["Code"],
    fontName="Courier",
    fontSize=7.2,
    leading=9,
    leftIndent=7,
    rightIndent=7,
    spaceBefore=2,
    spaceAfter=5
)


# ==========================================
# PDF CONTENT
# ==========================================

story = [
    Paragraph("Python File Handling", title),
    Paragraph("Short & Practical Revision Notes", subtitle),
]


# ==========================================
# NOTES
# ==========================================

sections = [

    (
        "1. Opening a File",
        'open("filename", "mode")'
    ),

    (
        "2. File Modes",
        "r → Read<br/>"
        "w → Write / Overwrite<br/>"
        "a → Append<br/>"
        "x → Create<br/>"
        "b → Binary<br/>"
        "t → Text"
    ),

    (
        "3. Writing",
        'f = open("student.txt", "w")<br/>'
        'f.write("Harsh Patel\\n")<br/>'
        'f.close()'
    ),

    (
        "4. writelines()",
        'students = ["Harsh\\n", "Raviraj\\n", "Jeel\\n"]<br/>'
        'f.writelines(students)'
    ),

    (
        "5. Reading",
        'f = open("student.txt", "r")<br/>'
        'data = f.read()<br/>'
        'print(data)<br/>'
        'f.close()'
    ),

    (
        "6. readline()",
        "Reads <b>ONE line</b> at a time."
    ),

    (
        "7. readlines()",
        "Reads all lines and returns a <b>LIST</b>."
    ),

    (
        "8. Reading with Loop",
        'with open("student.txt", "r") as f:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;for line in f:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(line, end="")'
    ),

    (
        "9. Append",
        'with open("student.txt", "a") as f:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;f.write("Bansari Patel\\n")'
    ),

    (
        "10. tell()",
        "Returns the current file cursor position."
    ),

    (
        "11. seek()",
        "Moves the file cursor.<br/>"
        "<b>seek(0)</b> → Beginning"
    ),

    (
        "12. with open()",
        "Automatically closes the file after the block finishes."
    ),

    (
        "13. Check File",
        'import os<br/>'
        'if os.path.exists("student.txt"):<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;print("File exists")'
    ),

    (
        "14. Delete File",
        'os.remove("student.txt")'
    ),

    (
        "15. Error Handling",
        'try:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;with open("abc.txt", "r") as f:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print(f.read())<br/>'
        'except FileNotFoundError:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;print("File not found!")'
    ),

    (
        "16. CSV File",
        'import csv<br/><br/>'
        'with open("students.csv", "w", newline="") as f:<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;writer = csv.writer(f)<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;writer.writerow(["Name", "Age"])<br/>'
        '&nbsp;&nbsp;&nbsp;&nbsp;writer.writerow(["Harsh", 22])'
    )
]


# ==========================================
# ADD NOTES TO PDF
# ==========================================

for heading_text, content in sections:

    story.append(
        Paragraph(heading_text, heading)
    )

    story.append(
        Paragraph(content, code_style)
    )


# ==========================================
# QUICK REVISION TABLE
# ==========================================

story.append(Spacer(1, 8))

story.append(
    Paragraph("Quick Revision", heading)
)


quick_data = [
    ["Function", "Use"],
    ["write()", "Write one string"],
    ["writelines()", "Write multiple strings"],
    ["read()", "Read complete file"],
    ["readline()", "Read one line"],
    ["readlines()", "Read all lines as a list"],
    ["tell()", "Current cursor position"],
    ["seek()", "Move cursor"],
    ["close()", "Close file"],
    ["with open()", "Automatically closes file"],
]


table = Table(
    quick_data,
    colWidths=[42 * mm, 125 * mm]
)


table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0),
         colors.HexColor("#1f4e79")),

        ("TEXTCOLOR", (0, 0), (-1, 0),
         colors.white),

        ("FONTNAME", (0, 0), (-1, 0),
         "Helvetica-Bold"),

        ("FONTNAME", (0, 1), (-1, -1),
         "Helvetica"),

        ("FONTSIZE", (0, 0), (-1, -1), 8),

        ("GRID", (0, 0), (-1, -1),
         0.4, colors.HexColor("#cccccc")),

        ("VALIGN", (0, 0), (-1, -1),
         "MIDDLE"),

        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [
             colors.white,
             colors.HexColor("#f5f7fa")
         ]),

        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ])
)


story.append(table)


# ==========================================
# CREATE PDF
# ==========================================

doc.build(story)

print("Python File Handling PDF created successfully!")