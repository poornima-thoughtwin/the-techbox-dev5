# periodic.py
# from apps.dashboard.task import send_notifiction
from celery import Celery
# from .models import Employee
app = Celery('task', broker="redis://localhost:6379/0")

@app.task
def see_you():
    print("I am  poonam!")
    #send_notifiction()
    # x = Employee.objects.all()
    # for i in x:
    # 	i.name
    # 	print(i.name)
    

app.conf.beat_schedule = {
    "run-in-5-seconds-task": {
        "task": "task.see_you",
        "schedule": 5.0
    }
}
