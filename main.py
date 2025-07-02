from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
from fpdf import FPDF
import os
import uuid

app = FastAPI()

@app.post("/convert-excel-to-pdf/")
async def convert_excel_to_pdf(file: UploadFile = File(...)):
    # Save the uploaded Excel file
    temp_excel_path = f"temp_{uuid.uuid4()}.xlsx"
    with open(temp_excel_path, "wb") as f:
        content = await file.read()
        f.write(content)

    # Read Excel file using pandas
    try:
        df = pd.read_excel(temp_excel_path)
    except Exception as e:
        os.remove(temp_excel_path)
        return {"error": f"Failed to read Excel: {str(e)}"}

    # Generate PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    col_widths = [pdf.get_string_width(str(col)) + 10 for col in df.columns]

    # Add header row
    for i, col in enumerate(df.columns):
        pdf.cell(col_widths[i], 10, str(col), border=1)
    pdf.ln()

    # Add data rows
    for _, row in df.iterrows():
        for i, col in enumerate(df.columns):
            cell_value = str(row[col])
            pdf.cell(col_widths[i], 10, cell_value, border=1)
        pdf.ln()

    temp_pdf_path = f"converted_{uuid.uuid4()}.pdf"
    pdf.output(temp_pdf_path)

    # Clean up Excel file
    os.remove(temp_excel_path)

    # Return PDF file as response
    return FileResponse(temp_pdf_path, media_type='application/pdf', filename="converted.pdf")
