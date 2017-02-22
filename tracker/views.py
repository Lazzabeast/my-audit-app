from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Evidence
from .forms import EvidenceForm

# Create your views here.
def post_list(request):
	evidences = Evidence.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'tracker/post_list.html', {'evidences':evidences})

def evidence_detail(request, pk):
	evidence = get_object_or_404(Evidence, pk=pk)
	return render(request, 'tracker/evidence_detail.html', {'evidence':evidence})

def evidence_new(request):
	if request.method == "POST":
		form = EvidenceForm(request.POST)
		
		if form.is_valid():
			post = form.save(commit=False)
			post.requestor = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('evidence_detail', pk=post.pk)		
	else:
		form = EvidenceForm()
	return render(request, 'tracker/evidence_edit.html', {'form': form})
	
def evidence_edit(request, pk):
    evidence = get_object_or_404(Evidence, pk=pk)
    if request.method == "POST":
        form = EvidenceForm(request.POST, instance=evidence)
        if form.is_valid():
            evidence = form.save(commit=False)
            evidence.author = request.user
            evidence.created_date = timezone.now()
            evidence.save()
            return redirect('evidence_detail', pk=evidence.pk)
    else:
        form = EvidenceForm(instance=evidence)
    return render(request, 'tracker/evidence_edit.html', {'form': form})