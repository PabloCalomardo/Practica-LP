// Generated from c:/Users/Enric/Documents/Practica-LP/exprs.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link exprsParser}.
 */
public interface exprsListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link exprsParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(exprsParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(exprsParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ExpresioLambda}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpresioLambda(exprsParser.ExpresioLambdaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ExpresioLambda}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpresioLambda(exprsParser.ExpresioLambdaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Operacioincompleta}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOperacioincompleta(exprsParser.OperacioincompletaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Operacioincompleta}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOperacioincompleta(exprsParser.OperacioincompletaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Operacio}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOperacio(exprsParser.OperacioContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Operacio}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOperacio(exprsParser.OperacioContext ctx);
	/**
	 * Enter a parse tree produced by the {@code funcion}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFuncion(exprsParser.FuncionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code funcion}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFuncion(exprsParser.FuncionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numovar}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNumovar(exprsParser.NumovarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numovar}
	 * labeled alternative in {@link exprsParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNumovar(exprsParser.NumovarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code numero}
	 * labeled alternative in {@link exprsParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterNumero(exprsParser.NumeroContext ctx);
	/**
	 * Exit a parse tree produced by the {@code numero}
	 * labeled alternative in {@link exprsParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitNumero(exprsParser.NumeroContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variable}
	 * labeled alternative in {@link exprsParser#expr2}.
	 * @param ctx the parse tree
	 */
	void enterVariable(exprsParser.VariableContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variable}
	 * labeled alternative in {@link exprsParser#expr2}.
	 * @param ctx the parse tree
	 */
	void exitVariable(exprsParser.VariableContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lambdafunc}
	 * labeled alternative in {@link exprsParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void enterLambdafunc(exprsParser.LambdafuncContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lambdafunc}
	 * labeled alternative in {@link exprsParser#lambdaExpr}.
	 * @param ctx the parse tree
	 */
	void exitLambdafunc(exprsParser.LambdafuncContext ctx);
	/**
	 * Enter a parse tree produced by the {@code operaciobinaria}
	 * labeled alternative in {@link exprsParser#infixExprComp}.
	 * @param ctx the parse tree
	 */
	void enterOperaciobinaria(exprsParser.OperaciobinariaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code operaciobinaria}
	 * labeled alternative in {@link exprsParser#infixExprComp}.
	 * @param ctx the parse tree
	 */
	void exitOperaciobinaria(exprsParser.OperaciobinariaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code operaciounaria}
	 * labeled alternative in {@link exprsParser#infixExpr}.
	 * @param ctx the parse tree
	 */
	void enterOperaciounaria(exprsParser.OperaciounariaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code operaciounaria}
	 * labeled alternative in {@link exprsParser#infixExpr}.
	 * @param ctx the parse tree
	 */
	void exitOperaciounaria(exprsParser.OperaciounariaContext ctx);
	/**
	 * Enter a parse tree produced by {@link exprsParser#operador}.
	 * @param ctx the parse tree
	 */
	void enterOperador(exprsParser.OperadorContext ctx);
	/**
	 * Exit a parse tree produced by {@link exprsParser#operador}.
	 * @param ctx the parse tree
	 */
	void exitOperador(exprsParser.OperadorContext ctx);
}