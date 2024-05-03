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
        return self.visit(expressio1) / self.visit(expressio2)

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
        self.taulaSimbols['x'] = 2
        llista = list(ctx.getChildren())
        print (self.taulaSimbols[llista[1].getText()])
        return (self.taulaSimbols[llista[1].getText()])

    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())