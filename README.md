# pydips

Multi-criteria Cantonese segmentation with **d**ashes, **i**ntermediates, **p**ipes, and **s**paces.

Note: This package is still in beta, there might be breaking changes in the future.
Currently supports macOS (Apple Silicon) and Linux (x86_64 with avx, avx2, and fma instructions)

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
