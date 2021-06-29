from django.conf.urls import url, include
from django.urls import reverse
from core.views import PokeMonView, LegendaryPokemonView, HomeTemplateView, LegendaryTemplateView

urlpatterns = [
    url(r'^api/v1/pokemon/$', PokeMonView.as_view()),
    url(r'^api/v1/legendaryPokemon/$', LegendaryPokemonView.as_view()),
    url(r'^api/v1/home/$', HomeTemplateView.as_view()),
    url(r'^api/v1/legendary/$', LegendaryTemplateView.as_view()),
]
