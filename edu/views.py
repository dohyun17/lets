from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from.models import Feed
# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        
        feeds = Feed.objects.all().order_by("id")
        return render(request, self.template_name,{'feed_list' : feeds})
    
class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        age = request.POST.get('age','0')
        print(f'age:{age}')
        if age=='':
            age=0
        else:
            age = int(age)

        pwd= request.POST.get('pwd', '')
        print(f'비밀전호:{pwd}')

        tel = request.POST.get('phone', '')
        print(f'전화번호:{tel}')

        param = request.POST.get("content")
        print("전달받은 내용:" + param)
        feed = Feed(content=param)
        feed.save()
        return redirect('edu:tag_study')
           