# pydips

Multi-criteria Cantonese segmentation with **d**ashes, **i**ntermediates, **p**ipes, and **s**paces.

Note: This package is still in beta, there might be breaking changes in the future.
Currently supports macOS (Apple Silicon) and Linux (x86_64 with avx, avx2, and fma instructions)

See https://github.com/AlienKevin/dips for more details on the segmentation model.

## Install

```sh
pip install pydips
```

## Usage

```python
>>> from pydips import BertModel
>>> model = BertModel()

>>> model.cut('阿張先生嗰時好nice㗎', mode='coarse')
['阿張先生', '嗰時', '好', 'nice', '㗎']

>>> model.cut('阿張先生嗰時好nice㗎', mode='fine')
['阿', '張', '先生', '嗰', '時', '好', 'nice', '㗎']

>>> model.cut('阿張先生嗰時好nice㗎', mode='dips_str')
'阿-張|先生 嗰-時 好 nice 㗎'

>>> model.cut('阿張先生嗰時好nice㗎', mode='dips')
['S', 'D', 'P', 'I', 'S', 'D', 'S', 'S', 'I', 'I', 'I', 'S']
```

## Release

1. Bump version in `pyproject.toml`
2. Clear the exising `dist` folder: `rm -rf dist/`
3. Buid: `python -m build`
4. Upload to TestPyPI: `twine upload -r testpypi dist/*`
5. Test TestPyPI version locally: `pip install -i https://test.pypi.org/simple/ pydips`
6. Upload to PyPI: `twine upload dist/*`
