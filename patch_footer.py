import os

# The replacement for the footer block
footer_template = """    <footer>
        <div class="container">
            <div class="footer-grid">
                <!-- Column 1: Brand & Action -->
                <div class="footer-brand">
                    <a href="/" class="logo">
                        Locy
                        <span translate="no" class="material-symbols-outlined notranslate verified-badge"
                            title="Official Infrastructure">verified</span>
                    </a>
                    <p data-i18n="footer_desc">The layer for last-mile logistics. No app to install. Just results.</p>
                    <a href="https://wa.me/message/2VAKQKH7ZNS3D1" class="btn-footer" target="_blank">
                        <span translate="no" class="material-symbols-outlined notranslate">chat</span>
                        <span data-i18n="footer_btn_chat">Start Chat</span>
                    </a>
                </div>

                <!-- Column 2: Product -->
                <div class="footer-col">
                    <h4 data-i18n="footer_col_product">Product</h4>
                    <a href="/product" data-i18n="footer_link_features">Features</a>
                    <a href="/pricing" data-i18n="footer_link_pricing">Pricing</a>
                    <a href="/use-cases/restaurants" data-i18n="footer_link_restaurants">Restaurants</a>
                    <a href="/use-cases/ecommerce" data-i18n="footer_link_ecommerce">E-Commerce</a>
                    <a href="/use-cases/emergency" data-i18n="footer_link_emergency">Emergency</a>
                </div>

                <!-- Column 3: Company -->
                <div class="footer-col">
                    <h4 data-i18n="footer_col_company">Company</h4>
                    <a href="/company" data-i18n="footer_link_about">About Us</a>
                    <a href="mailto:hi@locy.ai" class="btn-smart-copy" data-copy="hi@locy.ai"
                        style="text-decoration: none; cursor: pointer;" data-i18n="footer_link_contact">Contact</a>
                </div>

                <!-- Column 4: Legal -->
                <div class="footer-col">
                    <h4 data-i18n="footer_col_legal">Legal</h4>
                    <a href="/privacy" data-i18n="footer_link_privacy">Privacy Policy</a>
                    <a href="/terms" data-i18n="footer_link_terms">Terms of Service</a>
                </div>
            </div>

            <!-- Bottom Bar -->
            <div class="footer-bottom">
                <div class="copyright">
                    &copy; 2026 <a href="https://thinkpoint.ee" target="_blank"
                        style="color: inherit; text-decoration: none;">ThinkPoint OÜ</a>.
                </div>"""

def patch_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the footer start and bottom bar start
    start_idx = content.find('    <footer>')
    if start_idx == -1:
        start_idx = content.find('<footer>')

    end_idx = content.find('<div class="social-links">')
    if end_idx == -1:
        # Check if it was stripped (index.html has it stripped maybe)
        end_idx = content.find('<!-- Social Icons -->')
        if end_idx == -1:
            end_idx = content.find('            </div>\n        </div>\n    </footer>')

    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + footer_template + "\n" + content[end_idx-17:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Patched footer in {filepath}")

for root, _, files in os.walk('c:/Users/Mahir/Desktop/Locy'):
    for file in files:
        if file.endswith('.html'):
            patch_footer(os.path.join(root, file))
