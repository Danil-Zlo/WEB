from django.shortcuts import render
from django.core.paginator import Paginator


# Create your views here.
ANSWERS = [
    {
        'id': i,
        'title': f'Answer {i}',
        'content': f'Many-many and more information'
    } for i in range(1, 30)
]

QUESTIONS = [
    {
        'id': i,
        'title': f'Question {i}',
        'content': f'Long lorem ipsum {i}',
        # 'answers': ANSWERS[i],
    } for i in range(30)
]

def paginate(objects, page, per_page=5):
    
    # try :
    #     if not (isinstance(page, int)):
    #         page = 1
    # except TypeError:
    #     pass

    paginator = Paginator(objects, per_page)

    if int(page) > paginator.num_pages:
        page = paginator.page(page)
    elif int(page) < 1:
        page = 1

    page_obj = paginator.get_page(page)
    return page_obj

# request - HTTP запрос
def index(request):
    page = int(request.GET.get('page', 1))
    return render(request, template_name='index.html', context={'questions': paginate(QUESTIONS, page)})


def question(request, question_id):
    item = QUESTIONS[question_id]
    page = int(request.GET.get('page', 1))
    return render(request, template_name='question.html', context={'question': item, 'answers': paginate(ANSWERS, page)})


def ask(request):
    return render(request, template_name='ask.html')


def login(request):
    return render(request, template_name='login.html')


def register(request):
    return render(request, template_name='register.html')