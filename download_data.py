from module import RCMmodel
import urllib.request; urllib.request.urlretrieve(url, "fichier.nc")

dictionnaries of models
#model has to be among : CNRM-ESM2-1, EC-Earth3-Veg, EC-Earth3, IPSL-CM6A-LR, MIROC6, MPI-ESM1-2-HR, NorESM2-MM
#simu among
data = {"CNRM-ESM2-1" : ["HCLIM43_ALADIN", "RAGMO23E"],
                "EC-Earth3-Veg" : ["RACMO23E", ""],
                "EC-Earth3" : ["HCLIM43_ALADIN", "RACMO23E"],
                "IPSL-CM6A-LR" : ["HCLIM43_ALADIN",],
                "MIROC6" : ["HCLIM43_ALADIN"],
                "MPI-ESM1-2-HR" : ["HCLIM43_ALADIN","RACMO23E"],
                "NorESM2-MM" : ["HCLIM43_ALADIN", "RACMO23E"]}

Carbon_emmission = ["ssp555"]



model1_tas_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasAdjust/version-hackathon-102025/tasAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model1_tasmin_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasminAdjust/version-hackathon-102025/tasminAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model1_tasmax_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasmaxAdjust/version-hackathon-102025/tasmaxAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model1_huss_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/hussAdjust/version-hackathon-102025/hussAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model1_rsds_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rsdsAdjust/version-hackathon-102025/rsdsAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model1_rlds_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rldsAdjust/version-hackathon-102025/rldsAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model1_pr_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/prAdjust/version-hackathon-102025/prAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model1_sfcWind_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/sfcWindAdjust/version-hackathon-102025/sfcWindAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"

model1_tas_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasAdjust/version-hackathon-102025/tasAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model1_tasmin_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasminAdjust/version-hackathon-102025/tasminAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model1_tasmax_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasmaxAdjust/version-hackathon-102025/tasmaxAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model1_huss_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/hussAdjust/version-hackathon-102025/hussAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model1_rsds_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rsdsAdjust/version-hackathon-102025/rsdsAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model1_rlds_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rldsAdjust/version-hackathon-102025/rldsAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model1_pr_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/prAdjust/version-hackathon-102025/prAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model1_sfcWind_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/CNRM-ESM2-1/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/sfcWindAdjust/version-hackathon-102025/sfcWindAdjust_FR-Metro_CNRM-ESM2-1_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"

model2_tas_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasAdjust/version-hackathon-102025/tasAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model2_tasmin_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasminAdjust/version-hackathon-102025/tasminAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model2_tasmax_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasmaxAdjust/version-hackathon-102025/tasmaxAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_20150101-21001231.nc"
model2_huss_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/hussAdjust/version-hackathon-102025/hussAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model2_rsds_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rsdsAdjust/version-hackathon-102025/rsdsAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model2_rlds_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rldsAdjust/version-hackathon-102025/rldsAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model2_pr_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/prAdjust/version-hackathon-102025/prAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"
model2_huss_ssp585 = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/sfcWindAdjust/version-hackathon-102025/sfcWindAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_20150101-21001231.nc"

model2_tas_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasAdjust/version-hackathon-102025/tasAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model2_tasmin_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasminAdjust/version-hackathon-102025/tasminAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model2_tasmax_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/tasmaxAdjust/version-hackathon-102025/tasmaxAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-1985-2014_day_19500101-20141231.nc"
model2_huss_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/hussAdjust/version-hackathon-102025/hussAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model2_rsds_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rsdsAdjust/version-hackathon-102025/rsdsAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model2_rlds_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/rldsAdjust/version-hackathon-102025/rldsAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model2_pr_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/prAdjust/version-hackathon-102025/prAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"
model2_huss_histo = "https://object.files.data.gouv.fr/meteofrance-drias/SocleM-Climat-2025/RCM/EURO-CORDEX/EUR-12/NorESM2-MM/r1i1p1f2/CNRM-ALADIN64E1/ssp585/day/sfcWindAdjust/version-hackathon-102025/sfcWindAdjust_FR-Metro_NorESM2-MM_ssp585_r1i1p1f2_CNRM-MF_CNRM-ALADIN64E1_v1-r1_MF-CDFt-ANASTASIA-SAFRAN-1985-2014_day_19500101-20141231.nc"


import urllib.request
from pathlib import Path

# -------------------------------
# 1) Dictionnaire de tous les fichiers à télécharger
# -------------------------------
files_to_download = {
    # MODEL 1 - SSP585
    "M1_tas_ssp585"    : model1_tas_ssp585,
    "M1_tasmin_ssp585" : model1_tasmin_ssp585,
    "M1_tasmax_ssp585" : model1_tasmax_ssp585,
    "M1_huss_ssp585"   : model1_huss_ssp585,
    "M1_rsds_ssp585"   : model1_rsds_ssp585,
    "M1_rlds_ssp585"   : model1_rlds_ssp585,
    "M1_pr_ssp585"     : model1_pr_ssp585,
    "M1_sfcWind_ssp585": model1_sfcWind_ssp585,

    # MODEL 1 - HISTORIQUE
    "M1_tas_histo"     : model1_tas_histo,
    "M1_tasmin_histo"  : model1_tasmin_histo,
    "M1_tasmax_histo"  : model1_tasmax_histo,
    "M1_huss_histo"    : model1_huss_histo,
    "M1_rsds_histo"    : model1_rsds_histo,
    "M1_rlds_histo"    : model1_rlds_histo,
    "M1_pr_histo"      : model1_pr_histo,
    "M1_sfcWind_histo" : model1_sfcWind_histo,

    # MODEL 2 - SSP585
    "M2_tas_ssp585"    : model2_tas_ssp585,
    "M2_tasmin_ssp585" : model2_tasmin_ssp585,
    "M2_tasmax_ssp585" : model2_tasmax_ssp585,
    "M2_huss_ssp585"   : model2_huss_ssp585,
    "M2_rsds_ssp585"   : model2_rsds_ssp585,
    "M2_rlds_ssp585"   : model2_rlds_ssp585,
    "M2_pr_ssp585"     : model2_pr_ssp585,
    "M2_sfcWind_ssp585": model2_sfcWind_ssp585,

    # MODEL 2 - HISTORIQUE
    "M2_tas_histo"     : model2_tas_histo,
    "M2_tasmin_histo"  : model2_tasmin_histo,
    "M2_tasmax_histo"  : model2_tasmax_histo,
    "M2_huss_histo"    : model2_huss_histo,
    "M2_rsds_histo"    : model2_rsds_histo,
    "M2_rlds_histo"    : model2_rlds_histo,
    "M2_pr_histo"      : model2_pr_histo,
    "M2_sfcWind_histo" : model2_sfcWind_histo,
}

# -------------------------------
# 2) Dossier de sortie
# -------------------------------
outdir = Path("DATA")
outdir.mkdir(exist_ok=True)

# -------------------------------
# 3) Téléchargement + vérification
# -------------------------------
for label, url in files_to_download.items():
    outfile = outdir / f"{label}.nc"
    print(f"⏬ Téléchargement : {label}")

    try:
        urllib.request.urlretrieve(url, outfile)
    except Exception as e:
        print(f"❌ Erreur téléchargement {label} : {e}")
        continue

    # Vérification
    if outfile.exists() and outfile.stat().st_size > 0:
        print(f"✅ OK : {outfile.name}")
    else:
        print(f"❌ Fichier vide ou manquant : {outfile.name}")
