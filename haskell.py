from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.builder = []
        self.node_count = 0
        self.node_ids = {}

    
    def buida(self):
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

    #Expr2 -> numero
    def visitNum(self, ctx):
        [num] = ctx.getChildren()
        self.visit(num)
    
    #Expr2 -> id
    def visitVar(self, ctx):
        [var] = ctx.getChildren()
        self.visit(var)

    #-----------------------------
    #    OPERACIONS XUNGUES
    #-----------------------------



    #LAMBDA λ
    def visitLambdafunc(self, ctx):
        [barra,var,fletxa,iexpr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #Creem el node λ
        self.builder.append(f'  {node_id} [label=" λ"];')
        #Creem node operacio a una banda
        self.visit(iexpr)
        #flechita @ -> operacio
        self.builder.append(f'  {node_id} -> {self.get_node_id(iexpr)};')
        #Creem node variable NO SE PERQUÈ NO DETECTA COM A VARIABLE
        self.visit(var)
        #flechita @ -> variable
        self.builder.append(f'  {node_id} -> {self.get_node_id(var)};')

    def visitOperaciobinaria(self, ctx):
        [iexpr,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #Creem node @
        self.builder.append(f'  {node_id} [label="@"];')
        #Creem node operacio unaria
        self.visit(iexpr)
        #Creem node valor
        self.visit(expr)
        #fletxes @ -> operacio binaria i valor
        self.builder.append(f'  {node_id} -> {self.get_node_id(iexpr)};')
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')

    def visitOperaciounaria(self, ctx):
        [par1,op,par2,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #creem el node @
        self.builder.append(f'  {node_id} [label="@"];')

        #Creem el node operador
        self.visit(op) 
        #flechita @ -> node operador
        self.builder.append(f'  {node_id} -> {self.get_node_id(op)};') 
        #Creem el node expr2
        self.visit(expr)
        #flechita @ -> node expr2
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')


    #subsitucio de X per 4, és a dir @ i dps lambda
    def visitFuncion(self, ctx):
        [par,lexpr,par,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #Creem el node @
        self.builder.append(f'  {node_id} [label="@"];')
        #Creem la funció lambda
        self.visit(lexpr)
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(lexpr)};')
        #Creem el Numero NO EL DETECTA BÉ
        self.visit(expr)
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')
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

        
    

        
