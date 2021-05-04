"""
Django settings for tech_box project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import sys
import django_heroku
# import pdb; pdb.set_trace()
PROJECT_ROOT = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
from pathlib import Path
from unipath import Path
PROJECT_DIR = Path(__file__).ancestor(3)
PROJECT_APPS = Path(__file__).ancestor(2)

sys.path.insert(0, Path(PROJECT_APPS, 'apps'))


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@pj1fu)7b8(z!2#m@=5t+bk#q!$bl3fej$ce33(r#-9*1eu6m$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*','127.0.0.1','localhost:8000','techbox-dev5.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'apps',
    'apps.dashboard',
    'authentication',
    'celery',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    # 'payments.apps.PaymentsConfig', # new

]


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'tech_box.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'tech_box.wsgi.application'

# CACHE_MIDDLEWARE_ALIAS=
# CACHE_MIDDLEWARE_KEY_PRIFIX=

CACHE_MIDDLEWARE_SECONDS=5

CACHES = {
   'default': {
      'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
      'LOCATION': 'techbox_caches',
   }
}

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'facebook_db',
#         'USER': 'postgres',
#         'PASSWORD' : 'root',
#         'HOST' : 'localhost',
#         'PORT' : 5432,
    
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated'
    # ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ]
}
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'#DJNAGO BYdedult
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

# USE_TZ = True#bydefult
USE_TZ = False




STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL ="/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,"media")
LOGIN_REDIRECT_URL="/index/"
#.................................email send by message

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER ='poornima.thoughtwin@gmail.com'
EMAIL_HOST_PASSWORD ='poornimawin123@'
EMAIL_USE_TLS = True

def MAIL(userMail,Name):
    from django.http import HttpResponse,HttpResponseRedirect  
    import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    # user = User.objects.get(email = request.user)

    sender_email = "poornima.thoughtwin@gmail.com"
    receiver_email = userMail
    password = 'poornimawin123@'

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = f"hello {userMail}, welcome techbox You have borrowed one asset{Name}"
    html = f"""\
    <html>
    <body>
        <p>hello {userMail}<br>
        welcome techbox<br>
        You have borrowed one asset {Name} Thankyou
        </p>
    </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return HttpResponse("True")



BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

# sender_email = "themindzworld@gmail.com"
# receiver_email = userMail
# password = 'TeamWork@mindzworld@'



import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
sentry_sdk.init(
    dsn="https://fb0f5788be1646b99542892f869a6308@o570556.ingest.sentry.io/5735935",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)



STRIPE_PUBLISHABLE_KEY = 'pk_test_51ImuToSJYQKegLOCoF1Ltm4634GEAmvh1irwNcJo5PVGiJ0cN3SlGoXLY5pQyBGXRkzXRrfrf1w216UbFdm0VjBC00ZpWGo0Wz'
STRIPE_SECRET_KEY = 'sk_test_51ImuToSJYQKegLOCax5wBYbgM3zWITyfUKLrDuK9A1G2DV0mlQyILpNX7Lgx9bDgpVsYdUdSTgGjZCj3z6bZdKp600dlSvv0Xn'