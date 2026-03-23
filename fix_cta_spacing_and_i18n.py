import os

files_to_fix = [
    'c:/Users/Mahir/Desktop/Locy/index.html',
    'c:/Users/Mahir/Desktop/Locy/product/index.html',
    'c:/Users/Mahir/Desktop/Locy/pricing/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/ecommerce/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/emergency/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/restaurants/index.html'
]

for file in files_to_fix:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 1. Fix Margin gap
        content = content.replace('style="margin-bottom: 80px;"', 'style="margin: 80px auto;"')
        content = content.replace('style="margin-bottom: 80px; max-width: 800px;"', 'style="margin: 80px auto; max-width: 800px;"')
        
        # 2. Ensure i18n translation keys are unified to cta_title, cta_desc, cta_btn
        # We find the CTA box and replace everything inside it up to the </div>
        # Actually safer to string replace specific known lines or just rewrite the pre-footer block entirely.
        
        # The CTA block looks highly similar across pages. We can regex it.
        import re
        
        # We look for <section class="container" style="margin: 80px auto;"> ... </section>
        pattern = re.compile(r'(<section class="container" style="margin: 80px auto;[^>]*>).*?(</section>)', re.DOTALL)
        
        new_cta = r'''\1
        <div class="cta-box fade-in-up">
            <h2 class="display-medium" data-i18n="cta_title">Ready to speed up your fleet?</h2>
            <p class="body-large" style="max-width: 600px; margin: 0 auto 32px;" data-i18n="cta_desc">
                Save 30 seconds per delivery.
            </p>
            <a href="https://wa.me/message/2VAKQKH7ZNS3D1" class="btn btn-primary btn-whatsapp" data-i18n="cta_btn">
                Launch on WhatsApp
            </a>
        </div>
    \2'''
        
        content = re.sub(pattern, new_cta, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {file}")
    else:
        print(f"File not found: {file}")
