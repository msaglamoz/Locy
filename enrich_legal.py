import os
import re
import json

legal_updates = {
    # EN
    "en": {
        "cap_1_title": "Optimized Routing",
        "priv_title": "Privacy Policy",
        "priv_date": "Last Updated: January 16, 2026",
        "priv_h1": "1. Information We Collect",
        "priv_p1_1": "We collect the absolute minimum data required to provide our location services.",
        "priv_p1_2": "WhatsApp logs limited to metadata and phone numbers for routing context.",
        "priv_p1_3": "Package images submitted strictly for real-time address extraction.",
        "priv_h2": "2. Zero Retention Architecture",
        "priv_p2_1": "Locy operates strictly as a stateless processor by design.",
        "priv_p2_2": "Images sent to our processing system are converted to coordinates and routing data, then immediately purged from volatile memory.",
        "priv_h3": "3. How We Use Data",
        "priv_p3_1": "We use incoming data solely to provide real-time location intelligence.",
        "priv_p3_2": "We absolutely never use your proprietary delivery data to train our core foundation models.",
        "priv_h4": "4. Data Sharing & Third Parties",
        "priv_p4_1": "We never sell your data. We rely on enterprise-grade EU infrastructure providers bound by strict DPA agreements.",
        "priv_h5": "5. International Rights",
        "priv_p5_1": "As an EU-based infrastructure company, all our users globally benefit from strict GDPR-level privacy protections.",
        "priv_h6": "6. Data Controller & Contact",
        "priv_p6_1": "The entity responsible for processing your data is ThinkPoint OÜ.",
        "priv_p6_2": "Registry Code: 17131887 | Narva mnt 5, Tallinn 10117, Estonia | legal@thinkpoint.ee",
        "terms_title": "Terms of Service",
        "terms_date": "Effective Date: January 16, 2026",
        "terms_h1": "1. Acceptance of Terms",
        "terms_p1_1": "By integrating or using Locy's bot and API infrastructure, you agree to be bound by these Terms of Service.",
        "terms_h2": "2. Service Description",
        "terms_p2_1": "Locy is a spatial intelligence platform designed for the logistics, food delivery, and emergency sectors.",
        "terms_h3": "3. Acceptable Use Policy",
        "terms_p3_1": "You may only submit images related to genuine logistics or address verification tasks.",
        "terms_p3_2": "Reverse-engineering our API, scraping data, or abusing the service for unsupported purposes will result in permanent termination of access.",
        "terms_h4": "4. Service Level Agreement (SLA)",
        "terms_p4_1": "Enterprise customers under contract are guaranteed a 99.9% uptime SLA with priority routing queues.",
        "terms_h5": "5. Intellectual Property",
        "terms_p5_1": "ThinkPoint OÜ retains all rights, title, and interest in Locy software, ML models, and branding.",
        "terms_h6": "6. Governing Law",
        "terms_p6_1": "These Terms are governed by the laws of the Republic of Estonia.",
    },
    # TR
    "tr": {
        "cap_1_title": "Kusursuz Rota Planlama",
        "priv_title": "Gizlilik Politikası",
        "priv_date": "Son Güncelleme: 16 Ocak 2026",
        "priv_h1": "1. Topladığımız Bilgiler",
        "priv_p1_1": "Hizmetlerimizi sunabilmek için mümkün olan en asgari düzeyde veri topluyoruz.",
        "priv_p1_2": "Rota bağlamı için telefon numaraları ve meta verilere sınırlı WhatsApp kayıtları.",
        "priv_p1_3": "Sadece gerçek zamanlı adres çıkarımı amacıyla gönderilen kargo ve etiket görselleri.",
        "priv_h2": "2. Sıfır Veri Saklama Mimarisi",
        "priv_p2_1": "Locy, tamamen geçici bellek (stateless) kullanan bir işlemci olarak tasarlanmıştır.",
        "priv_p2_2": "İşleme sistemimize gönderilen görüntüler saniyeler içinde koordinat ve rotaya dönüştürülür ve hafızadan kalıcı olarak silinir.",
        "priv_h3": "3. Verileri Nasıl Kullanıyoruz",
        "priv_p3_1": "Gelen verileri yalnızca size gerçek zamanlı konum ve yönlendirme sağlamak için kullanırız.",
        "priv_p3_2": "Kendi özel teslimat verilerinizi temel yapay zeka modellerimizi eğitmek için KESİNLİKLE kullanmıyoruz.",
        "priv_h4": "4. Veri Paylaşımı",
        "priv_p4_1": "Verilerinizi asla satmayız. İşlemler için sıkı gizlilik sözleşmelerine bağlı kurumsal seviye bulut sağlayıcıları kullanıyoruz.",
        "priv_h5": "5. Uluslararası Haklar",
        "priv_p5_1": "AB merkezli bir altyapı şirketi olarak, küresel tüm kullanıcılarımıza GDPR düzeyinde katı gizlilik koruması sağlıyoruz.",
        "priv_h6": "6. Veri Sorumlusu ve İletişim",
        "priv_p6_1": "Verilerinizin işlenmesinden sorumlu kuruluş ThinkPoint OÜ'dür.",
        "priv_p6_2": "Kayıt Numarası: 17131887 | Narva mnt 5, Tallinn 10117, Estonya | legal@thinkpoint.ee",
        "terms_title": "Hizmet Şartları",
        "terms_date": "Yürürlük Tarihi: 16 Ocak 2026",
        "terms_h1": "1. Şartların Kabulü",
        "terms_p1_1": "Locy'nin altyapısını veya botunu kullanarak, bu Hizmet Şartlarına bağlı kalmayı kabul edersiniz.",
        "terms_h2": "2. Hizmet Açıklaması",
        "terms_p2_1": "Locy, lojistik, yemek teslimatı ve acil servis sektörleri için tasarlanmış uzamsal bir yapay zeka platformudur.",
        "terms_h3": "3. Kabul Edilebilir Kullanım Politikası",
        "terms_p3_1": "Yalnızca gerçek teslimat operasyonları veya adres doğrulama ile ilgili görselleri gönderebilirsiniz.",
        "terms_p3_2": "API kaynağımızı kırmak, veri kazımak (scraping) veya sistemi amacı dışında kötüye kullanmak hizmetin kalıcı olarak iptaliyle sonuçlanır.",
        "terms_h4": "4. Hizmet Seviyesi Anlaşması (SLA)",
        "terms_p4_1": "Kurumsal müşterilerimize sözleşmeleri kapsamında %99.9 çalışma süresi ve öncelikli rota garantisi sunulur.",
        "terms_h5": "5. Fikri Mülkiyet",
        "terms_p5_1": "ThinkPoint OÜ, Locy'nin yazılımı, makine öğrenimi modelleri ve markası üzerindeki tüm hakları saklı tutar.",
        "terms_h6": "6. Geçerli Kanun",
        "terms_p6_1": "Bu Şartlar Estonya Cumhuriyeti yasalarına tabidir ve buna göre yorumlanır.",
    },
    # DE
    "de": {
        "cap_1_title": "Perfektes Routing",
        "priv_title": "Datenschutzerklärung",
        "priv_date": "Zuletzt aktualisiert: 16. Januar 2026",
        "priv_h1": "1. Gesammelte Informationen",
        "priv_p1_1": "Wir erfassen nur die unbedingt erforderlichen Daten, um unsere Dienste bereitzustellen.",
        "priv_p1_2": "WhatsApp-Protokolle beschränkt auf Metadaten für den Routing-Kontext.",
        "priv_p1_3": "Paketbilder, die ausschließlich zur Echtzeit-Adresserkennung übermittelt werden.",
        "priv_h2": "2. Zero-Retention-Architektur",
        "priv_p2_1": "Locy arbeitet streng als zustandsloser Prozessor (Stateless).",
        "priv_p2_2": "An unser System gesendete Bilder werden in Koordinaten umgewandelt und sofort aus dem flüchtigen Speicher gelöscht.",
        "priv_h3": "3. Datennutzung",
        "priv_p3_1": "Wir nutzen Daten ausschließlich zur Bereitstellung von Echtzeit-Standortintelligenz.",
        "priv_p3_2": "Wir trainieren unsere Kernmodelle niemals mit Ihren proprietären Lieferdaten.",
        "priv_h4": "4. Datenweitergabe",
        "priv_p4_1": "Wir verkaufen niemals Ihre Daten. Wir nutzen Enterprise-Cloud-Anbieter unter strengen DSGVO-Verträgen.",
        "priv_h5": "5. Internationale Rechte",
        "priv_p5_1": "Als EU-basiertes Unternehmen genießen alle Nutzer automatisch DSGVO-konformen Datenschutz.",
        "priv_h6": "6. Verantwortliche Stelle",
        "priv_p6_1": "Die für die Verarbeitung Verantwortliche Stelle ist ThinkPoint OÜ.",
        "priv_p6_2": "Registernummer: 17131887 | Narva mnt 5, Tallinn 10117, Estland | legal@thinkpoint.ee",
        "terms_title": "Allgemeine Geschäftsbedingungen",
        "terms_date": "Inkrafttreten: 16. Januar 2026",
        "terms_h1": "1. Annahme der Bedingungen",
        "terms_p1_1": "Durch die Nutzung der Locy-Infrastruktur stimmen Sie diesen Bedingungen zu.",
        "terms_h2": "2. Leistungsbeschreibung",
        "terms_p2_1": "Locy ist eine Spatial-Intelligence-Plattform für Logistik, Essenslieferdienste und Notfälle.",
        "terms_h3": "3. Richtlinie zur akzeptablen Nutzung",
        "terms_p3_1": "Sie dürfen nur Bilder übermitteln, die mit echten Lieferungen oder Adressprüfungen in Zusammenhang stehen.",
        "terms_p3_2": "Reverse Engineering, Scraping oder sonstiger Missbrauch führt zur sofortigen Kündigung.",
        "terms_h4": "4. Service Level Agreement (SLA)",
        "terms_p4_1": "Vertragliche Enterprise-Kunden erhalten eine 99,9% Uptime-Garantie und priorisierte Warteschlangen.",
        "terms_h5": "5. Geistiges Eigentum",
        "terms_p5_1": "ThinkPoint OÜ behält alle Rechte an Locy-Software, ML-Modellen und Marken.",
        "terms_h6": "6. Geltendes Recht",
        "terms_p6_1": "Diese Bedingungen unterliegen estnischem Recht.",
    },
    # FR
    "fr": {
        "cap_1_title": "Routage Intelligent",
        "priv_title": "Politique de Confidentialité",
        "priv_date": "Dernière mise à jour : 16 janvier 2026",
        "priv_h1": "1. Informations Recueillies",
        "priv_p1_1": "Nous collectons le strict minimum nécessaire pour fournir nos services.",
        "priv_p1_2": "Logs WhatsApp limités aux métadonnées.",
        "priv_p1_3": "Images envoyées uniquement pour l'extraction d'adresses en temps réel.",
        "priv_h2": "2. Architecture Zéro Rétention",
        "priv_p2_1": "Locy fonctionne strictement comme un processeur sans état.",
        "priv_p2_2": "Les images sont converties en coordonnées et immédiatement purgées de la mémoire volatile.",
        "priv_h3": "3. Utilisation des Données",
        "priv_p3_1": "Nous utilisons les données uniquement pour fournir un routage immédiat.",
        "priv_p3_2": "Nous n'entraînons jamais nos modèles de base avec vos données de livraison.",
        "priv_h4": "4. Partage de Données",
        "priv_p4_1": "Nous ne vendons pas vos données. Nous collaborons avec des hébergeurs européens conformes au RGPD.",
        "priv_h5": "5. Droits Internationaux",
        "priv_p5_1": "En tant qu'entreprise européenne, nos utilisateurs bénéficient des protections du RGPD.",
        "priv_h6": "6. Contrôleur des Données",
        "priv_p6_1": "L'entité responsable du traitement est ThinkPoint OÜ.",
        "priv_p6_2": "Code: 17131887 | Narva mnt 5, Tallinn 10117, Estonie | legal@thinkpoint.ee",
        "terms_title": "Conditions Générales",
        "terms_date": "Date d'entrée en vigueur : 16 janvier 2026",
        "terms_h1": "1. Acceptation des Conditions",
        "terms_p1_1": "En utilisant l'infrastructure de Locy, vous acceptez ces Conditions Générales.",
        "terms_h2": "2. Description du Service",
        "terms_p2_1": "Locy est une plateforme d'intelligence spatiale pour la logistique et les urgences.",
        "terms_h3": "3. Utilisation Acceptable",
        "terms_p3_1": "Ne soumettez que des images liées à des livraisons réelles.",
        "terms_p3_2": "Le reverse engineering ou l'abus du système entraînera l'annulation de l'accès.",
        "terms_h4": "4. Niveau de Service (SLA)",
        "terms_p4_1": "Les clients Enterprise sous contrat bénéficient d'une SLA de 99,9%.",
        "terms_h5": "5. Propriété Intellectuelle",
        "terms_p5_1": "ThinkPoint OÜ conserve tous les droits sur les logiciels et modèles ML de Locy.",
        "terms_h6": "6. Loi Applicable",
        "terms_p6_1": "Ces Conditions sont régies par les lois de l'Estonie.",
    },
    # ES
    "es": {
        "cap_1_title": "Rutas Optimizadas",
        "priv_title": "Política de Privacidad",
        "priv_date": "Última Actualización: 16 de enero de 2026",
        "priv_h1": "1. Información que Recopilamos",
        "priv_p1_1": "Recopilamos el mínimo de datos para proporcionar nuestros servicios.",
        "priv_p1_2": "Datos de WhatsApp limitados a metadatos de enrutamiento.",
        "priv_p1_3": "Imágenes exclusivas para la extracción de ubicación en tiempo real.",
        "priv_h2": "2. Arquitectura de Cero Retención",
        "priv_p2_1": "Locy opera como un procesador sin estado (stateless).",
        "priv_p2_2": "Las imágenes enviadas a nuestro sistema se purgan de la memoria de inmediato.",
        "priv_h3": "3. Uso de Datos",
        "priv_p3_1": "Utilizamos los datos exclusivamente para ofrecer inteligencia espacial inmediata.",
        "priv_p3_2": "Nunca entrenamos modelos básicos con los datos privados de sus clientes.",
        "priv_h4": "4. Terceros",
        "priv_p4_1": "No vendemos datos. Operamos con proveedores empresariales bajo el RGPD.",
        "priv_h5": "5. Derechos Globales",
        "priv_p5_1": "Todos los usuarios globales se benefician de la seguridad RGPD de la UE.",
        "priv_h6": "6. Contacto Legal",
        "priv_p6_1": "La entidad responsable es ThinkPoint OÜ.",
        "priv_p6_2": "Registro: 17131887 | Narva mnt 5, Tallinn 10117, Estonia | legal@thinkpoint.ee",
        "terms_title": "Términos de Servicio",
        "terms_date": "Fecha Efectiva: 16 de enero de 2026",
        "terms_h1": "1. Aceptación",
        "terms_p1_1": "Al usar Locy, aceptas legalmente estos Términos.",
        "terms_h2": "2. Servicio",
        "terms_p2_1": "Locy es una plataforma de enrutamiento para logística y urgencias.",
        "terms_h3": "3. Uso Aceptable",
        "terms_p3_1": "Solo se pueden enviar solicitudes legítimas de logística.",
        "terms_p3_2": "Cualquier intento de fraude, ingeniería inversa o scraping será bloqueado permanentemente.",
        "terms_h4": "4. SLA Empresarial",
        "terms_p4_1": "Garantizamos 99.9% de uptime para clientes empresariales bajo contrato.",
        "terms_h5": "5. Propiedad Intelectual",
        "terms_p5_1": "ThinkPoint OÜ posee todos los derechos sobre Locy.",
        "terms_h6": "6. Ley Aplicable",
        "terms_p6_1": "Estos términos se rigen por las leyes de Estonia.",
    },
    # EE (Estonian)
    "ee": {
        "cap_1_title": "Nutikas Marsruutimine",
        "priv_title": "Privaatsuspoliitika",
        "priv_date": "Uuendatud: 16. jaanuar 2026",
        "priv_h1": "1. Kogutavad Andmed",
        "priv_p1_1": "Kogume teenuse osutamiseks vaid minimaalset teavet.",
        "priv_p1_2": "WhatsAppi logid on piiratud ainult metaandmetega.",
        "priv_p1_3": "Pildid aitavad meil pakkuda reaalajas koordinaate.",
        "priv_h2": "2. Salvestamise Puudumine",
        "priv_p2_1": "Meie süsteem ei talleta andmeid.",
        "priv_p2_2": "Pildid muudetakse koordinaatideks ja kustutatakse muutmälu abil kohe.",
        "priv_h3": "3. Andmete Kasutus",
        "priv_p3_1": "Andmeid kasutatakse ainult asukoha leidmiseks.",
        "priv_p3_2": "Me ei õpeta tehisaru kasutades teie isiklikke tarneandmeid.",
        "priv_h4": "4. Kolmandad Osapooled",
        "priv_p4_1": "Me ei müü kunagi teie andmeid.",
        "priv_h5": "5. Turvalisus",
        "priv_p5_1": "Locy töötab täielikus vastavuses EL-i andmekaitseseadustega.",
        "priv_h6": "6. Vastutav Töötleja",
        "priv_p6_1": "Andmete eest vastutab ThinkPoint OÜ.",
        "priv_p6_2": "Kood: 17131887 | Narva mnt 5, Tallinn 10117, Eesti | legal@thinkpoint.ee",
        "terms_title": "Teenusetingimused",
        "terms_date": "Jõustub: 16. jaanuar 2026",
        "terms_h1": "1. Nõustumine",
        "terms_p1_1": "Teenuseid kasutades nõustute meie tingimustega.",
        "terms_h2": "2. Teenus",
        "terms_p2_1": "Locy pakub logistikale digitaalset täpsust.",
        "terms_h3": "3. Hea Tava",
        "terms_p3_1": "Teenust tohib kasutada vaid seaduslikel tarnetel.",
        "terms_p3_2": "API pahatahtlik kasutamine on keelatud ja toob kaasa konto sulgemise.",
        "terms_h4": "4. SLA",
        "terms_p4_1": "Lepingulistel klientidel on 99.9% tööaja garantii.",
        "terms_h5": "5. Omandiõigus",
        "terms_p5_1": "Kõik õigused kuuluvad ThinkPoint OÜ-le.",
        "terms_h6": "6. Seadusandlus",
        "terms_p6_1": "Neid tingimusi reguleerib Eesti Vabariigi seadusandlus.",
    },
    # IT
    "it": {
        "cap_1_title": "Routing Ottimizzato",
        "priv_title": "Informativa sulla Privacy",
        "priv_date": "Ultimo aggiornamento: 16 gennaio 2026",
        "priv_h1": "1. Dati Raccolti",
        "priv_p1_1": "Raccogliamo il minimo indispensabile per i servizi di localizzazione.",
        "priv_p1_2": "Log di WhatsApp limitati ai metadati.",
        "priv_p1_3": "Immagini lette in tempo reale esclusivamente per ricavare l'indirizzo.",
        "priv_h2": "2. Zero Conservazione",
        "priv_p2_1": "Zero archiviazione persistente nel database.",
        "priv_p2_2": "Le foto diventano testi ed evaporano in millisecondi dalla RAM.",
        "priv_h3": "3. Utilizzo Dati",
        "priv_p3_1": "Gestiamo i flussi solo ed unicamente per rispondere ai fattorini.",
        "priv_p3_2": "Garantito: nessun modello IA viene addestrato con le tue consegne private.",
        "priv_h4": "4. Terze Parti",
        "priv_p4_1": "Mai dati venduti. Appoggi cloud schermati GDPR di alta fascia.",
        "priv_h5": "5. Tutela Globale",
        "priv_p5_1": "Applichiamo gli stringenti standard UE.",
        "priv_h6": "6. Titolare del Trattamento",
        "priv_p6_1": "Il responsabile è ThinkPoint OÜ.",
        "priv_p6_2": "P.Iva Estone: 17131887 | Narva mnt 5, Tallinn | legal@thinkpoint.ee",
        "terms_title": "Termini di Servizio",
        "terms_date": "In vigore: 16 gennaio 2026",
        "terms_h1": "1. Accettazione",
        "terms_p1_1": "L'uso assenso passivo della privacy estone e UE.",
        "terms_h2": "2. Cos'è Locy?",
        "terms_p2_1": "Locy è una piattaforma operativa logistica non rimborsabile senza app.",
        "terms_h3": "3. Uso Legittimo",
        "terms_p3_1": "Mandaci solo foto attinenti ai tuoi pacchi da depositare.",
        "terms_p3_2": "Abusare delle route causa ban permanente.",
        "terms_h4": "4. Impegno Enterprise",
        "terms_p4_1": "Server in garanzia uptime al 99.9%.",
        "terms_h5": "5. Diritto Software",
        "terms_p5_1": "Copyright intellettuale di ThinkPoint OÜ.",
        "terms_h6": "6. Normativa",
        "terms_p6_1": "Si applicano le corti in Estonia.",
    }
}

# The existing keys will be replaced or appended to translations.js.
# Actually, since the privacy keys exist, let's just re-inject them and clean up the old ones.
# Or simpler: load JSON, update TR keys, update all keys, dump string matching the structure.
# But it's simpler to just do string manipulation. We'll find each language block and replace it.
# We have a dictionary of dicts. We can use python's json tool to dump the dict, then replace inside the JS block.

filepath = 'c:/Users/Mahir/Desktop/Locy/locales/translations.js'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()
    
for lang, doc in legal_updates.items():
    lang_start = text.find(f'"{lang}": {{')
    if lang_start == -1: continue
    
    lang_end = text.find('},', lang_start)
    if lang_end == -1: lang_end = text.find('}\n', lang_start)
    if lang_end == -1: lang_end = len(text)
    
    block = text[lang_start:lang_end]
    
    # Let's remove old priv/terms lines from block to avoid duplicates
    lines = block.split('\n')
    new_lines = []
    for line in lines:
        if '"priv_' in line or '"terms_' in line or '"cap_1_title"' in line:
            continue
        new_lines.append(line)
    
    block = '\n'.join(new_lines)
    
    # Inject new ones right after the opening brace
    brace_idx = block.find('{')
    injection = ""
    for k, v in doc.items():
        v_escaped = v.replace('"', '\\"')
        injection += f'\n        "{k}": "{v_escaped}",'
    
    block = block[:brace_idx+1] + injection + block[brace_idx+1:]
    
    text = text[:lang_start] + block + text[lang_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated translations.js with extended legal pages.")
