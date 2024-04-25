import streamlit as st
import pandas as pd
import numpy as np
from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

st.title('HinNer by Pablo')
variable = st.text_input('Escriu la teva expressió', '3 + 4')
print(variable)

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0
    def visitSuma(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + '+')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())

class EvalVisitor(exprsVisitor):
    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        print(self.visit(expressio))
    def visitSuma(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) + self.visit(expressio2)
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())



input_stream  = InputStream(variable)
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

if parser.getNumberOfSyntaxErrors() == 0:
  visitor = TreeVisitor()
  visitor.visit(tree)
else:
  print(parser.getNumberOfSyntaxErrors(), 'errors de sintaxi.')
  print(tree.toStringTree(recog=parser))