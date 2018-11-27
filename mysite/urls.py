from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static                              # ch10 1/4
# settings 변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체에 대한 참조
from django.conf import settings
from mysite.views import HomeView  # 추가!!!

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(), name='home'),  # 추가!!!
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),          # ch10 3/4

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)     # ch10 4/4
