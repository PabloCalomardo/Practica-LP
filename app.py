import streamlit as st
import pandas as pd
import numpy as np
import keyboard
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

#dependencies de fitxers meus
import haskell as hk



st.title('HinNer by Pablo')
variable = st.text_input('Escriu la teva expressió', '3 + 4')
print(variable)

if 'visitador' not in st.session_state:
  st.session_state.visitador = hk.TreeVisitor()

if st.button('Entra el text'):
  input_stream  = InputStream(variable)
  lexer = exprsLexer(input_stream)
  token_stream = CommonTokenStream(lexer)
  parser = exprsParser(token_stream)
  tree = parser.root()

  if parser.getNumberOfSyntaxErrors() == 0:
    #evaluador de l'arbre
    st.session_state.visitador.visit(tree)
  else:
    print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
    print(tree.toStringTree(recog=parser))
    
  novaentrada = False
  st.session_state.clicked = False

