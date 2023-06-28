# AB Test: Comparing Bidding Methods' Conversion

## Project Summary

Facebook recently introduced a new bidding method called "average bidding" as an alternative to the existing "maximum bidding" method. One of our clients, bombabomba.com, has decided to test this new feature and wants to conduct an A/B test to determine if average bidding brings in more conversions compared to maximum bidding.

The A/B test has been running for 1 month, and bombabomba.com is now looking for you to analyze the results of this A/B test. The ultimate success metric for bombabomba.com is "Purchase." Therefore, the focus should be on the Purchase metric for statistical testing.

The dataset used in this project contains information about a company's website, including the number of ad impressions, clicks on ads, and earnings generated from these ads. There are two separate datasets for the control and test groups, which can be found in the ab_testing.xlsx file on different sheets. Maximum Bidding was applied to the control group, while Average Bidding was applied to the test group.

Variables:
- Impression: Number of ad impressions
- Click: Number of clicks on ads
- Purchase: Number of products purchased after clicking on ads
- Earning: Revenue generated from the purchased products

## Installation

1. Clone this project: `git clone https://github.com/YOUR_USERNAME/AB-Test-Bidding-Comparison.git`
2. Navigate to the project directory: `cd AB-Test-Bidding-Comparison`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run the project: `python main.py`

## Usage

1. Add the dataset to the "data" folder.
2. Run the project files.
3. Analyze the results and provide insights on the comparison between average bidding and maximum bidding in terms of conversion.

## Contributions

Contributions are welcome. To contribute to the project, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature/NewFeature`
3. Make changes and commit them: `git commit -am 'Added a new feature'`
4. Push the branch to your forked repository: `git push origin feature/NewFeature`
5. Create a pull request.
--------------------------------------
# AB Testi: Teklif Yöntemlerinin Dönüşümünün Karşılaştırılması

## Proje Özeti

Facebook, mevcut "maksimum teklif verme" yöntemine alternatif olarak "ortalama teklif verme" adında yeni bir teklif yöntemi tanıttı. Müşterilerimizden biri olan bombabomba.com, bu yeni özelliği test etmeye karar verdi ve ortalama teklifin maksimum teklife kıyasla daha fazla dönüşüm getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.

A/B testi 1 aydır devam ediyor ve bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor. Bombabomba.com için nihai başarı ölçütü "Satın Alma"dır. Bu nedenle, istatistiksel testler için Satın Alma metriğine odaklanılmalıdır.

Bu projede kullanılan veri seti, bir firmanın web sitesiyle ilgili bilgileri içermektedir. Bu bilgiler arasında reklam görüntüleme sayısı, reklamlara tıklama sayısı ve bu reklamlardan elde edilen kazançlar yer almaktadır. Kontrol ve test grupları için ayrı ayrı veri setleri bulunmaktadır ve bu veri setleri ab_testing.xlsx dosyasının farklı sayfalarında yer almaktadır. Kontrol grubuna "Maksimum Teklif Verme" uygulanırken, test grubuna "Ortalama Teklif Verme" uygulanmıştır.

Değişkenler:
- Impression: Reklam görüntüleme sayısı
- Click: Reklamlara tıklama sayısı
- Purchase: Reklamlara tıkladıktan sonra satın alınan ürün sayısı
- Earning: Satın alınan ürünlerden elde edilen gelir

## Kurulum

1. Bu projeyi klonlayın: `git clone https://github.com/KULLANICI_ADINIZ/AB-Test-Bidding-Comparison.git`
2. Projeler klasörüne gidin: `cd AB-Test-Bidding-Comparison`
3. Gerekli bağımlılıkları yükleyin: `pip install -r requirements.txt`
4. Projeyi çalıştırın: `python main.py`

## Kullanım

1. Veri setini "data" klasörüne ekleyin.
2. Projeyi çalıştırın.
3. Sonuçları analiz edin ve dönüşüm açısından ortalama teklif verme ile maksimum teklif verme arasındaki karşılaştırmaya ilişkin görüşler sağlayın.

## Katkılar

Katkılarınızı bekliyoruz. Projeye katkıda bulunmak için aşağıdaki adımları izleyin:

1. Bu depoyu kendi hesabınıza çatallayın (fork).
2. Kendi dalınızı oluşturun: `git

 checkout -b feature/YeniÖzellik`
3. Değişikliklerinizi yapın ve bunları işleyin: `git commit -am 'Yeni bir özellik ekledi'`
4. Dalınızı çatallanmış depo üzerinde yayınlayın: `git push origin feature/YeniÖzellik`
5. Bir çekme isteği (pull request) oluşturun.

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına başvurun.
