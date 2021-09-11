# to ensure a unique bible code, each has a hexidecimal. But, that's entirely human un-readable. So, key -> value.
# I'm basically taking user input as a key to look up a value on the versions_dict hash table.


def versions_dict():
    return dict([("SBLGNT", "9419b482b6506691-01"),
                 ("ESV", "f421fe261da7624f-01"),
                 ("NENDNP03", "0c2ff0a5c8b9069c-01"),
                 ("ARP", "b7ad344da9c39262-01"),
                 ("ASMIRV", "34690fafc7ffd7d4-02"),
                 ("ASMFB", "34690fafc7ffd7d4-01"),
                 ("НЗПРП", "17c44f6c89de00db-01"),
                 ("BENIRV", "4338bcf7a310c65f-02"),
                 ("BLA1890", "6855dabfcb711cc2-01"),
                 ("BKR", "c61908161b077c4c-01"),
                 ("KWERE", "dca01eb41e39d25d-01"),
                 ("ELO", "95410db44ef800c1-01"),
                 ("TKW", "542b32484b6e38c2-01"),
                 ("DWNT", "e578524a0893c6b7-01"),
                 ("DRA", "179568874c45066f-01"),
                 ("FBVNTPSALMS", "65eec8e0b60e656b-01"),
                 ("GNV", "c315fa9f71d4af3a-01"),
                 ("OJPS", "bf8f1c7f3f9045a5-01"),
                 ("KJV", "a6aee10bb058511c-01"),
                 ("ASV", "06125adad2d5898a-01"),
                 ("T4T", "0bc8836afa7427fa-01"),
                 ("WEB", "9879dbb7cfe39e4d-01"),
                 ("WEBBE", "7142879509583d59-01"),
                 ("WMB", "f72b840c855f362c-04"),
                 ("WMBBE", "04da588535d2f823-04"),
                 ("LSG", "2ef4ad5622cfd98b-01"),
                 ("VPFJ", "9b076bc0f1856204-01"),
                 ("MBKAMNT", "da905e46720432e2-01"),
                 ("KIRNT", "e8b818f49c7c2835-01"),
                 ("GUJBCS", "3548ab6114a312d4-02"),
                 ("GUJ", "3548ab6114a312d4-01"),
                 ("HINIRV", "705aad6832c6e4d2-02"),
                 ("TSI", "2dd568eeff29fb3c-01"),
                 ("DO885", "41f25b97f468e10b-01"),
                 ("KANIRV", "27d398e76e8b43bf-02"),
                 ("KAN", "27d398e76e8b43bf-01"),
                 ("KUTU", "f2f349d77ac8f8bc-01"),
                 ("KPG", "df7d5d71526afe9e-01"),
                 ("MUMNP18", "5591cba5ae063228-01"),
                 ("KBNT", "6aa52b968434d882-01"),
                 ("MALIRV", "9f78f34aabe691c9-02"),
                 ("MAL", "9f78f34aabe691c9-01"),
                 ("MARIRV", "f425394cc4a3cd5a-01"),
                 ("MB", "385573d4ba3ff72a-01"),
                 ("MKD", "abf017938be72f46-01"),
                 ("ARUNT", "5e51f89e89947acb-01"),
                 ("NDBV", "cb0425ae772bb042-01"),
                 ("NGBV", "324f457845cb5d21-01"),
                 ("TAKUU", "312df00520eac624-01"),
                 ("NLD1939", "ead7b4cc5007389c-01"),
                 ("ORYIRV", "365f988242c307d2-02"),
                 ("ORY", "365f988242c307d2-01"),
                 ("PANIRV", "7b929cf7aea665a3-02"),
                 ("UBG", "1c9761e0230da6e0-01"),
                 ("TFTP", "90799bb5b996fddc-01"),
                 ("PBV", "355792a03079ccdd-01"),
                 ("RNC", "33ac978af36830fa-02"),
                 ("LBV", "98d1c5bee401f80c-01"),
                 ("SANAS", "bb3df4b7c8587c77-01"),
                 ("SANBN", "8d1ad2c921d811c3-01"),
                 ("SANBU", "9449d4ad98193779-01"),
                 ("SANCO", "33b6449cacf22773-01"),
                 ("SANGJ", "e9ea572977b4f504-01"),
                 ("SANHK", "89007ccbb2eb5187-01"),
                 ("SANIA", "0b07fcef627a2db2-01"),
                 ("SANIS", "d4599ff3c6b97f3a-01"),
                 ("SANIT", "6bc5ae3d6dd9009a-01"),
                 ("SANKA", "c1f49ed98a65a544-01"),
                 ("SANKH", "6bb8b0fa7aca67c6-01"),
                 ("SANML", "119375d97b57cf04-01"),
                 ("SANOR", "5a27fd2a2de187c8-01"),
                 ("SANPN", "07225eadadcb079a-01"),
                 ("SANSI", "2c2cf8df5a22a46e-01"),
                 ("SANTM", "143e0e03cf5b12ae-01"),
                 ("SANTE", "aa146959e1d39b78-01"),
                 ("SANTH", "306d6ab1ca333a1e-01"),
                 ("SANTI", "018ff00d7f55cbc1-01"),
                 ("SANUR", "51b16e0b4b7c9825-01"),
                 ("SANVE", "9a875168ff4df1a3-01"),
                 ("SAN-DN", "e8b40ccabe793c0d-01"),
                 ("RVR09", "592420522e16049f-01"),
                 ("VBL", "482ddd53705278cc-01"),
                 ("AKG-MKAC", "2a65010324d677b6-01"),
                 ("SRP1865", "06995ce9cd23361b-01"),
                 ("SOSO", "bbeb583cd75c6356-01"),
                 ("AKS", "2d5220a02a7aaac6-01"),
                 ("SKB", "fa4317c59f0825e0-01"),
                 ("TAMIRV", "cd37ba0be852367d-02"),
                 ("TAM", "cd37ba0be852367d-01"),
                 ("TAYNT", "8e3b1a957009c6ca-01"),
                 ("TELIRV", "85653c8847391b02-02"),
                 ("TEL", "85653c8847391b02-01"),
                 ("GS", "30cb581bcc911c45-01"),
                 ("RWV", "25210406001d9aae-01"),
                 ("उर्दू बाइबिल", "5d73986246cb876f-01"),
                 ("SOBP15", "e01f11e9b4b8e338-01"),
                 ("VIDUNDA", "9a270e42b294fc37-01"),
                 ("KITABUNA", "afe8f67d8ba9025c-01"),
                 ("YAP", "8a448a0135a6a70a-01"),
                 ("ZIBT", "c9f3cf58d557a9f3-01	")])



