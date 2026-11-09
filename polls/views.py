from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, TemplateView, RedirectView, CreateView

from .forms import QuestionForm
from .models import Question, Choice

# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     question_list = Question.objects.all()
#     # output = ", ".join([q.question_text for q in question_list])
#     # return HttpResponse(output)
#     template = loader.get_template("index.html")
#     context = {"question_list": question_list}
#     return HttpResponse(template.render(context, request))

class IndexView(View):
    def get(self, request):
        questions = Question.objects.all()
        template = loader.get_template("index.html")
        context = {"question_list": questions}
        return HttpResponse(template.render(context, request))

    def post(self, request):
        pass

class QuestionList(ListView):
    model = Question

# def detail(request, question_slug):
#     # question = Question.objects.filter(id=question_id)
#     # if not question:
#     #     raise Http404
#     question = get_object_or_404(Question, qslug=question_slug)
#     # template = loader.get_template("details.html")
#     context = {"question": question}
#     # return HttpResponse(template.render(context, request))
#     return render(request, "details.html", context)

class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["choice_list"] = self.object.choice_set.all()
        context["num_choices"] = len(context["choice_list"])
        return context


class HomeView(View):
    name = "Guest"
    def get(self, request):
        return HttpResponse("Welcome " + self.name)

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_dict"] = {"name":"Ali", "surname":"Alavi"}
        context["my_list"] = [10, 20, 30]
        context["my_str"] = "Hey there!"
        return context

class HomeRedirectView(RedirectView):
    permanent = True
    pattern_name = "index"

class VoteView(View):
    def get(self, request, pk):
        try:
            ch = Choice.objects.get(pk=pk)
        except Choice.DoesNotExist:
            raise Http404("Question does not exist")
        ch.votes += 1
        ch.save()
        # return HttpResponse("Thank you for voting")
        return redirect("/polls/success/")

class CreateQuestionView(View):
    def get(self, request):
        template = loader.get_template("create_question.html")
        return HttpResponse(template.render({}, request))

    def post(self, request):
        question_text = request.POST.get("text")
        pub_date = request.POST.get("date")
        question = Question(question_text=question_text, pub_date=pub_date)
        question.save()
        # return HttpResponse("Thank you for submitting a question")
        # return HttpResponseRedirect("/polls/success/")
        return redirect("/polls/success/")

class CreateQuestionView3(View):
    def get(self, request):
        form = QuestionForm()
        return render(request, "create_question3.html", {'form': form})

    def post(self, request):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = Question(question_text=form.cleaned_data["question_text"], pub_date=form.cleaned_data["pub_date"])
            question.save()
            return redirect("/polls/success/")
        else:
            return render(request, "create_question3.html", {'form': form})

class CreateQuestionView2(CreateView):
    model = Question
    fields = ["question_text", "pub_date"]
    success_url = "/polls/success/"

class SuccessView(TemplateView):
    template_name = "success.html"