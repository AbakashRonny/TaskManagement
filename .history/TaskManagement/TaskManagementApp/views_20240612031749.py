from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime
from .models import DoListModel
# Create your views here.

def dolist_view(request):
    
    current_date=datetime.now().date()
    current_time=datetime.now().time()
    incomplete_task=DoListModel.objects.filter(Task_status=False)
    complete_task=DoListModel.objects.filter(Task_status=True)
    count_complete_task=DoListModel.objects.filter(Task_status=True).count()
    total_record=DoListModel.objects.all().count()
    progress = (count_complete_task / total_record) * 100

    d={
       'date':current_date,
       'current_time':current_time,
       'incomplete_task':incomplete_task,
       'complete_task':complete_task,
       'total_record':total_record,
       'count_complete_task':count_complete_task,
       'progress':progress
       }
    return render(request,'TaskManagementApp/home.html',d)

def add_task(request):
    Task_data=request.POST['add_task']
    DoListModel.objects.create(Task=Task_data)
    return redirect('dolist')

def task_done(request,id):
    record=get_object_or_404(DoListModel,id=id)
    record.Task_status=True
    record.save()
    return redirect('dolist')

def update_task(request,id):
    record=get_object_or_404(DoListModel,id=id)
    if request.method=='POST':
        updated_task=request.POST['update_task']
        record.Task=updated_task
        record.save()
        return redirect('dolist')

    task_name=record.Task
    d={'task_name':task_name,'record':record}
    return render(request,'TaskManagementApp/update.html',d)

def undo_task(request,id):
    record=get_object_or_404(DoListModel,id=id)
    record.Task_status=False
    record.save()
    return redirect('dolist')

def delete_task(request,id):
    record=get_object_or_404(DoListModel,id=id)
    record.delete()
    return redirect('dolist')

def clear_incomplete(request):
    clear=DoListModel.objects.filter(Task_status=False)
    clear.delete()
    return redirect('dolist')

def clear_complete(request):
    clear=DoListModel.objects.filter(Task_status=True)
    clear.delete()
    return redirect('dolist')