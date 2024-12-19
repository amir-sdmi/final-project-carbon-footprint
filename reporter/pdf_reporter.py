from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime

class ReportGenerator:
    def __init__(self, report_data, file_name=None):
        self.report_data = report_data
        if file_name is None:
            now = datetime.now()
            formatted_date = now.strftime("%Y-%m-%d-%H-%M-%S")
            file_name = f"reports/emissions_report_{formatted_date}.pdf"
        self.file_name = file_name

    def display_console(self):
        print("************************************")
        print("Emissions Report")
        print("************************************")
        for category, emissions in self.report_data.items():
            print(f"{category}: {emissions} kgCO2")
        print("************************************")

    def generate_pdf(self):
        doc = SimpleDocTemplate(self.file_name, pagesize=letter)
        elements = []
        
        data = [['Emission Category', 'CO2 Emissions (kgCO2)']] + \
               [[k, f"{v} kgCO2"] for k, v in self.report_data.items()]
        
        table = Table(data)
        table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.gray),('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),('BOTTOMPADDING', (0,0), (-1,0), 12),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),('GRID', (0,0), (-1,-1), 1, colors.black)
        ]))
        
        elements.append(table)
        doc.build(elements)