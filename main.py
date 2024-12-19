import tkinter as tk
from tkinter import scrolledtext, messagebox
from SPARQLWrapper import SPARQLWrapper, JSON

# Fonction pour exécuter une requête SPARQL
def run_sparql_query():
    query = query_text.get("1.0", tk.END).strip()
    if not query:
        messagebox.showwarning("Attention", "Veuillez entrer une requête SPARQL.")
        return

    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)

    try:
        results = sparql.query().convert()
        output_text.delete("1.0", tk.END)  # Effacer les résultats précédents
        for result in results["results"]["bindings"]:
            output_text.insert(tk.END, f"{result}\n")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {e}")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Requêtes SPARQL avec DBpedia")

# Zone pour entrer la requête SPARQL
query_label = tk.Label(root, text="Entrez votre requête SPARQL :")
query_label.pack(pady=5)

query_text = scrolledtext.ScrolledText(root, width=60, height=10)
query_text.pack(pady=5)

# Bouton pour exécuter la requête
run_button = tk.Button(root, text="Exécuter la requête", command=run_sparql_query)
run_button.pack(pady=5)

# Zone pour afficher les résultats
output_label = tk.Label(root, text="Résultats :")
output_label.pack(pady=5)

output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack(pady=5)

# Lancer la boucle principale
root.mainloop()