import numpy
num = 5


def judge():
    while True:
        ip = input('input command:')
        if ip != '1' and ip != '2' and ip != '3' and ip != '4' and ip != '5':
            print('input error!')
            continue
        elif ip == '1':
            return None
        elif ip == '2':
            for u in [0, 1, 2]:
                for v in X:
                    print(data[u][v], end='  ')
                print('')
            continue
        elif ip == '3':
            while True:
                print('input a ~ b:')
                a = int(input('a:'))
                b = int(input('b:'))
                if a >= b:
                    print('input error!')
                else:
                    return a, b
        elif ip == '4':
            num = int(input('input number to display once:'))
            while True:
                if num > 0 and num < 16:
                    return num
                else:
                    num = int(input('num is required to >0 and <16:'))
        else:
            exit()


ping = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に',
        'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
pian = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ',
        'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
yin = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si/shi', 'su', 'se', 'so', 'ta', 'ti/chi', 'tu/tsu', 'te', 'to', 'na', 'ni',
       'nu', 'ne', 'no', 'ha', 'hi', 'hu/fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo', 'n']
data = [ping, pian, yin]
print('begin\ninput \'1\' to continue, input \'2\' to show and input \'3\' to set range and input \'4\' to change mode and input \'5\' to exit.')
L = 45*[None]
counter = 0
a = 0
b = 45


while True:
    X = numpy.random.randint(a, b, size=num - 1)
    X = list(set(X))
    while True:
        temp = numpy.random.randint(a, b)  # 无法降低重复出现率
        if temp not in X:
            X.append(temp)
            if len(X) == num:
                break
    Y = numpy.random.randint(0, 3, size=num)  # 生成无重复序列X和模式序列Y，且长度均为num
    List = []
    for x in range(0, len(X)):
        List = List+[data[Y[x]][X[x]]]
    for x in List:
        print(x, end='  ')
    print('')
    temp = judge()
    if type(temp) == tuple:
        a, b = temp
    elif type(temp) == int:
        num = temp
