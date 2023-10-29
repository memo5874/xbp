import random

# クイズ情報を辞書で管理
quiz_data = {
    1: {
        "question": "次のうち、最も大きな惑星は何ですか？",
        "choices": ["A. 地球", "B. 木星", "C. 火星", "D. 金星"],
        "correct_answer": "B",
        "explanation": "木星は太陽系で最も大きな惑星です。"
    },
    2: {
        "question": "次のうち、最も長い川は何ですか？",
        "choices": ["A. ナイル川", "B. アマゾン川", "C. ミシシッピ川", "D. ユーフラテス川"],
        "correct_answer": "A",
        "explanation": "ナイル川は世界で最も長い川であり、エジプトに流れています。"
    },
    # 他のクイズ情報も同様に追加
}

# 1から辞書の長さまでのランダムな整数を生成
random_quiz_id = random.randint(1, len(quiz_data))

# ランダムなクイズ情報を取得
random_question = quiz_data[random_quiz_id]

# クイズを表示
question = random_question["question"]
choices = random_question["choices"]
correct_answer = random_question["correct_answer"]

print(question)
for choice in choices:
    print(choice)

# プレイヤーからの回答を受け付け、正誤を確認
player_answer = input("回答を選んでください（A/B/C/D）: ")

# 解説を表示
explanation = random_question["explanation"]
print("解説: " + explanation)

# プレイヤーの回答の正誤にかかわらず、解説を表示
