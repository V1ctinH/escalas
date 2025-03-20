from django.contrib import admin
from .models import Usuario, Evento, Escala

class EscalaInline(admin.TabularInline):
    model = Escala
    extra = 0



class UsuarioAdmin(admin.ModelAdmin): 
    #list_display = ('username', 'first_name', 'last_name', 'telefone', 'endereco', 'email', 'funcao',)
    def get_list_display(self, request):
        gestor_list_display=('username', 'first_name', 'last_name', 'telefone', 'endereco', 'email', 'funcao',)
        admin_list_display=('username', 'first_name', 'last_name', 'telefone', 'endereco', 'email', 'funcao', 'is_staff',)
        if request.user.is_superuser:
            return admin_list_display
        elif request.user.groups.filter(name='Gestores').exists():
            return gestor_list_display
        else:
            return super().get_list_display(request)
    
    search_fields = ('first_name', 'last_name', 'username', 'telefone',) 

    def get_list_filter(self, request):
        
        gestor_list_filter=('funcao',)
        admin_list_filter=('is_staff', 'funcao',)
        if request.user.is_superuser:
            return admin_list_filter
        elif request.user.groups.filter(name='Gestores').exists():
            return gestor_list_filter
        else:
            return super().get_list_filter(request)
   

    def get_fieldsets(self, request, obj = None):
        fieldsets = super().get_fieldsets(request, obj)
        if request.user.is_superuser:
            return fieldsets
       
        my_fieldsets = (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'telefone', 'endereco', 'funcao', 'is_active', 'is_superuser', 'is_staff',)
        })
        return (my_fieldsets,)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        all_users = super().get_queryset(request)
        simple_users = Usuario.objects.exclude(is_superuser=True)

        if request.user.is_superuser:
            return all_users
        elif request.user.groups.filter(name='Gestores').exists():
            return simple_users
        else:
            return queryset
        


class EventoAdmin(admin.ModelAdmin):
    inlines = [EscalaInline]

    @admin.display(description='Data')
    def data_formatada(self, obj):
        return obj.data.strftime('%d-%m-%Y')
   
    @admin.display(description='Participantes')
    def numero_participantes(self, obj):
        return obj.participantes.count()
    
    list_display = ('titulo', 'data_formatada', 'numero_participantes')
    search_fields = ('titulo',)


class EscalaAdmin(admin.ModelAdmin):
    list_display = ('evento',)


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Evento, EventoAdmin)
#admin.site.register(Escala, EscalaAdmin)