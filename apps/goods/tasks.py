from celery import task

@task
def say_hello(name):
    content = "hello {name},welcome django".format(name=name)
    return content