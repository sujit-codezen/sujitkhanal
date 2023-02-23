from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import AssignmentForm
from django.contrib import messages
# Create your views here.

class AssignmentFormView(View):
    form_class = AssignmentForm
    initial = {'key': 'value'}
    template_name = 'assignments/assignment_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(self.request, "Assignment requested successfully. We will contact you soon...")
            return HttpResponseRedirect('/assignment/form/')

        return render(request, self.template_name, {'form': form})