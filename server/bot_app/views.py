from django.shortcuts import render, redirect
from .forms import QueryForm, SignInForm, SignUpForm
from django.contrib import messages
from llama_cpp import Llama
from .models import *
from django.contrib.sessions.backends.file import SessionStore
from django.utils import timezone
from django.http import JsonResponse

session = SessionStore()

llama = Llama(
    model_path="/Users/zoobaziz/PycharmProjects/text-generation-interface/llama-local-server/llama-2-7b-chat.ggmlv3.q2_K.bin")


# Create your views here.
def index(request):
    if request.method == "POST":
        query = QueryForm(request.POST)
        if query.is_valid():
            query_txt = query.cleaned_data["query"]
            prompt = "Q: " + query_txt + "? A:"
            output = llama(prompt)
            response = output["choices"][0]["text"]
            user: User = User.objects.get(name=request.session["username"])
            queries = UserQueries(question_text=query_txt, query_response=response, user_id=user,
                                  timestamp=timezone.now())
            queries.save()
            query_response = queries.values('question_text', 'query_response')
            messages.success(request, query_response)
    # if request.method == "GET":
    username = request.session["username"]
    user = User.objects.get(name=username)
    data = UserQueries.objects.filter(user_id=user).values('question_text', 'query_response')
    return render(request, 'index.html', {'data': data})
    # return render(request, 'index.html')


def refresh_data(request):
    if request.method == "GET":
        username = request.session["username"]
        user = User.objects.get(name=username)
        data = UserQueries.objects.filter(user_id=user).values('question_text', 'query_response', 'timestamp')
        # print(data)
        return JsonResponse(list(data), safe=False)


def signin(request):
    if request.method == "POST":
        sign_in_details = SignInForm(request.POST)
        if sign_in_details.is_valid():
            username = sign_in_details.cleaned_data["username"]
            password = sign_in_details.cleaned_data["password"]
            user: User = User.objects.get(name=username)
            if password == user.password:
                createsession(request, user, username)
                return redirect(index)
            else:
                messages.warning(request, 'Incorrect Password')
    return render(request, 'login.html')


def createsession(request, user, username):
    session["username"] = username
    session.create()
    request.session = session
    session_details = SessionDetails(user_id=user, session_id=session.session_key,
                                     login_time=timezone.now())
    session_details.save()


def singup(request):
    if request.method == "POST":
        signup_details = SignUpForm(request.POST)
        if signup_details.is_valid():
            username = signup_details.cleaned_data["username"]
            password = signup_details.cleaned_data["password"]
            user = User(name=username, password=password, role='user')
            user.save()
            createsession()
            return redirect(index)

    return render(request, 'signup.html')
