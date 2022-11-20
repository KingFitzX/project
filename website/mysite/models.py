from django.db import models
import uuid

# Create your models here.
class ParamSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    country_alpha_cares_about = models.FloatField()
    country_alpha_no_nukes = models.FloatField()
    country_alpha_agression = models.FloatField()
    country_alpha_international_rep = models.FloatField()
    country_alpha_population = models.FloatField()

    country_beta_cares_about = models.FloatField()
    country_beta_no_nukes = models.FloatField()
    country_beta_agression = models.FloatField()
    country_beta_international_rep = models.FloatField()
    country_beta_population = models.FloatField()

    provocation = models.FloatField()

    ai_result = models.FloatField()

    def genParamSet(self, scenario):
        self.id = uuid.uuid4()

        self.country_alpha_cares_about = scenario["country_alpha"]["cares_about"]
        self.country_alpha_no_nukes = scenario["country_alpha"]["no_nukes"]
        self.country_alpha_agression = scenario["country_alpha"]["agression"]
        self.country_alpha_international_rep = scenario["country_alpha"]["international_rep"]
        self.country_alpha_population = scenario["country_alpha"]["population"]

        self.country_beta_cares_about = scenario["country_beta"]["cares_about"]
        self.country_beta_no_nukes = scenario["country_beta"]["no_nukes"]
        self.country_beta_agression = scenario["country_beta"]["agression"]
        self.country_beta_international_rep = scenario["country_beta"]["international_rep"]
        self.country_beta_population = scenario["country_beta"]["population"]

        self.provocation = scenario["country_alpha"]["provocation"]

        self.ai_result = 0.0

class Result(models.Model):
    params = models.ForeignKey(ParamSet, models.CASCADE)
    pressed = models.BooleanField()