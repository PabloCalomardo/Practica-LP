# HinNer by Pablo

HinNer by Pablo és una aplicació d'inferència de tipus amb un subconjunt de gramàtica de Haskell i Assignacions de Tipus, utilitzant les plataformes Streamlit i per a la gramàtica el llenguatge antlr4.
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

## Us

per obrir la web per defecte només cal executar les comandes següents, que crearan els fitxers necessaris per a poder executar l'app amb antlr4
```bash
antlr4 -Dlanguage=Python3 -no-listener -visitor hm.g4
streamlit run hm.py
```
Un cop dins, apareixerà una entrada de text on s'haurà d'inserir la comanda desitjada per a que el HinNer la reconegui i executi.
Si no es vol que es retorni error, cal que primer declareu el tipus tant del números que s'han d'utilitzar tant com de les operacions, les vàriables no cal ja que el propi programa en realitzarà la inferència.

un exemple d'usatge pot ser el següent:

```bash
2 :: N      (declarem 2 del tipus N)
(+) :: N -> N -> N      (declarem + com la operació binària que rep dos paràmetres del tipus N i retorna un altre de tipus N)

(+) 2 4     (fem la suma de 2 i 4)
\x -> (+) 2 x       (funció on s\'inferirà el tipus de x)
```

## Desenvolupament

## License

[MIT](https://choosealicense.com/licenses/mit/)