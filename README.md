# grandmetric_counter

Opis działania usługi:

Wywołanie endpointa HTTP GET "/user/<user_id>/counter" powoduje inkrementację licznika wewnętrznego o 1 (max. 1024) dla konkretnego <user_id> (wartości wyłącznie numeryczne od 1 do 65535). Jako wyjście zwracany jest dokument JSON z wartością po inkrementacji licznika per user np: {"user_id": 1, "counter": 2}. Rezultat powinien posiadać stosowne nagłówki HTTP, dla formatu dokumentu JSON. 

Możliwe jest zwiększanie licznika dowolnego usera (w ramach zakresu <user_id>), ale z ograniczeniem na ilość żądań do usługi: 5 wywołań na sekundę. Po przekroczeniu wartości limitu żądań klient HTTP wykonujący żądanie powinien zobaczyć stosowny kod HTTP i licznik nie może być zwiększany. Kiedy licznik osiągnie wartość większą od 1024 zwracamy kod HTTP 501. Dla błędnie wywołanego endpointa również należy zwrócić stosowny kod błędu HTTP.
