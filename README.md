# HinNer by Pablo

HinNer by Pablo és una aplicació d'inferència de tipus amb un subconjunt de gramàtica de Haskell i Assignacions de Tipus, utilitzant les plataformes Streamlit i per a la gramàtica el llenguatge antlr4.
És la pràctica de GEI-LP (edició 2023-2024 Q2).

## Installation

Per poder utilitzar aquest repositori s'ha de tenir instalat Streamlit o a partir del 10/06/2024 entrar buscar HinNer by Pablo a la web d'Streamlit.
Si es vol generar un visitador per a utilitzar l'aplicació en un projecte propi s'ha d'instalar també antlr4 i generar els visitadors.

```bash
pip install streamlit

pip install antlr4-tools
antlr4
pip install antlr4-python3-runtime
```

## Usage

```python
import foobar

# returns 'words'
foobar.pluralize('word')

# returns 'geese'
foobar.pluralize('goose')

# returns 'phenomenon'
foobar.singularize('phenomena')
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)