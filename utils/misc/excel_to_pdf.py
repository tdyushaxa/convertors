import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def excel_to_pdf(excel_file, pdf_file):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_file)

    # Convert the DataFrame to a list of lists for the table
    data = [df.columns.tolist()] + df.values.tolist()

    # Create a PDF document
    doc = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Create a Table object from the data
    table = Table(data)

    # Define the style for the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)),  # Header row background color
        ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)),         # Header row text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),             # Center align all cells
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),   # Header row font
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),            # Header row padding
        ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)),  # Table body background color
        ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),          # Table grid lines
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),       # Table body font
        ('FONTSIZE', (0, 1), (-1, -1), 12),                # Table body font size
        ('LEFTPADDING', (0, 0), (-1, -1), 6),              # Cell padding
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),             # Cell padding
    ])

    table.setStyle(style)

    # Build the PDF document
    elements = [table]
    doc.width += 1000
    doc.build(elements)

if __name__ == "__main__":
    excel_file = "example.xlsx"  # Replace with your Excel file name
    pdf_file = "output.pdf"      # Replace with your desired PDF file name
    excel_to_pdf(excel_file, pdf_file)