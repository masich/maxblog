from django.shortcuts import render
from .forms import FeedbackForm
from django.shortcuts import redirect


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect('/')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form})
