# grandmetric_counter

Opis działania usługi:

Wywołanie endpointa HTTP GET "/user/<user_id>/counter" powoduje inkrementację licznika wewnętrznego o 1 (max. 1024) dla konkretnego <user_id> (wartości wyłącznie numeryczne od 1 do 65535). Jako wyjście zwracany jest dokument JSON z wartością po inkrementacji licznika per user np: {"user_id": 1, "counter": 2}. Rezultat powinien posiadać stosowne nagłówki HTTP, dla formatu dokumentu JSON. 

Możliwe jest zwiększanie licznika dowolnego usera (w ramach zakresu <user_id>), ale z ograniczeniem na ilość żądań do usługi: 5 wywołań na sekundę. Po przekroczeniu wartości limitu żądań klient HTTP wykonujący żądanie powinien zobaczyć stosowny kod HTTP i licznik nie może być zwiększany. Kiedy licznik osiągnie wartość większą od 1024 zwracamy kod HTTP 501. Dla błędnie wywołanego endpointa również należy zwrócić stosowny kod błędu HTTP.



Instalacja na serwerze lokalnym (Linux):

1. W przygotowanym wirtualnym środowisku pobierz repozytorium: 
   git clone https://github.com/AniQl/grandmetric_counter.git

2. Zainstaluj wszystkie bilbioteki/framework'i będąc w folderze grandmetric_counter:
   pip install -r requirements.txt

3. Uruchom serwer z folderu grandmetric_counter:
   python3 main.py
   


Usługa została również wdrożona w chmurze publicznej używając Google Cloud Platform. Można ją zobaczyć na:
http://grandmetric-counter.appspot.com/

<p>Opis działania usługi:</p>
<p>Wywołanie endpointa HTTP GET “/user/&lt;user_id&gt;/counter” powoduje inkrementację licznika wewnętrznego o 1 (max. 1024) dla konkretnego &lt;user_id&gt; (wartości wyłącznie numeryczne od 1 do 65535). Jako wyjście zwracany jest dokument JSON z wartością po inkrementacji licznika per user np: {“user_id”: 1, “counter”: 2}. Rezultat powinien posiadać stosowne nagłówki HTTP, dla formatu dokumentu JSON.</p>
<p>Możliwe jest zwiększanie licznika dowolnego usera (w ramach zakresu &lt;user_id&gt;), ale z ograniczeniem na ilość żądań do usługi: 5 wywołań na sekundę. Po przekroczeniu wartości limitu żądań klient HTTP wykonujący żądanie powinien zobaczyć stosowny kod HTTP i licznik nie może być zwiększany. Kiedy licznik osiągnie wartość większą od 1024 zwracamy kod HTTP 501. Dla błędnie wywołanego endpointa również należy zwrócić stosowny kod błędu HTTP.</p>
<p>Instalacja na serwerze lokalnym (Linux):</p>
<ol>
<li>
<p>W przygotowanym wirtualnym środowisku pobierz repozytorium:<br>
git clone <a href="https://github.com/AniQl/grandmetric_counter.git">https://github.com/AniQl/grandmetric_counter.git</a></p>
</li>
<li>
<p>Zainstaluj wszystkie bilbioteki/framework’i będąc w folderze grandmetric_counter:<br>
pip install -r requirements.txt</p>
</li>
<li>
<p>Uruchom serwer z folderu grandmetric_counter:<br>
python3 <a href="http://main.py">main.py</a></p>
</li>
</ol>
<p>Usługa została również wdrożona w chmurze publicznej używając Google Cloud Platform. Można ją zobaczyć na:<br>
<a href="http://grandmetric-counter.appspot.com/">http://grandmetric-counter.appspot.com/</a></p>
