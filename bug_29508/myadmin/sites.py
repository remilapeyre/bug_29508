from django.contrib.admin.sites import AdminSite
from .forms import AdminAuthenticationForm


class MyAdminSite(AdminSite):
    login_form = AdminAuthenticationForm


site = MyAdminSite()
