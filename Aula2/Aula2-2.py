import numpy as np
import pandas as pd
import warnings 
import plotly.express as px
import seaborn as sns
import warnings 
warnings.filterwarnings("ignore")

df = pd.read_excel('/workspaces/Aulas-python/Aula2/producao_fabricas.xlsx')

print(df.describe)

var = df.var().round()
print(var)


# hist = px.histogram(df)
# hist.update_layout(width=600, height= 400, title_text="Distribuição das idades", yaxis_title="frequencia")
# hist.show()
