from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)

# data related to the learning module
learn_data = {
    '1': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '2',
        'prev': None
    },
    '2': {
        'name': 'valley fold',
        'diagram': '',
        'video': '',
        'next': '3',
        'prev': '1'
    },
    '3': {
        'name': 'reverse fold',
        'diagram': '',
        'video': '',
        'next': '4',
        'prev': '2'
    }
}

# data related to the quiz module
quiz_data = {
    '1': {
        'question': 'What fold is this?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '2',
        'prev': None
    },
    '2': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '3',
        'prev': '1'
    },
    '3': {
        'question': 'What fold is this?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '4',
        'prev': '2'
    },
    '4': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '5',
        'prev': '3'
    },
    '5': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '6',
        'prev': '4'
    },
    '6': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '7',
        'prev': '5'
    },
    '7': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '8',
        'prev': '6'
    },
    '8': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '9',
        'prev': '7'
    },
    '9': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '10',
        'prev': '8'
    },
    '10': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '11',
        'prev': '9'
    },
    '11': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '12',
        'prev': '10'
    },
    '12': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': '13',
        'prev': '11'
    },
    '13': {
        'question': 'What should it look like after the fold?',
        'diagram': '',
        'video': '',
        'answer': 'A',
        'next': None,
        'prev': '12'
    }
}
current_quiz_score = 0
num_quiz_question_done = 0
# data related to user choices
user_data = {
    '1':'',
    '2':'',
    '3':'',
    '4':'',
    '5':'',
    '6':'',
    '7':'',
    '8':'',
    '9':'',
    '10':'',
    '11':'',
    '12':'',
    '13':'',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn_step/<step_id>')
def view_step(step_id):
    step = learn_data.get(step_id)
    if step:
        return render_template('learn_step.html', step=step, steps = learn_data)
    else:
        return "Oops! We don't have a step with this index!!"
    
@app.route('/quiz/<prob_id>')
def take_quiz(prob_id):
    global current_quiz_score
    global user_data
    if prob_id == '1':
        current_quiz_score = 0
        for key in user_data:
            user_data[key] = ''
    prob = quiz_data.get(prob_id)
    if prob:
        # todo: render the quiz template with proper url
        return render_template('quiz.html', step=prob_id, prob = prob)
    else:
        return "Oops! We don't have a quiz problem with this index!!"

@app.route('/quiz/result')
def quiz_result():
    # todo: render the quiz template with proper url
    return render_template('quiz_result.html', quiz_score = current_quiz_score)

@app.route('/search', methods=['POST'])
def search():
    search_text = request.form.get('search', '').strip()
    search_results = [learn_data[key] for key in learn_data if search_text.lower() in learn_data[key]['name'].lower()]
    if search_results:
        return render_template('search_results.html', search_text=search_text, search_results=search_results, no_results=False)

    return render_template('search_results.html', search_text=search_text, search_results=[], no_results=True)

@app.route('/quiz/incre_score', methods=['POST'])
def incre_score():
    global current_quiz_score
    current_quiz_score += 1
    return jsonify(current_quiz_score = current_quiz_score)

@app.route('/quiz/add_choice', methods=['POST'])
def add_choice():
    global user_data
    json_data = request.get_json()
    id = json_data["id"]
    choice = json_data["choice"]
    user_data[id] = choice
    return jsonify(user_data = user_data)
# # todo: record user choices; may need to change name of the route
# @app.route('/add', methods=['GET', 'POST'])
# def add_user_data():
#     if request.method == 'POST':
#         # todo: fill this up
#         added_user_response = {
            
#         }

#         user_data[str(len(app_data) + 1)] = add_user_data
#         # todo: change this
#         return 200
#     return render_template('add.html', recipes = app_data)

if __name__ == '__main__':
    app.run(debug=True)