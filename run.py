from django.core.management import call_command

call_command("migrate")
call_command("createsuperuser", interactive=False, username="admin", email="gcmadeacc82@gmail.com")
