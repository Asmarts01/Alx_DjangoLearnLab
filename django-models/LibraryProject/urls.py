# Edit relationship_app/urls.py to include URL patterns that route to the newly created views. 
# Make sure to link both the function-based and class-based views.

"""LibraryProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from relationship_app.views import list_books, LibraryDetailView, list_books_text
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', list_books, name='list_books'),
    path('books/text/', list_books_text, name='list_books_text'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]
