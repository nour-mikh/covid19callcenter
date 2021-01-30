from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("behalf", views.behalf, name = "behalf"),
    path("suspected", views.suspected, name = "suspected"),
    path("test", views.test, name = "test"),
    path("risk", views.risk, name = "risk"),
    path("yessymp", views.yessymp, name = "yessymp"),
    path("nosymp", views.nosymp, name = "nosymp"),
    path("interact", views.interact, name = "interact"),
    path("symptoms", views.symptoms, name = "symptoms"),
    path("record", views.record, name = "record"),
    path("common", views.common, name = "common")
]