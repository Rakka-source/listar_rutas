from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .modelos_externos import ShopOrder, ShopOrderCartItems, ShopCartitem, ShopProduct

class CustomLoginView(LoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True  # Redirigir a los usuarios ya autenticados
    def get_success_url(self):
        # Redirige a la ruta base
        return '/'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Página después del logout

# Create your views here.


@login_required
def vista_principal(request):
    # Obtener todas las órdenes
    ordenes = ShopOrder.objects.using('external_db').all()

    # Crear una estructura para pasarla al template
    datos = []
    for orden in ordenes:
        # Obtener los ítems relacionados con la orden
        order_items = ShopOrderCartItems.objects.using('external_db').filter(order=orden)
        productos = []
        for item in order_items:
            cartitem = ShopCartitem.objects.using('external_db').get(id=item.cartitem.id)
            producto = ShopProduct.objects.using('external_db').get(id=cartitem.product.id)
            productos.append({
                'nombre': producto.name,
                'cantidad': cartitem.quantity
            })

        datos.append({
            'id': orden.id,
            'fecha_creada': orden.created_at,
            'direccion_envio': orden.shipping_address,
            'productos': productos,
        })

    # Renderizar la plantilla combinada
    return render(request, 'usuarios/principal.html', {
        'usuario': request.user,
        'datos': datos
    })