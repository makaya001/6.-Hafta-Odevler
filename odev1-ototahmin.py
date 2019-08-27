import random
print('Bilgisayarin tahmin etmesi icin bir sayi belirleyiniz.\
Belirleyeceginiz sayi 0-100 arasinda olmalidir')
#impor tile random modulune giridikten sonra
#kullanicinin ne yapsani gerektigi belirttik ve
#while dongusu ile bunun dogrulugunu kontrol
#edecek ve eger aksilik yoksa ilk donguden cikip
#ikinciye devam edecek
ustsinir=101
altsinir=0
while True :

    try:
        sayi = input('Lutfen tahmin edilmesi gereken sayiyi belirtiniz :')

        sayi=int(sayi)
        if sayi<0 or sayi>100 :
            print('Lutfen sayiyi 0 ile 100 arasinda belirleyin!')
            continue
        else :
            print('Sayiniz belirlendi')

            break

    except ValueError :
        print('Lutfen sadece tam sayi giriniz!')

while True :
    try:

        x = random.randint(altsinir, ustsinir)
        print('Tahmin :',x)
    #bu dongude kulanicinin belirledigi sayiyi cabuk bulabilmek
    #icin programin random yapacagi araligi kisa tuttum
        tahmin = input('Tahmin edilen sayi sizin sayinizdan buyukse - ye \
    kucukse + ya eger dogruysa enter\'a  basin lutfen')
        if tahmin == '':
            print("En sonunda :)")
            break
        if tahmin == '-':
            ustsinir=x-1
        elif tahmin == '+':
            altsinir=x+1
        else:
            print('Tekrar deneyin')
    except:
        print('Birseyler ters gitti lutfen tekrar deneyin')
        break





