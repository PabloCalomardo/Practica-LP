import streamlit as st
import pandas as pd
import numpy as np
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

#dependencies de fitxers meus
import dependencies as dp



st.title('HinNer by Pablo')
variable = st.text_input('Escriu la teva expressió', '3 + 4')
print(variable)

evaluador = dp.EvalVisitor()

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.button('Entra el text', on_click=click_button)

while(True):
  if st.session_state.clicked:
    input_stream  = InputStream(variable)
    lexer = exprsLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = exprsParser(token_stream)
    tree = parser.root()

    if parser.getNumberOfSyntaxErrors() == 0:
      #evaluador de l'arbre
      evaluador.visit(tree)
    else:
      print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
      print(tree.toStringTree(recog=parser))
    novaentrada = False
    st.session_state.clicked = False

