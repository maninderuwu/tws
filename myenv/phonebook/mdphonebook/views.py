from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

# Create your views here.

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html',{'contacts':contacts})

def add_contacts(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm()
    return render(request, 'addcontact.html',{'form':form})


def edit_contact(request, pk):
    contacts = get_object_or_404(Contact, pk=pk)
    if request.method =='POST':
        form = ContactForm(request.POST, instance=contacts)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contacts)
    return render(request, 'editcontact.html',{'form':form})

def delete_contact(request, pk):
    contacts = get_object_or_404(Contact, pk=pk)
    if request.method =='POST':
        contacts.delete()
        return redirect('index')
    return render(request, 'deletecontact.html',{'contacts':contacts})

