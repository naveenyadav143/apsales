import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import TorqueData


@csrf_exempt
def receive_torque(request):
    if request.method == "POST":
        data = json.loads(request.body)

        TorqueData.objects.create(
            torque=data["torque"]   # ✅ only torque
        )

        return JsonResponse({"status": "success"})

def get_torque_data(request):
    data = TorqueData.objects.order_by("timestamp")
    response = []

    for d in data:
        response.append({
            "torque": d.torque,
            "time": d.timestamp.strftime("%H:%M:%S")
        })

    return JsonResponse(response, safe=False)


def dashboard(request):
    return render(request, "torque/dashboard.html")
