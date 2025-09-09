from pathlib import Path
from openai import AzureOpenAI
from dotenv import load_dotenv
from tqdm import tqdm
import pandas as pd
import time, os

load_dotenv()

API_KEY = os.environ.get('API')

# Mallin määrittely
model_name = "gpt-4o-mini"
deployment = "gpt-4o-mini"

client = AzureOpenAI(     
    api_version="2024-12-01-preview",     
    azure_endpoint="https://oai-data-test.openai.azure.com/",     
    api_key=API_KEY, ) 

# API kutsufunktio
def call_openai_api(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            messages=[
                {        
                    "role": "system",
                    "content": "You are a highly intelligent system that can transform human-written text fields into structured JSON format.",
                    },
                {
                    "role": "user",
                    "content": prompt,
                    }
                ],
                    max_tokens=4096,
                    temperature=1.0,
                    top_p=1.0,
                    model=deployment
                    )
        return response.choices[0].message.content
    except Exception as e:
        return f"Virhe API-kutsussa: {e}"
    

# Funktio tietojen lukuun infokentistä
def extractValuesFromText(df, path_to_prompt, output_path, plant_name):
    """
    Tämä funktio on datasetille korjuuaika-taustatiedot-2020-2024-combined.xlsx

    Parametrit:

    df (DataFrame): Pandas DataFrame, joka sisältää käsiteltävän tekstidatan.
    path_to_prompt (str): Polku ohjeistustiedostoon (prompt), jota käytetään arvojen poiminnassa.
    output_path (str): Polku, johon tuotetut tulokset tallennetaan.
    plant_name (str): Kasvin nimi, jota prosessointi koskee; käytetään NaN-rivien tulosten nimeämisessä.
    """
    prompt_template_path = Path(path_to_prompt)
    prompt_template = prompt_template_path.read_text(encoding="utf-8")

    start = time.time()
    

    queries = df[['INFOTEKSTI','Kasvilajit', 'Lajikkeet', 'Nurmen ikä_x', 
                  'Lannoitus, ajankohta ja -määrä', 'Maalaji_x', 'Muut lisätiedot']].values

    # Välimuisti dictionary
    cache = {}

    with open(output_path, "w", encoding='utf-8') as file:
        for row in tqdm(queries, desc="Käydään rivejä läpi"):
            if all(pd.isnull(value) for value in row):
                file.write("Input: NaN -row **\n")
                file.write("Output: {\n")
                file.write(f'"{plant_name}": null,\n')
                file.write(f'"{plant_name} variety": null,\n')
                file.write(f'"{plant_name} %": null\n')
                file.write("}\n")
                file.write("------\n")
                continue

            infoteksti = row[0]

            if infoteksti in cache:
                response = cache[infoteksti]
            else:
                query = (
                    f"INFOTEKSTI: {row[0]}; "
                    f"Kasvilajit: {row[1]}; "
                    f"Lajikkeet: {row[2]}; "
                    f"Nurmen ikä: {row[3]}; "
                    f"Lannoitus, ajankohta ja -määrä: {row[4]}; "
                    f"Maalaji: {row[5]}; "
                    f"Muut lisätiedot: {row[6]};"
                )

                final_prompt = prompt_template.replace("{input_text}", query)

                response = call_openai_api(final_prompt)
                cache[infoteksti] = response

            end = time.time()

            file.write(f"Time: {round(end - start, 1)} s\n")
            file.write(f"Input: INFOTEKSTI: {row[0]}; Kasvilajit: {row[1]}; Lajikkeet: {row[2]}; Nurmen ikä: {row[3]}; Lannoitus, ajankohta ja -määrä: {row[4]}; Maalaji: {row[5]}; Muut lisätiedot: {row[6]};\n")
            file.write(f"Output: {response}\n")
            file.write("------\n")

    print(f"Tiedosto käyty läpi ja tulokset löytyvät kohteesta: {output_path}")