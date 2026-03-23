import os
import re

updates = {
    "en": {
        "hero_desc": "Stop driving in circles. Turn labels into verified coordinates instantly. Zero manual entry. Zero returned packages.",
        "hero_btn_whatsapp": "Launch on WhatsApp",
        "hero_check_api": "Enterprise API",
        "comp_hero_title": "The infrastructure for <span class=\"text-gradient\">last-mile.</span>",
        "comp_manifesto": "Logistics is broken at the curb. Drivers waste time typing labels while dispatchers guess locations. Locy delivers instant digital precision. No apps to install. Just coordinates.",
        "comp_val1_title": "Frictionless",
        "comp_val1_desc": "No app installs. No onboarding. We run where your fleet already operates: WhatsApp.",
        "comp_val2_title": "Sub-Second",
        "comp_val2_desc": "Latency measured in milliseconds. Because drivers don't have time to wait.",
        "comp_val3_desc": "Zero data retention. Images become coordinates and instantly vanish from memory.",
        "eco_hero_title": "Deliver right.<br><span class=\"text-gradient-cyan\">Every time.</span>",
        "eco_hero_desc": "Failed deliveries kill margins. Locy verifies every address before the truck even leaves the depot.",
        "eco_cta_title": "Ready to scale deliveries?",
        "eco_cta_desc": "Save 30 seconds per stop.",
        "em_hero_title": "When every <br><span class=\"text-gradient-alert\">second matters.</span>",
        "em_hero_desc": "GPS says 'You have arrived', but the door is blocks away. Locy routes responders to the exact entrance.",
        "rest_hero_title": "Hot food. <br><span class=\"text-gradient-red\">Fast logic.</span>",
        "rest_hero_desc": "Calling customers for directions destroys profit margins. Locy finds the exact door, every time.",
        "product_hero_title": "Never Type <span class=\"text-gradient\">Addresses Again.</span>",
        "product_hero_desc": "Forward photos via WhatsApp. Get exact coordinates in milliseconds. The delivery tool drivers actually use.",
        "product_seca_title": "Snap a photo. <br>We do the rest.",
        "product_seca_desc": "Drivers shouldn't be data entry clerks. Our AI extracts addresses from manifests instantly. You just drive.",
        "product_secb_title": "Pinpoint Precision.",
        "product_secb_desc": "We don't guess. We verify.",
        "product_secc_title": "Advanced Fleet Features.",
        "product_secc_desc": "Built for the realities of the road.",
        "cap_title": "Routing. Automated.",
        "cap_desc": "Replace manual review queues with automated certainty. No friction. Just delivery.",
        "flow_title": "Zero-friction integration.",
        "cta_title": "Ready to speed up your fleet?",
        "cta_desc": "Save 30 seconds per delivery.",
        "footer_desc": "The infrastructure for last-mile. No apps. Just results.",
        "sec2_title": "Zero Retention.",
        "sec2_desc": "Images processed. Instantly discarded. No data stored."
    },
    "tr": {
        "hero_desc": "Adres arayarak vakit kaybetmeyin. Etiketleri anında kesin koordinatlara dönüştürün. Sıfır manuel giriş, sıfır iade.",
        "hero_btn_whatsapp": "WhatsApp\\'ta Başlat",
        "comp_hero_title": "Kusursuz <span class=\"text-gradient\">Son Teslimat</span> İçin.",
        "comp_manifesto": "Lojistikte son kilometre kör noktadır. Sürücünüz adres arar, siz zarar edersiniz. Locy bu belirsizliği kesin konuma çevirir. Uygulama indirmek yok. Sadece net harita var.",
        "comp_val1_title": "Sürtünmesiz",
        "comp_val1_desc": "Uygulama yok. Eğitim yok. Filonuzun halihazırda olduğu yerde, WhatsApp\\'ta çalışıyoruz.",
        "comp_val2_title": "Milisaniyelik",
        "comp_val2_desc": "Gecikme süresi milisaniyelerle ölçülür. Çünkü sürücülerin beklemeye vakti yok.",
        "comp_val3_desc": "Sıfır veri saklama. Görüntüler koordinata dönüşür ve anında hafızadan silinir.",
        "eco_hero_title": "İlk Seferde Doğru.<br><span class=\"text-gradient-cyan\">Sıfır İade.</span>",
        "eco_hero_desc": "İade paketleri kârınızı eritir. Locy ile adresleri kargo aracı daha depodan çıkmadan %100 doğrulayın.",
        "eco_cta_title": "Teslimatları ölçeklemeye hazır mısınız?",
        "eco_cta_desc": "Teslimat başına 30 saniye kazanın.",
        "em_hero_title": "Her saniye <br><span class=\"text-gradient-alert\">önemli olduğunda.</span>",
        "em_hero_desc": "GPS 'Geldiniz' der, ancak kapı diğer sokaktadır. Locy acil durum ekiplerini doğru kapıya yönlendirir.",
        "rest_hero_title": "Sıcak yemek. <br><span class=\"text-gradient-red\">Akıllı teslimat.</span>",
        "rest_hero_desc": "Müşteriyi adres için aramak kâr marjınızı yok eder. Locy doğru kapıyı tek seferde bulur.",
        "product_hero_title": "Manuel Girişe <span class=\"text-gradient\">Son Verin.</span>",
        "product_hero_desc": "Fotoğrafı gönderin, milisaniyeler içinde kesin konumu alın. Sürücülerin kullanmak isteyeceği tek araç.",
        "product_seca_title": "Fotoğrafı çekin. <br>Gerisini biz hallederiz.",
        "product_seca_desc": "Sürücüler veri giriş personeli değildir. Yapay zekamız adresleri anında okur. Siz sadece sürün.",
        "product_secb_title": "Nokta Atışı Kesinlik.",
        "product_secb_desc": "Tahmin etmiyoruz. Doğruluyoruz.",
        "product_secc_title": "Gelişmiş Filo Özellikleri.",
        "product_secc_desc": "Yolun gerçekleri için tasarlandı.",
        "cap_title": "Otomatik, pürüzsüz yönlendirme.",
        "cap_desc": "Manuel süreci, kesin ve otomatik sistemle değiştirin. Gecikme yok. Sadece teslimat.",
        "flow_title": "Pürüzsüz entegrasyon.",
        "cta_title": "Filonuzu hızlandırmaya hazır mısınız?",
        "cta_desc": "Her teslimatta 30 saniye kazanın.",
        "footer_desc": "Son teslimat aşaması için güçlü altyapı. Uygulama yok. Anında sonuç.",
        "sec2_title": "Tam Gizlilik.",
        "sec2_desc": "Görseller işlenir. Anında silinir. Veri depolanmaz."
    },
    "de": {
        "hero_desc": "Suchen Sie nicht länger nach Adressen. Verwandeln Sie Paketfotos in Sekundenbruchteilen in exakte Koordinaten. Keine Tippfehler, keine Retouren.",
        "hero_btn_whatsapp": "Auf WhatsApp starten",
        "comp_hero_title": "Die Infrastruktur der <span class=\"text-gradient\">Letzten Meile.</span>",
        "comp_manifesto": "Logistik scheitert oft am letzten Meter. Fahrer verschwenden Zeit mit Tippen. Locy beendet das Raten und liefert sofortige digitale Präzision. Keine Apps. Nur exakte Daten.",
        "comp_val1_title": "Reibungslos",
        "comp_val1_desc": "Keine Apps. Kein Onboarding. Wir arbeiten dort, wo Ihre Flotte bereits ist: WhatsApp.",
        "comp_val2_title": "Millisekunden",
        "comp_val2_desc": "Wartezeit gibt es nicht. Unsere Latenz wird in Millisekunden gemessen.",
        "comp_val3_desc": "Null Datenspeicherung. Bilder werden zu Koordinaten und verschwinden sofort.",
        "eco_hero_title": "Direkt richtig.<br><span class=\"text-gradient-cyan\">Null Retouren.</span>",
        "eco_hero_desc": "Gescheiterte Lieferungen fressen Ihre Marge auf. Locy verifiziert jede Adresse, noch bevor das Fahrzeug das Depot verlässt.",
        "eco_cta_title": "Bereit zum Skalieren?",
        "eco_cta_desc": "Sparen Sie 30 Sekunden pro Stopp.",
        "em_hero_title": "Wenn jede <br><span class=\"text-gradient-alert\">Sekunde zählt.</span>",
        "em_hero_desc": "GPS sagt 'Sie sind da', aber die Tür ist woanders. Locy leitet Retter direkt zum richtigen Eingang.",
        "rest_hero_title": "Heißes Essen. <br><span class=\"text-gradient-red\">Schnelle Logistik.</span>",
        "rest_hero_desc": "Kunden nach dem Weg zu fragen, ruiniert Margen. Locy findet die exakte Tür. Immer.",
        "product_hero_title": "Tippen Sie nie wieder <span class=\"text-gradient\">Adressen.</span>",
        "product_hero_desc": "Senden Sie ein Foto über WhatsApp und erhalten Sie in Millisekunden die Koordinaten. Das Tool, das Fahrer nutzen.",
        "product_seca_title": "Foto machen. <br>Wir machen den Rest.",
        "product_seca_desc": "Fahrer sind keine Datenerfasser. Unsere KI liest jeden Zettel. Sie fahren.",
        "product_secb_title": "Punktgenau.",
        "product_secb_desc": "Wir raten nicht. Wir verifizieren.",
        "product_secc_title": "Für moderne Flotten.",
        "product_secc_desc": "Entwickelt für die Realität der Straße.",
        "cap_title": "Routing. Automatisiert.",
        "cap_desc": "Ersetzen Sie manuelle Prüfungen durch automatisierte Sicherheit. Keine Reibung.",
        "flow_title": "Reibungslose Integration.",
        "cta_title": "Bereit, Ihre Flotte zu beschleunigen?",
        "cta_desc": "Sparen Sie 30 Sekunden pro Lieferung.",
        "footer_desc": "Die Infrastruktur für die letzte Meile. Keine App. Nur Ergebnisse.",
        "sec2_title": "Kein Tracking.",
        "sec2_desc": "Bilder werden verarbeitet und sofort gelöscht. Null Speicherung."
    },
    "fr": {
        "hero_desc": "Ne tournez plus en rond. Transformez instantanément les photos de colis en coordonnées vérifiées. Zéro saisie. Zéro retour.",
        "hero_btn_whatsapp": "Lancer sur WhatsApp",
        "comp_hero_title": "L\\'infrastructure du <span class=\"text-gradient\">Dernier Kilomètre.</span>",
        "comp_manifesto": "La logistique échoue au dernier kilomètre. Les chauffeurs perdent du temps à taper. Locy apporte une précision numérique instantanée. Zéro app. Juste des coordonnées.",
        "comp_val1_title": "Sans Friction",
        "comp_val1_desc": "Aucune application. Aucun délai. Nous sommes là où se trouve votre flotte : WhatsApp.",
        "comp_val2_title": "Ultra Rapide",
        "comp_val2_desc": "Une latence mesurée en millisecondes. Parce que vos chauffeurs n\\'ont pas le temps d\\'attendre.",
        "comp_val3_desc": "Zéro conservation. Les images deviennent des coordonnées et s\\'effacent.",
        "eco_hero_title": "Du premier coup.<br><span class=\"text-gradient-cyan\">Zéro retour.</span>",
        "eco_hero_desc": "Les échecs détruisent vos marges. Locy vérifie chaque adresse avant le départ du camion.",
        "eco_cta_title": "Prêt à accélérer ?",
        "eco_cta_desc": "Gagnez 30 secondes par livraison.",
        "em_hero_title": "Quand chaque <br><span class=\"text-gradient-alert\">seconde compte.</span>",
        "em_hero_desc": "Le GPS dit 'Arrivé', mais la bonne porte est ailleurs. Locy guide les urgences vers la bonne entrée.",
        "rest_hero_title": "Repas chauds. <br><span class=\"text-gradient-red\">Action rapide.</span>",
        "rest_hero_desc": "Chercher l\\'adresse ruine vos marges. Locy trouve la porte exacte à chaque fois.",
        "product_hero_title": "Ne tapez plus <span class=\"text-gradient\">d\\'adresses.</span>",
        "product_hero_desc": "Transférez la photo via WhatsApp. Obtenez les coordonnées en millisecondes. L\\'outil préféré des livreurs.",
        "product_seca_title": "Prenez une photo. <br>Nous faisons le reste.",
        "product_seca_desc": "La conduite d\\'abord. Notre IA lit tout. Vous conduisez.",
        "product_secb_title": "Précision Extrême.",
        "product_secb_desc": "Nous ne devinons pas. Nous vérifions.",
        "cap_title": "Routage. Automatisé.",
        "cap_desc": "Remplacez le contrôle manuel par la certitude automatisée. Juste la livraison.",
        "flow_title": "Intégration transparente.",
        "cta_title": "Prêt à booster votre flotte ?",
        "cta_desc": "Économisez 30 secondes par arrêt.",
        "footer_desc": "L\\'infrastructure du dernier kilomètre. Sans appli. Juste des résultats.",
        "sec2_title": "Confidentialité Totale.",
        "sec2_desc": "Images traitées. Supprimées instantanément. Zéro stockage."
    },
    "es": {
        "hero_desc": "Deja de dar vueltas. Transforma fotos de paquetes en coordenadas verificadas al instante. Cero ingresos manuales. Cero devoluciones.",
        "hero_btn_whatsapp": "Lanzar en WhatsApp",
        "comp_hero_title": "La infraestructura para <span class=\"text-gradient\">La Última Milla.</span>",
        "comp_manifesto": "La logística falla en la puerta. Los conductores pierden tiempo escribiendo. Locy brinda precisión digital instantánea. Sin apps. Solo coordenadas.",
        "comp_val1_title": "Sin Fricción",
        "comp_val1_desc": "Sin instalaciones. Sin tutoriales. Funcionamos donde ya opera su flota: WhatsApp.",
        "comp_val2_title": "Cero Demoras",
        "comp_val2_desc": "Latencia medida en milisegundos. Porque sus conductores no tienen tiempo de esperar.",
        "comp_val3_desc": "Cero retención de datos. Las imágenes se convierten en coordenadas y se borran.",
        "eco_hero_title": "A la primera.<br><span class=\"text-gradient-cyan\">Cero devoluciones.</span>",
        "eco_hero_desc": "Las entregas fallidas destruyen sus márgenes. Locy verifica cada dirección antes de la salida.",
        "eco_cta_title": "¿Listo para escalar?",
        "eco_cta_desc": "Ahorre 30 segundos por parada.",
        "em_hero_title": "Cuando cada <br><span class=\"text-gradient-alert\">segundo cuenta.</span>",
        "em_hero_desc": "El GPS dice 'Has llegado', pero la puerta está lejos. Locy guía al personal a la entrada exacta.",
        "rest_hero_title": "Comida caliente. <br><span class=\"text-gradient-red\">Entrega rápida.</span>",
        "rest_hero_desc": "Llamar a los clientes destruye sus ganancias. Locy encuentra la puerta correcta, siempre.",
        "product_hero_title": "Nunca vuelvas a <span class=\"text-gradient\">escribir direcciones.</span>",
        "product_hero_desc": "Reenvía una foto por WhatsApp y obtén coordenadas en milisegundos. La única herramienta que los conductores usan.",
        "product_seca_title": "Toma una foto. <br>Nosotros haremos el resto.",
        "product_seca_desc": "Los conductores solo deben conducir. Nuestra IA extrae las direcciones. Así de fácil.",
        "product_secb_title": "Precisión Exacta.",
        "product_secb_desc": "No adivinamos. Verificamos.",
        "cap_title": "Rutas. Automatizadas.",
        "cap_desc": "Reemplace los procesos manuales por certeza automatizada.",
        "flow_title": "Integración sin fricción.",
        "cta_title": "¿Listo para acelerar tu flota?",
        "cta_desc": "Ahorre 30 segundos por entrega.",
        "footer_desc": "La infraestructura de la última milla. Solo resultados.",
        "sec2_title": "Privacidad Total.",
        "sec2_desc": "Imágenes procesadas y eliminadas. Cero almacenamiento."
    },
    "ee": {
        "hero_desc": "Ärge sõitke enam ringi. Muutke piltidest koordinaadid hetkega. Ei mingit käsitsi sisestamist. Null tagastust.",
        "hero_btn_whatsapp": "Ava WhatsAppis",
        "comp_hero_title": "Infrastruktuur <span class=\"text-gradient\">viimase kilomeetri jaoks.</span>",
        "comp_manifesto": "Logistika algab sageli valest uksest. Meie anname kohese digitaalse täpsuse.",
        "eco_hero_title": "Kohe õigesti.<br><span class=\"text-gradient-cyan\">Null tagastust.</span>",
        "eco_hero_desc": "Locy kinnitab iga aadressi enne laost väljumist.",
        "product_hero_title": "Ära sisesta enam <span class=\"text-gradient\">aadresse.</span>",
        "product_hero_desc": "Saada pilt WhatsAppi ja saa koordinaadid millisekunditega. Reaalne lahendus.",
        "product_seca_title": "Tee pilt. <br>Ja kõik.",
        "cap_title": "Nutikad marsruudid.",
        "flow_title": "Lihtne integreerimine.",
        "footer_desc": "Viimase kilomeetri infrastruktuur.",
        "sec2_title": "Null Andmete Säilitamist."
    },
    "it": {
        "hero_desc": "Basta girare a vuoto. Trasforma istantaneamente le foto in coordinate verificate. Zero inserimenti manuali. Zero resi.",
        "hero_btn_whatsapp": "Apri su WhatsApp",
        "comp_hero_title": "L\\'infrastruttura per <span class=\"text-gradient\">L\\'Ultimo Miglio.</span>",
        "comp_manifesto": "La logistica si blocca all\\'ultimo miglio. I guidatori perdono tempo a digitare. Locy offre precisione istantanea. Nessuna app. Solo coordinate.",
        "eco_hero_title": "Buona la prima.<br><span class=\"text-gradient-cyan\">Zero resi.</span>",
        "eco_hero_desc": "Le consegne fallite azzerano i margini. Locy verifica le località prima di partire.",
        "product_hero_title": "Mai più indirizzi <span class=\"text-gradient\">da digitare.</span>",
        "product_hero_desc": "Inoltra foto su WhatsApp. Ottieni coordinate istantanee. Lo strumento che i corrieri usano.",
        "cap_title": "Automazione del Routing.",
        "flow_title": "Integrazione trasparente.",
        "footer_desc": "L\\'infrastruttura dell\\'ultimo miglio. Senza App.",
        "sec2_title": "Rifiuto Archiviazione."
    }
}

filepath = 'c:/Users/Mahir/Desktop/Locy/locales/translations.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

for lang, kv in updates.items():
    lang_start = text.find(f'"{lang}": {{')
    if lang_start == -1:
        lang_start = text.find(f"'{lang}': {{")
    if lang_start == -1:
        lang_start = text.find(f"{lang}: {{")
    
    if lang_start != -1:
        lang_end = text.find('},', lang_start)
        if lang_end == -1: 
            lang_end = len(text)
            
        block = text[lang_start:lang_end]
        
        for k, v in kv.items():
            pattern = r'("' + k + r'"\s*:\s*)"((?:\\.|[^"\\])*)"'
            replacement = r'\1"' + v.replace('"', '\\"') + '"'
            block = re.sub(pattern, replacement, block)
            
        text = text[:lang_start] + block + text[lang_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Replacement complete.")
