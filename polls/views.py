from django.http import Http404
from django.shortcuts import get_object_or_404 , render
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Question ,Choice
import json
from rest_framework.response import Response


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
# def detail(request,question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#
#     question = get_object_or_404(Question,pk = question_id)
#     return render(request,'polls/detail.html',{"question":question})
#
# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request,'polls/results.html',{'question':question})
#
dict = {
        "state": 1,
        "amount": "(Z5juk",
        "grade": 2,
        "grade_name": "gYH",
        "expect_return_time":"wegwegwegwe",
        "b_grade_condition": "hM&!nz(",
        "b_grade_amount": "xElCt",
        "total_pay": "D)R9[",
        "available_car_models":[
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "http://img.crcz.com/allimg/201911/21/1574347702830943.jpg",
                "grade": 10
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "http://img.crcz.com/allimg/201911/21/1574347702830943.jpg",
                "grade": 50
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "http://img.crcz.com/allimg/201911/21/1574347702830943.jpg",
                "grade": 40
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "http://img.crcz.com/allimg/201911/21/1574347702830943.jpg",
                "grade": 30
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "http://img.crcz.com/allimg/201911/21/1574347702830943.jpg",
                "grade": 50
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "wGbBA",
                "grade": 40
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "wGbBA",
                "grade": 20
            },
            {
                "name": "g)rBh72",
                "mileage_max": "YyFaH^",
                "seat_count": 5,
                "img_key": "wGbBA",
                "grade": 10
            }
    ],
    "apply_return_time": "sfZE",
    "recheck_time": "qk*T",
    "car_deposit_explain":
        ["1. 用户使用高级车、豪华车时，需缴纳车辆押金才可用车。\n\n",
         "2. 车辆归还后，如未发生事故或对车辆造成损坏等，可申请退还车辆押金。\n\n",
         "3. 车辆押金申请退款后，系统将在5个工作日(申请当日不计)审核，审核通过后的5个工作日(审核当日不计)退还至原支付账户。\n\n4. 在系统退款之前，退款申请可撤销。\n"
         ]
    }
def test_zero(request):

    return HttpResponse(json.dumps(dict),content_type='application/json')


def cancel(request):
    request.method = request.POST

    dict["state"] = 1
    dic = {"detail":'true'}
    return HttpResponse(json.dumps(dic),content_type='application/json')

def applyrefund(request):
    dict["state"] = 2
    dic = {"detail": 'true'}
    return HttpResponse(json.dumps(dic),content_type='application/json')

def vote(request,question_id):
    question = get_object_or_404(Question,pk = question_id)
    print("我在调试")
    print(question)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except:
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':"You didn't selectd a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        print("我在调selected_choice")
        print(selected_choice)
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))




