from django.urls import path
from .views import receive_torque, get_torque_data,dashboard

urlpatterns = [
    path("api/torque/", receive_torque),      # POST
    path("api/torque/data/", get_torque_data), # GET
    path("", dashboard),

]
