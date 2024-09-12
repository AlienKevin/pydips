from pydips import BertModel

def test_cut():
    model = BertModel()
    assert model.cut('阿張先生嗰時好nice㗎', mode='coarse') == ['阿張先生', '嗰時', '好', 'nice', '㗎']
    assert model.cut('阿張先生嗰時好nice㗎', mode='fine') == ['阿', '張', '先生', '嗰', '時', '好', 'nice', '㗎']
    assert model.cut('阿張先生嗰時好nice㗎', mode='dips_str') == '阿-張|先生 嗰-時 好 nice 㗎'
    assert model.cut('阿張先生嗰時好nice㗎', mode='dips') == ['S', 'D', 'P', 'I', 'S', 'D', 'S', 'S', 'I', 'I', 'I', 'S']

if __name__ == '__main__':
    test_cut()
