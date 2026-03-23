import re

priv_path = 'c:/Users/Mahir/Desktop/Locy/privacy/index.html'
terms_path = 'c:/Users/Mahir/Desktop/Locy/terms/index.html'

privacy_html = r'''        <div class="container" style="max-width: 800px;">
            <h1 data-i18n="priv_title">Privacy Policy</h1>
            <p style="margin-top: 24px; color: var(--text-secondary);" data-i18n="priv_date">Last Updated: January 16, 2026</p>

            <h3 style="margin-top: 48px;" data-i18n="priv_h1">1. Information We Collect</h3>
            <ul style="color: var(--text-secondary); line-height: 1.6; padding-left: 20px; margin-bottom: 24px;">
                <li data-i18n="priv_p1_1">We collect the absolute minimum data required to provide our location services.</li>
                <li style="margin-top: 8px;" data-i18n="priv_p1_2">WhatsApp logs limited to metadata and phone numbers for routing context.</li>
                <li style="margin-top: 8px;" data-i18n="priv_p1_3">Package images submitted strictly for real-time address extraction.</li>
            </ul>

            <h3 style="margin-top: 32px;" data-i18n="priv_h2">2. Zero Retention Architecture</h3>
            <p data-i18n="priv_p2_1">Locy operates strictly as a stateless processor by design.</p>
            <p data-i18n="priv_p2_2">Images sent to our processing system are converted to coordinates and routing data, then immediately purged from volatile memory.</p>

            <h3 style="margin-top: 32px;" data-i18n="priv_h3">3. How We Use Data</h3>
            <p data-i18n="priv_p3_1">We use incoming data solely to provide real-time location intelligence.</p>
            <p data-i18n="priv_p3_2">We absolutely never use your proprietary delivery data to train our core foundation models.</p>

            <h3 style="margin-top: 32px;" data-i18n="priv_h4">4. Data Sharing & Third Parties</h3>
            <p data-i18n="priv_p4_1">We never sell your data. We rely on enterprise-grade EU infrastructure providers bound by strict DPA agreements.</p>

            <h3 style="margin-top: 32px;" data-i18n="priv_h5">5. International Rights</h3>
            <p data-i18n="priv_p5_1">As an EU-based infrastructure company, all our users globally benefit from strict GDPR-level privacy protections.</p>

            <h3 style="margin-top: 32px;" data-i18n="priv_h6">6. Data Controller & Contact</h3>
            <p data-i18n="priv_p6_1" style="margin-bottom: 8px;">The entity responsible for processing your data is ThinkPoint OÜ.</p>
            <p style="color: var(--text-secondary);" data-i18n="priv_p6_2">
                Registry Code: 17131887 | Narva mnt 5, Tallinn 10117, Estonia | legal@thinkpoint.ee
            </p>
        </div>'''

terms_html = r'''        <div class="container" style="max-width: 800px;">
            <h1 data-i18n="terms_title">Terms of Service</h1>
            <p style="margin-top: 24px; color: var(--text-secondary);" data-i18n="terms_date">Effective Date: January 16, 2026</p>

            <h3 style="margin-top: 48px;" data-i18n="terms_h1">1. Acceptance of Terms</h3>
            <p data-i18n="terms_p1_1">By integrating or using Locy's bot and API infrastructure, you agree to be bound by these Terms of Service.</p>

            <h3 style="margin-top: 32px;" data-i18n="terms_h2">2. Service Description</h3>
            <p data-i18n="terms_p2_1">Locy is a spatial intelligence platform designed for the logistics, food delivery, and emergency sectors.</p>

            <h3 style="margin-top: 32px;" data-i18n="terms_h3">3. Acceptable Use Policy</h3>
            <ul style="color: var(--text-secondary); line-height: 1.6; padding-left: 20px; margin-bottom: 24px;">
                <li data-i18n="terms_p3_1">You may only submit images related to genuine logistics or address verification tasks.</li>
                <li style="margin-top: 8px;" data-i18n="terms_p3_2">Reverse-engineering our API, scraping data, or abusing the service for unsupported purposes will result in permanent termination of access.</li>
            </ul>

            <h3 style="margin-top: 32px;" data-i18n="terms_h4">4. Service Level Agreement (SLA)</h3>
            <p data-i18n="terms_p4_1">Enterprise customers under contract are guaranteed a 99.9% uptime SLA with priority routing queues.</p>

            <h3 style="margin-top: 32px;" data-i18n="terms_h5">5. Intellectual Property</h3>
            <p data-i18n="terms_p5_1">ThinkPoint OÜ retains all rights, title, and interest in Locy software, ML models, and branding.</p>

            <h3 style="margin-top: 32px;" data-i18n="terms_h6">6. Governing Law</h3>
            <p data-i18n="terms_p6_1">These Terms are governed by the laws of the Republic of Estonia.</p>
        </div>'''

def patch_file(filepath, new_html):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    pattern = re.compile(r'<div class="container" style="max-width: 800px;">.*?</section>', re.DOTALL)
    new_block = new_html + '\n    </section>'
    
    content = re.sub(pattern, new_block, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
patch_file(priv_path, privacy_html)
patch_file(terms_path, terms_html)
print("Updated HTML structures.")
