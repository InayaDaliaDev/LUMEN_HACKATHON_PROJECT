# test_supabase.py — à lancer en local avec `python test_supabase.py`
from supabase import create_client

url = "PUT UR KEY"      # ton Project URL
key = "PUT UR KEY"# ta clé "anon public"

try:
    client = create_client(url, key)
    response = client.table("ping_test").select("*").execute()
    print("✅ Connexion réussie, réponse brute :", response)
except Exception as e:
    print("❌ Erreur :", e)