import streamlit as st

st.set_page_config(page_title='Test results calculator', page_icon='📝', layout='centered', initial_sidebar_state='collapsed')

class Answer:
    def __init__(self, category, value, question_number):
        self.category = category
        self.value = value
        self.question_number = question_number
    
    def __str__(self):
        return f'Category: {self.category}, Value: {self.value}, Question Number: {self.question_number}'

class Survey:
    def __init__(self, categories):
        self.categories = categories
        self.answers = {category: [] for category in categories}
        
    def add_answer(self, answer):
        self.answers[answer.category].append(answer)
    
    def calculate_score(self):
        scores = {category: 0 for category in self.categories}
        for category, answers in self.answers.items():
            for answer in answers:
                scores[category] += int(answer.value)
        return scores
    
    def output(self):
        answers_str = {category: [answer for answer in answers] for category, answers in self.answers.items()}
        scores = self.calculate_score()
        for category, score in scores.items():
            answers_str[category].append({'Score': score})
        return answers_str
        

def main_page():
    answers = {}

    st.title('Test results calculator')

    form = st.form('form')

    with form:
        # Create columns for the grid layout
        col1, col2, col3, col4 = st.columns(4)
        # Create a container for each column
        with col1:
            for i in range(0, 27):
                question_number = i * 4 + 1
                st.markdown('---')
                answer = st.radio(f'Select an answer for question {question_number}:', ['0', '1', '2', '3'], key=f'radio_{question_number}')
                answers[question_number] = answer

        with col2:
            for i in range(0, 27):
                question_number = i * 4 + 2
                st.markdown('---')
                answer = st.radio(f'Select an answer for question {question_number}:', ['0', '1', '2', '3'], key=f'radio_{question_number}')
                answers[question_number] = answer

        with col3:
            for i in range(0, 27):
                question_number = i * 4 + 3
                st.markdown('---')
                answer = st.radio(f'Select an answer for question {question_number}:', ['0', '1', '2', '3'], key=f'radio_{question_number}')
                answers[question_number] = answer

        with col4:
            for i in range(0, 27):
                question_number = i * 4 + 4
                st.markdown('---')
                answer = st.radio(f'Select an answer for question {question_number}:', ['0', '1', '2', '3'], key=f'radio_{question_number}')
                answers[question_number] = answer

        st.markdown('---')

        if st.form_submit_button('Submit'):
            calculate_score(answers)
    
st.cache_data()
def calculate_score(answers):        
    categories_page_one = ['IN1' , 'HY1' , 'LP1' , 'EF1' , 'AG1' , 'PR1' , 'GI1' , 'AN1' , 'AH1' , 'CD1' , 'OD1' , 'PI1' , 'NI1',
                            'IN2' , 'HY2' , 'LP2' , 'EF2' , 'AG2' , 'PR2' , 'GI2' , 'AN2' , 'AH2' , 'CD2' , 'OD2' , 'PI2' , 'NI2']
    survey = Survey(categories_page_one)

    for question_number , answer in answers.items():
        if question_number in [1,8,18,26,32,42]:
            survey.add_answer(Answer('NI1' , answer , question_number))
        if question_number in [31,33,38]:
            survey.add_answer(Answer('PI1' , answer , question_number))
        if question_number in [14,21,48,57,59]:
            survey.add_answer(Answer('OD1' , answer , question_number))
        if question_number in [6,11,16,27,30,39,41,56,58]:
            survey.add_answer(Answer('CD1' , answer , question_number))
        if question_number in [3,43,45,54,61]:
            survey.add_answer(Answer('AH1' , answer , question_number))
        if question_number in [2,28,35,47]:
            survey.add_answer(Answer('AN1' , answer , question_number))
        if question_number in [19,25,29,34,40,50]:
            survey.add_answer(Answer('GI1' , answer , question_number))
        if question_number in [10,13,24,62]:
            survey.add_answer(Answer('PR1' , answer , question_number))
        if question_number in [16,22,27,30,39,46,48,57,58]:
            survey.add_answer(Answer('AG1' , answer , question_number))
        if question_number in [34,37,63]:
            survey.add_answer(Answer('EF1' , answer , question_number))
        if question_number in [5,7,9,15,36,51,53,60]:
            survey.add_answer(Answer('LP1' , answer , question_number))
        if question_number in [19,43,45,50,52,54,55,61]:
            survey.add_answer(Answer('HY1' , answer , question_number))
        if question_number in [12,23,28,44,47,49]:
            survey.add_answer(Answer('IN1' , answer , question_number))
        if question_number in [74,80,105]:
            survey.add_answer(Answer('PI2' , answer , question_number))
        if question_number in [73,94,102]:
            survey.add_answer(Answer('OD2' , answer , question_number))
        if question_number in [65,76,78,89,91,96]:
            survey.add_answer(Answer('CD2' , answer , question_number))
        if question_number in [69,71,93,98,99,104]:
            survey.add_answer(Answer('AH2' , answer , question_number))
        if question_number in [68,79,84,95,97,101]:
            survey.add_answer(Answer('AN2' , answer , question_number))
        if question_number in [67,81,85,99]:
            survey.add_answer(Answer('GI2' , answer , question_number))
        if question_number in [64,92]:
            survey.add_answer(Answer('PR2' , answer , question_number))
        if question_number in [65,83,86,94,102]:
            survey.add_answer(Answer('AG2' , answer , question_number))
        if question_number in [72,75,79,84,90,97]:
            survey.add_answer(Answer('EF2' , answer , question_number))
        if question_number in [87]:
            survey.add_answer(Answer('LP2' , answer , question_number))
        if question_number in [69,71,93,98,99,104]:
            survey.add_answer(Answer('HY2' , answer , question_number))
        if question_number in [67,77,88,95]:
            survey.add_answer(Answer('IN2' , answer , question_number))
        
    output = survey.output()
    for category , element in output.items():
        st.header(f'Category: {category}')
        st.write("Score for Category: ", element[-1]['Score'])
        try :
            normalized_score = element[-1]['Score'] / ((len(element) - 1) * 3)
        except ZeroDivisionError:
            normalized_score = 0
        st.progress(normalized_score)
        expand = st.expander(f'Answers for category {category}', expanded=False)
        with expand:
            for answer in element[:-1]:
                st.markdown(f'Question Number: {answer.question_number} , Value: {answer.value}')
                
if __name__ == '__main__':
    main_page()
