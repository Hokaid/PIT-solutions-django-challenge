import requests
from django.core.management.base import BaseCommand
from planets.models import Planet

# Use the working GraphQL endpoint
GRAPHQL_URL = "https://swapi-graphql.eskerda.vercel.app/"
QUERY = '''
{
  allPlanets {
    planets {
      name
      population
      terrains
      climates
    }
  }
}
'''

class Command(BaseCommand):
    help = "Fetch planets from SWAPI GraphQL"

    def handle(self, *args, **kwargs):
        response = requests.post(GRAPHQL_URL, json={"query": QUERY})
        data = response.json()
        if "data" not in data:
            self.stderr.write(self.style.ERROR(f"Error in response: {data}"))
            return

        planets = data["data"]["allPlanets"]["planets"]

        for p in planets:
            pop = p["population"]
            try:
                pop = int(pop)
            except (ValueError, TypeError):
                pop = None

            Planet.objects.update_or_create(
                name=p["name"],
                defaults={
                    "population": pop,
                    "terrains": p["terrains"],
                    "climates": p["climates"],
                },
            )
        self.stdout.write(self.style.SUCCESS(f"Loaded {len(planets)} planets!"))
