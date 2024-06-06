from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.builder = []
        self.node_count = 0
        self.node_ids = {}

    #--------------------------
    #    FUNCIONS AUXILIARS
    #--------------------------

    def get_dot(self):
        return "digraph G {\n" + "\n".join(self.builder) + "\n}\n"

    def get_node_id(self, ctx):
        if ctx not in self.node_ids:
            self.node_ids[ctx] = self.node_count
            self.node_count += 1
        return self.node_ids[ctx]

    #--------------------------
    #       INICI VISITADOR
    #--------------------------


    def visitRoot(self, ctx):
        self.visit(ctx.expr())
        return None
    
    #Expressio lambda -> lambdafunc
    def visitExpresioLambda(self, ctx):
        self.visit(ctx.lambdaExpr())

    #Operacioincompleta -> infixExpr
    def visitOperacioincompleta(self, ctx):
        self.visit(ctx.infixExpr())

    #Operacio Completa -> infiExprComp
    def visitOperacio(self, ctx):
        self.visit(ctx.infixExprComp())

    #-----------------------------
    #    OPERACIONS XUNGUES
    #-----------------------------



    #LAMBDA λ
    def visitLambdafunc(self, ctx):
        node_id = self.get_node_id(ctx)
        #Creem el node λ
        self.builder.append(f'  {node_id} [label=" λ"];')
        #Creem node operacio a una banda
        self.visit(ctx.infixExprComp())
        #flechita @ -> operacio
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.infixExprComp())};')
        #Creem node variable NO SE PERQUÈ NO DETECTA COM A VARIABLE
        self.visit(ctx.ID())
        #flechita @ -> variable
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.ID())};')

    def visitOperaciobinaria(self, ctx):
        node_id = self.get_node_id(ctx)
        #Creem node @
        self.builder.append(f'  {node_id} [label="@"];')
        #Creem node operacio unaria
        self.visit(ctx.infixExpr())
        #Creem node valor
        self.visit(ctx.expr2())
        #fletxes @ -> operacio binaria i valor
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.infixExpr())};')
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.expr2())};')

    def visitOperaciounaria(self, ctx):
        node_id = self.get_node_id(ctx)
        #creem el node @
        self.builder.append(f'  {node_id} [label="@"];')

        #Creem el node operador
        self.visit(ctx.operador()) 
        #flechita @ -> node operador
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.operador())};') 
        #Creem el node expr2
        self.visit(ctx.expr2())
        #flechita @ -> node expr2
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.expr2())};')


    #subsitucio de X per 4, és a dir @ i dps lambda
    def visitFuncion(self, ctx):
        node_id = self.get_node_id(ctx)
        #Creem el node @
        self.builder.append(f'  {node_id} [label="@"];')
        #Creem la funció lambda
        self.visit(ctx.lambdaExpr())
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.lambdaExpr())};')
        #Creem el Numero NO EL DETECTA BÉ
        self.visit(ctx.NUMBER())
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(ctx.NUMBER())};')
        return None




    #-----------------------------
    #    NODES INDIVIDUALS
    #-----------------------------

    def visitNumovar(self, ctx):
        self.visit(ctx.expr2())
        return None

    def visitNumero(self, ctx):
        node_id = self.get_node_id(ctx)
        self.builder.append(f'  {node_id} [label="{ctx.NUMBER().getText()}"];')
        return None

    def visitVariable(self, ctx):
        node_id = self.get_node_id(ctx)
        self.builder.append(f'  {node_id} [label="{ctx.ID().getText()}"];')
        return None
    
    def visitOperador(self, ctx):
        #Creem el node Operador
        node_id = self.get_node_id(ctx)
        self.builder.append(f'  {node_id} [label="{ctx.getText()}"];')

        
    

        
