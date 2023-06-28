#####################################################
# AB Testi ile BiddingYöntemlerinin Dönüşümünün Karşılaştırılması
#####################################################
import pandas as pd

#####################################################
# İş Problemi
#####################################################

# Facebook kısa süre önce mevcut "maximumbidding" adı verilen teklif verme türüne alternatif
# olarak yeni bir teklif türü olan "average bidding"’i tanıttı. Müşterilerimizden biri olan bombabomba.com,
# bu yeni özelliği test etmeye karar verdi ve averagebidding'in maximumbidding'den daha fazla dönüşüm
# getirip getirmediğini anlamak için bir A/B testi yapmak istiyor.A/B testi 1 aydır devam ediyor ve
# bombabomba.com şimdi sizden bu A/B testinin sonuçlarını analiz etmenizi bekliyor.Bombabomba.com için
# nihai başarı ölçütü Purchase'dır. Bu nedenle, istatistiksel testler için Purchasemetriğine odaklanılmalıdır.




#####################################################
# Veri Seti Hikayesi
#####################################################

# Bir firmanın web site bilgilerini içeren bu veri setinde kullanıcıların gördükleri ve tıkladıkları
# reklam sayıları gibi bilgilerin yanı sıra buradan gelen kazanç bilgileri yer almaktadır.Kontrol ve Test
# grubu olmak üzere iki ayrı veri seti vardır. Bu veri setleriab_testing.xlsxexcel’ininayrı sayfalarında yer
# almaktadır. Kontrol grubuna Maximum Bidding, test grubuna AverageBiddinguygulanmıştır.

# impression: Reklam görüntüleme sayısı
# Click: Görüntülenen reklama tıklama sayısı
# Purchase: Tıklanan reklamlar sonrası satın alınan ürün sayısı
# Earning: Satın alınan ürünler sonrası elde edilen kazanç



#####################################################
# Proje Görevleri
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################

# 1. Hipotezleri Kur
# 2. Varsayım Kontrolü
#   - 1. Normallik Varsayımı (shapiro)
#   - 2. Varyans Homojenliği (levene)
# 3. Hipotezin Uygulanması
#   - 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi
#   - 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi
# 4. p-value değerine göre sonuçları yorumla
# Not:
# - Normallik sağlanmıyorsa direkt 2 numara. Varyans homojenliği sağlanmıyorsa 1 numaraya arguman girilir.
# - Normallik incelemesi öncesi aykırı değer incelemesi ve düzeltmesi yapmak faydalı olabilir.




#####################################################
# Görev 1:  Veriyi Hazırlama ve Analiz Etme
#####################################################

# Adım 1:  ab_testing_data.xlsx adlı kontrol ve test grubu verilerinden oluşan veri setini okutunuz. Kontrol ve test grubu verilerini ayrı değişkenlere atayınız.
import pandas as pd
df_control = pd.read_excel("DERSLER/MEASUREMENT PROBLEMS/case study- ab testing/ab_testing.xlsx",sheet_name="Control Group")
df_test = pd.read_excel ("DERSLER/MEASUREMENT PROBLEMS/case study- ab testing/ab_testing.xlsx", sheet_name="Test Group")
df_test.head()
df_control.head()
# Adım 2: Kontrol ve test grubu verilerini analiz ediniz.

df_test.head()
df_test["Purchase"].mean() #582.1
df_control["Purchase"].mean() #550.89
df_test.describe().T
df_control.describe().T
# Adım 3: Analiz işleminden sonra concat metodunu kullanarak kontrol ve test grubu verilerini birleştiriniz.

df = pd.concat([df_control,df_test],ignore_index=True)

df.tail()

df["Purchase"].mean() #total 566.5

#####################################################
# Görev 2:  A/B Testinin Hipotezinin Tanımlanması
#####################################################

# Adım 1: Hipotezi tanımlayınız.
#HO: M1=M2 (averagebidding'in maximumbidding'le aynı dönüşüm oranı olması)
#H1: M1 != M2 (farklı dönüşüm oranı)

# Adım 2: Kontrol ve test grubu için purchase(kazanç) ortalamalarını analiz ediniz

df.loc[:39]["Purchase"].mean() #550.894
df.loc[40:79]["Purchase"].mean() #582.106

#####################################################
# GÖREV 3: Hipotez Testinin Gerçekleştirilmesi
#####################################################

######################################################
# AB Testing (Bağımsız İki Örneklem T Testi)
######################################################


# Adım 1: Hipotez testi yapılmadan önce varsayım kontrollerini yapınız.Bunlar Normallik Varsayımı ve Varyans Homojenliğidir.

# Kontrol ve test grubunun normallik varsayımına uyup uymadığını Purchase değişkeni üzerinden ayrı ayrı test ediniz

#Normallik Varsayımı :H0: Normal dağılım varsayımı sağlanmaktadır.
#H1: Normal dağılım varsayımı sağlanmamaktadır.
#p < 0.05 H0 RED , p > 0.05 H0 REDDEDİLEMEZ
#Test sonucuna göre normallik varsayımı kontrol ve test grupları için sağlanıyor mu ? Elde edilen p-valuedeğerlerini yorumlayınız.
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",10)
pd.set_option("display.float_format", lambda x: "%.5f" % x)

test_stat, pvalue = shapiro(df_control.Purchase)
print(pvalue)
#control icin pval=0.58. p> 0.05 yani H0: Kabul edilir.
test_stat, pvalue = shapiro(df_test.Purchase)
print(pvalue)
#test icin pval= 0.15 p>0.05 yani H0: Kabul edilir. yani Normal dağılım varsayımı sağlanmaktadır.

##Varyans Homojenliği..

test_stat,pvalue = levene(df_control.Purchase, df_test.Purchase)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#pval= 0.1083 yani >0.05 yani H0: Kabul edilir. varyans homojenliğine sahiptir

# Adım 2: Normallik Varsayımı ve Varyans Homojenliği sonuçlarına göre uygun testi seçiniz

#varyans ve normallik varsayımına gore homojenlige sahiptir. bu sebeple iki örneklem t testi (parametrik test)

test_stat,pvalue= ttest_ind(df_control.Purchase,df_test.Purchase,equal_var=True)
print(test_stat,pvalue)
#pval = 0.349 yani >0.05 Yani H0:Reddedilemez.
##HO: M1=M2 (averagebidding'in maximumbidding'le aynı dönüşüm oranı olması) kabuldur.



# Adım 3: Test sonucunda elde edilen p_value değerini göz önünde bulundurarak kontrol ve test grubu satın alma
# ortalamaları arasında istatistiki olarak anlamlı bir fark olup olmadığını yorumlayınız.

#HO: M1=M2 (averagebidding'in maximumbidding'le aynı dönüşüm oranı olması) kabuldur. yani anlamlı bir istatistik farkı yoktur.

##############################################################
# GÖREV 4 : Sonuçların Analizi
##############################################################

# Adım 1: Hangi testi kullandınız, sebeplerini belirtiniz.

#parametrik test kullandık cunku iki grubun Normallik Varsayımı  ve Varyans Homojenliği  sağlandı. onlar içinse (shapiro) ve (levene) testlerini kullandık.

# Adım 2: Elde ettiğiniz test sonuçlarına göre müşteriye tavsiyede bulununuz.

#yeni teklif verme türü olan  "maximumbidding" daha fazla dönüşüm getirmemektedir. şu an için gerek olmayan bir inavasyondur.


