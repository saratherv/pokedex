from rest_framework import serializers
from core.models import Pokemon


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pokemon
        fields = ("name","typeOne","typeTwo","total","hp","attack","defense","specialAttack","specialDefense","speed","generation","isLegendary",)