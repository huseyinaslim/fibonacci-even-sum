#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fibonacci serisinin belirli bir sayıya kadar olan çift sayılarının
toplamını hesaplayan program. Süper optimize edilmiş versiyon.
"""

import argparse
import sys
import time


def fibonacci_even_sum_formula(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını
    kapalı formül kullanarak hesaplar.

    Args:
        n (int): Üst sınır değeri

    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0

    # Son çift Fibonacci sayısını bul
    k = 0
    fib = 0

    # İlk çift Fibonacci sayısı 2'dir (F(3))
    # Sonraki çift sayılar F(6), F(9), F(12), ... şeklindedir
    # Yani F(3k) şeklinde ifade edilebilir

    # n'den küçük veya eşit olan son çift Fibonacci sayısını bul
    while fib <= n:
        # F(3k) = [φ^(3k) - (-1/φ)^(3k)]/√5 formülünü kullanabiliriz
        # Ancak büyük k değerleri için bu hesaplama hassas olmayabilir
        # Bu yüzden iteratif olarak son çift Fibonacci sayısını buluyoruz
        k += 1
        # F(3k) hesapla - altın oran kullanarak
        phi = (1 + 5 ** 0.5) / 2
        psi = (1 - 5 ** 0.5) / 2
        fib = int((phi ** (3 * k) - psi ** (3 * k)) / (5 ** 0.5))

    # Bir önceki k değerine dön
    k -= 1

    # Çift Fibonacci sayılarının toplamı için kapalı formül:
    # Sum(F(3i)) = [F(3k+2) - 1]/2 (i=1 to k için)
    # F(3k+2) hesapla
    phi = (1 + 5 ** 0.5) / 2
    psi = (1 - 5 ** 0.5) / 2
    fib_3k_plus_2 = int((phi ** (3 * k + 2) - psi ** (3 * k + 2)) / (5 ** 0.5))

    # Formülü uygula
    return (fib_3k_plus_2 - 1) // 2


def fibonacci_even_sum_direct(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını
    doğrudan çift Fibonacci sayılarını hesaplayarak bulur.

    Args:
        n (int): Üst sınır değeri

    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0

    # Fibonacci serisinde çift sayılar F(3), F(6), F(9), ... şeklindedir
    # Yani her 3. sayı çifttir

    # İlk çift Fibonacci sayısı 2'dir
    b_val, c_val = 1, 2
    total = 0

    while c_val <= n:
        if c_val % 2 == 0:  # Çift sayı kontrolü
            total += c_val

        # Bir sonraki Fibonacci sayısını hesapla
        # Değişkenleri kaydırarak ilerliyoruz
        b_val, c_val = c_val, b_val + c_val

    return total


def fibonacci_even_sum(n):
    """
    Fibonacci serisinin n sayısına kadar olan çift sayılarının toplamını
    hesaplar. Optimize edilmiş iteratif yöntem.

    Args:
        n (int): Üst sınır değeri

    Returns:
        int: Fibonacci serisinin n'e kadar olan çift sayılarının toplamı
    """
    if n < 2:
        return 0

    # Fibonacci serisinde her 3. sayı çifttir
    # F(3k) = 4*F(3k-3) + F(3k-6)
    # Bu özelliği kullanarak sadece çift Fibonacci sayılarını hesaplayabiliriz
    a_val, b_val = 0, 2  # İlk çift Fibonacci sayısı 2'dir
    total = 0

    while b_val <= n:
        total += b_val
        # Bir sonraki çift Fibonacci sayısını hesapla
        # F(n+3) = 4*F(n) + F(n-3)
        a_val, b_val = b_val, 4 * b_val + a_val

    return total


def fibonacci_even_sum_original(n):
    """
    Orijinal yöntem - karşılaştırma için.
    """
    if n < 2:
        return 0

    # Değişken adlarını değiştirdik ve kullanıyoruz
    prev, current = 1, 2  # a_val ve b_val yerine daha açıklayıcı isimler
    total = 0

    while current <= n:
        if current % 2 == 0:
            total += current
        prev, current = current, prev + current

    return total


def main():
    """Ana program fonksiyonu."""
    parser = argparse.ArgumentParser(
        description=(
            "Fibonacci serisinin belirli bir sayıya kadar olan "
            "çift sayılarının toplamını hesaplar."
        )
    )
    parser.add_argument(
        "number",
        type=int,
        help="Fibonacci serisinin üst sınır değeri"
    )
    parser.add_argument(
        "--compare",
        action="store_true",
        help="Tüm algoritmaları karşılaştır"
    )
    parser.add_argument(
        "--formula",
        action="store_true",
        help="Kapalı formül kullanarak hesapla"
    )
    parser.add_argument(
        "--direct",
        action="store_true",
        help="Doğrudan yöntem kullanarak hesapla"
    )

    args = parser.parse_args()

    if args.number < 0:
        print("Lütfen pozitif bir sayı giriniz.")
        sys.exit(1)

    if args.formula:
        # Kapalı formül kullanarak hesapla
        result = fibonacci_even_sum_formula(args.number)
        print(f"Fibonacci serisinin {args.number} sayısına kadar olan "
              f"çift sayılarının toplamı: {result}")
        return

    if args.direct:
        # Doğrudan yöntem kullanarak hesapla
        result = fibonacci_even_sum_direct(args.number)
        print(f"Fibonacci serisinin {args.number} sayısına kadar olan "
              f"çift sayılarının toplamı: {result}")
        return

    if args.compare:
        # Performans karşılaştırması
        print(f"N = {args.number} için performans karşılaştırması:")

        # Düzeltilmiş formül
        start_time = time.time()
        result_formula = fibonacci_even_sum_formula(args.number)
        formula_time = time.time() - start_time
        print(f"Kapalı formül: {result_formula} "
              f"(Süre: {formula_time:.6f} saniye)")

        # Doğrudan yöntem
        start_time = time.time()
        result_direct = fibonacci_even_sum_direct(args.number)
        direct_time = time.time() - start_time
        print(f"Doğrudan yöntem: {result_direct} "
              f"(Süre: {direct_time:.6f} saniye)")

        # Standart yöntem
        start_time = time.time()
        result_standard = fibonacci_even_sum(args.number)
        standard_time = time.time() - start_time
        print(f"Standart yöntem: {result_standard} "
              f"(Süre: {standard_time:.6f} saniye)")

        # Sonuçların doğruluğunu kontrol et
        if result_formula == result_direct == result_standard:
            print(f"Tüm yöntemler aynı sonucu verdi: {result_standard}")
        else:
            print("HATA: Yöntemler farklı sonuçlar verdi!")
            print(f"Kapalı formül: {result_formula}")
            print(f"Doğrudan yöntem: {result_direct}")
            print(f"Standart yöntem: {result_standard}")
        return

    # Normal çalıştırma
    result = fibonacci_even_sum(args.number)
    print(f"Fibonacci serisinin {args.number} sayısına kadar olan "
          f"çift sayılarının toplamı: {result}")


if __name__ == "__main__":
    main()
