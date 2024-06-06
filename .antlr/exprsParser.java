// Generated from c:/Users/Enric/Documents/Practica-LP/exprs.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class exprsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, NUMBER=5, ID=6, WS=7, PLUS=8, MINUS=9, 
		MULT=10, DIV=11;
	public static final int
		RULE_root = 0, RULE_expr = 1, RULE_expr2 = 2, RULE_expr3 = 3, RULE_lambdaExpr = 4, 
		RULE_infixExprComp = 5, RULE_infixExpr = 6, RULE_operador = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "expr", "expr2", "expr3", "lambdaExpr", "infixExprComp", "infixExpr", 
			"operador"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'\\'", "'->'", null, null, null, "'+'", "'-'", "'*'", 
			"'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "NUMBER", "ID", "WS", "PLUS", "MINUS", 
			"MULT", "DIV"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "exprs.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public exprsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RootContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EOF() { return getToken(exprsParser.EOF, 0); }
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(16);
			expr();
			setState(17);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OperacioContext extends ExprContext {
		public InfixExprCompContext infixExprComp() {
			return getRuleContext(InfixExprCompContext.class,0);
		}
		public OperacioContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpresioLambdaContext extends ExprContext {
		public LambdaExprContext lambdaExpr() {
			return getRuleContext(LambdaExprContext.class,0);
		}
		public ExpresioLambdaContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VarContext extends ExprContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public VarContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumContext extends ExprContext {
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public NumContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ExprContext {
		public LambdaExprContext lambdaExpr() {
			return getRuleContext(LambdaExprContext.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public FuncionContext(ExprContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OperacioincompletaContext extends ExprContext {
		public InfixExprContext infixExpr() {
			return getRuleContext(InfixExprContext.class,0);
		}
		public OperacioincompletaContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		ExprContext _localctx = new ExprContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_expr);
		try {
			setState(29);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				_localctx = new ExpresioLambdaContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				lambdaExpr();
				}
				break;
			case 2:
				_localctx = new OperacioincompletaContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				infixExpr();
				}
				break;
			case 3:
				_localctx = new OperacioContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(21);
				infixExprComp();
				}
				break;
			case 4:
				_localctx = new FuncionContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(22);
				match(T__0);
				setState(23);
				lambdaExpr();
				setState(24);
				match(T__1);
				setState(25);
				expr2();
				}
				break;
			case 5:
				_localctx = new NumContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(27);
				expr2();
				}
				break;
			case 6:
				_localctx = new VarContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(28);
				expr3();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr2Context extends ParserRuleContext {
		public Expr2Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr2; }
	 
		public Expr2Context() { }
		public void copyFrom(Expr2Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumeroContext extends Expr2Context {
		public TerminalNode NUMBER() { return getToken(exprsParser.NUMBER, 0); }
		public NumeroContext(Expr2Context ctx) { copyFrom(ctx); }
	}

	public final Expr2Context expr2() throws RecognitionException {
		Expr2Context _localctx = new Expr2Context(_ctx, getState());
		enterRule(_localctx, 4, RULE_expr2);
		try {
			_localctx = new NumeroContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(NUMBER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Expr3Context extends ParserRuleContext {
		public Expr3Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr3; }
	 
		public Expr3Context() { }
		public void copyFrom(Expr3Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends Expr3Context {
		public TerminalNode ID() { return getToken(exprsParser.ID, 0); }
		public VariableContext(Expr3Context ctx) { copyFrom(ctx); }
	}

	public final Expr3Context expr3() throws RecognitionException {
		Expr3Context _localctx = new Expr3Context(_ctx, getState());
		enterRule(_localctx, 6, RULE_expr3);
		try {
			_localctx = new VariableContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LambdaExprContext extends ParserRuleContext {
		public LambdaExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lambdaExpr; }
	 
		public LambdaExprContext() { }
		public void copyFrom(LambdaExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class LambdafuncContext extends LambdaExprContext {
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public InfixExprCompContext infixExprComp() {
			return getRuleContext(InfixExprCompContext.class,0);
		}
		public LambdafuncContext(LambdaExprContext ctx) { copyFrom(ctx); }
	}

	public final LambdaExprContext lambdaExpr() throws RecognitionException {
		LambdaExprContext _localctx = new LambdaExprContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_lambdaExpr);
		try {
			_localctx = new LambdafuncContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(T__2);
			setState(36);
			expr3();
			setState(37);
			match(T__3);
			setState(38);
			infixExprComp();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InfixExprCompContext extends ParserRuleContext {
		public InfixExprCompContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_infixExprComp; }
	 
		public InfixExprCompContext() { }
		public void copyFrom(InfixExprCompContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OperaciobinariaContext extends InfixExprCompContext {
		public InfixExprContext infixExpr() {
			return getRuleContext(InfixExprContext.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public OperaciobinariaContext(InfixExprCompContext ctx) { copyFrom(ctx); }
	}

	public final InfixExprCompContext infixExprComp() throws RecognitionException {
		InfixExprCompContext _localctx = new InfixExprCompContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_infixExprComp);
		try {
			_localctx = new OperaciobinariaContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			infixExpr();
			setState(43);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				{
				setState(41);
				expr2();
				}
				break;
			case ID:
				{
				setState(42);
				expr3();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InfixExprContext extends ParserRuleContext {
		public InfixExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_infixExpr; }
	 
		public InfixExprContext() { }
		public void copyFrom(InfixExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OperaciounariaContext extends InfixExprContext {
		public OperadorContext operador() {
			return getRuleContext(OperadorContext.class,0);
		}
		public Expr2Context expr2() {
			return getRuleContext(Expr2Context.class,0);
		}
		public Expr3Context expr3() {
			return getRuleContext(Expr3Context.class,0);
		}
		public OperaciounariaContext(InfixExprContext ctx) { copyFrom(ctx); }
	}

	public final InfixExprContext infixExpr() throws RecognitionException {
		InfixExprContext _localctx = new InfixExprContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_infixExpr);
		try {
			_localctx = new OperaciounariaContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(45);
			match(T__0);
			setState(46);
			operador();
			setState(47);
			match(T__1);
			setState(50);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				{
				setState(48);
				expr2();
				}
				break;
			case ID:
				{
				setState(49);
				expr3();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperadorContext extends ParserRuleContext {
		public TerminalNode PLUS() { return getToken(exprsParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(exprsParser.MINUS, 0); }
		public TerminalNode MULT() { return getToken(exprsParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(exprsParser.DIV, 0); }
		public OperadorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operador; }
	}

	public final OperadorContext operador() throws RecognitionException {
		OperadorContext _localctx = new OperadorContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_operador);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 3840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u000b7\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0003\u0001\u001e\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0003\u0005,\b\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u00063\b\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0000\u0000\b\u0000\u0002\u0004\u0006\b"+
		"\n\f\u000e\u0000\u0001\u0001\u0000\b\u000b5\u0000\u0010\u0001\u0000\u0000"+
		"\u0000\u0002\u001d\u0001\u0000\u0000\u0000\u0004\u001f\u0001\u0000\u0000"+
		"\u0000\u0006!\u0001\u0000\u0000\u0000\b#\u0001\u0000\u0000\u0000\n(\u0001"+
		"\u0000\u0000\u0000\f-\u0001\u0000\u0000\u0000\u000e4\u0001\u0000\u0000"+
		"\u0000\u0010\u0011\u0003\u0002\u0001\u0000\u0011\u0012\u0005\u0000\u0000"+
		"\u0001\u0012\u0001\u0001\u0000\u0000\u0000\u0013\u001e\u0003\b\u0004\u0000"+
		"\u0014\u001e\u0003\f\u0006\u0000\u0015\u001e\u0003\n\u0005\u0000\u0016"+
		"\u0017\u0005\u0001\u0000\u0000\u0017\u0018\u0003\b\u0004\u0000\u0018\u0019"+
		"\u0005\u0002\u0000\u0000\u0019\u001a\u0003\u0004\u0002\u0000\u001a\u001e"+
		"\u0001\u0000\u0000\u0000\u001b\u001e\u0003\u0004\u0002\u0000\u001c\u001e"+
		"\u0003\u0006\u0003\u0000\u001d\u0013\u0001\u0000\u0000\u0000\u001d\u0014"+
		"\u0001\u0000\u0000\u0000\u001d\u0015\u0001\u0000\u0000\u0000\u001d\u0016"+
		"\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001c"+
		"\u0001\u0000\u0000\u0000\u001e\u0003\u0001\u0000\u0000\u0000\u001f \u0005"+
		"\u0005\u0000\u0000 \u0005\u0001\u0000\u0000\u0000!\"\u0005\u0006\u0000"+
		"\u0000\"\u0007\u0001\u0000\u0000\u0000#$\u0005\u0003\u0000\u0000$%\u0003"+
		"\u0006\u0003\u0000%&\u0005\u0004\u0000\u0000&\'\u0003\n\u0005\u0000\'"+
		"\t\u0001\u0000\u0000\u0000(+\u0003\f\u0006\u0000),\u0003\u0004\u0002\u0000"+
		"*,\u0003\u0006\u0003\u0000+)\u0001\u0000\u0000\u0000+*\u0001\u0000\u0000"+
		"\u0000,\u000b\u0001\u0000\u0000\u0000-.\u0005\u0001\u0000\u0000./\u0003"+
		"\u000e\u0007\u0000/2\u0005\u0002\u0000\u000003\u0003\u0004\u0002\u0000"+
		"13\u0003\u0006\u0003\u000020\u0001\u0000\u0000\u000021\u0001\u0000\u0000"+
		"\u00003\r\u0001\u0000\u0000\u000045\u0007\u0000\u0000\u00005\u000f\u0001"+
		"\u0000\u0000\u0000\u0003\u001d+2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}