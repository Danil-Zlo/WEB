from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
ANSWERS = [
    {
        'id': i,
        'title': f'Answer {i}',
        'content': f'Many-many and more information'
    } for i in range(1, 12)
]

QUESTIONS = [
    {
        'title': f'Question {i}',
        'id': i,
        'content': f'Long lorem ipsum {i}',
        # 'answers': ANSWERS[i],
    } for i in range(30)
]

def paginate(objects, request, per_page=5):
    try:
        page = request.GET.get('page', 1)
        paginator = Paginator(objects, per_page)    
        page_obj = paginator.get_page(page)
        return page_obj
    except (IndexError, ValueError):
        return render(request, template_name='404.html')


# request - HTTP запрос
def index(request):
    return render(request, template_name='index.html', context={'questions': paginate(QUESTIONS, request)})


def hot(request):
    return render(request, template_name='hot.html', context={'questions': paginate(QUESTIONS, request)})


def question(request, question_id):
    try:
        item = QUESTIONS[question_id]
        return render(request, template_name='question.html', context={'question': item, 'answers': paginate(ANSWERS, request)})
    except IndexError:
        return render(request, template_name='404.html')


def ask(request):
    return render(request, template_name='ask.html')


def login(request):
    return render(request, template_name='login.html')


def register(request):
    return render(request, template_name='register.html')


def pageNotFound(request):
    return render(request, template_name='404.html')