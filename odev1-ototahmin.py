import random
print('Bilgisayarin tahmin etmesi icin bir sayi belirleyiniz.\
Belirleyeceginiz sayi 0-100 arasinda olmalidir')
#impor tile random modulune giridikten sonra
#kullanicinin ne yapsani gerektigi belirttik ve
#while dongusu ile bunun dogrulugunu kontrol
#edecek ve eger aksilik yoksa ilk donguden cikip
#ikinciye devam edecek
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
x = random.randint(0, 100)
print('ilk tahmin', x)

while True :
#bu dongude kulanicinin belirledigi sayiyi cabuk bulabilmek
#icin programin random yapacagi araligi kisa tuttum
        tahmin = input('Tahmin edilen sayi sizin sayinizdan buyukse - ye \
    kucukse + ya eger dogruysa enter\'a  basin lutfen')
        if tahmin == '':
            print("En sonunda :)")
            break
        if tahmin == '-':

            y = random.randint((sayi-3),(sayi+3))
            print(y)
        elif tahmin == '+':
            z = random.randint((sayi - 3),(sayi+3))
            print(z)
        else:
            print('Tekrar deneyin')
#program calisiyor aksilik yok fakat bi sayiyi
#bulmaya calisirken birden fazla ayni tahmini
#aliyoruz umarim duzeltebilirim


