import os
import json

filepath = 'c:/Users/Mahir/Desktop/Locy/locales/translations.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    '"comp_hero_title": "<span class=\\"text-gradient\\">Son Kilometre</span> i\\u00e7in Tasarland\\u0131."':
    '"comp_hero_title": "Kusursuz <span class=\\"text-gradient\\">Son Teslimat</span> i\\u00e7in Tasarland\\u0131."',

    '"rest_hero_title": "S\\u0131cak yemek. <br><span class=\\"text-gradient-red\\">So\\u011fuk mant\\u0131k.</span>"':
    '"rest_hero_title": "S\\u0131cak yemek. <br><span class=\\"text-gradient-red\\">Ak\\u0131ll\\u0131 teslimat.</span>"',

    '"pricing_hero_sub": "KULLANIM BAZLI F\\u0130YATLANDIRMA"':
    '"pricing_hero_sub": "KULLANDIK\\u00c7A \\u00d6DE"',

    '"pricing_hero_title": "Sadece ge\\u00e7erli <span class=\\"text-gradient\\">koordinatlar</span> i\\u00e7in \\u00f6deyin.<br>Ba\\u015fka hi\\u00e7bir \\u015fey i\\u00e7in de\\u011fil."':
    '"pricing_hero_title": "Sadece <span class=\\"text-gradient\\">do\\u011fru konumlar</span> i\\u00e7in \\u00f6deyin.<br>Fazlas\\u0131 i\\u00e7in de\\u011fil."',

    '"product_hero_title": "Adres Yazmay\\u0131 <span class=\\"text-gradient\\">B\\u0131rak\\u0131n.</span>"':
    '"product_hero_title": "Manuel Giri\\u015fe <span class=\\"text-gradient\\">Son Verin.</span>"',

    '"product_feat6_title": "Sessiz Hata Korumas\\u0131"':
    '"product_feat6_title": "Kesintisiz \\u0130\\u015fleyi\\u015f"',

    '"product_feat7_title": "Sanal Canl\\u0131 Dispe\\u00e7er"':
    '"product_feat7_title": "Sanal Operasyon Merkezi"',

    '"hero_title": "Foto\\u011fraf g\\u00f6nder.<br>Konum al."':
    '"hero_title": "Foto\\u011fraf g\\u00f6nder.<br>Kesin konum al."',

    '"demo_badge": "CANLI S\\u0130STEM"':
    '"demo_badge": "CANLI DEMO"',

    '"demo_title": "Demo Makinesi."':
    '"demo_title": "Canl\\u0131 Test Ekran\\u0131."',

    '"cap_title": "Son kilometre i\\u00e7in katman."':
    '"cap_title": "Kusursuz son teslimatlar i\\u00e7in altyap\\u0131."',

    '"cap_2_title": "Ana Dil Botu"':
    '"cap_2_title": "\\u00c7ok Dilli Yapay Zeka"',

    '"cap_1_desc": "Zikzak \\u00e7izmeyi b\\u0131rak\\u0131n. Duraklar\\u0131 mant\\u0131ksal olarak s\\u0131ral\\u0131yoruz. A \\u2192 B \\u2192 C."':
    '"cap_1_desc": "Karma\\u015f\\u0131k rotalar\\u0131 b\\u0131rak\\u0131n. Duraklar\\u0131 en k\\u0131sa s\\u00fcreye g\\u00f6re s\\u0131ral\\u0131yoruz."',

    '"flow_title": "S\\u0131f\\u0131r s\\u00fcrt\\u00fcnmeli entegrasyon."':
    '"flow_title": "P\\u00fcr\\u00fczs\\u00fcz entegrasyon."',

    '"footer_desc": "Son kilometre lojisti\\u011fi i\\u00e7in katman. Uygulama yok. Sadece sonu\\u00e7."':
    '"footer_desc": "Son teslimat a\\u015famas\\u0131 i\\u00e7in g\\u00fc\\u00e7l\\u00fc altyap\\u0131. Uygulama yok, an\\u0131nda sonu\\u00e7 var."'
}

for old, new in replacements.items():
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced: {old[:30]}...")
    else:
        print(f"WARNING: Could not find: {old}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done patching translations.js for TR.")
