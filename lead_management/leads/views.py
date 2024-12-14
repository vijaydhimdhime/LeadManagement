from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead
from .forms import LeadForm
from django.http import JsonResponse

def lead_dashboard(request):
    #return render(request, 'leads/dashboard.html', )
    return render(request, 'leads/dashboard.html', )

def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads/lead_list.html', {'leads': leads})

def lead_create(request):
    form = LeadForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lead_list')
    return render(request, 'leads/lead_form.html', {'form': form})

def lead_update(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    form = LeadForm(request.POST or None, instance=lead)
    if form.is_valid():
        form.save()
        return redirect('lead_list')
    return render(request, 'leads/lead_form.html', {'form': form})

def lead_delete(request, pk):
    lead = get_object_or_404(Lead, pk=pk)
    if request.method == 'POST':
        lead.delete()
        return redirect('lead_list')
    return render(request, 'leads/lead_confirm_delete.html', {'lead': lead})

def export_leads_json(request):
    # Fetch all leads
    leads = Lead.objects.all().values('first_name', 'last_name', 'email', 'phone')
    data = list(leads)  # Convert queryset to list of dictionaries
    return JsonResponse(data, safe=False)  # Return JSON response