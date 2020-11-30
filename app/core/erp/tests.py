# Create your tests here.

from config.wsgi import *

from core.erp.models import Type, Employee

# vamos a hacer un Listar

# Listar
# Select * from Tabla

# query = Type.objects.all()
# print(query)

# Insersion

# t = Type()
# t.name = 'Perejil'
# t.save()

#t = Type(name='Perezoso').save()

# Edicion

# t = Type.objects.get(id=1)
# print(t.name)

# t = Type.objects.get(pk=1)
# print(t.name)


# Eliminacion

# t = Type.objects.get(id=1)
# t.delete()

# t = Type.objects.get(id=3)
# t.delete()

# try:
    # t = Type.objects.get(id=2)
    # t.name = 'Presidente'
    # t.save()
# except Exception as e:
    # print(e)


# t = Type.objects.get(id=2)
# t.delete()

#t = Type(name='prueba').save()

#t = Type(name='viba').save()
# t = Type(name='hola').save()

# obj = Type.objects.filter(name__contains='pre')
# print(obj)

# Si tenemos Presidente Primera en mayusculas
# usamos icontains

# obj = Type.objects.filter(name__icontains='terry')
# obj = Type.objects.filter(name__startswith='p')
# obj = Type.objects.filter(name__startswith='p')
# obj = Type.objects.filter(name__endswith='a')
# obj = Type.objects.filter(name__in=['viba','hola'])
# obj = Type.objects.filter(name__in=['viba','hola']).count()
# obj = Type.objects.filter(name__icontains='terry').query
# obj = Type.objects.filter(name__contains='terry').query
# obj = Type.objects.filter(name__endswith='a').exclude(id=5)
# print(obj)

# Employee.objects.filter(type_id=1)
# obj = Employee.objects.filter(type_id=1)

# for i in Type.objects.filter(name__endswith='a')
    # print(i.name)


