import random


class MyModel:
    def __init__(self):
        print("MyModel 인스턴스가 생성되었습니다.")

    def predict(self, input_text, spam_filter=[]):

        is_spam = True if any(word in input_text for word in spam_filter) else False
        predict_score = 1 if is_spam else 0
        return {
            "input": input_text,
            "reason": "금지어가 포함되어 있습니다." if is_spam else "특이사항 없음",
            "is_spam": is_spam,
            "score": predict_score,
        }
