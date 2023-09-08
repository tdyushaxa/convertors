import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

def excel_to_pdf(input_excel_file, output_pdf_file):
    # Read Excel data into a DataFrame
    if input_excel_file.endswith('.csv'):
        df = pd.read_csv(input_excel_file)
    else:
        df = pd.read_excel(input_excel_file)

    # Create a PDF document
    c = canvas.Canvas(output_pdf_file, pagesize=letter)

    # Convert DataFrame to a list of lists
    table_data = [list(df.columns)] + df.values.tolist()

    # Create a table from the Excel data
    table = Table(table_data)

    # Define table style
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])

    table.setStyle(style)

    # Calculate table size
    table.wrapOn(c, 400, 600)
    table.drawOn(c, 50, 600)

    # Save the PDF
    c.save()