import json

new_data = {
    "en": {
        "priv_title": "Privacy Policy",
        "priv_date": "Last Updated: January 16, 2026",
        "priv_h1": "1. Zero Retention Architecture",
        "priv_p1": "Locy is designed as a stateless processor. Images sent to our processing system are converted to coordinates and routing data, then immediately flushed from volatile memory.",
        "priv_h2": "2. Data Processing",
        "priv_p2": "We use Multimodal AI to analyze address labels. This processing happens in real-time. We do not use customer data to train our core models.",
        "priv_h3": "3. Data Controller",
        "priv_p3": "The entity responsible for processing your data is <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Registry Code: 17131887<br>Address: Narva mnt 5, Tallinn 10117, Estonia<br>Contact: legal@thinkpoint.ee",
        
        "terms_title": "Terms & Conditions",
        "terms_date": "Effective Date: January 16, 2026",
        "terms_h1": "1. Service Provider",
        "terms_p1": "Locy is a service provided by <strong>ThinkPoint OÜ</strong> (Registry Code: 17131887), a limited liability company incorporated under the laws of Estonia.",
        "terms_h2": "2. Acceptable Use Policy",
        "terms_p2": "By using Locy, you agree to submit only images related to logistics and address verification. We reserve the right to terminate access for abusive traffic patterns.",
        "terms_h3": "3. Governing Law",
        "terms_p3": "These Terms shall be governed by and construed in accordance with the laws of the Republic of Estonia."
    },
    "tr": {
        "priv_title": "Gizlilik Politikası",
        "priv_date": "Son Güncelleme: 16 Ocak 2026",
        "priv_h1": "1. Sıfır Veri Saklama Mimarisi",
        "priv_p1": "Locy tamamen geçici (stateless) bir veri işlemcisidir. Sisteme gönderilen adres görüntüleri sadece koordinat ve rotaya dönüştürülür ve geçici bellekten hemen silinir.",
        "priv_h2": "2. Veri İşleme",
        "priv_p2": "Adresleri analiz etmek için Çok Modlu Yapay Zeka kullanıyoruz. Bu işlem gerçek zamanlı gerçekleşir. Temel modellerimizi eğitmek için müşteri verilerini kesinlikle kullanmıyoruz.",
        "priv_h3": "3. Veri Sorumlusu",
        "priv_p3": "Verilerinizin işlenmesinden sorumlu kuruluş <strong>ThinkPoint OÜ</strong> firmasıdır.",
        "priv_p4": "Kayıt Numarası: 17131887<br>Adres: Narva mnt 5, Tallinn 10117, Estonya<br>İletişim: legal@thinkpoint.ee",
        
        "terms_title": "Kullanım Koşulları",
        "terms_date": "Yürürlük Tarihi: 16 Ocak 2026",
        "terms_h1": "1. Hizmet Sağlayıcı",
        "terms_p1": "Locy, Estonya yasalarına göre kurulmuş sınırlı sorumlu bir şirket olan <strong>ThinkPoint OÜ</strong> (Kayıt Numarası: 17131887) tarafından sağlanan bir hizmettir.",
        "terms_h2": "2. Kabul Edilebilir Kullanım Politikası",
        "terms_p2": "Locy'i kullanarak, yalnızca lojistik ve adres doğrulaması ile ilgili görüntüleri göndermeyi kabul edersiniz. Kötü niyetli trafik modelleri için erişimi sonlandırma hakkımızı saklı tutuyoruz.",
        "terms_h3": "3. Geçerli Kanun",
        "terms_p3": "Bu Koşullar, Estonya Cumhuriyeti yasalarına tabidir ve bu yasalara göre yorumlanacaktır."
    },
    "de": {
        "priv_title": "Datenschutzerklärung",
        "priv_date": "Zuletzt aktualisiert: 16. Januar 2026",
        "priv_h1": "1. Architektur ohne Vorratsspeicherung",
        "priv_p1": "Locy ist als zustandsloser Prozessor konzipiert. Bilder, die an unser Verarbeitungssystem gesendet werden, werden sofort gelöscht.",
        "priv_h2": "2. Datenverarbeitung",
        "priv_p2": "Wir verwenden Multimodale KI, um Adressetiketten zu analysieren. Wir verwenden keine Kundendaten, um unsere KI Modelle zu trainieren.",
        "priv_h3": "3. Datenverantwortlicher",
        "priv_p3": "Die für die Verarbeitung Ihrer Daten verantwortliche Stelle ist <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Registernummer: 17131887<br>Adresse: Narva mnt 5, Tallinn 10117, Estland<br>Kontakt: legal@thinkpoint.ee",
        
        "terms_title": "Allgemeine Geschäftsbedingungen",
        "terms_date": "Datum des Inkrafttretens: 16. Januar 2026",
        "terms_h1": "1. Dienstleister",
        "terms_p1": "Locy ist ein Dienst der <strong>ThinkPoint OÜ</strong> (Registernummer: 17131887), einer nach den Gesetzen der Republik Estland gegründeten Gesellschaft mit beschränkter Haftung.",
        "terms_h2": "2. Richtlinie zur akzeptablen Nutzung",
        "terms_p2": "Durch die Nutzung von Locy stimmen Sie zu, nur Bilder im Zusammenhang mit Logistik und Adressüberprüfung zu übermitteln. Wir behalten uns das Recht vor, den Zugang bei missbräuchlichem Traffic zu kündigen.",
        "terms_h3": "3. Geltendes Recht",
        "terms_p3": "Diese Bedingungen unterliegen den Gesetzen der Republik Estland und werden in Übereinstimmung mit diesen ausgelegt."
    },
    "fr": {
        "priv_title": "Politique de Confidentialité",
        "priv_date": "Dernière mise à jour : 16 janvier 2026",
        "priv_h1": "1. Architecture Sans Rétention",
        "priv_p1": "Locy est conçu comme un processeur sans état. Les images envoyées à notre système de traitement sont purgées de la mémoire volatile immédiatement.",
        "priv_h2": "2. Traitement des Données",
        "priv_p2": "Nous utilisons une IA Multimodale. Nous n'utilisons pas les données des clients pour entraîner nos modèles de base.",
        "priv_h3": "3. Contrôleur des Données",
        "priv_p3": "L'entité responsable du traitement de vos données est <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Code d'enregistrement : 17131887<br>Adresse : Narva mnt 5, Tallinn 10117, Estonie<br>Contact : legal@thinkpoint.ee",
        
        "terms_title": "Conditions Générales",
        "terms_date": "Date d'entrée en vigueur : 16 janvier 2026",
        "terms_h1": "1. Fournisseur de Service",
        "terms_p1": "Locy est un service fourni par <strong>ThinkPoint OÜ</strong> (Code d'enregistrement : 17131887).",
        "terms_h2": "2. Politique d'Utilisation Acceptable",
        "terms_p2": "En utilisant Locy, vous acceptez de ne soumettre que des images liées à la logistique.",
        "terms_h3": "3. Loi Applicable",
        "terms_p3": "Ces Conditions sont régies par et interprétées conformément aux lois de la République d'Estonie."
    },
    "es": {
        "priv_title": "Política de Privacidad",
        "priv_date": "Última Actualización: 16 de enero de 2026",
        "priv_h1": "1. Arquitectura de Cero Retención",
        "priv_p1": "Locy está diseñado como un procesador sin estado. Las imágenes se purgan de la memoria de inmediato.",
        "priv_h2": "2. Procesamiento de Datos",
        "priv_p2": "Utilizamos IA Multimodal en tiempo real. No utilizamos datos de clientes para entrenar nuestros modelos.",
        "priv_h3": "3. Controlador de Datos",
        "priv_p3": "La entidad responsable de procesar sus datos es <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Código de Registro: 17131887<br>Dirección: Narva mnt 5, Tallinn 10117, Estonia<br>Contacto: legal@thinkpoint.ee",
        
        "terms_title": "Términos y Condiciones",
        "terms_date": "Fecha de Efectividad: 16 de enero de 2026",
        "terms_h1": "1. Proveedor de Servicio",
        "terms_p1": "Locy es un servicio provisto por <strong>ThinkPoint OÜ</strong> (Código: 17131887).",
        "terms_h2": "2. Política de Uso Aceptable",
        "terms_p2": "Reservamos el derecho de rescindir el uso por tráfico abusivo y mal uso de nuestros sistemas logísticos.",
        "terms_h3": "3. Ley Aplicable",
        "terms_p3": "Estos Términos se regirán y constituirán de acuerdo con las leyes de la República de Estonia."
    },
    "et": {
        "priv_title": "Privaatsuspoliitika",
        "priv_date": "Viimati uuendatud: 16. jaanuar 2026",
        "priv_h1": "1. Andmete Säilitamise Puudumine",
        "priv_p1": "Locy on loodud olekuvaba töötlejana. Kujutised ja andmed kustutatakse mälust automaatselt pärast koordinaatide väljastamist.",
        "priv_h2": "2. Andmetöötlus",
        "priv_p2": "Me kasutame asukohtade analüüsimiseks mitmeliigilist AI-d. Me ei treeni AI mudeleid klientide saadetud sisenditega.",
        "priv_h3": "3. Vastutav Töötleja",
        "priv_p3": "Teie andmete töötlemise eest vastutav isik on <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Registrikood: 17131887<br>Aadress: Narva mnt 5, Tallinn 10117, Eesti<br>Kontakt: legal@thinkpoint.ee",
        
        "terms_title": "Kasutustingimused",
        "terms_date": "Jõustumiskuupäev: 16. jaanuar 2026",
        "terms_h1": "1. Teenusepakkuja",
        "terms_p1": "Locy põhineb Eestis asutatud usaldusühingule <strong>ThinkPoint OÜ</strong> (Registrikood: 17131887).",
        "terms_h2": "2. Lubatud Kasutuse Eeskiri",
        "terms_p2": "Süsteemi on lubatud sisestada üksnes logistika ja saadetistega sobilikke pakisaatelehti ja viiteid.",
        "terms_h3": "3. Kohaldatav Õigus",
        "terms_p3": "Käesolevatele tingimustele kohaldub Eesti Vabariigi seadustik."
    },
    "it": {
        "priv_title": "Informativa sulla Privacy",
        "priv_date": "Ultimo aggiornamento: 16 gennaio 2026",
        "priv_h1": "1. Architettura a Conservazione Zero",
        "priv_p1": "Locy è progettato come un elaboratore senza stato. Le immagini inviate al nostro sistema vengono convertite in coordinate temporanee per poi svanire dalla memoria.",
        "priv_h2": "2. Elaborazione dei dati",
        "priv_p2": "Utilizziamo l'IA multimodale in tempo reale. Non addestriamo modelli sui dati dei consumatori.",
        "priv_h3": "3. Titolare del Trattamento",
        "priv_p3": "L'entità che controlla le informazioni è <strong>ThinkPoint OÜ</strong>.",
        "priv_p4": "Codice Registro: 17131887<br>Indirizzo: Narva mnt 5, Tallinn 10117, Estonia<br>Info: legal@thinkpoint.ee",
        
        "terms_title": "Termini e Condizioni",
        "terms_date": "In vigore dal: 16 gennaio 2026",
        "terms_h1": "1. Fornitore",
        "terms_p1": "Locy è erogato da <strong>ThinkPoint OÜ</strong> (IT, Estonia: 17131887).",
        "terms_h2": "2. Politica uso corretto",
        "terms_p2": "Richiediamo all'utente di fornire i log delle etichette limitati ad usi consoni della logistica. Non tolleriamo alcun traffico bot.",
        "terms_h3": "3. Foro Competente",
        "terms_p3": "Questi Termini rispettano i vincoli di legge in vigore nell'Estonia (Unione Europea)."
    }
}

with open("C:/Users/Mahir/Desktop/Locy/locales/translations.js", "r", encoding="utf-8") as f:
    text = f.read()

for lang, data in new_data.items():
    search_str = f'"{lang}": {{'
    keys_str = ""
    for k, v in data.items():
        keys_str += f'        "{k}": {json.dumps(v)},\n'
    replace_str = f'"{lang}": {{\n' + keys_str
    text = text.replace(search_str, replace_str, 1)

with open("C:/Users/Mahir/Desktop/Locy/locales/translations.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Patch 5 (Legal) done!")
