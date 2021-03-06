from django.urls import path
from zayavki.views import ZayavkaUpdate, ZayavkaDetail, ZayavkaCreate, ZayavkaFilterList, process_command, add_comment



app_name = "zayavki"

urlpatterns = [
    path("", ZayavkaFilterList.as_view(), name="zayavki_list"),
    path('<str:filter>/', ZayavkaFilterList.as_view(), name='zayavki_filter_list'),    
    path("create", ZayavkaCreate.as_view(), name="zayavka-create"),
    path("<int:pk>", ZayavkaDetail.as_view(), name="zayavka-detail"),
    path("<int:pk>/update", ZayavkaUpdate.as_view(), name="zayavka-update"),
    path("command", process_command, name="zayavka-command"),
    path("add_comment", add_comment, name="add-comment"),
    # path("return_to_prev_page", return_to_prev_page, name="return_to_prev_page")
    
    
    
]
