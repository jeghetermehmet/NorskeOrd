from norsk_ord import NorskOrd

årstider = [NorskOrd("høst"),
        NorskOrd("vinter"),
        NorskOrd("vår"),
        NorskOrd("sommer")]

for årstid in årstider:
    årstid.skriv_ord()
    if årstid.sjekk_norske():
        årstid.fjern_norske()

for årstid in årstider:
    årstid.skriv_ord()