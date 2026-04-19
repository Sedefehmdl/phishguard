from flask import Flask, render_template, jsonify, request, session
import json, os, random, time
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'phishguard-secret-2024'

# ── Load data ──────────────────────────────────────────────────────────────
BASE = os.path.dirname(__file__)

with open(os.path.join(BASE, 'data', 'emails.json'),  encoding='utf-8') as f: EMAILS     = json.load(f)
with open(os.path.join(BASE, 'data', 'threats.json'), encoding='utf-8') as f: THREATS    = json.load(f)
with open(os.path.join(BASE, 'data', 'quiz.json'),    encoding='utf-8') as f: QUIZ_DATA  = json.load(f)
with open(os.path.join(BASE, 'data', 'stats.json'),   encoding='utf-8') as f: SITE_STATS = json.load(f)

# ── Routes ─────────────────────────────────────────────────────────────────
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simulator')
def simulator():
    return render_template('simulator.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/threats')
def threats():
    return render_template('threats.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# ── API ────────────────────────────────────────────────────────────────────
@app.route('/api/emails')
def api_emails():
    mode = request.args.get('mode', 'mixed')
    count = int(request.args.get('count', 5))
    pool = EMAILS if mode == 'mixed' else [e for e in EMAILS if e['is_phish'] == (mode == 'phish')]
    sample = random.sample(pool, min(count, len(pool)))
    # Strip answer before sending
    safe = [{k:v for k,v in e.items() if k != 'is_phish'} for e in sample]
    session['current_emails'] = {e['id']: e['is_phish'] for e in sample}
    return jsonify(safe)

@app.route('/api/check_email', methods=['POST'])
def check_email():
    data = request.json
    email_id = data.get('id')
    user_answer = data.get('answer')  # True = phish, False = legit
    current = session.get('current_emails', {})
    correct_answer = current.get(str(email_id))
    if correct_answer is None:
        return jsonify({'error': 'Email not found'}), 404
    is_correct = (user_answer == correct_answer)
    email = next((e for e in EMAILS if e['id'] == email_id), None)
    return jsonify({
        'correct': is_correct,
        'answer': correct_answer,
        'explanation': email.get('explanation', ''),
        'red_flags': email.get('red_flags', []),
        'trust_indicators': email.get('trust_indicators', [])
    })

@app.route('/api/quiz')
def api_quiz():
    difficulty = request.args.get('difficulty', 'medium')
    questions = [q for q in QUIZ_DATA if q['difficulty'] == difficulty]
    if not questions:
        questions = QUIZ_DATA
    sample = random.sample(questions, min(10, len(questions)))
    safe = [{k:v for k,v in q.items() if k != 'correct'} for q in sample]
    session['quiz_answers'] = {str(q['id']): q['correct'] for q in sample}
    return jsonify(safe)

@app.route('/api/quiz/answer', methods=['POST'])
def quiz_answer():
    data = request.json
    qid = str(data.get('id'))
    chosen = data.get('answer')
    answers = session.get('quiz_answers', {})
    correct = answers.get(qid)
    question = next((q for q in QUIZ_DATA if str(q['id']) == qid), None)
    return jsonify({
        'correct': chosen == correct,
        'correct_answer': correct,
        'explanation': question.get('explanation', '') if question else ''
    })

@app.route('/api/threats')
def api_threats():
    category = request.args.get('category', None)
    if category:
        filtered = [t for t in THREATS if t['category'] == category]
    else:
        filtered = THREATS
    return jsonify(filtered)

@app.route('/api/stats')
def api_stats():
    return jsonify(SITE_STATS)

@app.route('/api/score', methods=['POST'])
def submit_score():
    data = request.json
    score = data.get('score', 0)
    total = data.get('total', 10)
    pct = round((score / total) * 100)
    badge = get_badge(pct)
    return jsonify({'percentage': pct, 'badge': badge, 'score': score, 'total': total})

def get_badge(pct):
    if pct >= 90: return {'name': 'Elite Analyst', 'icon': '🛡️', 'color': '#00ff9d'}
    if pct >= 75: return {'name': 'Threat Hunter',  'icon': '🔍', 'color': '#00c8ff'}
    if pct >= 60: return {'name': 'Security Aware', 'icon': '⚡', 'color': '#f0c040'}
    if pct >= 40: return {'name': 'Learning Mode',  'icon': '📚', 'color': '#ff9944'}
    return {'name':  'Needs Training',               'icon': '⚠️', 'color': '#ff4444'}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
