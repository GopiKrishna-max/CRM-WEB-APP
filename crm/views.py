from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Contact
from .forms import ContactForm

@login_required
def contact_list(request):
    q = request.GET.get('q', '')
    if q:
        contacts = Contact.objects.filter(first_name__icontains=q) | Contact.objects.filter(last_name__icontains=q) | Contact.objects.filter(email__icontains=q)
    else:
        contacts = Contact.objects.all().order_by('-created_at')
    return render(request, 'crm/contact_list.html', {'contacts': contacts, 'q': q})

@login_required
def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'crm/contact_form.html', {'form': form})

@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'crm/contact_form.html', {'form': form, 'contact': contact})

@login_required
def contact_delete(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    return render(request, 'crm/contact_confirm_delete.html', {'contact': contact})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('contact_list')
    else:
        form = UserCreationForm()
    return render(request, 'crm/signup.html', {'form': form})

@login_required
def dashboard(request):
    from .models import Contact, Deal
    contact_count = Contact.objects.count()
    deal_count = Deal.objects.count()
    recent_contacts = Contact.objects.order_by('-created_at')[:5]
    return render(request, 'crm/dashboard.html', {
        'contact_count': contact_count,
        'deal_count': deal_count,
        'recent_contacts': recent_contacts,
    })
