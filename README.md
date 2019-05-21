# Info
<p><b>Opis działania usługi:</b></p>
<p>Wywołanie endpointa HTTP GET “/user/&lt;user_id&gt;/counter” powoduje inkrementację licznika wewnętrznego o 1 (max. 1024) dla konkretnego &lt;user_id&gt; (wartości wyłącznie numeryczne od 1 do 65535). Jako wyjście zwracany jest dokument JSON z wartością po inkrementacji licznika per user np: {“user_id”: 1, “counter”: 2}. Rezultat powinien posiadać stosowne nagłówki HTTP, dla formatu dokumentu JSON.</p>
<p>Możliwe jest zwiększanie licznika dowolnego usera (w ramach zakresu &lt;user_id&gt;), ale z ograniczeniem na ilość żądań do usługi: 5 wywołań na sekundę. Po przekroczeniu wartości limitu żądań klient HTTP wykonujący żądanie powinien zobaczyć stosowny kod HTTP i licznik nie może być zwiększany. Kiedy licznik osiągnie wartość większą od 1024 zwracamy kod HTTP 501. Dla błędnie wywołanego endpointa również należy zwrócić stosowny kod błędu HTTP.</p>
<p><b>Instalacja na serwerze lokalnym (Linux):</b></p>
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
python3 main.py</p>
<li>
<p>Wejdź na:<br>
<a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a></p>
</li>
</li>
</ol>
<p><b>Dodatkowo:</b></p>
<p>Usługa została również wdrożona w chmurze publicznej używając Google Cloud Platform. Można ją zobaczyć na:<br>
<a href="http://grandmetric-counter.appspot.com/">http://grandmetric-counter.appspot.com/</a></p>


Instrukcja obsługi:
/user/user_id - wyświetla user_id z wraz z licznikiem "counter". (user_id wartości 1-65535)

/user/user_id/counter - inkrementuje licznik danego "user_id" o jeden.

/reset - resetuje licznik każdego "user_id"
