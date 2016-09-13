import logging
from django.shortcuts import render
from django.views.generic import *
from .models import *	
from django.apps import apps
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class Home(View):

	def get(self, request):
		context = {}

		template = "home.html"
		return render (request, template, context)

class Dashboard(View):

	def get(self, request):
		musrenbang = Musrenbang.objects.all()
		pippk = Pippk.objects.all()
		status_musrenbang_kordinir =  Musrenbang.objects.filter(status='di akomodir')
		status_musrenbang_belum =  Musrenbang.objects.filter(status='belum di akomodir')
		status_musrenbang_tolak =  Musrenbang.objects.filter(status='di tolak')

		status_pippk_kordinir =  Pippk.objects.filter(status='di akomodir')
		status_pippk_belum =  Pippk.objects.filter(status='belum di akomodir')
		status_pippk_tolak =  Pippk.objects.filter(status='di tolak')

		context = {"musrenbang":musrenbang, "pippk":pippk, 'musrenbang_kordinir':{"kordinir":status_musrenbang_kordinir, "belum":status_musrenbang_belum, "tolak":status_musrenbang_tolak}, 'pippk_kordinir':{"kordinir":status_pippk_kordinir, "belum":status_pippk_belum, "tolak":status_pippk_tolak}}

		template = "content/dashboard.html"
		return render (request, template, context)

class Login(View):

	def get(self, request):
		if request.user.is_authenticated():
			return redirect('%s' %( "/dashboard/"))
		context = {}
		template = "content/login.html"
		return render (request, template, context)
	def post (self, request):
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']                                                                                                                                                                                                        
			login_form =  authenticate(username=username, password=password)
			response_data = {}                                                                              
			if login_form is not None:
				if login_form.is_active:
					login(request,login_form)
					return  redirect('%s' % ("/"))
			else:
				context = {'failed':True}
				template = "content/login.html"
				return render (request, template, context)

def logout(request):
	auth.logout(request)
	return  redirect('%s' % ("/login"))
	
class ReportMusrenbangList(ListView):
	template_name = "report_musrenbang/index.html"
	model = Musrenbang

	def get_queryset(self):
		return eval(self.model.__name__).objects.all()

class ReportPippkList(ListView):
	template_name = "report_pippk/index.html"
	model = Pippk

	def get_queryset(self):
		return eval(self.model.__name__).objects.all()

class BaseListViewSetting(PermissionRequiredMixin, ListView):

	login_url = '/login/'
	def get_permission_required(self):
		return ['base.add_%s'% self.model.__name__.lower()]
	
class BaseCreateSetting(PermissionRequiredMixin, CreateView):

	def get_permission_required(self):
		return ['base.add_%s'% self.form_class.Meta.model.__name__.lower()]

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)

class BaseUpdateSetting(PermissionRequiredMixin, UpdateView):

	def get_permission_required(self):
		return ['base.change_%s'% self.form_class.Meta.model.__name__.lower()]

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)
# Kecamatan
class KecamatanList(BaseListViewSetting):
	template_name = "kecamatan/index.html"
	model = Kecamatan

class KecamatanCreateView(BaseCreateSetting):
	form_class = KecamatanForm
	template_name = 'kecamatan/_create.html'

class KecamatanDeleteView(DeleteView):
	model = Kecamatan
	success_url = reverse_lazy('Kecamatan')
	template_name = 'kecamatan/_delete.html'

class KecamatanUpdateView(UpdateView):
	model = Kecamatan
	form_class = KecamatanForm
	template_name = 'kecamatan/_update.html'

# Kelurahan
class KelurahanList(BaseListViewSetting):
	template_name = "kelurahan/index.html"
	model = Kelurahan

class KelurahanCreateView(BaseCreateSetting):
	form_class = KelurahanForm
	template_name = 'kelurahan/_create.html'

class KelurahanDeleteView(DeleteView):
	model = Kelurahan
	success_url = reverse_lazy('Kelurahan')
	template_name = 'kelurahan/_delete.html'

class KelurahanUpdateView(UpdateView):
	model = Kelurahan
	form_class = KelurahanForm
	template_name = 'kelurahan/_update.html'

# Rw
class RwList(BaseListViewSetting):
	template_name = "rw/index.html"
	model = Rw

class RwCreateView(BaseCreateSetting):
	form_class = RwForm
	template_name = 'rw/_create.html'

class RwDeleteView(DeleteView):
	model = Rw
	success_url = reverse_lazy('Rw')
	template_name = 'rw/_delete.html'

class RwUpdateView(UpdateView):
	model = Rw
	form_class = RwForm
	template_name = 'rw/_update.html'

# Lpm
class LpmList(BaseListViewSetting):
	template_name = "lpm/index.html"
	model = Lpm

class LpmCreateView(BaseCreateSetting):
	form_class = LpmForm
	template_name = 'lpm/_create.html'

class LpmDeleteView(DeleteView):
	model = Lpm
	success_url = reverse_lazy('Lpm')
	template_name = 'lpm/_delete.html'

class LpmUpdateView(UpdateView):
	model = Lpm
	form_class = LpmForm
	template_name = 'lpm/_update.html'

# Pkk
class PkkList(BaseListViewSetting):
	template_name = "pkk/index.html"
	model = Pkk

class PkkCreateView(BaseCreateSetting):
	form_class = PkkForm
	template_name = 'pkk/_create.html'

class PkkDeleteView(DeleteView):
	model = Pkk
	success_url = reverse_lazy('Pkk')
	template_name = 'pkk/_delete.html'

class PkkUpdateView(UpdateView):
	model = Pkk
	form_class = PkkForm
	template_name = 'pkk/_update.html'

# Karang Taruna
class KarangTarunaList(BaseListViewSetting):
	template_name = "karang_taruna/index.html"
	model = KarangTaruna

class KarangTarunaCreateView(BaseCreateSetting):
	form_class = KarangTarunaForm
	template_name = 'karang_taruna/_create.html'

class KarangTarunaDeleteView(DeleteView):
	model = KarangTaruna
	success_url = reverse_lazy('KarangTaruna')
	template_name = 'karang_taruna/_delete.html'

class KarangTarunaUpdateView(UpdateView):
	model = KarangTaruna
	form_class = KarangTarunaForm
	template_name = 'karang_taruna/_update.html'

# # Urusan
class UrusanList(BaseListViewSetting):
	template_name = "urusan/index.html"
	model = Urusan

class UrusanCreateView(BaseCreateSetting):
	form_class = UrusanForm
	template_name = 'urusan/_create.html'

class UrusanDeleteView(DeleteView):
	model = Urusan
	success_url = reverse_lazy('Urusan')
	template_name = 'urusan/_delete.html'

class UrusanUpdateView(UpdateView):
	model = Urusan
	form_class = UrusanForm
	template_name = 'urusan/_update.html'

# Bidang
class BidangList(BaseListViewSetting):
	template_name = "bidang/index.html"
	model = Bidang

class BidangCreateView(BaseCreateSetting):
	form_class = BidangForm
	template_name = 'bidang/_create.html'
	success_url = '/'

class BidangDeleteView(DeleteView):
	model = Bidang
	success_url = reverse_lazy('Bidang')
	template_name = 'bidang/_delete.html'

class BidangUpdateView(UpdateView):
	model = Bidang
	form_class = BidangForm
	template_name = 'bidang/_update.html'

# Program
class ProgramList(BaseListViewSetting):
	template_name = "program/index.html"
	model = Program

class ProgramCreateView(BaseCreateSetting):
	form_class = ProgramForm
	template_name = 'program/_create.html'

class ProgramDeleteView(DeleteView):
	model = Program
	success_url = reverse_lazy('Program')
	template_name = 'program/_delete.html'

class ProgramUpdateView(UpdateView):
	model = Program
	form_class = ProgramForm
	template_name = 'program/_update.html'

# Kegiatan
class KegiatanList(BaseListViewSetting):
	template_name = "kegiatan/index.html"
	model = Kegiatan

class KegiatanCreateView(BaseCreateSetting):
	form_class = KegiatanForm
	template_name = 'kegiatan/_create.html'

class KegiatanDeleteView(DeleteView):
	model = Kegiatan
	success_url = reverse_lazy('Kegiatan')
	template_name = 'kegiatan/_delete.html'

class KegiatanUpdateView(UpdateView):
	model = Kegiatan
	form_class = KegiatanForm
	template_name = 'kegiatan/_update.html'

# Prioritas Daerah
class PrioritasDaerahList(BaseListViewSetting):
	template_name = "prioritas_daerah/index.html"
	model = PrioritasDaerah

class PrioritasDaerahCreateView(BaseCreateSetting):
	form_class = PrioritasDaerahForm
	template_name = 'prioritas_daerah/_create.html'

class PrioritasDaerahDeleteView(DeleteView):
	model = PrioritasDaerah
	success_url = reverse_lazy('PrioritasDaerah')
	template_name = 'prioritas_daerah/_delete.html'

class PrioritasDaerahUpdateView(UpdateView):
	model = PrioritasDaerah
	form_class = PrioritasDaerahForm
	template_name = 'prioritas_daerah/_update.html'

# Sasaran Daerah
class SasaranDaerahList(BaseListViewSetting):
	template_name = "sasaran_daerah/index.html"
	model = SasaranDaerah

class SasaranDaerahCreateView(BaseCreateSetting):
	form_class = SasaranDaerahForm
	template_name = 'sasaran_daerah/_create.html'

class SasaranDaerahDeleteView(DeleteView):
	model = SasaranDaerah
	success_url = reverse_lazy('SasaranDaerah')
	template_name = 'sasaran_daerah/_delete.html'

class SasaranDaerahUpdateView(UpdateView):
	model = SasaranDaerah
	form_class = SasaranDaerahForm
	template_name = 'sasaran_daerah/_update.html'

# Skpd Tujuan
class SkpdTujuanList(BaseListViewSetting):
	template_name = "skpd_tujuan/index.html"
	model = SkpdTujuan

class SkpdTujuanCreateView(BaseCreateSetting):
	form_class = SkpdTujuanForm
	template_name = 'skpd_tujuan/_create.html'

class SkpdTujuanDeleteView(DeleteView):
	model = SkpdTujuan
	success_url = reverse_lazy('SkpdTujuan')
	template_name = 'skpd_tujuan/_delete.html'

class SkpdTujuanUpdateView(UpdateView):
	model = SkpdTujuan
	form_class = SkpdTujuanForm
	template_name = 'skpd_tujuan/_update.html'

# Agenda
class AgendaList(BaseListViewSetting):
	template_name = "agenda/index.html"
	model = Agenda

class AgendaCreateView(BaseCreateSetting):
	form_class = AgendaForm
	template_name = 'agenda/_create.html'

class AgendaDetailView(DetailView):
	model = Agenda
	template_name = 'agenda/detail_view.html'

class AgendaDeleteView(DeleteView):
	model = Agenda
	success_url = reverse_lazy('Agenda')
	template_name = 'agenda/_delete.html'

class AgendaUpdateView(BaseUpdateSetting):
	model = Agenda
	form_class = AgendaForm
	template_name = 'agenda/_update.html'

# Musrenbang
class MusrenbangList(ListView):
	template_name = "musrenbang/index.html"
	model = Musrenbang

	def get(self, request):
		
		try:
			if str(request.user.groups.all()[0]) in ['admin', 'musrenbang', 'pippk'] or request.user.is_superuser:
			
				return super(MusrenbangList, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		except:
			if request.user.is_superuser:
				return super(MusrenbangList, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
	
	def get_queryset(self):
		if self.request.user.is_superuser or self.request.user.groups.all()[0] == "admin":
			return eval(self.model.__name__).objects.all()

		return eval(self.model.__name__).objects.filter(kecamatan=self.request.user.detailuser.kecamatan, kelurahan = self.request.user.detailuser.kelurahan, rw = self.request.user.detailuser.rw, lpm = self.request.user.detailuser.lpm, pkk = self.request.user.detailuser.pkk , karangtaruna = self.request.user.detailuser.karangtaruna) # return untuk view_customer_scope_ atau view_site_scope_

class MusrenbangCreateView(CreateView):
	form_class = MusrenbangForm
	template_name = 'musrenbang/_create.html'

	def get(self, request):
		try:
			if str(request.user.groups.all()[0]) in ['musrenbang', 'pippk'] :
				return super(MusrenbangCreateView, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		except:
			return redirect(reverse('Dashboard'))
	
	def form_valid(self, form):
		
		form.instance.status = 'belum di akomodir'
		form.instance.tipe = self.request.user.detailuser.tipe
		form.instance.kecamatan = self.request.user.detailuser.kecamatan
		form.instance.kelurahan = self.request.user.detailuser.kelurahan
		form.instance.rw = self.request.user.detailuser.rw
		form.instance.pkk = self.request.user.detailuser.pkk
		form.instance.lpm = self.request.user.detailuser.lpm
		form.instance.karangtaruna = self.request.user.detailuser.karangtaruna
		

		return super(MusrenbangCreateView, self).form_valid(form) 

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)

class MusrenbangDetailView(DetailView):
	model = Musrenbang
	template_name = 'musrenbang/detail_view.html'

	def post(self, request, pk):
		obj = eval(self.model.__name__).objects.get(pk=pk)
		obj.status = "di akomodir"
		obj.save()
		return redirect(reverse('%sDetail'% self.model.__name__, args=(pk,)))

class MusrenbangUpdateView(UpdateView):
	model = Musrenbang
	form_class = MusrenbangForm
	template_name = 'musrenbang/_update.html'

	def get(self, request, **kwargs):
		try:
			if str(request.user.groups.all()[0]) in ['musrenbang', 'pippk'] :
				return super(MusrenbangUpdateView, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		except:
			return redirect(reverse('Dashboard'))

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.model.__name__)

class MusrenbangTolakView(UpdateView):
	model = Musrenbang
	form_class = MusrenbangTolakForm
	template_name = 'musrenbang/_tolak.html'

	def get(self, request, pk):
		obj = eval(self.model.__name__).objects.get(pk=pk)
		if not self.request.user.is_superuser:
			if obj.status != 'belum di akomodir' or not self.request.user.groups.all()[0] == "admin" :
				return redirect(reverse('%sDetail'% self.model.__name__, args=(pk,)))
		return super(MusrenbangTolakView, self).get(request,pk)

	def form_valid(self, form):
		
		form.instance.status = 'di tolak'
		
		return super(MusrenbangTolakView, self).form_valid(form) 
	
	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.model.__name__)

	def get_queryset(self):
		if self.request.user.is_superuser or self.request.user.groups.all()[0] == "admin":
			return eval(self.model.__name__).objects.all()
		return eval(self.model.__name__).objects.filter(lpm=self.request.user.detailuser.lpm, pkk = self.request.user.detailuser.pkk, karangtaruna = self.request.user.detailuser.karangtaruna, rw = self.request.user.detailuser.rw)

class PippkTolakView(UpdateView):
	model = Pippk
	form_class = PippkTolakForm
	template_name = 'pippk/_tolak.html'

	def get(self, request, pk):
		obj = eval(self.model.__name__).objects.get(pk=pk)
		if not self.request.user.is_superuser:
			if obj.status != 'belum di akomodir' or not self.request.user.groups.all()[0] == "admin" :
				return redirect(reverse('%sDetail'% self.model.__name__, args=(pk,)))
		return super(PippkTolakView, self).get(request,pk)

	def form_valid(self, form):
		
		form.instance.status = 'di tolak'
		
		return super(PippkTolakView, self).form_valid(form)
	
	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.model.__name__)

	def get_queryset(self):
		if self.request.user.is_superuser or self.request.user.groups.all()[0] == "admin":
			return eval(self.model.__name__).objects.all()
		return eval(self.model.__name__).objects.filter(lpm=self.request.user.detailuser.lpm, pkk = self.request.user.detailuser.pkk, karangtaruna = self.request.user.detailuser.karangtaruna, rw = self.request.user.detailuser.rw)

class MusrenbangDeleteView(DeleteView):
	model = Musrenbang
	success_url = reverse_lazy('Musrenbang')
	template_name = 'musrenbang/_delete.html'

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.model.__name__)
	

# Pippk
class PippkList(ListView):
	template_name = "pippk/index.html"
	model = Pippk
	def get(self, request):
		
		try:
			if str(request.user.groups.all()[0]) in ['admin', 'pippk'] or request.user.is_superuser:
				return super(PippkList, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		except:
			if request.user.is_superuser:
				return super(PippkList, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		
	def get_queryset(self):
		if self.request.user.is_superuser or self.request.user.groups.all()[0] == "admin":
			return eval(self.model.__name__).objects.all()
		return eval(self.model.__name__).objects.filter( rw = self.request.user.detailuser.rw, lpm=self.request.user.detailuser.lpm, pkk = self.request.user.detailuser.pkk, karangtaruna = self.request.user.detailuser.karangtaruna)

class PippkCreateView(CreateView):
	form_class = PippkForm
	template_name = 'pippk/_create.html'

	def get(self, request):
		try:
			if str(request.user.groups.all()[0]) in ['pippk'] :
				return super(PippkCreateView, self).get(request)
			else:
				return redirect(reverse('Dashboard'))
		except:
			return redirect(reverse('Dashboard'))

	def form_valid(self, form):
		
		form.instance.status = 'belum di akomodir'
		form.instance.tipe = self.request.user.detailuser.tipe
		form.instance.lpm = self.request.user.detailuser.lpm
		form.instance.rw = self.request.user.detailuser.rw
		form.instance.pkk = self.request.user.detailuser.pkk
		form.instance.karangtaruna = self.request.user.detailuser.karangtaruna
		form.instance.kelurahan = self.request.user.detailuser.kelurahan
		return super(PippkCreateView, self).form_valid(form) 

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)

class PippkDetailView(DetailView):
	model = Pippk
	template_name = 'pippk/detail_view.html'
	def post(self, request, pk):
		obj = eval(self.model.__name__).objects.get(pk=pk)
		obj.status = "di akomodir"
		obj.alasan = None
		obj.save()
		return redirect(reverse('%sDetail'% self.model.__name__, args=(pk,)))

class PippkUpdateView(UpdateView):
	model = Pippk
	form_class = PippkForm
	template_name = 'pippk/_update.html'


	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)

class PippkDeleteView(DeleteView):
	model = Pippk
	success_url = reverse_lazy('Pippk')
	template_name = 'pippk/_delete.html'

# Saran
class SaranList(ListView):
	template_name = "saran/index.html"
	model = Saran

class SaranCreateView(CreateView):
	form_class = SaranForm
	template_name = 'saran/_create.html'

	def get_success_url(self):
		url = self.request.GET.get('next',False)
		if url:
			return url
		return reverse('%s'% self.form_class.Meta.model.__name__)

class SaranDetailView(DetailView):
	model = Saran
	template_name = 'saran/detail_view.html'

class SaranDeleteView(DeleteView):
	model = Saran
	success_url = reverse_lazy('Saran')
	template_name = 'saran/_delete.html'

# Informasi
class InformasiMusrenbang(View):

	def get(self, request):
		context = {}
		template = "informasi/musrenbang_info.html"
		return render (request, template, context)

class InformasiPippk(View):

	def get(self, request):
		context = {}
		template = "informasi/pippk_info.html"
		return render (request, template, context)

# User
class DetailUserList(BaseListViewSetting):
	template_name = "user_detail/index.html"
	model = DetailUser

class DetailUserCreateView(BaseCreateSetting):
	form_class = DetailUserForm
	template_name = 'user_detail/_create.html'
	
	def form_valid(self, form):
		try :
			if form.data['tipe'] in ['kecamatan', 'kelurahan']:
				groups = Group.objects.get(name__icontains='musrenbang')
			elif form.data['tipe'] in ['rw', 'lpm', 'pkk', 'karangtaruna']:
				groups = Group.objects.get(name__icontains='pippk')

			obj_usr = User.objects.create_user(
												username = form.data['username'], 
												password = form.data['password'],
												email = form.data['email'],	
												# first_name = form.data['first_name'],
												# last_name = form.data['last_name'],
												is_active =  form.data.get('is_active', False),
												is_staff =  form.data.get('is_staff', False)
												)
			form.instance.user = obj_usr
			# form.instance.full_name = form.data['first_name']+" "+form.data['last_name']
			groups.user_set.add(obj_usr)
		except:
	
			obj_usr = User.objects.filter(
												username = form.data['username'], 
												password = form.data['password'],
												email = form.data['email'],	
												is_active =  form.data.get('is_active', False),
												is_staff =  form.data.get('is_staff', False)
												)
			obj_usr.delete()
		return super(DetailUserCreateView, self).form_valid(form) 

class DetailUserDeleteView(DeleteView):
	model = DetailUser
	success_url = reverse_lazy('DetailUser')
	template_name = 'user_detail/_delete.html'

class DetailUserUpdateView(BaseUpdateSetting):
	model = DetailUser
	form_class = DetailUserForm
	template_name = 'user_detail/_update.html'

	def get_initial(self):
		return { 'username': self.object.user.username, 'password':self.object.user.password, 'email':self.object.user.email, 'is_staff':self.object.user.is_staff, 'is_active':self.object.user.is_active }

	def form_valid(self, form):
		if form.data['tipe'] in ['kecamatan', 'kelurahan']:
			groups = Group.objects.get(name__icontains='musrenbang')
		elif form.data['tipe'] in ['rw', 'lpm', 'pkk', 'karangtaruna']:
			groups = Group.objects.get(name__icontains='Pippk')

		User.objects.filter(pk=self.object.user.id).update(username = form.data['username'], 
											password = form.data['password'],
											email = form.data['email'],	
											# first_name = form.data['first_name'],
											# last_name = form.data['last_name'],
											is_active =  form.data.get('is_active', False),
											is_staff =  form.data.get('is_staff', False))
	
		# form.instance.full_name = form.data['first_name']+" "+form.data['last_name']
		self.object.user.groups.clear()
		groups.user_set.add(self.object.user.id)
		return super(DetailUserUpdateView, self).form_valid(form) 

#============================================================================================================================
class ServiceList(View):
	def prepare_list(self, result_filter, extra_fields):

		res = []
		for data in result_filter:
			res_extra_fields = {}

			for obj_field in extra_fields:
				
				split_obj_name = obj_field.split(".")
				if split_obj_name:
					obj_to_fetch = data
					for obj in split_obj_name:
						res_extra_fields[obj_field] = getattr(obj_to_fetch, obj)
						obj_to_fetch = res_extra_fields[obj_field]
				else:
					res_extra_fields[obj_field] = getattr(data, obj_field)
			
			res_field_name = self.request.GET.get('result_field_name',"name")
			# part.name
			list_res_field_name = res_field_name.split('.')
			# [part, name]
			print list_res_field_name,"*****************************"

			final_name = ''

			if len(list_res_field_name)>1:
				curr=0
				obj_data2 = None
				for res_f_n in list_res_field_name:
					print curr,"CURRRR",res_f_n
					if curr==0:
						# data.field
						new_obj = getattr(data, res_f_n)
						obj_data2 = new_obj
					else:
						# obj_data2.field
						new_obj = getattr(obj_data2, res_f_n)
						final_name = new_obj

					
					curr+=1
			else:
				final_name = getattr(data,res_field_name)
							
			res.append({'id':data.id, 'name':final_name, 'extra_fields':res_extra_fields})

		return res

	def get(self, request, *args, **kwargs):
		# print request.POST,"<<<<<<<,POST"
		# print request.GET,"GETTTTTTTTTT<<<<"
		Model = apps.get_model('base',kwargs['model'])
		# logging.error(request.GET['q'])
		query_search = request.GET.get('q',False)
		query_fields = request.GET.getlist('fields[]') # 
		and_filter = request.GET.get('and_filter')#
		tpl_q = Q(name__icontains=query_search)

		if query_fields:
			tpl_q = []
			logging.info("Loading with fields kwargs")
			for field in query_fields:
				if field !='id':
					tpl_q.append({field+"__icontains":query_search})
				else:
					tpl_q.append({field+"__exact":query_search})
					print "EXACT----------------------------------"

			q_obj = None
			for q in tpl_q:
				if q_obj==None:
					q_obj = Q(**q)
				else:
					q_obj |= Q(**q)
			tpl_q = q_obj
	
		if and_filter:
			filter_and = json.loads(and_filter)
			resfilter = Model.objects.filter(tpl_q).filter(**filter_and)
		else:
			resfilter = Model.objects.filter(tpl_q)

		res = self.prepare_list(resfilter, request.GET.getlist('extra_fields[]'))	
		

		return JsonResponse({'status':True,'items':res})
		
# ===========================================================================================================================

# def login_custom(request):
# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']                                                                                                                                                                                                        
# 		login_form =  authenticate(username=username, password=password)
# 		response_data = {}                                                                              
# 		if login_form is not None:
# 			if login_form.is_active:
# 				login(request,login_form)
# 				return  redirect('%s' % ("/"))
# 		else:
# 			context = {}
# 			template = "content/login.html"
# 			return render (request, template, context)


