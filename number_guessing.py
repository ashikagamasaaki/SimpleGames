import random

my_point = 50

hint_datas = {
    '0': '答えてみる(間違えると10点マイナス)',
    '1': '偶数かどうか(8ポイントマイナス)',
    '2': '3の倍数かどうか(7ポイントマイナス)',
    '3': '5の倍数かどうか(5ポイントマイナス)',
    '4': '7の倍数かどうか(3ポイントマイナス)',
    '5': '9の倍数かどうか(1ポイントマイナス)'
}

minus_points = {
    '0': 10,
    '1': 8,
    '2': 7,
    '3': 5,
    '4': 3,
    '5': 1
}

# 正解の数字に関する処理
def answer():
    ans = random.randint(10, 99)
    return ans

# ヒントに関する処理
def hint(ans_num, operation):
    hint_ans = ''
    if operation == '1':
        hint_ans = f'{hint_datas.get(operation)} ---> {ans_num % 2 == 0}'
    elif operation == '2':
        hint_ans = f'{hint_datas.get(operation)} ---> {ans_num % 3 == 0}'
    elif operation == '3':
        hint_ans = f'{hint_datas.get(operation)} ---> {ans_num % 5 == 0}'
    elif operation == '4':
        hint_ans = f'{hint_datas.get(operation)} ---> {ans_num % 7 == 0}'
    else:
        hint_ans = f'{hint_datas.get(operation)} ---> {ans_num % 9 == 0}'
    return hint_ans


# ポイント計算に関する処理
def calc(operation):
    minus = minus_points.get(operation)
    global my_point
    my_point -= minus


# 表示に関する処理
def display(ans_num):
    str_num = str(ans_num)
    total = int(str_num[0]) + int(str_num[1])
    txt = "10から99の数字をあてます。\n\
あなたは最初に50点もっていて、ヒントを開くたび、誤答をするたびに点数が引かれていきます。\n\
10の位と1の位の数の和は{}です。\n\
----------------------------------------\n".format(total)

    hint_txt = ''    
    for n, t in hint_datas.items():
        hint_txt = hint_txt +  f'[{n}]: {t} \n'

    return txt + hint_txt


# クライアントとのやり取りに関する処理
def client():
    operation = input('回答するか、ヒントを聞くか選択してください(0~5の数字から選択)')
    return operation
    


def main():
    # 正解の数字取得
    ans_num = answer()
    
    # 最初の問題文表示
    print(display(ans_num))
        
    while True:
        operation = client()
        
        if operation not in ['0', '1', '2', '3', '4', '5']:
            print('入力が不正です。0~5の数値で入力してください。')
            continue
        
        if operation == '0':
            answer_operation = input('回答を入力してください')
            if int(answer_operation) == ans_num:
                print('正解です。おめでとうございます。')
                break
            else:
                print('不正解です。')
                calc(operation)
        else:
            print(hint(ans_num, operation))
            calc(operation)
        
        if my_point > 0:
            print(f'現在のポイントは{my_point}です。')
            continue
        else:
            print('残念、ポイントがなくなりました。終了です。')
            break



if __name__ == '__main__':
    main()