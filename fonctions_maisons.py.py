import pandas as pd

def extraire_la_premiere_lettre(serie):
  # Récupère une Série en argument
  # Retourne une DataFrame (compatibilité col. Trans)
  return pd.DataFrame(serie.str[0])