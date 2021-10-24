from django.shortcuts import render, get_object_or_404, redirect
#from django.utils import timezone
from pytz import utc, timezone

from datetime import timedelta, datetime
from .models import Publication, Patent, Notice, News,RelatedProject, AutoNews, CompanyList

from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger


def index(request):
    return render(request, 'web/index.html')

#ABOUT##########################################################################################################################

def GreetingPage(request):
    return render(request, 'web/greetingTemp.html')

def MemberImageList(request):
    return render(request, 'web/memberTemp.html')

def LabTextList(request):
    return render(request, 'web/lab.html')

def ProjectPage(request):
    return render(request, 'web/introduction.html')

#NEWS&INFO##########################################################################################################################
def NoticeTextList(request):
    return render(request, 'web/notice.html')

def Newsletter(request):
    return render(request, 'web/news.html')

def Newsletter21(request):
    return render(request, 'web/news21.html')
#RESEARCH##########################################################################################################################

class AutomaticNews(ListView):
    model = CompanyList
    template_name = 'web/automaticnews.html'
    paginate_by = 5
    queryset = AutoNews.objects.order_by('-id')

    def get(self, request):
        context = {'company_list' : CompanyList.objects.all()}
        return render(request, self.template_name, context)

class AutomaticNewsList(ListView):
    model = AutoNews
    template_name = 'web/automaticnews_list.html'
    queryset = AutoNews.objects.order_by('-id')
    paginate_by = 10

    def get(self, request, company):
        filters = list(filter(lambda x: x.company == company, AutoNews.objects.all()))
        filters.reverse()
        paginator = Paginator(filters, self.paginate_by)
        page = request.GET.get('page')
        #if your django version 2.0.4 just get_page
        if page == None:
            page = 1
        filter_list = paginator.page(page)

        # counting page number
        if filter_list.has_next() == False :
            acc_num = 0
        else :
            mod = paginator.count % self.paginate_by
            acc_num = (paginator.num_pages-int(page)-1) * self.paginate_by + mod

        context = {'filter_list': filter_list, 'acc_num' : acc_num}
        return render(request, self.template_name, context)

class AutomaticNewsDetail(DetailView):
    model = AutoNews
    template_name = 'web/automaticnews_detail.html'

    def get(self, request, pk):
        autonews = AutoNews.objects.get(pk = pk)
        my_company = autonews.company
        my_datetime = autonews.datetime
        #KST = timezone('Asia/Seoul')
        KST = timezone('UTC')
        
        predict_date = my_datetime.date()+timedelta(days=28)
        today = KST.localize(datetime.now())
        is_future = predict_date > today.date()
        predict = AutoNews.objects.filter(company=my_company, datetime__icontains=predict_date).values('id')
        predict_id = predict.values('id')

        predict_pk = 0
        if(predict_id.exists()) :
            predict_pk = predict_id[0]['id']

        only_2018 = ['amorepacific','hyundaimobis','lghousehold','samsungcnt','samsungsds']
        last_2018_date = datetime(2018, 12, 31, 23, 59, 59, 0).replace(tzinfo=KST)

        is_only_2018 = False
        if my_company in only_2018 and my_datetime.date() > last_2018_date.date() :
            is_only_2018 = True

        # print("predict_pk", predict_pk)
        # print("is_only_2018", is_only_2018)
        context = {'autonews':autonews, 'predict_pk':predict_pk, 'is_future':is_future, 'is_only_2018':is_only_2018}
        return render(request, self.template_name, context)

def stock(request):
    return render(request, 'web/stockTemp.html')

def financialIndex(request):
    return render(request, 'web/financial_index.html')

class PublicationTextList(ListView):
    model = Publication
    template_name = 'web/publication.html'
    queryset = model.objects.order_by('-id')
    paginate_by = 10 #how much show your list

    def get(self, request):
        obj = list(Publication.objects.all())
        obj.reverse()

        paginator = Paginator(obj, self.paginate_by)
        page = request.GET.get('page') #if your django version 2.0.4 just use get_page
        if page == None:
            page = 1
        object_list = paginator.page(page)

        if object_list.has_next() == False :
            acc_num = 0
        else :
            mod = paginator.count % self.paginate_by
            acc_num = (paginator.num_pages-int(page)-1) * self.paginate_by + mod

        context = {'object_list': object_list, 'acc_num' : acc_num}
        return render(request, self.template_name, context)

class JournalTextList(ListView):
    model = Publication
    template_name = 'web/publication.html'
    queryset = model.objects.order_by('-id')
    paginate_by = 10 #how much show your list

    def get(self, request):
        obj = list(Publication.objects.all())
        obj.reverse()

        paginator = Paginator(obj, self.paginate_by)
        page = request.GET.get('page') #if your django version 2.0.4 just use get_page
        if page == None:
            page = 1
        object_list = paginator.page(page)

        if object_list.has_next() == False :
            acc_num = 0
        else :
            mod = paginator.count % self.paginate_by
            acc_num = (paginator.num_pages-int(page)-1) * self.paginate_by + mod

        context = {'object_list': object_list, 'acc_num' : acc_num}
        return render(request, self.template_name, context)

class PatentTextList(ListView):
    model = Patent
    template_name = 'web/patent.html'

    def get_context_data(self, **kwargs):
        context = super(PatentTextList, self).get_context_data(**kwargs)
        return context

#OPEN SOURCE##########################################################################################################################
def githubRedirect(request):
    return redirect('https://github.com/OpenXAIProject')

def youtubeRedirect(request):
    return redirect('https://www.youtube.com/channel/UCGxsfIsOry_LdBaPSet2p7g')

def OpenData(request):
    return render(request, 'web/opendata.html')

class RelatedProject(ListView):
    model = RelatedProject
    template_name = 'web/relatedproject.html'
    queryset = model.objects.order_by('-id')
    paginate_by = 4 #how much show your list

    def get_context_data(self, **kwargs):
        context = super(RelatedProject, self).get_context_data(**kwargs)
        return context

#Contact##########################################################################################################################
def Contact(request):
    return render(request, 'web/contact.html')

#### temporary use greeting model
def Symposium(request):
    return render(request, 'web/Symposium18.html')

def Symposium_ko(request):
    return render(request, 'web/Symposium18_ko.html')

def Workshop19(request):
    return render(request, 'web/workshop19.html')

def Tutorial19(request):
    return render(request, 'web/tutorial19.html')

def Tutorial20(request):
    return render(request, 'web/tutorial20.html')

def Workshop20(request):
    return render(request, 'web/workshop20.html')

def XaiTutorial(request):
    return render(request, 'web/xai_tutorial.html')

def Popup(request):
    return render(request, 'web/popup.html')
