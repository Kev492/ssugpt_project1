from flask import Flask, render_template, request, redirect, url_for
import openai
import os #환경변수

app = Flask(__name__)

# 환경 변수에서 OpenAI API 키 읽어오기
openai.api_key = OPENAI_API_KEY
#os.getenv('OPENAI_API_KEY')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/askgpt', methods=['GET', 'POST'])
def gpt():
    if request.method == 'POST':
        user_input = request.form['user_input']

        # GPT-3 모델을 사용하여 질문에 답변 생성
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        generated_text = response['choices'][0]['message']['content']

        return render_template('chat.html', response=generated_text)

    return render_template('chat.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)