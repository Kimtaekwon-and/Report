import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein_Distance 

class SimpleChatBot:
    def __init__(self, filepath):
        self.questions, self.answers = self.load_data(filepath)
        
    def load_data(self, filepath):
        data = pd.read_csv(filepath)
        questions = data['Q'].tolist()  # 질문열만 뽑아 파이썬 리스트로 저장
        answers = data['A'].tolist()   # 답변열만 뽑아 파이썬 리스트로 저장
        return questions, answers

    def find_best_answer(self, input_sentence):

        #Levenshtein_Distance.py 의 calc_distance 함수를 이용하여 input과 question의 유사도 측정
        similarities = Levenshtein_Distance.calc_distance(input_sentence,self.questions)
        best_match_index = similarities.index(min(similarities))   # 값이 가장 낮은 인덱스를 반환
        
        return self.answers[best_match_index]#best한 답변을 측정

#csv 경로
filepath = 'ChatbotData.csv'

#챗봇 instance
chatbot = SimpleChatBot(filepath)

# '종료'라는 단어가 입력될 때까지 챗봇과의 대화를 반복합니다.
while True:
    input_sentence = input('You: ')
    if input_sentence.lower() == '종료':
        break
    response = chatbot.find_best_answer(input_sentence)
    print('Chatbot:', response)
    
