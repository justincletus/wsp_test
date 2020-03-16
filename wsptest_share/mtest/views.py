from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, TestForm
from .models import Questions, Test, SubmitedAnswer
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.apps import apps
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.response import Response
from django.contrib import messages
from django.template.loader import render_to_string

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = Questions.objects.all()
        serialzer = QuestionSerializer(queryset, many=True)
        return Response(serialzer.data)
    

def index(request, *args, **kwargs):    
    tests = testFn(request)
    
    return render(request, 'index.html', 
                  {
                      'tests': tests
                  })

def testFn(request, *args, **kwargs):
    try:
        tests = Test.objects.all()
    except:
        return Http404('No test found')
    
    return tests

@login_required
def testList(request, *args, **kwargs):
    try:
        tests = testFn(request)
    except Test.DoesNoExist:
        return redirect(request, 'home')
    user = request.user
    
    if user.is_staff:
        return render(request, 'testlist.html', {
            'tests': tests
        })
    
    return render(request, 'test.html', {
        'tests': tests
    })


@login_required
def testQuestions(request, pk):
    questions = Questions.objects.filter(title=pk).values('id', 'question','a1', 'a2','a3','a4','answer','marks')
    number_of_questions = Questions.objects.filter(title=pk).count()
    
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    
    if user.is_staff:
        try:
            test = Test.objects.get(pk=pk)
            form = QuestionForm()
            if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                    form.save()
                
        except Test.DoesNotExist:
            return Http404('No test found')
        return render(request, 'testquestion.html', {
            'test': test,
            'questions': questions,
            'form': form
            
        })
    
    submittedAns1 = SubmitedAnswer.objects.all()   
    
    question_id = 0
    
    for x in questions:
        question_id = x['id']
        break
    
    try: 
        userAns = SubmitedAnswer.objects.get(user=current_user)
        return redirect('submitted_test')
    except SubmitedAnswer.DoesNotExist:
        pass

    # try:
    #     userAns = SubmitedAnswer.objects.filter(user=request.user).values('id','user', 'answer', 'marks')
    #     print(userAns)
    #     test_name = Test.objects.get(pk=pk)
        
    #     return redirect('submitted_test')
        
    # except SubmitedAnswer.DoesNotExist:
    #     info = messages.add_message(request, messages.INFO, 'No submitted record')  
    
    
    Profile = apps.get_model('app_registration', 'Profile')
    profile = Profile.objects.filter(user=user).get()
    
    mail_subject = 'Skill Test Score'
    to_mail = request.user.email    
        
    if request.method == 'POST':
        data = request.POST.copy()
        total_marks = 0
        avarage = 0.0
        data1 = []        
        for x,y in data.items():
            data1.append(y)
        
        data1 = data1[2:]
        data3 = []
        
        for x in questions:
            for j in data1:
                if j == x['answer']:
                    total_marks += int(x['marks'])  
        try:
            avarage = (total_marks/number_of_questions) * 100
            if avarage > float(40):
                message = f"""
                You have successfully pass the test. your test score is {avarage}
                """              
                # print(avarage)
                email = EmailMessage(mail_subject, message, to=[to_mail])
                try:
                    email.send()                
                except:
                    print('Email sending failed')
            else:
                message = f"""
                You need to improve your skill. Your test score is {avarage}
                """                
                
                email = EmailMessage(mail_subject, message, to=[to_mail])
                try:
                    email.send()
                except:
                    print('Email sending failed')
        except:
            print("Number should not divide by zero.")
            
        # for i in range(len(data1)):
        #     submittedAns = SubmitedAnswer()
        #     submittedAns.user = request.user
        #     submittedAns.question = ques_id
        #     submittedAns.answer = form_ans
        #     submittedAns.marks = avarage
        #     submittedAns.status = True
        #     submittedAns.save()
        
        
        
        
        return redirect('test_list')
            
    return render(request, 'test.html', {
        'questions': questions
    })
    
@login_required
def testCategory(request, *args, **kwargs):
    
    form = TestForm()
    
    test_category = Test.objects.all()
    
    if request.method == 'POST':
        data = request.POST.copy()
        form.user = request.user
        if form.is_valid():            
            form.save()
            return HttpResponse('Test category created')
        else:
            print("Form validation failed")            
            
    return render(request, 'testcategory.html', {
        'form': form
    })

@login_required
def submittedTest(request, *args, **kwagrs):
    
    submittedAns = SubmitedAnswer.objects.all()
        
    user = request.user
    if not user.is_staff:        
        try:
            subAns = SubmitedAnswer.objects.filter(user=user).values('id','user', 'answer', 'marks')
            sub_mark = 0
            for x in subAns:
                sub_mark = x['marks']
                
            # print(subAns)
            # ques = Questions.objects.get(question=subAns.question)
            return render(request, 'submitted_test.html', {
                'userAnswers': subAns
            })
        except SubmitedAnswer.DoesNotExist:
            info = messages.add_message(request, messages.INFO, "You have not submitted Test yet!")
            # return render(request, 'test.html', {
            #     'messages': info
            # })
            return redirect('test_list')
        
    return render(request, 'submitted_test.html', {
        'submittedAns': submittedAns
    })   
    
    