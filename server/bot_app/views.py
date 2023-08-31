from django.shortcuts import render
from .forms import QueryForm
from django.contrib import messages
from llama_cpp import Llama


# Create your views here.
def index(request):
    if request.method == "POST":
        query = QueryForm(request.POST)
        if query.is_valid():
            queryTxt = query.cleaned_data["query"]
            llama = Llama(model_path="/Users/zoobaziz/PycharmProjects/text-generation-interface/llama-local-server/llama-2-7b-chat.ggmlv3.q2_K.bin")
            prompt = "Q: "+queryTxt+"? A:"
            output = llama(prompt)
            messages.success(request, output["choices"][0]["text"])
    return render(request, 'index.html')

