import pandas as pd
import streamlit as st
#from crewai import Crew, Process
#from my_agents import criar_agente_revisor
#from my_tasks import criar_task_analise
import os
from PIL import Image
import time

from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer
import torch

#from myutils import load_model

st.write('Libs carregadas')

@st.cache_resource
def load_model():
    model_path = "TucanoBR/ViTucano-1b5-v1"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained(model_path) #, trust_remote_code=True)
    model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return tokenizer, model

html_page_title = """
     <div style="background-color:black;padding=60px">
         <p style='text-align:center;font-size:50px;font-weight:bold'>Carregar um modelo do Huggingface</p>
     </div>
               """               
st.markdown(html_page_title, unsafe_allow_html=True)


huggingface = Image.open("img/huggingface_logo.png")
st.sidebar.image(huggingface,caption="",use_container_width=True)

st.sidebar.markdown("# Menu")
option = st.sidebar.selectbox("Menu", ["Carregar", 'About'], label_visibility='hidden')

if option == 'Carregar':
    try:
        with st.spinner ('Wait for it...we are working...please') :
            #time.sleep(5)
            
            tokenizer, model = load_model()
            # Testando o modelo
            #input_text = "Exemplo de entrada"
            #inputs = tokenizer(input_text, return_tensors="pt")
            #outputs = model.generate(**inputs)
            #st.write(tokenizer.decode(outputs[0], skip_special_tokens=True))
            
            #model_path = "TucanoBR/ViTucano-1b5-v1"
            #device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            #st.write("Carregar modelo")
            #model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True)
            #model = AutoModel.from_pretrained("TucanoBR/ViTucano-1b5-v1",trust_remote_code=True,  revision="main")

            
            model.to(device)
            tokenizer = AutoTokenizer.from_pretrained(model_path)
            
            prompt = "Quais os principais elementos dessa imagem?"

            # Caso você tenha uma imagem no seu ambiente local, basta passar o endereço da imagem
            # (e.g., path/to/image.jpg).
            image_file="https://raw.githubusercontent.com/Nkluge-correa/TinyLLaVA_Factory/refs/heads/main/assets/sample.jpg"
            output_text, _ = model.chat(prompt=prompt, image=image_file, tokenizer=tokenizer)

            # Imprima o output do modelo!
            st.write(output_text)
        
        
    except:
        st.error("Houston, we have a problem.")
if option == 'About':
    st.markdown("### Testando carregar modelo a partir do huggingface.")
    
