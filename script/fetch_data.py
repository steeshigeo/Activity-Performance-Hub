import os
import json
import requests

GAS_API_URL = "https://script.google.com/macros/s/AKfycbxAAdUZ1LQfD6GOnGFf364ixUlyNT_FVwb2lZUcIi4sCSIBmmluz1KkyQlFIEPeWHipHA/exec"

def fetch_and_save():
    print("Fetching data dari Google Apps Script Web App...")
    response = requests.get(GAS_API_URL, timeout=60)
    response.raise_for_status()
    
    data = response.json()
    
    # Pastikan folder data ada
    os.makedirs("data", exist_ok=True)
    
    # Simpan sebagai file JSON lokal
    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print("Berhasil memperbarui data/data.json!")

if __name__ == "__main__":
    fetch_and_save()
