from django.contrib import admin
# Tek bir yerden toplu import daha temizdir
from .models import (
    CustomUser, Category, Course, Module,
    Lesson, Enrollment, LessonProgress,
    Review, Certificate, SystemLog
)

# 1. Modülleri kursun içinde satır içi (inline) göstermek için
class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

# 2. CustomUser Admin Kaydı
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    list_filter = ('role',)
    search_fields = ('username', 'email')

# 3. Course Admin Kaydı (HATA BURADAYDI)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'price', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'description')

# 4. Diğer Modülleri Kaydet (Burada Course, CustomUser gibi yukarıda @ ile kaydettiklerini SİLDİM)
admin.site.register(Category)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Enrollment)
admin.site.register(LessonProgress)
admin.site.register(Review)
admin.site.register(Certificate)
admin.site.register(SystemLog)