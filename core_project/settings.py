import os
from pathlib import Path
from dotenv import load_dotenv

# 1. Klasör Yolları ve Çevresel Değişkenler
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

# GÜVENLİK NOTU: Gerçek projede bunu .env içine almalısın
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
ALLOWED_HOSTS = []

# 2. Uygulamalar
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lms_app',  # Senin uygulaman
]

# 3. Ara Katmanlar (Middleware) - Hataları çözen kısım
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core_project.urls'

# 4. Şablonlar (Templates) - Admin hatasını çözen kısım
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'lms_app' / 'templates'], # Şablon klasörün
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core_project.wsgi.application'

# 5. AWS RDS (MSSQL) Veritabanı
DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT', '1433'),
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'extra_params': 'Connection Timeout=30;',
        },
    }
}

# 6. Statik Dosyalar (İstediğin düzeltme burada)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "lms_app" / "static",
]
# Canlıya geçişte (collectstatic) dosyaların toplanacağı yer
STATIC_ROOT = BASE_DIR / "staticfiles"

# 7. Diğer Önemli Ayarlar
AUTH_USER_MODEL = 'lms_app.CustomUser'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]