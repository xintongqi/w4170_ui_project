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
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '2',
        'prev': None
    },
    '2': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '3',
        'prev': '1'
    },
    '3': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '4',
        'prev': '2'
    },
    '4': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '5',
        'prev': '3'
    },
    '5': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '6',
        'prev': '4'
    },
    '6': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '7',
        'prev': '5'
    },
    '7': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '8',
        'prev': '6'
    },
    '8': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '9',
        'prev': '7'
    },
    '9': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '10',
        'prev': '8'
    },
    '10': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '11',
        'prev': '9'
    },
    '11': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '12',
        'prev': '10'
    },
    '12': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': '13',
        'prev': '11'
    },
    '13': {
        'name': 'mountain fold',
        'diagram': '',
        'video': '',
        'next': None,
        'prev': '12'
    }
}
quiz_score = 0
# data related to user choices
user_data = {
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
    prob = quiz_data.get(prob_id)
    if prob:
        # todo: render the quiz template with proper url
        return render_template('quiz.html', step=prob_id, prob = prob)
    else:
        return "Oops! We don't have a quiz problem with this index!!"

@app.route('/quiz/result')
def quiz_result():
    # todo: render the quiz template with proper url
    return render_template('quiz_result.html', quiz_score = quiz_score)

@app.route('/search', methods=['POST'])
def search():
    search_text = request.form.get('search', '').strip()
    search_results = [learn_data[key] for key in learn_data if search_text.lower() in learn_data[key]['name'].lower()]
    if search_results:
        return render_template('search_results.html', search_text=search_text, search_results=search_results, no_results=False)

    return render_template('search_results.html', search_text=search_text, search_results=[], no_results=True)

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