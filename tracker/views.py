from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Evidence

# Create your views here.
def post_list(request):
	evidences = Evidence.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'tracker/post_list.html', {'evidences':evidences})

def evidence_detail(request, pk):
	evidence = get_object_or_404(Evidence, pk=pk)
	return render(request, 'tracker/evidence_detail.html', {'evidence':evidence})
