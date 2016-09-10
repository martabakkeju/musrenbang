from __future__ import unicode_literals
from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

# Create your models here.
class Kecamatan(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class KecamatanAdmin(admin.ModelAdmin):
	list_display = ('name',)

class KecamatanForm(ModelForm):
	class Meta:
		model = Kecamatan
		fields = ['name']

class Kelurahan(models.Model):
	name = models.CharField(max_length=50, unique=True)
	kecamatan = models.ForeignKey('Kecamatan', on_delete=models.PROTECT, related_name='kelurahan')

	def __unicode__(self):
		return self.name

class KelurahanAdmin(admin.ModelAdmin):
	list_display = ('name', 'kecamatan')

class KelurahanForm(ModelForm):
	class Meta:
		model = Kelurahan
		fields = ['name', 'kecamatan']

class Rw(models.Model):
	name = models.CharField(max_length=50, unique=True)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT, related_name='rw')

	def __unicode__(self):
		return self.name

class RwAdmin(admin.ModelAdmin):
	list_display = ('name', 'kelurahan')

class RwForm(ModelForm):
	class Meta:
		model = Rw
		fields = ['name', 'kelurahan']

class Lpm(models.Model):
	name = models.CharField(max_length=50, unique=True)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT, related_name='lpm')

	def __unicode__(self):
		return self.name

class LpmAdmin(admin.ModelAdmin):
	list_display = ('name', 'kelurahan')

class LpmForm(ModelForm):
	class Meta:
		model = Lpm
		fields = ['name', 'kelurahan']

class Pkk(models.Model):
	name = models.CharField(max_length=50, unique=True)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT, related_name='pkk')

	def __unicode__(self):
		return self.name

class PkkAdmin(admin.ModelAdmin):
	list_display = ('name', 'kelurahan')

class PkkForm(ModelForm):
	class Meta:
		model = Pkk
		fields = ['name', 'kelurahan']

class KarangTaruna(models.Model):
	name = models.CharField(max_length=50, unique=True)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT, related_name='karangtaruna')

	def __unicode__(self):
		return self.name

class KarangTarunaAdmin(admin.ModelAdmin):
	list_display = ('name', 'kelurahan')

class KarangTarunaForm(ModelForm):
	class Meta:
		model = KarangTaruna
		fields = ['name', 'kelurahan']

class Urusan(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class UrusanAdmin(admin.ModelAdmin):
	list_display = ('name',)

class UrusanForm(ModelForm):
	class Meta:
		model = Urusan
		fields = ['name']
	
class Bidang(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class BidangAdmin(admin.ModelAdmin):
	list_display = ('name',)

class BidangForm(ModelForm):
	class Meta:
		model = Bidang
		fields = ['name']

class Program(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class ProgramAdmin(admin.ModelAdmin):
	list_display = ('name',)

class ProgramForm(ModelForm):
	class Meta:
		model = Program
		fields = ['name']

class Kegiatan(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class KegiatanAdmin(admin.ModelAdmin):
	list_display = ('name',)

class KegiatanForm(ModelForm):
	class Meta:
		model = Kegiatan
		fields = ['name']

class PrioritasDaerah(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class PrioritasDaerahAdmin(admin.ModelAdmin):
	list_display = ('name',)

class PrioritasDaerahForm(ModelForm):
	class Meta:
		model = PrioritasDaerah
		fields = ['name']	

class SasaranDaerah(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class SasaranDaerahAdmin(admin.ModelAdmin):
	list_display = ('name',)
	
class SasaranDaerahForm(ModelForm):
	class Meta:
		model = SasaranDaerah
		fields = ['name']	

class SkpdTujuan(models.Model):
	name = models.CharField(max_length=50, unique=True)

	def __unicode__(self):
		return self.name

class SkpdTujuanAdmin(admin.ModelAdmin):
	list_display = ('name',)

class SkpdTujuanForm(ModelForm):
	class Meta:
		model = SkpdTujuan
		fields = ['name']

class Musrenbang(models.Model):
	TIPE = (
		('kecamatan', 'kecamatan'),
		('kelurahan', 'kelurahan'),
		('rw', 'rw'),
		('lpm', 'lpm'),
		('pkk', 'pkk'),
		('karangtaruna', 'karangtaruna'),
	)
	tipe = models.CharField(choices=TIPE, max_length=15)	
	kecamatan = models.ForeignKey('Kecamatan', on_delete=models.PROTECT)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT, blank=True, null=True)
	rw = models.ForeignKey('Rw', on_delete=models.PROTECT, blank=True, null=True)
	lpm = models.ForeignKey('Lpm', on_delete=models.PROTECT, blank=True, null=True)
	pkk = models.ForeignKey('Pkk', on_delete=models.PROTECT, blank=True, null=True)
	karangtaruna = models.ForeignKey('KarangTaruna', on_delete=models.PROTECT, blank=True, null=True)
	urusan = models.ForeignKey('Urusan', on_delete=models.PROTECT)
	bidang = models.ForeignKey('Bidang', on_delete=models.PROTECT)
	prioritasdaerah = models.ForeignKey('PrioritasDaerah', on_delete=models.PROTECT)
	sasarandaerah = models.ForeignKey('SasaranDaerah', on_delete=models.PROTECT)
	program = models.ForeignKey('Program', on_delete=models.PROTECT)
	kegiatan = models.ForeignKey('Kegiatan', on_delete=models.PROTECT)
	sasaran = models.CharField(max_length=50)
	volume = models.CharField(max_length=10)
	usulan = models.IntegerField()
	STATUS = (
		('di akomodir', 'Di Akomodir'),
		('belum di akomodir', 'Belum Di Akomodir'),
		('di tolak', 'Di Tolak'),
	)
	status = models.CharField(choices=STATUS, default='belum', max_length=19)
	skpdtujuan = models.ForeignKey('SkpdTujuan', on_delete=models.PROTECT)
	lokasi = models.CharField(max_length=50)
	# foto_kegiatan = models.ImageField(null=True, blank=True, upload_to='foto/')
	alasan = models.CharField(max_length=300, blank=True, null= True)

	def is_data_consistent(self):

		is_valid = True 
		err_msgs = []
		if self.tipe in ['lpm', 'pkk', 'karangtaruna', 'rw']:
			if self.usulan < 20000000:
				err_msgs.append(ValidationError('Untuk di Musrenbang (RW,LPM,PKK,KARANG TARUNA) Lebih dari >20 Juta Masukan Usulan Anda di Musrenbang')) 
				is_valid = False 
		return {'status':is_valid, "err_msgs":err_msgs}

	def clean(self):
		is_data_consistent = self.is_data_consistent()
		if not is_data_consistent['status']:
			raise ValidationError(is_data_consistent['err_msgs'])
		return super(Musrenbang, self).clean()
class MusrenbangTolakForm(ModelForm):
	class Meta:
		model = Musrenbang
		fields = ['alasan']

	def clean(self):

		if self.instance.id:
			if not self.cleaned_data["alasan"]:
				raise ValidationError("di butuhkan alasan")



class MusrenbangForm(ModelForm):
	class Meta:
		model = Musrenbang
		fields = ['usulan','urusan', 'bidang', 'prioritasdaerah', 'sasarandaerah', 'program', 'kegiatan', 'sasaran', 'volume', 'skpdtujuan','lokasi', 'alasan', 'tipe']
		widgets = {
			'urusan': forms.Select(attrs={'id':'urusan', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'bidang': forms.Select(attrs={'id':'bidang', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'prioritasdaerah': forms.Select(attrs={'id':'prioritasdaerah', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'sasarandaerah': forms.Select(attrs={'id':'sasarandaerah', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'program': forms.Select(attrs={'id':'program', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'kegiatan': forms.Select(attrs={'id':'kegiatan', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'skpdtujuan': forms.Select(attrs={'id':'urusan', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
		}
class MusrenbangAdmin(admin.ModelAdmin):
	list_display = ('urusan', 'bidang', 'prioritasdaerah', 'sasarandaerah', 'program', 'kegiatan', 'sasaran', 'volume','status', 'skpdtujuan', 'alasan', 'lokasi', 'usulan')

class Pippk(models.Model):
	TIPE = (
		('rw', 'rw'),
		('lpm', 'lpm'),
		('pkk', 'pkk'),
		('karangtaruna', 'karangtaruna'),
	)

	tipe = models.CharField(choices=TIPE, max_length=15)
	kelurahan = models.ForeignKey('Kelurahan', on_delete=models.PROTECT)
	rw = models.ForeignKey('Rw', on_delete=models.PROTECT, blank=True, null=True)
	lpm = models.ForeignKey('Lpm', on_delete=models.PROTECT, blank=True, null=True)
	pkk = models.ForeignKey('Pkk', on_delete=models.PROTECT, blank=True, null=True)
	karangtaruna = models.ForeignKey('KarangTaruna', on_delete=models.PROTECT, blank=True, null=True)
	urusan = models.ForeignKey('Urusan', on_delete=models.PROTECT)
	bidang = models.ForeignKey('Bidang', on_delete=models.PROTECT)
	prioritasdaerah = models.ForeignKey('PrioritasDaerah', on_delete=models.PROTECT)
	sasarandaerah = models.ForeignKey('SasaranDaerah', on_delete=models.PROTECT)
	program = models.ForeignKey('Program', on_delete=models.PROTECT)
	kegiatan = models.ForeignKey('Kegiatan', on_delete=models.PROTECT)
	sasaran = models.CharField(max_length=50)

	volume = models.CharField(max_length=10)
	usulan = models.IntegerField()
	STATUS = (
		('di akomodir', 'Di Akomodir'),
		('belum di akomodir', 'Belum Di Akomodir'),
		('di tolak', 'Di Tolak'),
	)
	status = models.CharField(choices=STATUS, max_length=20)
	lokasi = models.CharField(max_length=50, blank=True, null= True)
	alasan = models.CharField(max_length=50, blank=True, null= True)

	def is_data_consistent(self):
		is_valid = True 
		err_msgs = []
		if self.usulan > 20000000:
			err_msgs.append(ValidationError('Untuk di PIPPK Lebih dari >20 Juta Masukan Usulan Anda di Musrenbang')) 
			is_valid = False 
		return {'status':is_valid, "err_msgs":err_msgs}

	def clean(self):
		is_data_consistent = self.is_data_consistent()
		if not is_data_consistent['status']:
			raise ValidationError(is_data_consistent['err_msgs'])
		return super(Pippk, self).clean()
		
class PippkForm(ModelForm):
	class Meta:
		model = Pippk
		fields = ['usulan', 'urusan', 'bidang', 'prioritasdaerah', 'sasarandaerah', 'program', 'kegiatan', 'sasaran', 'volume', 'lokasi', 'alasan']
		widgets = {
			'urusan': forms.Select(attrs={'id':'urusan', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'bidang': forms.Select(attrs={'id':'bidang', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'prioritasdaerah': forms.Select(attrs={'id':'prioritasdaerah', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'sasarandaerah': forms.Select(attrs={'id':'sasarandaerah', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'program': forms.Select(attrs={'id':'program', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
			'kegiatan': forms.Select(attrs={'id':'kegiatan', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
		}
class PippkTolakForm(ModelForm):
	class Meta:
		model = Pippk
		fields = ['alasan']


	def clean(self):

		if self.instance.id:
			if not self.cleaned_data["alasan"]:
				raise ValidationError("di butuhkan alasan")


class PippkAdmin(admin.ModelAdmin):
	list_display = ('usulan', 'urusan', 'bidang', 'prioritasdaerah', 'sasarandaerah', 'program', 'kegiatan', 'sasaran', 'volume','status', 'lokasi', 'alasan')

class Saran(models.Model):
	nama_lengkap = models.CharField(max_length=40)
	email = models.EmailField(max_length=40)
	telp = models.CharField(max_length=12)
	no_ktp = models.CharField(max_length=16)
	judul = models.CharField(max_length=45)
	pesan = models.TextField()
	terima = models.BooleanField(default=False)

class SaranForm(ModelForm):
	class Meta:
		model = Saran
		fields = ['nama_lengkap', 'email', 'telp', 'no_ktp', 'judul', 'pesan']

class SaranAdmin(admin.ModelAdmin):
	list_display = ('nama_lengkap', 'email', 'telp', 'no_ktp', 'judul', 'pesan', 'terima')

class Agenda(models.Model):
	kecamatan = models.ForeignKey('Kecamatan', blank=True, null=True)
	kelurahan = models.ForeignKey('Kelurahan', blank=True, null=True)
	rw = models.ForeignKey('Rw', blank=True, null=True)
	waktu = models.DateTimeField()
	keterangan = models.TextField(blank=True, null=True)

class AgendaForm(ModelForm):
	class Meta:
		model = Agenda
		fields = ['kecamatan', 'kelurahan', 'rw', 'waktu', 'keterangan']

class AgendaAdmin(admin.ModelAdmin):
	list_display = ('kecamatan', 'kelurahan', 'rw', 'waktu', 'keterangan')
	
class DetailUser(models.Model):
	full_name = models.CharField(max_length=50, blank=False)
	user = models.OneToOneField(User, related_name="detailuser")
	kecamatan = models.ForeignKey('Kecamatan', blank=True, null=True)
	kelurahan = models.ForeignKey('Kelurahan', blank=True, null=True)
	rw =  models.ForeignKey('Rw', blank=True, null=True)
	lpm =  models.ForeignKey('Lpm', blank=True, null=True)
	pkk =  models.ForeignKey('Pkk', blank=True, null=True)
	karangtaruna =  models.ForeignKey('KarangTaruna', blank=True, null=True)

	TIPE = (
		('kecamatan','Kecamatan'),
		('kelurahan','Kelurahan'),
		('rw','Rw'),
		('lpm','Lpm'),
		('pkk','Pkk'),
		('karangtaruna','Karang Taruna'),
		
	)
	tipe = models.CharField(max_length=20, choices=TIPE)

	class Meta:
		unique_together = ('kecamatan', 'kelurahan', 'rw', 'lpm', 'pkk', 'karangtaruna')


	def delete(self, *args, **kwargs):
		super(DetailUser, self).delete( *args, **kwargs)
		user = User.objects.filter(pk=self.user.id)
		user.delete()

	def save(self, *args, **kwargs):
		if not self.pk:
			if self.tipe == 'rw':
				self.kelurahan = self.rw.kelurahan
			elif self.tipe == 'lpm':
				print "masuk"
				self.kelurahan = self.lpm.kelurahan
			elif self.tipe == 'pkk':
				self.kelurahan = self.pkk.kelurahan
			elif self.tipe == 'karangtaruna':
				self.kelurahan = self.karangtaruna.kelurahan
			# print self.kelurahan,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
		super(DetailUser, self).save( *args, **kwargs)

	def is_data_consistent(self):
		is_valid = True 
		err_msgs = []
		
		if not self.pk:
			if self.tipe == 'rw':
				if not self.rw:
					err_msgs.append(ValidationError("RW Harus di isi")) 
					is_valid = False 

				if DetailUser.objects.filter(rw=self.rw, lpm=None, pkk=None, karangtaruna=None):
					err_msgs.append(ValidationError("User untuk Rw Ini sudah ada")) 
					is_valid = False 
			elif self.tipe == 'lpm':
				if not self.lpm:
					err_msgs.append(ValidationError("LPM Harus di isi")) 
					is_valid = False 

				if DetailUser.objects.filter(lpm=self.lpm):
					err_msgs.append(ValidationError("User untuk LPM Ini sudah ada")) 
					is_valid = False 
			elif self.tipe == 'pkk':
				if not self.pkk:
					err_msgs.append(ValidationError("PKK Harus di isi")) 
					is_valid = False 

				if DetailUser.objects.filter(pkk=self.pkk):
					err_msgs.append(ValidationError("User untuk PKK Ini sudah ada")) 
					is_valid = False 
			elif self.tipe == 'karangtaruna':
				if not self.karangtaruna:
					err_msgs.append(ValidationError("Karang Taruna Harus di isi")) 
					is_valid = False 
				if DetailUser.objects.filter(karangtaruna=self.karangtaruna):
					err_msgs.append(ValidationError("User untuk Karang Taruna Ini sudah ada"))
					is_staff_valid = False 
			elif self.tipe == 'kelurahan':
				if not self.kelurahan:
					err_msgs.append(ValidationError("Kelurahan Harus di isi")) 
					is_valid = False 
				if DetailUser.objects.filter(kelurahan=self.kelurahan, rw=None, lpm=None, pkk=None, karangtaruna=None):
					err_msgs.append(ValidationError("User untuk kelurahan Ini sudah ada")) 
					is_valid = False 
			elif self.tipe == 'kecamatan':
				if not self.kecamatan:
					err_msgs.append(ValidationError("Kecamatan Harus di isi")) 
					is_valid = False 
				
				if DetailUser.objects.filter(kecamatan=self.kecamatan, kelurahan=None, rw=None, lpm=None, pkk=None, karangtaruna=None):
					err_msgs.append(ValidationError("User untuk Kecamatan Ini sudah ada")) 
					is_valid = False
		else:
			userdb = DetailUser.objects.get(pk=self.pk)
			if userdb.tipe != self.tipe:
				if self.tipe == 'rw':
					if not self.rw:
						err_msgs.append(ValidationError("RW Harus di isi")) 
						is_valid = False 

					if DetailUser.objects.filter(rw=self.rw, lpm=None, pkk=None, karangtaruna=None):
						err_msgs.append(ValidationError("User untuk Rw Ini sudah ada")) 
						is_valid = False 
				elif self.tipe == 'lpm':
					if not self.lpm:
						err_msgs.append(ValidationError("LPM Harus di isi")) 
						is_valid = False 

					if DetailUser.objects.filter(lpm=self.lpm):
						err_msgs.append(ValidationError("User untuk LPM Ini sudah ada")) 
						is_valid = False 
				elif self.tipe == 'pkk':
					if not self.pkk:
						err_msgs.append(ValidationError("PKK Harus di isi")) 
						is_valid = False 

					if DetailUser.objects.filter(pkk=self.pkk):
						err_msgs.append(ValidationError("User untuk PKK Ini sudah ada")) 
						is_valid = False 
				elif self.tipe == 'karangtaruna':
					if not self.karangtaruna:
						err_msgs.append(ValidationError("Karang Taruna Harus di isi")) 
						is_valid = False 
					if DetailUser.objects.filter(karangtaruna=self.karangtaruna):
						err_msgs.append(ValidationError("User untuk Karang Taruna Ini sudah ada"))
						is_staff_valid = False 
				elif self.tipe == 'kelurahan':
					if not self.kelurahan:
						err_msgs.append(ValidationError("Kelurahan Harus di isi")) 
						is_valid = False 
					if DetailUser.objects.filter(kelurahan=self.kelurahan, rw=None, lpm=None, pkk=None, karangtaruna=None):
						err_msgs.append(ValidationError("User untuk kelurahan Ini sudah ada")) 
						is_valid = False 
				elif self.tipe == 'kecamatan':
					if not self.kecamatan:
						err_msgs.append(ValidationError("Kecamatan Harus di isi")) 
						is_valid = False 
					
					if DetailUser.objects.filter(kecamatan=self.kecamatan, kelurahan=None, rw=None, lpm=None, pkk=None, karangtaruna=None):
						err_msgs.append(ValidationError("User untuk Kecamatan Ini sudah ada")) 
						is_valid = False


			
		return {'status':is_valid, "err_msgs":err_msgs}

	def clean(self):
		is_data_consistent = self.is_data_consistent()
		if not is_data_consistent['status']:
			raise ValidationError(is_data_consistent['err_msgs'])
		return super(DetailUser, self).clean()
		


class DetailUserAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'user', 'kecamatan', 'kelurahan', 'rw', 'lpm', 'pkk', 'karangtaruna', 'tipe')

class DetailUserForm(ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "data-validate":"required", 'min':'8', "data-message-required":"Please Input Username."}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Email'}))
	# first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}))
	# last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}))
	# date_joined = forms.DateField(widget = forms.DateInput(attrs={'class': 'form-control datepicker', 'data-format':"yyyy-mm-dd"}))
	is_staff = forms.BooleanField(required=False)
	is_active = forms.BooleanField(initial=True)
	class Meta:
		model = DetailUser
		fields = ['full_name', 'kecamatan', 'kelurahan', 'rw', 'lpm', 'pkk', 'karangtaruna', 'tipe']
		widgets = {
			'tipe': forms.Select(attrs={'id':'tipe', 'class': 'form-control', 'data-validate': 'required', 'data-message-required': 'Please Input Tipe'}),
		}


	



	

	# def __unicode__(self):
	# 	return self.full_name

	# def is_data_consistent(self):
	# 	is_valid = False 
	# 	err_msgs = []
	# 	try:
	# 		if self.site.customer.id != self.customer.id:
	# 			err_msgs.append(ValidationError("Site is not valid"))
	# 		else:
	# 			is_valid = True
	# 	except:
	# 		is_valid = True
	# 	return {'status':is_valid, "err_msgs":err_msgs}

	# def clean(self):
	# 	is_data_consistent = self.is_data_consistent()
	# 	if not is_data_consistent['status']:
	# 		raise ValidationError(is_data_consistent['err_msgs'])
	# 	return super(BaseModels, self).clean()
