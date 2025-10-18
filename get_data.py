import requests
import pandas as pd

def get_data(cep):

    endpoint = f"https://viacep.com.br/ws/{cep}/json/"

    response = requests.get(endpoint)

    cep_info = response.json()

    return cep_info


users_path = "C:\\Users\\Liz\\Desktop\\api\\01-bronze-raw\\users.csv"
users_df = pd.read_csv(users_path)

cep_lists = users_df['cep'].tolist()

cep_info_list = []

for cep in cep_lists:
    cep_clean = cep.replace("-", "")
    cep_info = get_data(cep_clean)

    if "erro" in cep_info:
        continue

    cep_info_list.append(cep_info)

cep_info_df = pd.DataFrame(cep_info_list)

cep_info_df.to_csv("01-bronze-raw/cep_info.csv", index = False)

print(cep_info_df.head())