from flask import Flask, render_template
import os

app = Flask(__name__)

picFolder = os.path.join('static','pics')
app.config['UPLOAD_FOLDER'] = picFolder

@app.route('/')
def index():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'pt.jpg')
    return render_template('index.html', user_image = pic1)

@app.route('/k1.html')
def book_1():
    title_1 = "<h1>KSIĘGA PIERWSZA<br>GOSPODARSTWO</h1>"
    subtitle_1 = "<h2>Treść:</h2>"
    content_1 = "<h3>Powrót panicza - Spotkanie się najpierwsze w pokoiku, drugie u stołu - Ważna Sędziego nauka o grzeczności - Podkomorzego uwagi polityczne nad modami - Początek sporu o Kusego i Sokoła - Żale Wojskiego - Ostatni Woźny Trybunału - Rzut oka na ówczesny stan polityczny Litwy i Europy.</h3>" 
    return render_template('k1.html', title = title_1, subtitle = subtitle_1, content = content_1)

@app.route('/k2.html')
def book_2():
    title_2 = "<h1>KSIĘGA DRUGA<br>ZAMEK</h1>"
    subtitle_2 = "<h2>Treść:</h2>"
    content_2 = "<h3>Polowanie z chartami na upatrzonego - Gość w zamku - Ostatni z dworzan opowiada historię ostatniego z Horeszków - Rzut oka w sad - Dziewczyna w ogórkach - Śniadanie - Pani Telimeny anegdota petersburska - Nowy wybuch sporów o Kusego i Sokoła - Interwencja Robaka - Rzecz Wojskiego - Zakład - Dalej w grzyby!</h3>"
    return render_template('k2.html', title = title_2, subtitle = subtitle_2, content = content_2)


@app.route('/k3.html')
def book_3():
    title_3 = "<h1>KSIĘGA TRZECIA<br>UMIZGI</h1>"
    subtitle_3 = "<h2>Treść:</h2>"
    content_3 = "<h3>Wyprawa Hrabi na sad - Tajemnicza nimfa gęsi pasie - Podobieństwo grzybobrania do przechadzki cieniów elizejskich - Gatunki grzybów - Telimena w Świątyni dumania - Narady tyczące się postanowienia Tadeusza - Hrabia pejzażysta - Tadeusza uwagi malarskie nad drzewami i obłokami - Hrabiego myśli o sztuce - Dzwon - Bilecik - Niedźwiedź, Mospanie!</h3>"
    return render_template('k3.html', title = title_3, subtitle = subtitle_3, content = content_3)


@app.route('/k4.html')
def book_4():
    title_4 = "<h1>KSIĘGA CZWARTA <br>DYPLOMATYKA I ŁOWY</h1>"
    subtitle_4 = "<h2>Treść:</h2>"
    content_4 = "<h3>Zjawisko w papilotach budzi Tadeusza - Za późne postrzeżenie omyłki - Karczma - Emisariusz - Zręczne użycie tabakiery zwraca dyskusję na właściwą drogę - Matecznik - Niedźwiedź- Niebezpieczeństwo Tadeusza i Hrabiego - Trzy strzały - Spór Sagalasówki z Sanguszkówką, rozstrzygniony na stronę jednorurki Horeszkowskiej - Bigos - Wojskiego powieść o pojedynku Dowejki z Domejką, przerwana szczuciem kota - Koniec powieści o Dowejce i Domejce.</h3>"
    return render_template('k4.html', title = title_4, subtitle = subtitle_4, content = content_4)


@app.route('/k5.html')
def book_5():
    title_5 = "<h1>KSIĘGA PIĄTA<br>KŁÓTNIA</h1>"
    subtitle_5 = "<h2>Treść:</h2>"
    content_5 = "<h3>Plany myśliwskie Telimeny - Ogrodniczka wybiera się na wielki świat i słucha nauk opiekunki - Strzelcy wracają - Wielkie zadziwienie Tadeusza - Spotkanie się powtórne w Świątyni dumania i zgoda, ułatwiona za pośrednictwem mrówek - U stołu wytacza się rzecz o łowach - Powieść Wojskiego o Rejtanie i księciu Denassów, przerwana - Zagajenie układów między stronami, także przerwane - Zjawisko z kluczem - Kłótnia - Hrabia z Gerwazym odbywają radę wojenną.</h3>"
    return render_template('k5.html', title = title_5, subtitle = subtitle_5, content = content_5)


@app.route('/k6.html')
def book_6():
    title_6 = "<h1>KSIĘGA SZÓSTA<br>ZAŚCIANEK</h1>"
    subtitle_6 = "<h2>Treść:</h2>"
    content_6 = "<h3>Pierwsze ruchy wojenne zajazdu - Wyprawa Protazego - Robak z panem Sędzią radzą o rzeczy publicznej - Dalszy ciąg wyprawy Protazego, bezskutecznej - Ustęp o konopiach - Zaścianek szlachecki Dobrzyn - Opisanie domostwa i osoby Maćka Dobrzyńskiego.</h3>"
    return render_template('k6.html', title = title_6, subtitle = subtitle_6, content = content_6)


@app.route('/k7.html')
def book_7():
    title_7 = "<h1>KSIĘGA SIÓDMA<br>RADA</h1>"
    subtitle_7 = "<h2>Treść:</h2>"
    content_7 = "<h3>Zbawienne rady Bartka, zwanego Prusak - Głos żołnierski Maćka Chrzciciela - Głos polityczny pana Buchmana - Jankiel radzi ku zgodzie, którą Scyzoryk rozcina - Rzecz Gerwazego, z której okazują się wielkie skutki wymowy sejmowej - Protestacja starego Maćka - Nagłe przybycie posiłków wojennych zrywa naradę - Hejże na Soplice!</h3>"
    return render_template('k7.html', title = title_7, subtitle = subtitle_7, content = content_7)


@app.route('/k8.html')
def book_8():
    title_8 = "<h1>KSIĘGA ÓSMA<br>ZAJAZD</h1>"
    subtitle_8 = "<h2>Treść:</h2>"
    content_8 = "<h3>Astronomia Wojskiego - Uwaga Podkomorzego nad kometami - Tajemnicza scena w pokoju Sędziego - Tadeusz, chcąc zręcznie wyplątać się, wpada w wielkie kłopoty - Nowa Dydo- Zajazd - Ostatnia woźnieńska protestacja - Hrabia zdobywa Soplicowo - Szturm i rzeź - Gerwazy piwnicznym - Uczta zajazdowa.</h3>"
    return render_template('k8.html', title = title_8, subtitle = subtitle_8, content = content_8)


@app.route('/k9.html')
def book_9():
    title_9 = "<h1>KSIĘGA DZIEWIĄTA<br>BITWA</h1>"
    subtitle_9 = "<h2>Treść:</h2>"
    content_9 = "<h3>O niebezpieczeństwach wynikających z nieporządnego obozowania - Odsiecz niespodziana - Smutne położenie szlachty - Odwiedziny kwestarskie są wróżbą ratunku - Major Płut zbytnią zalotnością ściąga na siebie burzę - Wystrzał z krócicy, hasło boju - Czyny Kropiciela, czyny i niebezpieczeństwa Maćka - Konewka zasadzką ocala Soplicowo - Posiłki jezdne, atak na piechotę - Czyny Tadeusza - Pojedynek dowódców przerwany zdradą - Wojski stanowczym manewrem przechyla szalę boju - Czyny krwawe Gerwazego - Podkomorzy zwyciężca wspaniałomyślny.</h3>"
    return render_template('k9.html', title = title_9, subtitle = subtitle_9, content = content_9)


@app.route('/k10.html')
def book_10():
    title_10 = "<h1>KSIĘGA DZIESIĄTA<br>EMIGRACJA. JACEK</h1>"
    subtitle_10 = "<h2>Treść:</h2>"
    content_10 = "<h3>Narada tycząca się zabezpieczenia losu zwycięzców - Układy z Rykowem - Pożegnanie - Ważne odkrycie - Nadzieja.</h3>"
    return render_template('k10.html', title = title_10, subtitle = subtitle_10, content = content_10)


@app.route('/k11.html')
def book_11():
    title_11 = "<h1>KSIĘGA JEDENASTA<br>ROK 1812</h1>"
    subtitle_11 = "<h2>Treść:</h2>"
    content_11 = "<h3>Wróżby wiosenne - Wkroczenie wojsk - Nabożeństwo - Rehabilitacja urzędowa śp. Jacka Soplicy - Z rozmów Gerwazego i Protazego wnosić można bliski koniec procesu - Umizgi ułana z dziewczyną - Rozstrzyga się spór o Kusego i Sokoła - Zaczem goście zgromadzają się na biesiadę - Przedstawienie wodzom par narzeczonych.</h3>"
    return render_template('k11.html', title = title_11, subtitle = subtitle_11, content = content_11)


@app.route('/k12.html')
def book_12():
    title_12 = "<h1>KSIĘGA DWUNASTA<br>KOCHAJMY SIĘ</h1>"
    subtitle_12 = "<h2>Treść:</h2>"
    content_12 = "<h3>Ostatnia uczta staropolska - Arcyserwis - Objaśnienie jego figur - Jego ruchy - Dąbrowski udarowany - Jeszcze o Scyzoryku. - Kniaziewicz udarowany. - Pierwszy akt urzędowy Tadeusza przy objęciu dziedzictwa - Uwagi Gerwazego - Koncert nad koncertami - Polonez - Kochajmy się!</h3>"
    return render_template('k12.html', title = title_12, subtitle = subtitle_12, content = content_12)

if __name__ == '__main__':
    app.run()
