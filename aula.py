import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


st.title('Aula do dia 16/04')

image = Image.open('peppers.png')

imagem_color_arr = np.array(image)

img_gray = np.mean(imagem_color_arr, axis=2)

st.text(img_gray.shape)

# limiar = st.slider('Limiar?', 0, 255, 25)

# st.text(limiar)

img_gray = np.mean(imagem_color_arr, axis=2)

num_color = st.selectbox("Quantas cores?", \
    (2, 4, 8, 16, 32, 64, 128))


if num_color == 2:
    img_gray[img_gray < 127]  = 0
    img_gray[img_gray >= 127]  = 255

else:
    aux = int(255//num_color) + 1
    
    for i in range(num_color):
        if(i == 0):
            img_gray[img_gray < aux]
            img_gray[img_gray > (255 - aux)] = 255
        else:
            img_gray[((aux * i) < img_gray) & (img_gray < (aux * i+1))] = aux * i


new_image = Image.fromarray(img_gray)
st.image([new_image.convert("L"), image], caption=['Cinza', 'colorida'], width=480,) 