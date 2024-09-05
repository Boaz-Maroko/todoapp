from django.urls import path
from .views import tasks_view, save_tasks

# app name  is used to namespace the apps so 
# calls to its URLs aren't ambigous

app_name = "tasks"

# urlpatterns match requests from the client to respective
# views in the server

urlpatterns = [
    path("", tasks_view, name="home"),
    path("create", save_tasks, name="create"),
    # path("done/<int:task_id>/", done_task, name="done")
]