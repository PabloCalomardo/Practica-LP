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


input_stream  = InputStream(variable)
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
  #arbre de nodes
  visitor = dp.TreeVisitor()
  visitor.visit(tree)

  #evaluador de l'arbre
  visitor2 = dp.EvalVisitor()
  visitor2.visit(tree)
else:
  print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
  print(tree.toStringTree(recog=parser))