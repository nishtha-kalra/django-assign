from polls.models import *
from django.contrib.auth import *

class RegisterHelp(object):

    @staticmethod
    def add_details(name, email, password, re_password):
        obj = register()
        obj.name = name
        obj.email = email
        obj.password = password
        obj.re_password = re_password
        obj.save()
        return 0

    @staticmethod
    def validate_details(name, password):
        obj = register.objects.get(name=name, password=password)
        return obj

class DirectoryHelp(object):

    @staticmethod
    def add_to_dir(dir_name, phone_number, alt_number, address):
        dir = directory()
        dir.dir_name = dir_name
        dir.phone_number = phone_number
        dir.alt_number = alt_number
        dir.address = address
        dir.save()
        return 0

    @staticmethod
    def get_details():
        return directory.objects.all()

    @staticmethod
    def delete(id):
        return directory.objects.filter(id=id).delete()

    @staticmethod
    def get_entry_details(id):
        return directory.objects.get(pk=id)

    @staticmethod
    def update(id, ename, phone_no, alt_no, addrs):
        entry = directory.objects.get(pk=id)
        entry.dir_name = ename
        entry.phone_number = phone_no
        entry.address = addrs
        entry.alt_number = alt_no
        entry.save()
        return 0






