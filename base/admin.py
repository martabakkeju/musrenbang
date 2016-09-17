from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Kecamatan,KecamatanAdmin)
admin.site.register(Kelurahan,KelurahanAdmin)
admin.site.register(Rw,RwAdmin)
admin.site.register(Lpm,LpmAdmin)
admin.site.register(Pkk,PkkAdmin)
admin.site.register(KarangTaruna,KarangTarunaAdmin)
admin.site.register(Bidang,BidangAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Kegiatan,KegiatanAdmin)
admin.site.register(PrioritasDaerah,PrioritasDaerahAdmin)
admin.site.register(SasaranDaerah,SasaranDaerahAdmin)
admin.site.register(DetailUser,DetailUserAdmin)
admin.site.register(Musrenbang,MusrenbangAdmin)
admin.site.register(SkpdTujuan, SkpdTujuanAdmin)
admin.site.register(Pippk, PippkAdmin)
admin.site.register(Saran, SaranAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(PelaksanaanMusrenbang, PelaksanaanMusrenbangAdmin)
admin.site.register(PelaksanaanPippk, PelaksanaanPippkAdmin)
