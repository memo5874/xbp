import random
random_quiz_id = random.randint(1, 8)
quiz_data = {
    #クイズ情報
    1: {
        "question": "1453=0,1915=1,2409=2,6010=3,9981=4,8848=?",
        "choices": ["A. 4", "B. 5", "C. 6", "D. 18000"],
        "correct_answer": "C",
        "explanation": "数字にある〇の数に注目してみよう"
    },
    2: {
        "question": "ある大学が生態系に大きな害をもたらす藻を発見しました。その藻は毎日二倍に増殖するため、わずか３０日でため池が藻でいっぱいになり、貴重な水源が汚染されてしまいます。この藻がため池の半分を占めるようになるのは何日目でしょう？",
        "choices": ["A. 15日目", "B. 29日目", "C. 31日目"],
        "correct_answer": "B",
        "explanation": "ため池が藻でいっぱいになるのは３０日のため、半分になるのはその前日の２９日目となる" 
    },
    3: {
        "question": "58は初雪八落、初雪八落は0。39は覆夏竹、覆夏竹は14。99は毯牡丹、毬牡丹は8。27は暖陽花、暖陽花は4。初雪八落、覆夏竹、毬牡丹、暖陽花を全て合わせると？",
        "choices": ["A. 162", "B. 42", "C. 365"],
        "correct_answer": "A",
        "explanation": "文章前半の２つの数字をばらばらにして掛け算して答えを出すと、文章が成り立つようになっている。"
    },
    4: {
        "question": "マイケル、サリー、リリアの三人のうち、一人は善人、一人は悪人、一人は嘘つきです。善人は事実しか言わず、悪人は嘘しか言いません。嘘つきは事実を言ったかと思えば、嘘を言うというように、なんでも言います。ある日リリアが「サリーは善人ではなく悪人だ」と言いました。そしてサリーは「マイケルとリリアのどちらか一人は善人だ」と言いました。三人のうち、嘘つきは誰でしょうか？",
        "choices": ["A. マイケル", "B. サリー", "C. リリア"],
        "correct_answer": "B",
        "explanation": "①サリーが善人だと仮定...発言内容から善人が2人にいることになってしまうため破綻②サリーが悪人だと仮定...残った2人のどちらかが善人という発言内容が真実になってしまうため破綻③消去法でサリーが嘘つきになる"
    }, 
    5: {
        "question": "ある家には大きな駐車場があり、４２台の車が停められています。ある日、泥棒が数台のタイヤを盗んでいきました。現在はその４２台のうち、タイヤが３つしかない車が数台あります。保険会社の社員が損害の査定にやってきて、駐車場に停められている車のタイヤの数を数えたところ、そこには全部で１５４のタイヤがありました。タイヤを盗まれた車は何台でしょう？",
        "choices": ["A. 42台", "B. 14台", "C. 28台"],
        "correct_answer": "B",
        "explanation": "①元々のタイヤの数は42✖4=168②盗まれたタイヤの数は168-154=14③1つの車から2つ以上タイヤは盗まれていないため答えは14台"  
    }, 
    6: {
        "question": "数日前にある家でタイヤを盗んだ犯人を見つけました。当時、警察は容疑者をケビン、ミカエル、セレスの三人に絞り込んでいました。三人は言い争って譲りません。ケビンは「タイヤを盗んだのはミカエルだ！」と言いました。頭のいい警察官の一人はすぐに犯人を察しました。自分の部下を試すため、頭のいい警察官はすぐに誰が泥棒かを言わずに、「おかしいな。三人の中で泥棒だけが嘘をついてない」と言いました。家の車のタイヤを盗んだのは一体誰でしょう？",
        "choices": ["A. ケビン", "B. ミカエル", "C. セレス"],
        "correct_answer": "C",
        "explanation": "①ケビンが犯人と仮定すると、「ミカエルが犯人」という話が正しくなり犯人が2人になってしまう②ミカエルが犯人と仮定すると、ケビンの発言は嘘で「ミカエルは犯人じゃない」となり話が成り立たない③上記を踏まえると、ケビンの発言が成り立つ犯人はセレスとなる"
    },
    7: {
        "question": "飛鳥は友達と「花色推理」のゲームをしています。飛鳥は大輔、雅、そしていつも一緒に遊んでいるお姉さんの頭に紙の花を挿しました。紙の花は全部で四つあり、白が二つ、紫が二つ。飛鳥を含め、誰も自分と他の人の頭にある紙の花の色を見ていません。次に、飛鳥は皆に前を向いて一列に並んでもらいました。先頭から飛鳥、大輔、雅、お姉さんです。それぞれ前を向いており、自分の前の人しか見えていません。後ろを振り返ったり、自分の頭の紙の花を見たりしてはいけません。公平を期すため、飛鳥はお姉さんに目隠ししました。彼女は背が高いからです。しかし、本人たちには見えていませんが、私たちが横を通り過ぎたとき、飛鳥と雅の頭にあるのは白い花、大輔とお姉さんの頭にあるのは紫の花であることが一目瞭然でした。いくら飛鳥が公平にしようと頑張っても、このゲームでは一人だけ自分の頭の花の色がわかってしまいます。それは誰でしょうか？",
        "choices": ["A. 飛鳥", "B. 大輔", "C. 雅", "D. お姉さん"],
        "correct_answer": "B",
        "explanation": "飛鳥...一番前にいるため他の人の色の判別不可能 雅...前2人が別の色の場合判別不可能 お姉さん...目隠しされているため判別不可能 大輔...ルカの判別内容によって色の判別が可能"
    },
    8: {
        "question": "1+4=5,5+5=10,10+6=4,11+8=7,9+9=?",
        "choices": ["A. 18", "B. 2", "C. 6", "D. 7"],
        "correct_answer": "C",
        "explanation": "数字を時刻として考えると？"
    },
    }


random_question = quiz_data[random_quiz_id]

question = random_question["question"]
choices = random_question["choices"]
correct_answer = random_question["correct_answer"]

print(question)
for choice in choices:
    print(choice)

player_answer = input("回答を選んでください（A/B/C/D）: ")





if player_answer.upper() == correct_answer:
    print("正解です！")
    
else:
    print("不正解です。正解は " + correct_answer + " です。")

response = input("解説が必要ですか？（はい/いいえ）: ")
if response.lower() == "はい":
    print("explanation")

explanation = random_question["explanation"]
print(explanation)




       
                   
