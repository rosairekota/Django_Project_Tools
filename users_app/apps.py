from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'users_app'

    def ready(self):
    	import users_app.signals
