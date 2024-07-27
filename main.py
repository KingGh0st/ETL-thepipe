#Se debe importar la API Key como variable del entorno de Windows
from thepipe.extract import extract_from_file
import pandas as pd

def extract_pdf(schema,file,model):
    results = extract_from_file(
        file_path = file,
        schema = schema,
        ai_model = model
    )
    return results

def transform_data(data):
    df = pd.DataFrame(data)
    return df

def load_data_excel(data):
    data.to_excel("Notas.xlsx", index=False, sheet_name="Notas")
    

def load_data_csv(data):
    data.to_csv("Notas.csv", index=False)

schema = { #Organización de los datos que se quieren extraer del PDF
    "Nombre": "string",
    "Apellido(s)": "string",
    "PARCIAL 2": "string",
}

file =  r"ETL-thepipe\SO - Notas Parcial 2 -2023.pdf", #Reemplazar con PDF
model = "openai/gpt-4o-mini"

test = extract_pdf(schema,file,model)
print(test)
df = transform_data(test)
print(df.head())
