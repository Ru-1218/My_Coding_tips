from googletrans import Translator

translator = Translator()

trans_en = translator.translate('定量的データ', dest='en')

print(trans_en.text)

# 安定でないのでtry,exceptしてエラーが出たら何度でも繰り返すようにして使う方がいいかも
