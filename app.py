import streamlit as st
import pandas as pd
import numpy as np


def avalua_expressio_haskell(cadena):
    # Elimina els espais en blanc i divideix la cadena en tokens
    tokens = cadena.split()

    # Comprova si la cadena està buida
    if not tokens:
        return False

    # Comprova el primer token
    primer_token = tokens[0]
    if primer_token.isdigit():
        return True
    elif primer_token.isalpha():
        return True
    elif (primer_token in ["+","-","/","*"]):
        return True
    elif primer_token.startswith("\\"):
        # Comprova si és una funció lambda
        if "->" in cadena:
            return True
        else:
            return False
    elif primer_token == "(":
        # Cas base recursiu parentesis
        return avalua_expressio_haskell(cadena.rfind(")",-1,0))
    else:
        return "Operació incompleta"

st.title('HinNer by Pablo')
title = st.text_input('Escriu la teva expressió', '(+) 2 4')
print(avalua_expressio_haskell(title))

