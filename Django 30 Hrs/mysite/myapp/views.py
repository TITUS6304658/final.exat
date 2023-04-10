from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from myapp.models import project
from django.http import JsonResponse
from myapp.models import project
from myapp.models import title
from django.shortcuts import render, redirect
from .forms import AnswerForm, OwnerForm ,QuestionForm,projectForm,contracForm,DATEQuestionForm
from django.contrib import messages
from myapp.models import Answer
from myapp.models import result
from myapp.models import system_action
from myapp.models import owner
from myapp.models import title
from myapp.models import contract
from itertools import chain
from django.db import connection
from .models import title, project, contract, result
# Create your views here.


    
def my_view(request):
    results =project.objects.all()
    if request.method == 'POST':
        questForm = AnswerForm(request.POST)
        if questForm.is_valid():
            questForm = questForm.save(commit=False)
            questForm.user = request.user
            questForm.save()
            messages.success(request, 'Question has been added.')
            return redirect('edit_data', id=questForm.id)
    
    return render(request, 'myapp/home.html', {'results': results})
    
def my_viewtitle(request, project_id):
    results = title.objects.filter(contract_id__project_id=project_id)
    topic = project.objects.all()
    contracts = contract.objects.all()
    form = DATEQuestionForm() # Added line
    year = request.GET.get('year') # Added line
    quarter_no = request.GET.get('quarter_no') # Added line
    ...

    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM myapp_title INNER JOIN myapp_contract ON myapp_title.contract_id_id = myapp_contract.contracte_id WHERE myapp_contract.project_id_id = %s', [project_id])
        rows = cursor.fetchall()
    return render(request, 'myapp/questio.html', {'results': results, 'contracts': contracts, 'topic': topic,'rows': rows, 'form': form, 'year': year, 'quarter_no': quarter_no})
def save_text(request):
    title_id = request.GET.get('title_id')
    results = title.objects.filter(title_id=title_id)
    topic = project.objects.all()
    contracts = contract.objects.all()

    if request.method == 'POST':
        date_form = DATEQuestionForm(request.POST)
        answer_form = AnswerForm(request.POST)

        if date_form.is_valid() and answer_form.is_valid():
            owner_id = request.GET.get('title_id')
            owner_instance = owner.objects.filter(title_id=owner_id).first()
            if not owner_instance:
                messages.error(request, 'Invalid request. Owner does not exist.')
                return redirect('my_viewtitle')

            result_obj = result.objects.filter(owner_id=owner_instance).first()
            if result_obj:
                messages.error(request, 'Answer has already been submitted for this owner.')
                return redirect('edit_data', id=result_obj.id)

            date_instance = date_form.save(commit=False)  # Save the date_form instance
            answer_instance = answer_form.save(commit=False)

            result_instance = result(year=date_instance.year, quarter_no=date_instance.quarter_no, result=answer_instance.result, problem=answer_instance.problem, solution=answer_instance.solution, owner_id=owner_instance)

            result_instance.save()

            messages.success(request, 'Answer has been added.')
            return redirect('my_view')
        else:
            messages.error(request, 'There was an error with the submitted data. Please check and try again.')

    else:
        owner_id = request.GET.get('title_id')
        if not owner_id:
            messages.error(request, 'Invalid request. Title ID is missing.')
            return redirect('my_viewtitle')
        owner_instance = owner.objects.filter(title_id=owner_id).first()
        if not owner_instance:
            messages.error(request, 'Invalid request. Owner does not exist.')
            return redirect('my_viewtitle')

        result_obj = result.objects.filter(owner_id=owner_instance).first()
        if result_obj:
            answer_form = AnswerForm(instance=result_obj)
            date_form = DATEQuestionForm(initial={'year': result_obj.year, 'quarter_no': result_obj.quarter_no})
        else:
            answer_form = AnswerForm(initial={'owner_id': owner_instance})
            date_form = DATEQuestionForm()

    return render(request, 'myapp/ans_quiz_only.html', {'form': answer_form, 'date_form': date_form, 'results': results, 'topic': topic, 'contracts': contracts})


def get_data(request):
    title_id = request.GET.get('title_id')
    title_obj = get_object_or_404(title, title_id=title_id)
    owner_obj = get_object_or_404(owner, title_id=title_obj)
    result_objs = result.objects.filter(owner_id=owner_obj)
    return render(request, 'ans.html', {'result_objs': result_objs})

def mainmenu (request):

    return render(request,'myapp/questio.html')

def home(request):
    
    return render(request,'myapp/login.html')



def ask_form(request):
    data = title.objects.all()
    AnswerForm.save()
    messages.success(request,'Answer has been added.')
    return render(request, 'myapp/questio.html', {'data': data})

def save_data(request):
    form = QuestionForm()
    if request.method == 'POST':
        quest_form = QuestionForm(request.POST)
        if quest_form.is_valid():
            quest_form = quest_form.save(commit=False)
            quest_form.user = request.user
            quest_form.save()
            messages.success(request, 'Question has been added.')
            return redirect('save_owner')  # Redirect to the 'save_owner' view
    return render(request, 'myapp/ans.html', {'form': form})
def save_owner(request):
    form=OwnerForm
    if request.method=='POST':
        ownerFrom=OwnerForm(request.POST)
        if ownerFrom.is_valid():
           ownerFrom=ownerFrom.save(commit=False)
           ownerFrom.user=request.user
           ownerFrom.save()
           messages.success(request,'ownerFrom has been added.')
           return redirect('my_view')
    return render(request,'myapp/ans.html',{'form':form})
#def edit_data(request, id):
    #data = result.objects.get(id=id)
    #form = AnswerForm(instance=data)
    #if request.method == 'POST':
     #   form = AnswerForm(request.POST, instance=data)
      ##  if form.is_valid():
         #   form.save()
        #    messages.success(request, 'Data has been updated.')
          #  return redirect('my_view')
    #return render(request, 'myapp/edit_data.html', {'form': form})
#def edit_data(request, id):
   # answer = result.objects.get(id=id)
    #if request.method == 'POST':
       # form = AnswerForm(request.POST, instance=answer)
        #if form.is_valid():
            #form.save()
           # return redirect('my_view')
    #else:
        #form = AnswerForm(instance=answer)
    #return render(request, 'edit_data.html', {'form': form})
#def edit_data(request, id):
    #data = result.objects.get(id=id)
   # form = AnswerForm(instance=data)
   # if request.method == 'POST':
    #    form = AnswerForm(request.POST, instance=data)
     #   if form.is_valid():
           # form.save()
          #  messages.success(request, 'Data has been updated.')
          #  return redirect('my_view')
   # return render(request, 'myapp/edit_data.html', {'form': form})

def edit_data(request, id):
    data = result.objects.get(id=id)
    answer_form = AnswerForm(instance=data)
    date_form = DATEQuestionForm(instance=data)

    if request.method == 'POST':
        answer_form = AnswerForm(request.POST, instance=data)
        date_form = DATEQuestionForm(request.POST, instance=data)

        if answer_form.is_valid() and date_form.is_valid():
            date_instance = date_form.save(commit=False)
            answer_instance = answer_form.save(commit=False)

            data.year = date_instance.year
            data.quarter_no = date_instance.quarter_no
            data.result = answer_instance.result
            data.problem = answer_instance.problem
            data.solution = answer_instance.solution

            data.save()

            messages.success(request, 'Data has been updated.')
            return redirect('my_view')

    return render(request, 'myapp/edit_data.html', {'answer_form': answer_form, 'date_form': date_form})


def login(request):
    print("login")
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'my_app/login.html')

def save_data2(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.save()
            return redirect('mainmenu')
    else:
        form = AnswerForm()
    return render(request, 'save_data.html', {'form': form})
def adminmin(request):
    return render(request, 'myapp/adminmin.html')
def projectject(request, id=None):
    if id:
        project_data = project.objects.get(id=id)
        form = projectForm(instance=project_data)
    else:
        form = projectForm()

    if request.method == 'POST':
        if id:
            form = projectForm(request.POST, instance=project_data)
        else:
            form = projectForm(request.POST)

        if form.is_valid():
            project_data = form.save(commit=False)
            project_data.user = request.user
            project_data.save()
            if id:
                messages.success(request, 'Project has been updated.')
                return redirect('edit_project_topic_for_admin', id=project_data.id)
            else:
                messages.success(request, 'Project has been added.')
                return redirect('my_view')

    return render(request, 'myapp/ans.html', {'form': form})

def contracttract(request):
    form=contracForm
    if request.method=='POST':
        contracFormss=contracForm(request.POST)
        if contracFormss.is_valid():
           contracFormss= contracFormss.save(commit=False)
           contracFormss.user=request.user
           contracFormss.save()
           messages.success(request,' projectFrom has been added.')
           return redirect('my_view')
    return render(request,'myapp/ans.html',{'form':form})


# project views.py
  
def showed_project_table(request):
    
    topic = project.objects.all()
   
   
    return render(request,'myapp/showed_project.html', { 'topic': topic})





def edit_project_topic_for_admin(request, id):
    project_data = project.objects.get( project_id=id)
    form = projectForm(instance=project_data)
    if request.method == 'POST':
        form = projectForm(request.POST, instance=project_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been updated.')
            return redirect('my_view')
    return render(request, 'myapp/edit_data_admin.html', {'form': form})

def delete_project(request, id):
    if request.method == 'POST':
        proj = project.objects.get(pk=id)
        proj.delete()
        return redirect('my_view')
    return redirect('showed_project_table')

# contract views.py
def showed_contract_table(request):
    
   con = contract.objects.all()
   
   
   return render(request,'myapp/showed_contract.html', { 'con': con})




def edit_contract_topic_for_admin(request, id):
    contract_data = contract.objects.get( contracte_id=id)
    form = contracForm(instance=contract_data)
    if request.method == 'POST':
        form = contracForm(request.POST, instance=contract_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been updated.')
            return redirect('my_view')
    return render(request, 'myapp/edit_data_admin.html', {'form': form})


def delete_contract(request, id):
    if request.method == 'POST':
       cont = contract.objects.get(pk=id)
       cont.delete()
       return redirect('my_view')
    return redirect('showed_contract_table')




#title
def showed_title_table(request):
    
   tit = title.objects.all()
   pro = project.objects.all()
   co = contract.objects.all()
   return render(request,'myapp/showed_title.html', { 'tit': tit, 'pro': pro,'co': co})

def edit_title_topic_for_admin(request, id):
    title_data = title.objects.get( title_id=id)
    form = QuestionForm(instance=title_data)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=title_data)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been updated.')
            return redirect('my_view')
    return render(request, 'myapp/edit_data_admin.html', {'form': form})



def delete_title(request, id):
    if request.method == 'POST':
        tit = title.objects.get(pk=id)
        tit.delete()
        return redirect('my_view')
    return redirect('showed_title_table')

def main(request):
    return render(request,'myapp/main.html')


def sub_date(request):
    results =project.objects.all()
    form = DATEQuestionForm() # Added line
    return render(request,'myapp/sub_date.html', {'results': results, 'form': form})
def approve_form(request, project_id):
    year = request.GET.get('year')
    quarter_no = request.GET.get('quarter_no')
    results = title.objects.filter(contract_id__project_id=project_id, owner__result__year=year).distinct()
    topic = project.objects.all()
    contracts = contract.objects.all()
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM myapp_title INNER JOIN myapp_contract ON myapp_title.contract_id_id = myapp_contract.contracte_id WHERE myapp_contract.project_id_id = %s', [project_id])
        rows = cursor.fetchall()
    return render(request, 'myapp/appove.html', {'results': results, 'contracts': contracts, 'topic': topic, 'rows': rows})


def home_appove(request):
    results =project.objects.all()
    if request.method == 'POST':
        questForm = AnswerForm(request.POST)
        if questForm.is_valid():
            questForm = questForm.save(commit=False)
            questForm.user = request.user
            questForm.save()
            messages.success(request, 'Question has been added.')
            return redirect('edit_data', id=questForm.id)
    return render(request,'myapp/appove_home.html', {'results': results})


def approve_sub_date(request):
    results = project.objects.all()
    form = DATEQuestionForm()
    return render(request, 'myapp/appove_sub_date.html', {'results': results, 'form': form})


def save_text_appove(request):
    title_id = request.GET.get('title_id')
    results = title.objects.filter(title_id=title_id)
    topic = project.objects.all()
    contracts = contract.objects.all()

    if request.method == 'POST':
        date_form = DATEQuestionForm(request.POST)
        answer_form = AnswerForm(request.POST)

        if date_form.is_valid() and answer_form.is_valid():
            owner_id = request.GET.get('title_id')
            owner_instance = owner.objects.filter(title_id=owner_id).first()
            if not owner_instance:
                messages.error(request, 'Invalid request. Owner does not exist.')
                return redirect('my_viewtitle')

            result_obj = result.objects.filter(owner_id=owner_instance).first()
            if result_obj:
                messages.error(request, 'Answer has already been submitted for this owner.')
                return redirect('edit_data', id=result_obj.id)

            date_instance = date_form.save(commit=False)  # Save the date_form instance
            answer_instance = answer_form.save(commit=False)

            result_instance = result(year=date_instance.year, quarter_no=date_instance.quarter_no, result=answer_instance.result, problem=answer_instance.problem, solution=answer_instance.solution, owner_id=owner_instance)

            result_instance.save()

            messages.success(request, 'Answer has been added.')
            return redirect('my_view')
        else:
            messages.error(request, 'There was an error with the submitted data. Please check and try again.')

    else:
        owner_id = request.GET.get('title_id')
        if not owner_id:
            messages.error(request, 'Invalid request. Title ID is missing.')
            return redirect('my_view')
        owner_instance = owner.objects.filter(title_id=owner_id).first()
        if not owner_instance:
            messages.error(request, 'Invalid request. Owner does not exist.')
            return redirect('my_view')

        result_obj = result.objects.filter(owner_id=owner_instance).first()
        if result_obj:
            answer_form = AnswerForm(instance=result_obj)
            date_form = DATEQuestionForm(initial={'year': result_obj.year, 'quarter_no': result_obj.quarter_no})
        else:
            answer_form = AnswerForm(initial={'owner_id': owner_instance})
            date_form = DATEQuestionForm()

    return render(request, 'myapp/ans_quiz_only_appove.html', {'form': answer_form, 'date_form': date_form, 'results': results, 'topic': topic, 'contracts': contracts})
