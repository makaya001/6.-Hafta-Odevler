import random
sekil = [['-','-','-'],
['-','-','-'],
['-','-','-']]
for i in sekil:
    print(*i)
kazanmadurumu = [[[0, 0], [1, 0], [2, 0]],#+
[[0, 1], [1, 1], [2, 1]],#+
[[0, 2], [1, 2], [2, 2]],#+
[[0, 0], [0, 1], [0, 2]],#+
[[1, 0], [1, 1], [1, 2]],#+
[[2, 0], [2, 1], [2, 2]],#+
[[0, 0], [1, 1], [2, 2]],#+
[[0, 2], [1, 1], [2, 0]]]
print('\ncikmak icin q\'ya basiniz:')
sayac=1
ofaktor=[]
xfaktor=[]
print('\ncikmak icin q\'ya basiniz:')
#oyun tahtasinin seklini belirledik ve kazanma durumu
#icin gerekli kosulu bir degiskene atadik ve donguye girdik
while True :
    try:
        if sayac%2==0 :
            isaret='O'
            if isaret=='O' :
#kurdugumuz sayac sayesinde sira her O ya gelme durumunda
#oncelikle kazanma durumu olusmasi durumunda program oyunu
#kazanabilecek durumunun olusmasi durumunda
#son hamlesini oyunu kazanmak icin yapmis olacak
                for i in kazanmadurumu :
                    for x in ofaktor :
                        if len(x)==len(i)-1 :
                            if sekil[0][0]=='O' and sekil[0][1]=='O' :
                                if sekil[0][2]=='-':
                                    sekil[0][2]='O'
                            elif sekil[0][0]=='O' and sekil[0][2]=='O':
                                if sekil[0][1]=='-':
                                    sekil[0][1] = 'O'
                            elif sekil[0][1]=='O' and sekil[0][2]=='O' :
                                if sekil[0][0]=='-':
                                    sekil[0][0] = 'O'
                            elif sekil[1][0]=='O' and sekil[1][1]=='O':
                                if sekil[1][2]=='-':
                                    sekil[1][2]='O'
                            elif sekil[1][1]=='O' and sekil[1][2]=='O':
                                if sekil[1][0]=='-':
                                    sekil[1][0]='O'
                            elif sekil[1][0]=='O' and sekil[1][2]=='O' :
                                if sekil[1][1]=='-':
                                    sekil[1][1]='O'
                            elif sekil[2][0]=='O' and sekil[2][1]=='O' :
                                if sekil[2][2]=='-':
                                    sekil[2][2]='O'
                            elif sekil[2][0]=='O' and sekil[2][2]=='O':
                                if sekil[2][1]=='-':
                                    sekil[2][1]='O'
                            elif sekil[2][1]=='O' and sekil[2][2]=='O':
                                if sekil[2][0]=='-':
                                    sekil[2][0]='O'
                            elif sekil[0][0]=='O' and sekil[1][0]=='O' :
                                if sekil[2][0]=='-':
                                    sekil[2][0]='O'
                            elif sekil[0][0] == 'O' and sekil[2][0]=='O':
                               if sekil[1][0]=='-':
                                    sekil[1][0]='O'
                            elif sekil[1][0]=='O'and sekil[2][0]=='O' :
                                if sekil[0][0]=='-':
                                    sekil[0][0]='O'
                            elif sekil[0][1]=='O' and sekil[1][1]=='O':
                               if sekil[2][1]=='-':
                                    sekil[2][1]='O'
                            elif sekil[0][1]=='O' and sekil[2][1]=='O':
                                if sekil[1][1]=='-':
                                    sekil[1][1] ='O'
                            elif sekil[1][1]=='O' and sekil[2][1]=='O':
                                if sekil[0][1]=='-':
                                    sekil[0][1] ='O'
                            elif sekil[0][2]=='O' and sekil[1][2]=='O':
                                if sekil[2][2]=='-':
                                    sekil[2][2]='O'
                            elif sekil[0][2] == 'O' and sekil[2][2]=='O':
                                if sekil[1][2]=='-':
                                    sekil[1][2] ='O'
                            elif sekil[1][2]=='O' and sekil[2][2]=='O':
                                if sekil[0][2]=='-':
                                    sekil[0][2] ='O'
                            elif sekil[0][0]=='O' and sekil[1][1]=='O':
                                if sekil[2][2]=='-':
                                    sekil[2][2]='O'
                            elif sekil[0][0] == 'O' and sekil[2][2]=='O':
                                if sekil[1][1]=='-':
                                    sekil[1][1] ='O'
                            elif sekil[1][1]=='O'and sekil[2][2]=='O':
                                if sekil[0][0]=='-':
                                    sekil[0][0] ='O'
                            elif sekil[0][2]=='O' and sekil[1][1]=='O':
                                if sekil[2][0]=='-':
                                    sekil[2][0]='O'
                            elif sekil[0][2]=='O' and sekil[2][0]=='O':
                                if sekil[1][1]=='-':
                                    sekil[1][1]='O'
                            elif sekil[1][1] and sekil[2][0]=='O':
                                if sekil[0][2]=='-':
                                    sekil[0][2] ='O'
                            else:
                                continue

#eger kazanma durumu olusmuyorsa random ile rasgele bir yere
#yazmasini sagliyoruz ve sayac yardimiyla sirayi kullaniciya veriyoruz
                x=random.randint(0,2)
                y=random.randint(0,2)
                if sekil[x][y]=='-':
                    sekil[x][y]='O'
                    ofaktor += [[x, y]]
                    sayac+=1
                elif sekil[x][y]!='-':
                    continue
                for i in sekil:
                    print(*i)

        elif sayac%2!=0:
            isaret='X'
            if isaret=='X':
                satir = input('Soldan saga dogru yazmak istediginiz satiri seciniz\n\
    ilk satir icin 1\'e ikinci satir icin 2\'ye ucuncu satir icin 3\'e basiniz:')
                sutun = input('Yukaridan asagi yazmak istediginiz sutunu seciniz\n\
    ilk sutun icin 1\'e ikinci sutun icin 2\'ye ucuncu sutun icin 3\'e basiniz:')
                if satir == 'q' or sutun == 'q':
                    print('Programdan cikiliyor!')
                    break
                satir = int(satir)
                sutun = int(sutun)
                satir -= 1
                sutun -= 1
                if sekil[satir][sutun]=='-':
                    sekil[satir][sutun]='X'
                    xfaktor += [[satir, sutun]]
                    sayac+=1
#kullanicidan aldigimiz input u int e cevirerek
#bunu listeye yazabilecegimiz hale getirdik
#eger kullanici dolu olan bi kareye yazmak isterse
#bunun mumkun olmadigi belirtip kullanicidan
#tekrar input istiyoruz boylece kullanicinin
#hakki yanmamis oluyor
                elif sekil[satir][sutun]!='-':
                    print('Dolu olan kareler tekrar yazilamaz')
                    for i in sekil:
                        print(*i)
                    continue
#yukarida belirttigimiz kazanama durumlarinin her birini
#for dongusu yardimiyla kimin kazandigini belirledik
        for i in kazanmadurumu:
            o = [z for z in i if z in ofaktor]
            x = [z for z in i if z in xfaktor]
            if len(o) == len(i):
                print('O KAZANDI!')
                quit()
            if len(x) == len(i):
                print('X KAZANDI!')
                quit()
        else :
            print('Yeni bir oyuna ne dersin?')
#kullanicinin bizim istedigimiz degerler disinda
#bir sey girmesi durumunda ise bizim istedigimiz
#hata mesajlarini almasini sagladik ve donguyu basa aldik
    except ValueError :
        print('Lutfen 1,2,3\'den birini kullanin!')
        continue
    except IndexError :
        print('Lutfen sadece tek bir sayi girin ve\
1,2,3\'den birini kullanin!')
        continue
#program genel olarak calisiyor fakat arada bilgisayar 2 defa birden O
#girme durumu oldu bunun neden oldugunu bulamadim
#ve yine bu duruma bagli olarak oyunun devaminda program calismayi birakiyor
#ve bunda herhangi bi hata mesaji yayinlamiyor