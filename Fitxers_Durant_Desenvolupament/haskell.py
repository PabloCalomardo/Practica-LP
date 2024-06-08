from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.builder = []
        self.node_count = 0
        self.abc_count = 0
        self.node_ids = {}
        self.abecedari = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.taula = {}
        self.preinferencia = {}
        self.inferencia = {}
        self.assig = False

    
    def buida(self):
        self.builder = []
        self.node_count = 0
        self.abc_count = 0
        self.node_ids = {}
        self.preinferencia = {}
        self.inferencia = {}
        self.abecedari = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.assig = False

    def afegit(self):
        return self.assig
    
    def tipus(self):
        return self.taula

    def getinferencia(self):
        return self.inferencia
    
    def canviaabecedari(self):
        self.builder = []
        self.node_ids = {}
        count = 0
        while count < self.abc_count:
            self.abecedari[count] = self.inferencia[self.abecedari[count]]
            count += 1
        self.abc_count = 0
            
            
    def error(self):
        if("Type Error" in self.inferencia):
            return self.inferencia["Type Error"]
        return ""

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

    def trobatipus(self,tipus1, tipus2):
        if(tipus2 >= 'a'):  #inferència de tipus
            self.inferencia[tipus2] = tipus1[1]
        elif(tipus2 != tipus1[1]): # Mirem si el tipus2 és el que toca
            self.inferencia["Type Error"] = "Type Error: "+ tipus1[1]+" vs " +tipus2
        
        return tipus1[6:-1]
    
    def trobatipuslambda(self,tipus1, tipus2):
        if(tipus2 >= 'a'):  #inferència de tipus
            tipus2 = self.inferencia[tipus2]
        return '('+tipus1+' -> '+tipus2+ ')'
            
    #--------------------------
    #       INICI VISITADOR
    #--------------------------

    def visitAssignacio(self, ctx):
        self.assig = True
        self.visit(ctx.assig())

    def visitExpressio(self, ctx):
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

    def visitNormalassig(self, ctx):
        [var] = ctx.getChildren()
        self.visit(var)

    def visitOperassig(self, ctx):
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
        lletra = self.abecedari[self.abc_count]
        self.builder.append(f'  {node_id} [label=" λ \n'+self.abecedari[self.abc_count]+'"];')
        self.abc_count += 1
        #Creem node operacio a una banda
        tipusabst = self.visit(iexpr)
        #flechita @ -> operacio
        self.builder.append(f'  {node_id} -> {self.get_node_id(iexpr)};')
        #Creem node variable NO SE PERQUÈ NO DETECTA COM A VARIABLE
        tipusvar = self.visit(var)
        #flechita @ -> variable
        self.builder.append(f'  {node_id} -> {self.get_node_id(var)};')
        resultat = self.trobatipuslambda(tipusabst,tipusvar)
        self.inferencia[lletra] = resultat
        return self.inferencia[lletra]




    def visitOperaciobinaria(self, ctx):
        [iexpr,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #Creem node @
        lletra = self.abecedari[self.abc_count]
        self.builder.append(f'  {node_id} [label="@\n'+lletra+'"];')
        self.abc_count += 1
        #Creem node operacio unaria
        tipusoperacio = self.visit(iexpr)
        #Creem node valor
        tipusexpresio = self.visit(expr)
        #fletxes @ -> operacio binaria i valor
        self.builder.append(f'  {node_id} -> {self.get_node_id(iexpr)};')
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')

        resultat = self.trobatipus(tipusoperacio,tipusexpresio)
        self.inferencia[lletra] = resultat
        return self.inferencia[lletra]

    def visitOperaciounaria(self, ctx):
        [par1,op,par2,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        #creem el node @
        lletra = self.abecedari[self.abc_count]
        self.builder.append(f'  {node_id} [label="@\n'+lletra+'"];')
        self.abc_count += 1
        #Creem el node operador
        tipusoperacio = self.visit(op) 
        #flechita @ -> node operador
        self.builder.append(f'  {node_id} -> {self.get_node_id(op)};') 
        #Creem el node expr2
        tipusexpresio = self.visit(expr)
        #flechita @ -> node expr2
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')

        resultat = self.trobatipus(tipusoperacio,tipusexpresio)
        self.inferencia[lletra] = resultat
        return self.inferencia[lletra]


    #subsitucio de X per 4, és a dir @ i dps lambda
    def visitFuncion(self, ctx):
        [par,lexpr,par,expr] = ctx.getChildren()
        node_id = self.get_node_id(ctx)
        lletra = self.abecedari[self.abc_count]
        #Creem el node @
        self.builder.append(f'  {node_id} [label="@\n'+self.abecedari[self.abc_count]+'"];')
        self.abc_count += 1
        #Creem la funció lambda
        tipuslexpr = self.visit(lexpr) 
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(lexpr)};')
        #Creem el Numero NO EL DETECTA BÉ
        tipusexpresio = self.visit(expr)
        #Creem la fletxa
        self.builder.append(f'  {node_id} -> {self.get_node_id(expr)};')
        resultat = self.trobatipus(tipuslexpr,tipusexpresio)
        self.inferencia[lletra] = resultat
        return self.inferencia[lletra]
    
    def visitNassig(self, ctx):
        [num,dospunts,cap] = ctx.getChildren()
        self.taula[num.getText()] = cap.getText()

    def visitOpassig(self, ctx):
        [par,op,par2,dospunts,cap,fletxa,expr4] = ctx.getChildren()
        self.taula['('+op.getText()+')'] = '('+cap.getText()+' -> '+self.visit(expr4)+')'
    
    def visitCaprec(self, ctx):
        [cap,fletxa,expr4] = ctx.getChildren()
        return '('+cap.getText()+' -> '+self.visit(expr4)+')'
    
    def visitCap(self, ctx):
        [cap] = ctx.getChildren()
        return cap.getText()

    #-----------------------------
    #    NODES INDIVIDUALS
    #-----------------------------

    def visitNumovar(self, ctx):
        return self.visit(ctx.expr2())

    def visitNumero(self, ctx):
        node_id = self.get_node_id(ctx)
        if (ctx.getText() in self.taula):
            self.builder.append(f'  {node_id} [label="{ctx.getText()}\n'+self.taula[ctx.getText()]+'"];')
            return self.taula[ctx.getText()]
        else:
            raise Exception("Error en la creació de l'arbre","El nombre " + ctx.getText() + " no ha sigut declarat a la taula")

    def visitVariable(self, ctx):
        node_id = self.get_node_id(ctx)
        lletra = self.abecedari[self.abc_count]
        if ctx.ID().getText() not in self.preinferencia:
            self.preinferencia[ctx.ID().getText()] = self.abc_count
            self.builder.append(f'  {node_id} [label="{ctx.ID().getText()}\n'+lletra+'"];')
            self.abc_count += 1
            return lletra

        else:
            self.builder.append(f'  {node_id} [label="{ctx.ID().getText()}\n'+self.abecedari[self.preinferencia[ctx.ID().getText()]]+'"];')
            return self.abecedari[self.preinferencia[ctx.ID().getText()]]
    
    def visitOperador(self, ctx):
        node_id = self.get_node_id(ctx)
        if ('('+ctx.getText()+')' in self.taula):
            self.builder.append(f'  {node_id} [label="{ctx.getText()}\n'+self.taula['('+ctx.getText()+')']+'"];')
            return self.taula['('+ctx.getText()+')']
        else:
            raise Exception("Error en la creació de l'arbre","L'operador (" + ctx.getText() + ") no ha sigut declarat a la taula")



        
    

        