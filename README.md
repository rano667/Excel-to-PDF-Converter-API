# 📊 Excel to PDF Converter API

This is a FastAPI-based microservice that converts uploaded Excel files (`.xlsx`) into formatted PDF documents.

## 🚀 Features

- Upload `.xlsx` files via API
- Convert tabular data to PDF using FPDF
- Download generated PDF immediately
- Simple, clean RESTful endpoint with Swagger UI

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) - API framework
- [Uvicorn](https://www.uvicorn.org/) - ASGI server
- [pandas](https://pandas.pydata.org/) - Excel reading
- [openpyxl](https://openpyxl.readthedocs.io/) - Excel engine
- [fpdf](https://pyfpdf.github.io/fpdf2/) - PDF generation

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/excel-to-pdf-api.git
cd excel-to-pdf-api

# Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
