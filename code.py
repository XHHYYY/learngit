import numpy
def judge():
    while True:
        ip=input('input command:')
        if ip!='1' and ip !='2' and ip!='3' and ip != '4' and ip != '5':
            print('input error!')
            continue
        elif ip == 1:
            return None
        elif ip=='2':
            print(ping[x],pian[x],yin[x])
            continue
        elif ip == '3':
            print('input a ~ b:')
            a=int(input('a:'))
            b=int(input('b:'))
            return a,b
        elif ip == 4:
            num=int(input('input number to display once:'))
            while True:
                if num>4 and num<16:
                    return num
                else:
                    num=int(input('input number to display once:'))
        else:
            exit()
ping = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は', 'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら', 'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん']
pian = ['ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス', 'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ', 'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ', 'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン']
yin = ['a', 'i', 'u', 'e', 'o', 'ka', 'ki', 'ku', 'ke', 'ko', 'sa', 'si/shi', 'su', 'se', 'so', 'ta', 'ti/chi', 'tu/tsu', 'te', 'to', 'na', 'ni', 'nu', 'ne', 'no', 'ha', 'hi', 'hu/fu', 'he', 'ho', 'ma', 'mi', 'mu', 'me', 'mo', 'ya', 'yu', 'yo', 'ra', 'ri', 'ru', 're', 'ro', 'wa', 'wo','n']
print('begin\ninput \'1\' to continue, input \'2\' to show and input \'3\' to set range and input \'4\' to change mode and input \'5\' to exit.')
L=45*[None]
counter=0
a=0
b=45
num = 0
print('input mode:')
temp=judge()

while True:
    if None not in L:
        L=(b-a)*[None]
    x=numpy.random.randint(a,b)
    while True:
        if x not in L:
            L[counter]=x
            break
        else:
            x=numpy.random.randint(a,b)
    counter=(counter+1)%(b-a)
    y=numpy.random.randint(1,4)
    if y==1:
        print(ping[x])
        temp=judge()
        if type(temp)==tuple:
            a,b=temp
            L=(b-a)*[None]
    elif y==2:
        print(pian[x])
        temp=judge()
        if type(temp)==tuple:
            a,b=temp
            L=(b-a)*[None]
        elif type(temp)==int:
            num=temp
    else:
        print(yin[x])
        temp=judge()
        if type(temp)==tuple:
            a,b=temp
            L=(b-a)*[None]