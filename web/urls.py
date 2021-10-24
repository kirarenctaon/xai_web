from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<subMenu>.+)/$', views.subMenu, name='subMenu'),

    # List
    url(r'^about/greeting/$', views.GreetingPage, name='greeting'),
    url(r'^about/member/$', views.MemberImageList, name='member'),
    url(r'^about/lab/$', views.LabTextList, name='lab'),
    url(r'^about/introduction/$', views.ProjectPage, name='introduction'),

    url(r'^news&info/notice/$', views.NoticeTextList, name='notice'),
    url(r'^news&info/news/2020$', views.Newsletter, name='news'),
    url(r'^news&info/news/2021$', views.Newsletter21, name='news21'),

    url(r'^research/automatic_news/$', views.AutomaticNews.as_view(), name='autonews'),
    url(r'^research/automatic_news/list/(?P<company>.+)/$', views.AutomaticNewsList.as_view(), name='autonews_list'),
    url(r'^research/automatic_news/detail/(?P<pk>\d+)/$', views.AutomaticNewsDetail.as_view(), name='autonews_detail'),

    # url(r'^research/demoresource/$', views.DemoresourceImageList.as_view(), name='demoresource'),
    url(r'^research/unist_index/$', views.financialIndex, name='financial_index'),
    url(r'^research/stock_commodity/$', views.stock, name='stock_commodity'),
    url(r'^research/publication/$', views.PublicationTextList.as_view(), name='publication'),
    url(r'^research/patent/$', views.PatentTextList.as_view(), name='patent'),

    #opensource
    url(r'^opensource/github/$', views.githubRedirect, name='github'),
    url(r'^opensource/relatedproject/$', views.RelatedProject.as_view(), name='relatedproject'),
    url(r'^opensource/youtube/$', views.youtubeRedirect, name='youtube'),
    url(r'^opensource/opendata/$', views.OpenData, name='opendata'),

    url(r'^xai_tutorial/$', views.XaiTutorial, name='Tutorial4all'),

    # Symposium
    url(r'^Symposium/2018/$', views.Symposium, name='Symposium18'),
    url(r'^Symposium/2018/korean/$', views.Symposium_ko, name='Symposium18_ko'),
    url(r'^popups/2018/$', views.Popup, name='popup'),
    url(r'^workshop/2019/$', views.Workshop19, name='Workshop19'),
    url(r'^Tutorial/2019/$', views.Tutorial19, name='Tutorial19'),
    url(r'^Tutorial/2020/$', views.Tutorial20, name='Tutorial20'),
    url(r'^workshop/2020/$', views.Workshop20, name='Workshop20'),
    #contact
    url(r'^contact/$', views.Contact, name='contact'),
]
