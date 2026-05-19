import math

MATERIALS = {
    "aluminium": 0.05,
    "timbal": 0.15,
    "kayu": 0.02,
    "bata": 0.08,
    "beton": 0.12
}

def efek_jarak(I0: float, jarak: float) -> float:
    return I0 / (jarak ** 2)

def efek_shielding(I0: float, material: str, ketebalan: float) -> float:
    mu = MATERIALS[material]
    return I0 * math.exp(-mu * ketebalan)

def efek_waktu(intensitas: float, waktu: int) -> float:
    return intensitas * waktu

def simulasi_eksterna(I0: float, jarak: float, waktu: int, material: str, ketebalan: float):
    intensitas_jarak = efek_jarak(I0, jarak)
    intensitas_shield = efek_shielding(intensitas_jarak, material, ketebalan)
    dosis = efek_waktu(intensitas_shield, waktu)

    print("\n=== HASIL SIMULASI EKSTERNA ===")
    print(f"Intensitas awal: {I0} mSv")
    print(f"Jarak: {jarak} m")
    print(f"Material: {material}, Ketebalan: {ketebalan} cm")
    print(f"Waktu paparan: {waktu} detik")
    print(f"Intensitas setelah jarak: {intensitas_jarak:.2f} mSv")
    print(f"Intensitas setelah shielding: {intensitas_shield:.2f} mSv")
    print(f"Dosis radiasi: {dosis:.2f} mSv")

    if dosis < 50:
        status = "Aman"
    elif dosis < 200:
        status = "Waspada"
    else:
        status = "Bahaya!"
    print(f"Status: {status}")
