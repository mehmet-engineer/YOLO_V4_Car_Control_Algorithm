import time

def gorev_hesapla(saniye_sayaci,toplam_sure,previous):
    durum = False
    current = time.time()
    if previous == 0:
        pass
    else:
        gecen_zaman = current - previous
        toplam_sure = toplam_sure + gecen_zaman
    if toplam_sure > 1:
        toplam_sure = 0
        saniye_sayaci = saniye_sayaci + 1
        print("1 metre ilerleniyor... Sayac: ",saniye_sayaci)
        durum = True
    previous = current
    return (durum,saniye_sayaci,toplam_sure,previous)