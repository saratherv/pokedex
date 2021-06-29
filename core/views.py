from django.shortcuts import render
import pandas as pd
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.decorators import APIView
from rest_framework.response import Response
from core.models import Pokemon
from core.serializers import PokemonSerializer


# Create your views here.

class PokeMonView(CreateAPIView, ListAPIView):
    """
    API to fetch pokemons from CSV and return list
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        
        df = pd.read_csv("Pokemon.csv")
        for index, row in df.iterrows():
            Pokemon.objects.update_or_create(
                name = row["Name"],
                defaults={
                    "typeOne" : row["Type 1"],
                    "typeTwo" : row["Type 2"],
                    "total" : row["Total"],
                    "hp" : row["HP"],
                    "attack" : row["Attack"],
                    "defense" : row["Defense"],
                    "specialAttack" : row["Sp. Atk"],
                    "specialDefense" : row["Sp. Def"],
                    "speed" : row["Speed"],
                    "generation" : row["Generation"],
                    "isLegendary" : row["Legendary"],
                }
            )
        return Response({"sucess" : True, "code": 200, "message" : "Saved Data"})
    
    def get(self, request):
        pokemonData = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemonData, many=True)
        return Response({"success" : True, "code" : 200, "data" : serializer.data})


class LegendaryPokemonView(ListAPIView):
    """
    API to return list of legendary pokemons
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        pokemonData = Pokemon.objects.filter(isLegendary=True)
        serializer = PokemonSerializer(pokemonData, many=True)
        return Response({"success" : True, "code" : 200, "data" : serializer.data})


class HomeTemplateView(APIView):

    """
    Rendering data on frontend
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        pokemonData = Pokemon.objects.all()
        serializer = PokemonSerializer(pokemonData, many=True)
        return render(request, 'home.html', {"pokemons" : serializer.data})


class LegendaryTemplateView(APIView):

    """
    Rendering data on frontend
    """
    permission_classes = (AllowAny,)

    def get(self, request):
        pokemonData = Pokemon.objects.filter(isLegendary=True)
        serializer = PokemonSerializer(pokemonData, many=True)
        return render(request, 'legendary.html', {"pokemons" : serializer.data})
