from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mythingworks.views.home', name='home'),
    # url(r'^mythingworks/', include('mythingworks.foo.urls')),
    #url(r'^$',include(app_urls)),
    # Uncomment the admin/doc line below to enable admin documentation:
  	url(r'^$',views.catalog,name="catalog"),
  	url(r'^cart/$',views.cart,name="cart"),
  	url(r'^cart/remove/$',views.removefromcart,name="remove"),
  	url(r'^cart/checkout/$',views.checkout,name="checkout"),
  	url(r'^cart/checkout/complete/$',views.completeOrder,name="complete_order"),
  	url(r'^admin_login$',views.adminLogin,name="admin_login"),
  	url(r'^admin_panel$',views.adminDashboard,name='admin')

  )
