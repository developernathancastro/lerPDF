# Import for the Desktop Bot
from botcity.document_processing import *
import pathlib
import pandas as pd

dados = []

def lerPDF(arquivo):
    reader = PDFReader()
    parser = reader.read_file(arquivo)

    _date = parser.get_first_entry("Date:")
    date  = parser.read(_date, 1.357143, -1.2, 3.095238, 2.4)
    print('Date: ' + date)
    
    _bill_to = parser.get_first_entry("Bill to:")
    bill_to = parser.read(_bill_to, 1.222222, -1.8, 4.037037, 3.5)
    print('Bill to: ' + bill_to)
    
    _balance_due = parser.get_first_entry("Balance due:")
    balance_due = parser.read(_balance_due, 1.12, -1.25, 1.666667, 2.916667)
    print('Balance Due: ' + balance_due)
    
    _contact = parser.get_first_entry("Contact:")
    contact = parser.read(_contact, 1.223684, -1.2, 4.973684, 3.8)
    print('Contact: ' + contact)

    dados.append([date, bill_to, contact, balance_due])

arquivos = pathlib.Path(r'C:\Users\natha\Processamento de arquivos PDF - BotCity\lerPDF\docs').glob('*.pdf')

for arquivo in arquivos:
    lerPDF(arquivo)

df = pd.DataFrame(dados, columns=['Date', 'Bill to', 'Contact', 'Balance due'])
df.to_csv('dados_pdf.csv', sep=',', index=False)







