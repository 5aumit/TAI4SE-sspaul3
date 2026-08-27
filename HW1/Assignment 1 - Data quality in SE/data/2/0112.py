
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime, timedelta

class DeadlineMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__module__ == 'api.views' and view_func.__name__ == 'ComingsoonData':
            return None
        if view_func.__module__ == 'django.contrib.admin.sites' or request.user.is_superuser:
            return None
        else:
            survey = datetime(2019, 9, 16, 23, 50, 0, 0) #茶會調查結束時間
            teatime = datetime(2019, 9, 17, 18, 30, 0, 0) #茶會開始時間
            if survey - datetime.now() <= timedelta(milliseconds=0): #調查結束
                if teatime - datetime.now() <= timedelta(milliseconds=0): #調查結束+茶會開始
                    if view_func.__module__ == 'enter.views' and view_func.__name__ == 'attend':
                        messages.add_message(request, messages.INFO, '表單已結束提交', extra_tags='teatimestart')
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        return None
                else: #調查結束+茶會未開始
                    if view_func.__module__ == 'joinclub.views' and view_func.__name__ == 'comingsoon':
                        return None
                    else: #從調查表單轉址->表單已結束提交，其他->茶會尚未開始
                        if view_func.__module__ == 'enter.views' and view_func.__name__ == 'attend':
                            messages.add_message(request, messages.INFO, '表單已結束提交', extra_tags='teatimeform')
                        else:
                            messages.add_message(request, messages.INFO, '茶會尚未開始', extra_tags='yetstart')
                        return HttpResponseRedirect(reverse('comingsoon'))
            else: #調查未結束
                if view_func.__module__ == 'joinclub.views' and view_func.__name__ == 'comingsoon':
                    return None
                elif view_func.__module__ == 'enter.views' and view_func.__name__ == 'attend':
                    return None
                else:
                    if view_func.__module__ == 'joinclub.views' and view_func.__name__ == 'index':
                        return HttpResponseRedirect(reverse('comingsoon'))
                    else:
                        messages.add_message(request, messages.INFO, '茶會尚未開始', extra_tags='yetstart')
                        return HttpResponseRedirect(reverse('comingsoon'))




