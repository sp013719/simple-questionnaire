# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from random import shuffle
import csv
import json

_question_amount = 55


def index(request):

    return render(request, 'question/index.html', {})


def get_question(request):
    questions = []

    f = open('Questions for AWS.csv', 'r')

    for row in csv.DictReader(f):
        question = dict()
        question['question'] = replace_line_break(row['Questions'])
        question['choices'] = split_choice(row['Choices'])
        question['ans'] = split_answer(row['Correct Answers'])
        question['note'] = replace_line_break(row['Notes'])

        questions.append(question)

    selected_questions = shuffle_questions(questions)

    return HttpResponse(json.dumps(selected_questions), content_type='application/json')


def shuffle_questions(questions):
    shuffle(questions)

    return questions[0:_question_amount]


def replace_line_break(question_str=''):
    return question_str.replace('\n', ' ')


def split_choice(choices_str=''):
    mapper = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
    choices = []

    for idx, choice_str in enumerate(choices_str.split('\n')):
        choice = dict()
        choice['option'] = mapper.get(idx)
        choice['desc'] = (choice_str[choice_str.find(' '):]).strip()
        choices.append(choice)

    return choices


def split_answer(answers_str=''):
    answers = []

    for ans in answers_str.split(','):
        answers.append(ans.strip().upper())

    return answers