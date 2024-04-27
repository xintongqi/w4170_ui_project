from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)

"""
https://i.postimg.cc/qRR3NkMQ/UI-design-q1-2.png
https://i.postimg.cc/TPQb2yGp/UI-design-q1-5-choice-A.png
https://i.postimg.cc/JhRJWNff/UI-design-q1-5-choice-B.png
https://i.postimg.cc/ZRMy31Wm/UI-design-q3-4.png
https://i.postimg.cc/kgQ8Z1pN/UI-design-q5.png
https://i.postimg.cc/htYLVz66/UI-design-boat1.png
https://i.postimg.cc/Hsp9mCbZ/UI-design-boat2.png
https://i.postimg.cc/8zcdFBKL/UI-design-boat3.png
https://i.postimg.cc/DfQPRz44/UI-design-boat4.png
https://i.postimg.cc/xTtyTFR0/UI-design-boat5.png
https://i.postimg.cc/gjKyhMbH/UI-design-boat6.png
https://i.postimg.cc/SsCfSSZ5/UI-design-boat7.png
https://i.postimg.cc/fysjkGpb/UI-design-boat8.png
https://i.postimg.cc/zf9kYbkK/UI-design-boat9.png
"""
boat_links= [
    "https://i.postimg.cc/htYLVz66/UI-design-boat1.png",
    "https://i.postimg.cc/Hsp9mCbZ/UI-design-boat2.png",
    "https://i.postimg.cc/8zcdFBKL/UI-design-boat3.png",
    "https://i.postimg.cc/DfQPRz44/UI-design-boat4.png",
    "https://i.postimg.cc/xTtyTFR0/UI-design-boat5.png",
    "https://i.postimg.cc/gjKyhMbH/UI-design-boat6.png",
    "https://i.postimg.cc/SsCfSSZ5/UI-design-boat7.png",
    "https://i.postimg.cc/fysjkGpb/UI-design-boat8.png",
    ]
boat_choice_links = [
    {"Y": "https://www.youtube.com/embed/sdcc3z7jKyU?si=5eHejcYI3DUY7Bfs", "N":"https://www.youtube.com/embed/QzkoZMnnj5c?si=sA2ovIjjVh8hXgOm"},
    {"Y": "https://www.youtube.com/embed/Vvb93Wr85Aw?si=FtQo3_vfgyIIH_BS", "N":"https://www.youtube.com/embed/kpb2I2KKzfI?si=cRAEubMzzCZR2UPJ"},
    {"Y": "https://www.youtube.com/embed/sa0FX3Cn1XE?si=14ebWdrqC_87YjYh", "N":"https://www.youtube.com/embed/aJ1jknkz-sQ?si=Lp_zX6yfRmHreo3-"},
    {"Y": "https://www.youtube.com/embed/JxAKcGBAYCo?si=S2HZuCXzm-tAJd4Y", "N":"https://www.youtube.com/embed/ZIgVge7Lad8?si=EjEG0pa0YPDrCITP"},
    {"Y": "https://www.youtube.com/embed/dk36dIN78yk?si=Pe_FS01TW0kKXfEu", "N":"https://www.youtube.com/embed/DsG_VNDEdQQ?si=PFt0jpQZdpF2WSGF"},
    {"Y": "https://www.youtube.com/embed/RzhbDiBuVG8?si=eIyJbx1fH0fWSt24", "N":"https://www.youtube.com/embed/R9FidAAmzD4?si=u_cnjdffAP6FtqJJ"},
    {"Y": "https://www.youtube.com/embed/sJxCA6ecqXk?si=ytCoXuMevCfLjWao", "N":"https://www.youtube.com/embed/XD3pvVKBL3c?si=OneXZxdp96f_psO7"},
    {"Y": "https://www.youtube.com/embed/cOVL-k57ch4?si=BV8VkNSbhUx1NFyN", "N":"https://www.youtube.com/embed/tORuAaF1X5k?si=Wd-fLBal08W2Qh3n"}
    ]
# data related to the learning module
learn_data = {
    '1': {
        'id': '1',
        'name': 'Mountain Fold',
        'diagram': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d2/Orisymbol_mountain_fold.svg/1000px-Orisymbol_mountain_fold.svg.png',
        'video': 'https://www.youtube.com/embed/2jmhd7BPHx0?si=mkOOLQx60T1608_j&autoplay=1&loop=1&playlist=2jmhd7BPHx0',
        'next': '2',
        'prev': None,
        'description': 'Fold the paper away from you and create a mountain ridge.',
        'notion': [ 'empty arrow', 'two dots and a slash']
    },
    '2': {
        'id': '2',
        'name': 'Valley Fold',
        'diagram': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Origami_symbol_valley_fold.svg/1000px-Origami_symbol_valley_fold.svg.png',
        'video': 'https://www.youtube.com/embed/j5OWOyz5VLk?si=Zj7grpqVRZq-Fxco&autoplay=1&loop=1&playlist=j5OWOyz5VLk',
        'next': '3',
        'prev': '1',
        'description': 'Fold the paper towards you and create a valley.' ,
        'notion': [ 'solid arrow', 'only shashes, not dots']
    },
    '3': {
        'id': '3',
        'name': 'Pull',
        'diagram': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Orisymbol_pull.svg/1000px-Orisymbol_pull.svg.png',
        'video': 'https://www.youtube.com/embed/ZtD1X2gZmSs?si=3zhMJR4yz9bYMLEz&autoplay=1&loop=1&playlist=ZtD1X2gZmSs',
        'next': '4',
        'prev': '2',
        'description': 'Pull the paper in the direction of the arrow.',
        'notion': ['a fat, empty arrow', 'no arrow tail', 'no dots or slashes']
    },
    '4': {
        'id': '4',
        'name': 'Open',
        'diagram': 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/Orisymbol_open.svg/1000px-Orisymbol_open.svg.png',
        'video': 'https://www.youtube.com/embed/pxjdk0Jbn1E?si=9OnCdo6-DpIBBhM8&autoplay=1&loop=1&playlist=pxjdk0Jbn1E',
        'next': 'transition',
        'prev': '3',
        'description': 'Open the paper in the direction of the arrow.',
        'notion': ['a fat, emtpy arrow', 'a curved tail', 'no dots or slashes']
    },
    
}

# data related to the quiz module
quiz_data = {
    '1': {
        'question': 'What fold is this?',
        'diagram': 'https://i.postimg.cc/qRR3NkMQ/UI-design-q1-2.png',
        'video': '',
        'A': 'Mountain Fold',
        'B':'Valley Fold',
        'answer': 'A',
        'next': '2',
        'prev': None
    },
    '2': {
        'question': 'What should it look like after the fold?',
        'diagram': 'https://i.postimg.cc/qRR3NkMQ/UI-design-q1-2.png',
        'video': '',
        'A': '<img class = "quiz-choice-diagram" src="https://i.postimg.cc/TPQb2yGp/UI-design-q1-5-choice-A.png" alt="choice A">',
        'B':'<img class = "quiz-choice-diagram" src="https://i.postimg.cc/JhRJWNff/UI-design-q1-5-choice-B.png" alt="choice B">',
        'answer': 'B',
        'next': '3',
        'prev': '1'
    },
    '3': {
        'question': 'What fold is this?',
        'diagram': 'https://i.postimg.cc/ZRMy31Wm/UI-design-q3-4.png',
        'video': '',
        'A': 'Mountain Fold',
        'B':'Valley Fold',
        'answer': 'B',
        'next': '4',
        'prev': '2'
    },
    '4': {
        'question': 'What should it look like after the fold?',
        'diagram': 'https://i.postimg.cc/ZRMy31Wm/UI-design-q3-4.png',
        'video': '',
        'A': '<img class = "quiz-choice-diagram" src="https://i.postimg.cc/TPQb2yGp/UI-design-q1-5-choice-A.png" alt="choice A">',
        'B':'<img class = "quiz-choice-diagram" src="https://i.postimg.cc/JhRJWNff/UI-design-q1-5-choice-B.png" alt="choice B">',
        'answer': 'A',
        'next': '5',
        'prev': '3'
    },
    '5': {
        'question': 'What should it look like after the fold?',
        'diagram': 'https://i.postimg.cc/kgQ8Z1pN/UI-design-q5.png',
        'video': '',
        'A': '<img class = "quiz-choice-diagram" src="https://i.postimg.cc/TPQb2yGp/UI-design-q1-5-choice-A.png" alt="choice A">',
        'B':'<img class = "quiz-choice-diagram rotated" src="https://i.postimg.cc/TPQb2yGp/UI-design-q1-5-choice-A.png" alt="choice B">',
        'answer': 'B',
        'next': '6',
        'prev': '4'
    },
    '6': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[0],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[0]['N']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[0]['Y']+'frameborder="0"></iframe>',
        'answer': 'B',
        'next': '7',
        'prev': '5'
    },
    '7': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[1],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[1]['N']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[1]['Y']+'frameborder="0"></iframe>',
        'answer': 'B',
        'next': '8',
        'prev': '6'
    },
    '8': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[2],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[2]['Y']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[2]['N']+'frameborder="0"></iframe>',
        'answer': 'A',
        'next': '9',
        'prev': '7'
    },
    '9': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[3],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[3]['N']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[3]['Y']+'frameborder="0"></iframe>',
        'answer': 'B',
        'next': '10',
        'prev': '8'
    },
    '10': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[4],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[4]['Y']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[4]['N']+'frameborder="0"></iframe>',
        'answer': 'A',
        'next': '11',
        'prev': '9'
    },
    '11': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[5],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[5]['Y']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[5]['N']+'frameborder="0"></iframe>',
        'answer': 'A',
        'next': '12',
        'prev': '10'
    },
    '12': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[6],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[6]['Y']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[6]['N']+'frameborder="0"></iframe>',
        'answer': 'A',
        'next': '13',
        'prev': '11'
    },
    '13': {
        'question': 'What should it look like after the fold?',
        'diagram': boat_links[7],
        'video': '',
        'A': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[7]['N']+'frameborder="0"></iframe>',
        'B': '<iframe class="quiz-choice-diagram" src='+boat_choice_links[7]['Y']+'frameborder="0"></iframe>',
        'answer': 'B',
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
    return render_template('index.html', learn_data=learn_data)

@app.route('/learn_step/<step_id>')
def view_step(step_id):
    step = learn_data.get(step_id)
    if step:
        return render_template('learn_step.html', step=step, steps = learn_data)
    else:
        return "Oops! We don't have a step with this index!!"

@app.route('/transition')
def transition():
    return render_template('transition.html')
    
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
        return render_template('quiz.html', step=prob_id, prob = prob)
    else:
        return "Oops! We don't have a quiz problem with this index!!"

@app.route('/quiz/result')
def quiz_result():
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

if __name__ == '__main__':
    app.run(debug=True)