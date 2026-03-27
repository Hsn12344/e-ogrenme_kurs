from django.db import models
from .users import CustomUser
from django.utils.text import slugify  # Slug oluşturmak için


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(unique=True, blank=True)  # URL için
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self): return self.name

    class Meta: verbose_name_plural = "Kategoriler"


class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kurs Başlığı")
    slug = models.SlugField(unique=True, blank=True)  # URL için
    description = models.TextField(verbose_name="Açıklama")

    # related_name='taught_courses' yaparak öğrenci kayıtlarından ayırdık
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='taught_courses')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='courses')

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # EKRAN İÇİN KRİTİK: Kursun kapak fotoğrafı
    image = models.ImageField(upload_to='course_images/', null=True, blank=True, verbose_name="Kapak Resmi")

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug: self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self): return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)

    class Meta: ordering = ['order']  # Modüller sırasına göre dizilsin

    def __str__(self): return f"{self.course.title} - {self.title}"


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    video_url = models.URLField(blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, help_text="Örn: 10:45")  # Ekstra bilgi

    def __str__(self): return self.title