"""musrenbang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import patterns
from base import views as base_views
from base.views import *
from django.conf.urls import patterns
from musrenbang import settings

urlpatterns = [

    url(r'^admin/', admin.site.urls),
     url(r'^$', Home.as_view(), name="Home"),    
    url(r'^Dashboard/$', Dashboard.as_view(), name="Dashboard"),    
    url(r'^login/$', Login.as_view(), name="Login"),
    url(r'^logout/',base_views.logout, name="Logout"),

    url(r'^kecamatan/$', KecamatanList.as_view(), name="Kecamatan"),
    url(r'^kecamatan/add/$', KecamatanCreateView.as_view(), name="KecamatanAdd"),
    url(r'^kecamatan/delete/(?P<pk>\d+)/$', KecamatanDeleteView.as_view(), name="KecamatanDelete"),
    url(r'^kecamatan/update/(?P<pk>\d+)/$', KecamatanUpdateView.as_view(), name="KecamatanUpdate"),

    url(r'^user/$', DetailUserList.as_view(), name="DetailUser"),
    url(r'^user/add/$', DetailUserCreateView.as_view(), name="DetailUserAdd"),
    url(r'^user/delete/(?P<pk>\d+)/$', DetailUserDeleteView.as_view(), name="DetailUserDelete"),
    url(r'^user/update/(?P<pk>\d+)/$', DetailUserUpdateView.as_view(), name="DetailUserUpdate"),

    url(r'^kelurahan/$', KelurahanList.as_view(), name="Kelurahan"),
    url(r'^kelurahan/add/$', KelurahanCreateView.as_view(), name="KelurahanAdd"),
    url(r'^kelurahan/delete/(?P<pk>\d+)/$', KelurahanDeleteView.as_view(), name="KelurahanDelete"),
    url(r'^kelurahan/update/(?P<pk>\d+)/$', KelurahanUpdateView.as_view(), name="KelurahanUpdate"),
    
    url(r'^lpm/$', LpmList.as_view(), name="Lpm"),
    url(r'^lpm/add/$', LpmCreateView.as_view(), name="LpmAdd"),
    url(r'^lpm/delete/(?P<pk>\d+)/$', LpmDeleteView.as_view(), name="LpmDelete"),
    url(r'^lpm/update/(?P<pk>\d+)/$', LpmUpdateView.as_view(), name="LpmUpdate"),

    url(r'^pkk/$', PkkList.as_view(), name="Pkk"),
    url(r'^pkk/add/$', PkkCreateView.as_view(), name="PkkAdd"),
    url(r'^pkk/delete/(?P<pk>\d+)/$', PkkDeleteView.as_view(), name="PkkDelete"),
    url(r'^pkk/update/(?P<pk>\d+)/$', PkkUpdateView.as_view(), name="PkkUpdate"),

    url(r'^karang-taruna/$', KarangTarunaList.as_view(), name="KarangTaruna"),
    url(r'^karang-taruna/add/$', KarangTarunaCreateView.as_view(), name="KarangTarunaAdd"),
    url(r'^karang-taruna/delete/(?P<pk>\d+)/$', KarangTarunaDeleteView.as_view(), name="KarangTarunaDelete"),
    url(r'^karang-taruna/update/(?P<pk>\d+)/$', KarangTarunaUpdateView.as_view(), name="KarangTarunaUpdate"),

    url(r'^rw/$', RwList.as_view(), name="Rw"),
    url(r'^rw/add/$', RwCreateView.as_view(), name="RwAdd"),
    url(r'^rw/delete/(?P<pk>\d+)/$', RwDeleteView.as_view(), name="RwDelete"),
    url(r'^rw/update/(?P<pk>\d+)/$', RwUpdateView.as_view(), name="RwUpdate"),

    url(r'^urusan/$', UrusanList.as_view(), name="Urusan"),
    url(r'^urusan/add/$', UrusanCreateView.as_view(), name="UrusanAdd"),
    url(r'^urusan/delete/(?P<pk>\d+)/$', UrusanDeleteView.as_view(), name="UrusanDelete"),
    url(r'^urusan/update/(?P<pk>\d+)/$', UrusanUpdateView.as_view(), name="UrusanUpdate"),

    url(r'^bidang/$', BidangList.as_view(), name="Bidang"),
    url(r'^bidang/add/$', BidangCreateView.as_view(), name="BidangAdd"),
    url(r'^bidang/delete/(?P<pk>\d+)/$', BidangDeleteView.as_view(), name="BidangDelete"),
    url(r'^bidang/update/(?P<pk>\d+)/$', BidangUpdateView.as_view(), name="BidangUpdate"),

    url(r'^program/$', ProgramList.as_view(), name="Program"),
    url(r'^program/add/$', ProgramCreateView.as_view(), name="ProgramAdd"),
    url(r'^program/delete/(?P<pk>\d+)/$', ProgramDeleteView.as_view(), name="ProgramDelete"),
    url(r'^program/update/(?P<pk>\d+)/$', ProgramUpdateView.as_view(), name="ProgramUpdate"),

    url(r'^kegiatan/$', KegiatanList.as_view(), name="Kegiatan"),
    url(r'^kegiatan/add/$', KegiatanCreateView.as_view(), name="KegiatanAdd"),
    url(r'^kegiatan/delete/(?P<pk>\d+)/$', KegiatanDeleteView.as_view(), name="KegiatanDelete"),
    url(r'^kegiatan/update/(?P<pk>\d+)/$', KegiatanUpdateView.as_view(), name="KegiatanUpdate"),

    url(r'^prioritas-daerah/$', PrioritasDaerahList.as_view(), name="PrioritasDaerah"),
    url(r'^prioritas-daerah/add/$', PrioritasDaerahCreateView.as_view(), name="PrioritasDaerahAdd"),
    url(r'^prioritas-daerah/delete/(?P<pk>\d+)/$', PrioritasDaerahDeleteView.as_view(), name="PrioritasDaerahDelete"),
    url(r'^prioritas-daerah/update/(?P<pk>\d+)/$', PrioritasDaerahUpdateView.as_view(), name="PrioritasDaerahUpdate"),

    url(r'^sasaran-daerah/$', SasaranDaerahList.as_view(), name="SasaranDaerah"),
    url(r'^sasaran-daerah/add/$', SasaranDaerahCreateView.as_view(), name="SasaranDaerahAdd"),
    url(r'^sasaran-daerah/delete/(?P<pk>\d+)/$', SasaranDaerahDeleteView.as_view(), name="SasaranDaerahDelete"),
    url(r'^sasaran-daerah/update/(?P<pk>\d+)/$', SasaranDaerahUpdateView.as_view(), name="SasaranDaerahUpdate"),

    url(r'^skpd-tujuan/$', SkpdTujuanList.as_view(), name="SkpdTujuan"),
    url(r'^skpd-tujuan/add/$', SkpdTujuanCreateView.as_view(), name="SkpdTujuanAdd"),
    url(r'^skpd-tujuan/delete/(?P<pk>\d+)/$', SkpdTujuanDeleteView.as_view(), name="SkpdTujuanDelete"),
    url(r'^skpd-tujuan/update/(?P<pk>\d+)/$', SkpdTujuanUpdateView.as_view(), name="SkpdTujuanUpdate"),
        
    url(r'^musrenbang/$', MusrenbangList.as_view(), name="Musrenbang"),
    url(r'^musrenbang/add/$', MusrenbangCreateView.as_view(), name="MusrenbangAdd"),
    url(r'^musrenbang/(?P<pk>\d+)/$', MusrenbangDetailView.as_view(), name="MusrenbangDetail"),
    url(r'^musrenbang/delete/(?P<pk>\d+)/$', MusrenbangDeleteView.as_view(), name="MusrenbangDelete"),
    url(r'^musrenbang/update/(?P<pk>\d+)/$', MusrenbangUpdateView.as_view(), name="MusrenbangUpdate"),
    url(r'^musrenbang/tolak/(?P<pk>\d+)/$', MusrenbangTolakView.as_view(), name="MusrenbangTolak"),

    url(r'^pippk/$', PippkList.as_view(), name="Pippk"),
    url(r'^pippk/add/$', PippkCreateView.as_view(), name="PippkAdd"),
    url(r'^pippk/(?P<pk>\d+)/$', PippkDetailView.as_view(), name="PippkDetail"),
    url(r'^pippk/delete/(?P<pk>\d+)/$', PippkDeleteView.as_view(), name="PippkDelete"),
    url(r'^pippk/update/(?P<pk>\d+)/$', PippkUpdateView.as_view(), name="PippkUpdate"),
    url(r'^pippk/tolak/(?P<pk>\d+)/$', PippkTolakView.as_view(), name="PippkTolak"),

    # url(r'^pelaksanaan-musrenbang/$', PelaksanaanMusrenbangList.as_view(), name="PelaksanaanMusrenbang"),
    url(r'^pelaksanaan-musrenbang/add/$', PelaksanaanMusrenbangCreateView.as_view(), name="PelaksanaanMusrenbangAdd"),
    # url(r'^pelaksanaan-musrenbang/(?P<pk>\d+)/$', PelaksanaanMusrenbangDetailView.as_view(), name="PelaksanaanMusrenbangDetail"),
    # url(r'^pelaksanaan-musrenbang/delete/(?P<pk>\d+)/$', PelaksanaanMusrenbangDeleteView.as_view(), name="PelaksanaanMusrenbangDelete"),
    # url(r'^pelaksanaan-musrenbang/update/(?P<pk>\d+)/$', PelaksanaanMusrenbangUpdateView.as_view(), name="PelaksanaanMusrenbangUpdate"),

    # url(r'^pelaksanaan-pippk/$', PelaksanaanPippkList.as_view(), name="PelaksanaanPippk"),
    url(r'^pelaksanaan-pippk/add/$', PelaksanaanPippkCreateView.as_view(), name="PelaksanaanPippkAdd"),
    # url(r'^pelaksanaan-pippk/(?P<pk>\d+)/$', PelaksanaanPippkDetailView.as_view(), name="PelaksanaanPippkDetail"),
    # url(r'^pelaksanaan-pippk/delete/(?P<pk>\d+)/$', PelaksanaanPippkDeleteView.as_view(), name="PelaksanaanPippkDelete"),
    # url(r'^pelaksanaan-pippk/update/(?P<pk>\d+)/$', PelaksanaanPippkUpdateView.as_view(), name="PelaksanaanPippkUpdate"),

    url(r'^saran/$', SaranList.as_view(), name="Saran"),
    url(r'^saran/add/$', SaranCreateView.as_view(), name="SaranAdd"),
    url(r'^saran/(?P<pk>\d+)/$', SaranDetailView.as_view(), name="SaranDetail"),
    url(r'^saran/delete/(?P<pk>\d+)/$', SaranDeleteView.as_view(), name="SaranDelete"),

    url(r'^agenda/$', AgendaList.as_view(), name="Agenda"),
    url(r'^agenda/add/$', AgendaCreateView.as_view(), name="AgendaAdd"),
    url(r'^agenda/(?P<pk>\d+)/$', AgendaDetailView.as_view(), name="AgendaDetail"),
    url(r'^agenda/delete/(?P<pk>\d+)/$', AgendaDeleteView.as_view(), name="AgendaDelete"),
    url(r'^agenda/update/(?P<pk>\d+)/$', AgendaUpdateView.as_view(), name="AgendaUpdate"),

    url(r'^informasi-musrenbang/$', InformasiMusrenbang.as_view(), name="InformasiMusrenbang"),
    url(r'^informasi-pippk/$', InformasiPippk.as_view(), name="InformasiPippk"),

    # url(r'^confirm-status/(?P<model>[a-zA-Z,.]+)/(?P<ids>[0-9]+)/(?P<status>[a-zA-Z,.]+)/$', base_views.ConfirmStatus, name="ConfirmStatus"),
    url(r'^service/(?P<model>\w+)/$', ServiceList.as_view(), name="Service"),
    url(r'^report-musrenbang/$', ReportMusrenbangList.as_view(), name="ReportMusrenbang"),
     url(r'^report-pippk/$', ReportPippkList.as_view(), name="ReportPippk"),
    

]

urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
