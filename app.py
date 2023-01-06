import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly_express as px
import streamlit as st
from PIL import Image
import plotly.graph_objects as go
import os


file_path = os.path.join(os.path.dirname(__file__),"PET_CONS_PSUP_DC_NUS_MBBL_A.xls")

#df = pd.read_excel("C:/Users/piotr/PycharmProjects/web_app/PET_CONS_PSUP_DC_NUS_MBBL_A.xls", sheet_name="Data 1")
df = pd.read_excel(file_path, sheet_name="Data 1")


st.set_page_config(page_title='U.S. Product Supplied for Crude Oil and Petroleum Products',
                   page_icon=':pray:',
                   layout='wide')
st.header('Historical Data')
st.subheader('We need forecast for 2022! and 2023')

#i = df.index
#c = df.columns

p = df.iloc[47:, 1:4]
date = df.iloc[47:, 0]
#product_name = df.iloc[1:2,1:4]

product_name = ['P S of Crude Oil and Petroleum Products (1000 Barrels)',
                    'P S of Crude Oil (1000 Barrels)',
                    'P S of Hydrocarbon Gas Liquids (1000 Barrels)'
                    ]
d = np.array(df.iloc[47:, 1:4])
dates = np.array(date)

#prod = pd.Series(product_name)

#print(df.tail(41))

#new_df = pd.DataFrame(p, index=dates, columns=product_name)

#d = pd.DataFrame(np.random.randn(41, 4), index=dates, columns=["A", "B", "C", "D"])

#print(date)

#df = pd.Series(df)

ts = pd.DataFrame(d,index=dates, columns=product_name)

#print(dates)

#plt.figure();

chart = px.line(ts,
                title = 'Historical Data in use',
                #markers=True
                )


st.plotly_chart(chart)
st.dataframe(ts)
#ts.plot();

#p=plt.legend(loc='best');


#plt.show()

#st.write(plt.show())

x = np.arange(10)

fig = go.Figure(data=go.Scatter(x=x, y=x**2))
st.plotly_chart(fig)