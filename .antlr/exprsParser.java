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
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, NUMBER=6, ID=7, CAP=8, WS=9, PLUS=10, 
		MINUS=11, MULT=12, DIV=13;
	public static final int
		RULE_root = 0, RULE_expr = 1, RULE_expr2 = 2, RULE_expr3 = 3, RULE_assig = 4, 
		RULE_expr4 = 5, RULE_normAssig = 6, RULE_opAssig = 7, RULE_lambdaExpr = 8, 
		RULE_infixExprComp = 9, RULE_infixExpr = 10, RULE_operador = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"root", "expr", "expr2", "expr3", "assig", "expr4", "normAssig", "opAssig", 
			"lambdaExpr", "infixExprComp", "infixExpr", "operador"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'->'", "'::'", "'\\'", null, null, null, null, "'+'", 
			"'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "NUMBER", "ID", "CAP", "WS", "PLUS", 
			"MINUS", "MULT", "DIV"
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
		public RootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_root; }
	 
		public RootContext() { }
		public void copyFrom(RootContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignacioContext extends RootContext {
		public AssigContext assig() {
			return getRuleContext(AssigContext.class,0);
		}
		public TerminalNode EOF() { return getToken(exprsParser.EOF, 0); }
		public AssignacioContext(RootContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ExpressioContext extends RootContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode EOF() { return getToken(exprsParser.EOF, 0); }
		public ExpressioContext(RootContext ctx) { copyFrom(ctx); }
	}

	public final RootContext root() throws RecognitionException {
		RootContext _localctx = new RootContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_root);
		try {
			setState(30);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				_localctx = new ExpressioContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(24);
				expr();
				setState(25);
				match(EOF);
				}
				break;
			case 2:
				_localctx = new AssignacioContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(27);
				assig();
				setState(28);
				match(EOF);
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
			setState(42);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				_localctx = new ExpresioLambdaContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(32);
				lambdaExpr();
				}
				break;
			case 2:
				_localctx = new OperacioincompletaContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				infixExpr();
				}
				break;
			case 3:
				_localctx = new OperacioContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(34);
				infixExprComp();
				}
				break;
			case 4:
				_localctx = new FuncionContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(35);
				match(T__0);
				setState(36);
				lambdaExpr();
				setState(37);
				match(T__1);
				setState(38);
				expr2();
				}
				break;
			case 5:
				_localctx = new NumContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(40);
				expr2();
				}
				break;
			case 6:
				_localctx = new VarContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(41);
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
			setState(44);
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
			setState(46);
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
	public static class AssigContext extends ParserRuleContext {
		public AssigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assig; }
	 
		public AssigContext() { }
		public void copyFrom(AssigContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NormalassigContext extends AssigContext {
		public NormAssigContext normAssig() {
			return getRuleContext(NormAssigContext.class,0);
		}
		public NormalassigContext(AssigContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OperassigContext extends AssigContext {
		public OpAssigContext opAssig() {
			return getRuleContext(OpAssigContext.class,0);
		}
		public OperassigContext(AssigContext ctx) { copyFrom(ctx); }
	}

	public final AssigContext assig() throws RecognitionException {
		AssigContext _localctx = new AssigContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_assig);
		try {
			setState(50);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
			case ID:
				_localctx = new NormalassigContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				normAssig();
				}
				break;
			case T__0:
				_localctx = new OperassigContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				opAssig();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class Expr4Context extends ParserRuleContext {
		public Expr4Context(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr4; }
	 
		public Expr4Context() { }
		public void copyFrom(Expr4Context ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CapContext extends Expr4Context {
		public TerminalNode CAP() { return getToken(exprsParser.CAP, 0); }
		public CapContext(Expr4Context ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CaprecContext extends Expr4Context {
		public TerminalNode CAP() { return getToken(exprsParser.CAP, 0); }
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public CaprecContext(Expr4Context ctx) { copyFrom(ctx); }
	}

	public final Expr4Context expr4() throws RecognitionException {
		Expr4Context _localctx = new Expr4Context(_ctx, getState());
		enterRule(_localctx, 10, RULE_expr4);
		try {
			setState(56);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				_localctx = new CapContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(52);
				match(CAP);
				}
				break;
			case 2:
				_localctx = new CaprecContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(53);
				match(CAP);
				setState(54);
				match(T__2);
				setState(55);
				expr4();
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
	public static class NormAssigContext extends ParserRuleContext {
		public NormAssigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_normAssig; }
	 
		public NormAssigContext() { }
		public void copyFrom(NormAssigContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NassigContext extends NormAssigContext {
		public TerminalNode CAP() { return getToken(exprsParser.CAP, 0); }
		public TerminalNode NUMBER() { return getToken(exprsParser.NUMBER, 0); }
		public TerminalNode ID() { return getToken(exprsParser.ID, 0); }
		public NassigContext(NormAssigContext ctx) { copyFrom(ctx); }
	}

	public final NormAssigContext normAssig() throws RecognitionException {
		NormAssigContext _localctx = new NormAssigContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_normAssig);
		int _la;
		try {
			_localctx = new NassigContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_la = _input.LA(1);
			if ( !(_la==NUMBER || _la==ID) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(59);
			match(T__3);
			setState(60);
			match(CAP);
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
	public static class OpAssigContext extends ParserRuleContext {
		public OpAssigContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_opAssig; }
	 
		public OpAssigContext() { }
		public void copyFrom(OpAssigContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class OpassigContext extends OpAssigContext {
		public OperadorContext operador() {
			return getRuleContext(OperadorContext.class,0);
		}
		public TerminalNode CAP() { return getToken(exprsParser.CAP, 0); }
		public Expr4Context expr4() {
			return getRuleContext(Expr4Context.class,0);
		}
		public OpassigContext(OpAssigContext ctx) { copyFrom(ctx); }
	}

	public final OpAssigContext opAssig() throws RecognitionException {
		OpAssigContext _localctx = new OpAssigContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_opAssig);
		try {
			_localctx = new OpassigContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__0);
			setState(63);
			operador();
			setState(64);
			match(T__1);
			setState(65);
			match(T__3);
			setState(66);
			match(CAP);
			setState(67);
			match(T__2);
			setState(68);
			expr4();
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
		enterRule(_localctx, 16, RULE_lambdaExpr);
		try {
			_localctx = new LambdafuncContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__4);
			setState(71);
			expr3();
			setState(72);
			match(T__2);
			setState(73);
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
		enterRule(_localctx, 18, RULE_infixExprComp);
		try {
			_localctx = new OperaciobinariaContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			infixExpr();
			setState(78);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				{
				setState(76);
				expr2();
				}
				break;
			case ID:
				{
				setState(77);
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
		enterRule(_localctx, 20, RULE_infixExpr);
		try {
			_localctx = new OperaciounariaContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(80);
			match(T__0);
			setState(81);
			operador();
			setState(82);
			match(T__1);
			setState(85);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NUMBER:
				{
				setState(83);
				expr2();
				}
				break;
			case ID:
				{
				setState(84);
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
		enterRule(_localctx, 22, RULE_operador);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15360L) != 0)) ) {
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
		"\u0004\u0001\rZ\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0003"+
		"\u0000\u001f\b\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001+\b\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0003\u00043\b\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u00059\b\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0003\tO\b\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0003\nV\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0000"+
		"\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0000"+
		"\u0002\u0001\u0000\u0006\u0007\u0001\u0000\n\rW\u0000\u001e\u0001\u0000"+
		"\u0000\u0000\u0002*\u0001\u0000\u0000\u0000\u0004,\u0001\u0000\u0000\u0000"+
		"\u0006.\u0001\u0000\u0000\u0000\b2\u0001\u0000\u0000\u0000\n8\u0001\u0000"+
		"\u0000\u0000\f:\u0001\u0000\u0000\u0000\u000e>\u0001\u0000\u0000\u0000"+
		"\u0010F\u0001\u0000\u0000\u0000\u0012K\u0001\u0000\u0000\u0000\u0014P"+
		"\u0001\u0000\u0000\u0000\u0016W\u0001\u0000\u0000\u0000\u0018\u0019\u0003"+
		"\u0002\u0001\u0000\u0019\u001a\u0005\u0000\u0000\u0001\u001a\u001f\u0001"+
		"\u0000\u0000\u0000\u001b\u001c\u0003\b\u0004\u0000\u001c\u001d\u0005\u0000"+
		"\u0000\u0001\u001d\u001f\u0001\u0000\u0000\u0000\u001e\u0018\u0001\u0000"+
		"\u0000\u0000\u001e\u001b\u0001\u0000\u0000\u0000\u001f\u0001\u0001\u0000"+
		"\u0000\u0000 +\u0003\u0010\b\u0000!+\u0003\u0014\n\u0000\"+\u0003\u0012"+
		"\t\u0000#$\u0005\u0001\u0000\u0000$%\u0003\u0010\b\u0000%&\u0005\u0002"+
		"\u0000\u0000&\'\u0003\u0004\u0002\u0000\'+\u0001\u0000\u0000\u0000(+\u0003"+
		"\u0004\u0002\u0000)+\u0003\u0006\u0003\u0000* \u0001\u0000\u0000\u0000"+
		"*!\u0001\u0000\u0000\u0000*\"\u0001\u0000\u0000\u0000*#\u0001\u0000\u0000"+
		"\u0000*(\u0001\u0000\u0000\u0000*)\u0001\u0000\u0000\u0000+\u0003\u0001"+
		"\u0000\u0000\u0000,-\u0005\u0006\u0000\u0000-\u0005\u0001\u0000\u0000"+
		"\u0000./\u0005\u0007\u0000\u0000/\u0007\u0001\u0000\u0000\u000003\u0003"+
		"\f\u0006\u000013\u0003\u000e\u0007\u000020\u0001\u0000\u0000\u000021\u0001"+
		"\u0000\u0000\u00003\t\u0001\u0000\u0000\u000049\u0005\b\u0000\u000056"+
		"\u0005\b\u0000\u000067\u0005\u0003\u0000\u000079\u0003\n\u0005\u00008"+
		"4\u0001\u0000\u0000\u000085\u0001\u0000\u0000\u00009\u000b\u0001\u0000"+
		"\u0000\u0000:;\u0007\u0000\u0000\u0000;<\u0005\u0004\u0000\u0000<=\u0005"+
		"\b\u0000\u0000=\r\u0001\u0000\u0000\u0000>?\u0005\u0001\u0000\u0000?@"+
		"\u0003\u0016\u000b\u0000@A\u0005\u0002\u0000\u0000AB\u0005\u0004\u0000"+
		"\u0000BC\u0005\b\u0000\u0000CD\u0005\u0003\u0000\u0000DE\u0003\n\u0005"+
		"\u0000E\u000f\u0001\u0000\u0000\u0000FG\u0005\u0005\u0000\u0000GH\u0003"+
		"\u0006\u0003\u0000HI\u0005\u0003\u0000\u0000IJ\u0003\u0012\t\u0000J\u0011"+
		"\u0001\u0000\u0000\u0000KN\u0003\u0014\n\u0000LO\u0003\u0004\u0002\u0000"+
		"MO\u0003\u0006\u0003\u0000NL\u0001\u0000\u0000\u0000NM\u0001\u0000\u0000"+
		"\u0000O\u0013\u0001\u0000\u0000\u0000PQ\u0005\u0001\u0000\u0000QR\u0003"+
		"\u0016\u000b\u0000RU\u0005\u0002\u0000\u0000SV\u0003\u0004\u0002\u0000"+
		"TV\u0003\u0006\u0003\u0000US\u0001\u0000\u0000\u0000UT\u0001\u0000\u0000"+
		"\u0000V\u0015\u0001\u0000\u0000\u0000WX\u0007\u0001\u0000\u0000X\u0017"+
		"\u0001\u0000\u0000\u0000\u0006\u001e*28NU";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}