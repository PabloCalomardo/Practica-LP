# HinNer by Pablo

HinNer by Pablo és una aplicació d'inferència de tipus amb un subconjunt de gramàtica de Haskell i Assignacions de Tipus, utilitzant la plataforma Streamlit i per a la gramàtica el llenguatge antlr4.
És la pràctica de GEI-LP (edició 2023-2024 Q2).

## Instalació

Per poder utilitzar aquest repositori s'ha de tenir instalat Streamlit o a partir del 10/06/2024 entrar buscar HinNer by Pablo a la web d'Streamlit.
Si es vol generar un visitador per a utilitzar l'aplicació en un projecte propi s'ha d'instalar també antlr4 i generar els visitadors.

```bash
pip install streamlit

pip install antlr4-tools
antlr4
pip install antlr4-python3-runtime
```

## Ús

per obrir la web per defecte només cal executar les comandes següents, que crearan els fitxers necessaris per a poder executar l'app amb antlr4
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
streamlit run hm.py
```
Un cop dins, apareixerà una entrada de text on s'haurà d'inserir la comanda desitjada per a que el HinNer la reconegui i executi (cal apretar el botó per a que el programa la detecti).
Si no es vol que es retorni error, cal que primer declareu el tipus tant del números que s'han d'utilitzar tant com de les operacions, les vàriables no cal ja que el propi programa en realitzarà la inferència.

un exemple d'ús pot ser el següent:

```bash
2 :: N      (declarem 2 del tipus N)
(+) :: N -> N -> N      (declarem + com la operació binària que rep dos paràmetres del tipus N i retorna un altre de tipus N)

(+) 2 4     (fem la suma de 2 i 4)
\x -> (+) 2 x       (funció on s'inferirà el tipus de x)
```

## Funcionament
Principalment el compilador accepta dos tipus de seqüencies:

Declaracions:
- enter :: Tipus
- Operacio :: Tipus -> Tipus ... (Tants com es vulgui)

Operacions (cal destacar que només s'acceptaran Operacions i Enters que prèviament se n'hagi declarat el Tipus):
- Enter
- Variable
- (operació) Enter/Variable ... (Tants Enters/Variables com s'hagi definit el tipus de l'operació)
- \Variable -> (Operacio) Enter/Variable Enter/Variable   (Funció Lambda)
- (\Variable -> (Operacio) Enter/Variable Enter/Variable) Enter  (Aplicació d'una funció lambda)

Per a les Declaracions només apareixerà per pantalla una taula on hi haurà tots els enters i operacions que se n'ha declarat el tipus.
Per a les operacions es mostrarà:
- La taula de declaracions descrita anteriorment
- Un Graf sintàctic on, les variables que no estiguin declarades simprement tindran assignades una lletra minúscula de l'abecedari
- Una Taula d'inferència on cada lletra assignada tindrà el seu corresponent Tipus
- Una nova versió del Graf Anterior on les lletres hauran estat substituïdes pels Tipus corresponents (Aquest és el graf definitiu amb inferència)

Cal destacar que hi ha control d'errors, i que si en qualsevol dels casos que falla, es detindrà la creació dels grafs i es mostrarà l'error per pantalla.


## Desenvolupament
El procés de desenvolupament principalment ha estat seguir les tasques de [ENUNCIAT HINNER](https://github.com/gebakx/lp-hinner-24) i de la documentació de l'assignatura.
Inicialment he creat la gramàtica haskell per a poder identificar correctament les expressions, desprès he creat un visitador molt primitiu que permetès crear un arbre i escriure'l en format DOT.

En segon pas he hagut d'afegir els tipus dels nodes al graf (creant un nou diccionari de Tipus) i he afegit la sintaxi de declaració a la gramàtica.

Finalment he hagut de fer la funció d'inferència modificant el visitador per un més semblant a l'evaluador de la documentació (ja vaig haver de fer que la majoria de les funcions del visitador retornessin el seu tipus)
