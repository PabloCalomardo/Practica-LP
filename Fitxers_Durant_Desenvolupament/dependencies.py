from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor

class TreeVisitor(exprsVisitor):
    def __init__(self):
        self.nivell = 0
        taulaSimbols = {}

    def visitSumaresta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '+'):
            print('  ' *  self.nivell + '+')
        else:
            print('  ' *  self.nivell + '-')
        
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitMuldiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '*'):
            print('  ' *  self.nivell + '*')
        else:
            print('  ' *  self.nivell + '/')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitPotencia(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('  ' *  self.nivell + '^')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())
    
    def visitVariable(self, ctx:exprsParser.VariableContext):
        [numero] = list(ctx.getChildren())
        print("  " * self.nivell + numero.getText())


class EvalVisitor(exprsVisitor):

    def __init__(self):
        self.taulaSimbols = {}
    

    def visitRoot(self, ctx):
        [expressio] = list(ctx.getChildren())
        
        print(self.visit(expressio))

    def visitPotencia(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return pow(self.visit(expressio1),self.visit(expressio2) )


    def visitSumaresta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '+'):
            return self.visit(expressio1) + self.visit(expressio2)
        return self.visit(expressio1) - self.visit(expressio2)

    def visitMuldiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if(operador.getText() == '*'):
            return self.visit(expressio1) * self.visit(expressio2)
        return self.visit(expressio1) // self.visit(expressio2)
    
    def visitIgual(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] == self.visit(numero):
            return True
        return False
    
    def visitDiferent(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] != self.visit(numero):
            return True
        return False
    
    def visitMenorigual(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] <= self.visit(numero):
            return True
        return False
    
    def visitMesgranigual(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] >= self.visit(numero):
            return True
        return False

    def visitMenor(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] < self.visit(numero):
            return True
        return False
    
    def visitMajor(self, ctx):
        [var,igual,numero] = list(ctx.getChildren())
        if self.taulaSimbols[var.getText()] > self.visit(numero):
            return True
        return False

    def visitInstr2(self, ctx:exprsParser.Instr2Context):
        llista = list(ctx.getChildren())
        if(len(llista) > 1):
            return self.visit(llista[0]) and self.visit(llista[1])
        return self.visit(llista[0])
    
    def visitCond2(self,ctx):
        llista = list(ctx.getChildren())
        if(len(llista) > 1):
            return self.visit(llista[0]) and self.visit(llista[1])
        return self.visit(llista[0])
            

    def visitVariable(self, ctx:exprsParser.VariableContext):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    
        # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        llista = list(ctx.getChildren())
        self.taulaSimbols[llista[0].getText()] = self.visit(llista[2])
        return self.visit(llista[2])

    # Visit a parse tree produced by exprsParser#escriu.
    def visitEscriu(self, ctx:exprsParser.EscriuContext):
        print(dict (self.taulaSimbols))
        llista = list(ctx.getChildren())
        return self.taulaSimbols[llista[1].getText()]
    
    def visitIf(self,ctx:exprsParser.IfContext):
        llista = list(ctx.getChildren())
        if self.visit(llista[1]):
            return self.visit(llista[3])
        return None

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())

