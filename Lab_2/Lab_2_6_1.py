
alphavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю']

alphavit = {key: 0 for key in alphavit}

with open("article_rus.txt", "r", encoding="utf8") as file:
    str = file.read()

for chr in str:
    if chr.lower() in alphavit.keys():
        alphavit[chr.lower()] += 1

for i in alphavit:
    print(i + ":", alphavit[i])