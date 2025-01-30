from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
#import streamlit as st


    
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def load_model():
    model_path = "TucanoBR/ViTucano-1b5-v1"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = AutoModelForCausalLM.from_pretrained(model_path, trust_remote_code=True, revision='main')
    model.to(device)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return tokenizer, model

# Test the function
try:
    tokenizer, model = load_model()
    print("Model and tokenizer loaded successfully!")
except Exception as e:
    print(f"Error: {e}")
