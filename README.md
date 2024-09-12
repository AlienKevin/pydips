# pydips

Multi-criteria Cantonese segmentation with **d**ashes, **i**ntermediates, **p**ipes, and **s**paces.

Note: This package is still in beta, there might be breaking changes in the future.

## Install

```sh
$ pip install pydips
```

## Usage

```python
>>> import pydips
>>> pydips.cut('阿張先生嗰時好nice㗎', mode='coarse')
['阿張先生', '嗰時', '好', 'nice', '㗎']
>>> pydips.cut('阿張先生嗰時好nice㗎', mode='fine')
['阿', '張', '先生', '嗰', '時', '好', 'nice', '㗎']
>>> pydips.cut('阿張先生嗰時好nice㗎', mode='dips_str')
'阿-張|先生 嗰-時 好 nice 㗎'
```
