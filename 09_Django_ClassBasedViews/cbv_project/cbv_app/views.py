from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

# Create your views here.
## FUNCTION BASED VIEW
def index(request):
    return render(request, "index.html")

## CLASS BASED VIEW (very basic with return of http response)
class CBView(View):
    def get(self,request):
        return HttpResponse("Class Based Views are cool!")

## CLASS BASED VIEW (how you should use it)
class IndexView(TemplateView):
    template_name = "index_cbv.html"

class CBViewContent(TemplateView):
    template_name = "context_cbv.html"
    
    def get_context_data(self, **kwargs):
        # kwargs = keyword arguments
        # args = arguments
        # *args >> single asterisk: will give you all the function parameters as a tuple
        # **kwargs >> double asterisk will give you all keyword arguments except for those corresponding parameter as a dictionary: this allows you to define key value pairs
        # def foo(**kwargs): ...
        # bar(name="one", age=27)
        context = super().get_context_data(**kwargs)
        context["context"] = "BASIC CONTEXT"
        return context
    