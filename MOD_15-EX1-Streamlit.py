import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import time

st.set_page_config(layout = 'wide')


#1 - Plotando pontos em um mapa (a partir da latitude e longitude)

st.markdown("### 1) Plotando pontos em um gráfico:")

map_data = pd.DataFrame(

    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],

    columns=['lat', 'lon']
    
    )

st.map(map_data)




#2 - Checkbok que quando marcado mostra um data-frame

st.markdown("### 2) Checkbox para ocultar/exibir um dataframe:")

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data



#3 - Select box que exibe o número selecionado

st.markdown("### 3) Select box que exibe o número selecionado:")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option




#4 - Escreve um dataframe
st.markdown("### 4) Gerando um dataframe:")

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


#5 - Escreve um dataframe
st.markdown("### 5) Dataframe com alguns valores pintados de amarelo:")

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))



#6 - Gráfico de linhas
st.markdown("### 6) Gráfico de linhas:")

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



#7 - Slider e tira a raíz quadrada do que for selecionado
st.markdown("### 7) Slider e tira a raíz quadrada do que for selecionado:")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)



#8 - Caixa de texto que escreve na tela o conteúdo digitado
st.markdown("### 8 Caixa de texto que escreve na tela o conteúdo digitado:")

st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name



#9 - Input para receber uma data
st.markdown("### 9) Input para receber uma data:")

data = st.date_input(label="Choose a date")

st.write(data)


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)





#10 - Faz uma contagem e monstra uma barra com a progressão

st.markdown("### 10) Contagem até 100:")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'