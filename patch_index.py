import os

filepath = 'c:/Users/Mahir/Desktop/Locy/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    # Comparison Old
    '<h3 style="margin-bottom: 24px; color: #E11D48;">The Old Way</h3>': '<h3 style="margin-bottom: 24px; color: #E11D48;" data-i18n="comp_old_title">The Old Way</h3>',
    '<h4>Manual Address Typing</h4>': '<h4 data-i18n="comp_old_1_title">Manual Address Typing</h4>',
    '<p>Drivers waste minutes typing labels.</p>': '<p data-i18n="comp_old_1_desc">Drivers waste minutes typing labels.</p>',
    '<h4>Wrong Locations</h4>': '<h4 data-i18n="comp_old_2_title">Wrong Locations</h4>',
    '<p>Pins land in the middle of the street.</p>': '<p data-i18n="comp_old_2_desc">Pins land in the middle of the street.</p>',
    '<h4>Time Loss</h4>': '<h4 data-i18n="comp_old_3_title">Time Loss</h4>',
    '<p>Calling customers for directions.</p>': '<p data-i18n="comp_old_3_desc">Calling customers for directions.</p>',
    
    # Comparison New
    '<h3 style="margin-bottom: 24px; color: #059669;">The Locy Way</h3>': '<h3 style="margin-bottom: 24px; color: #059669;" data-i18n="comp_new_title">The Locy Way</h3>',
    '<h4>Photo -> AI -> Location</h4>': '<h4 data-i18n="comp_new_1_title">Photo -> AI -> Location</h4>',
    '<p>Snap a photo. We extract the address.</p>': '<p data-i18n="comp_new_1_desc">Snap a photo. We extract the address.</p>',
    '<h4>No Typing, No Mistakes</h4>': '<h4 data-i18n="comp_new_2_title">No Typing, No Mistakes</h4>',
    '<p>Zero manual entry errors.</p>': '<p data-i18n="comp_new_2_desc">Zero manual entry errors.</p>',
    '<h4>Works in WhatsApp</h4>': '<h4 data-i18n="comp_new_3_title">Works in WhatsApp</h4>',
    '<p>No new apps to install.</p>': '<p data-i18n="comp_new_3_desc">No new apps to install.</p>',
    
    # Security 1
    '<h2 style="font-size: 2rem; color: white;">Built for enterprise-grade operations</h2>': '<h2 style="font-size: 2rem; color: white;" data-i18n="sec_title">Built for enterprise-grade operations</h2>',
    '<p>End-to-end encrypted</p>': '<p data-i18n="sec_1">End-to-end encrypted</p>',
    '<p>No data stored</p>': '<p data-i18n="sec_2">No data stored</p>',
    '<p>GDPR-ready</p>': '<p data-i18n="sec_3">GDPR-ready</p>',
    '<p>WhatsApp API Compliant</p>': '<p data-i18n="sec_4">WhatsApp API Compliant</p>',
    
    # Capabilities
    '<h5 class="fade-in-up">CAPABILITIES</h5>': '<h5 class="fade-in-up" data-i18n="cap_overline">CAPABILITIES</h5>',
    '<h2 class="fade-in-up">The layer for last-mile.</h2>': '<h2 class="fade-in-up" data-i18n="cap_title">The layer for last-mile.</h2>',
    '<p class="fade-in-up">We replace manual review queues with automated certainty. No apps to install.\n                    No\n                    friction.</p>': '<p class="fade-in-up" data-i18n="cap_desc">We replace manual review queues with automated certainty. No apps to install. No friction.</p>',
    '<h3>Route Optimization</h3>': '<h3 data-i18n="cap_1_title">Route Optimization</h3>',
    '<p style="margin-bottom: 0;">Stop zigzagging. We order the stops logically. A → B → C.</p>': '<p style="margin-bottom: 0;" data-i18n="cap_1_desc">Stop zigzagging. We order the stops logically. A → B → C.</p>',
    '<h3>Native Language Bot</h3>': '<h3 data-i18n="cap_2_title">Native Language Bot</h3>',
    '<p style="margin-bottom: 0;">The bot speaks the driver\'s language automatically based on country\n                        code.</p>': '<p style="margin-bottom: 0;" data-i18n="cap_2_desc">The bot speaks the driver\'s language automatically based on country code.</p>',
    '<h3>Branded Smart Links</h3>': '<h3 data-i18n="cap_3_title">Branded Smart Links</h3>',
    '<p style="margin-bottom: 0;">Short, professional links that build trust. No scary long URLs.</p>': '<p style="margin-bottom: 0;" data-i18n="cap_3_desc">Short, professional links that build trust. No scary long URLs.</p>',

    # Workflow
    '<h5 class="fade-in-up">WORKFLOW</h5>': '<h5 class="fade-in-up" data-i18n="flow_overline">WORKFLOW</h5>',
    '<h2 class="fade-in-up">Zero-friction integration.</h2>': '<h2 class="fade-in-up" data-i18n="flow_title">Zero-friction integration.</h2>',
    '<h3>Send</h3>': '<h3 data-i18n="flow_1_title">Send</h3>',
    '<p>Courier sends a photo of the package address in WhatsApp.</p>': '<p data-i18n="flow_1_desc">Courier sends a photo of the package address in WhatsApp.</p>',
    '<h3>Process</h3>': '<h3 data-i18n="flow_2_title">Process</h3>',
    '<p>Our AI extracts the address and verifies coordinate precision.</p>': '<p data-i18n="flow_2_desc">Our AI extracts the address and verifies coordinate precision.</p>',
    '<h3>Navigate</h3>': '<h3 data-i18n="flow_3_title">Navigate</h3>',
    '<p>Bot replies with a pinned location link in seconds.</p>': '<p data-i18n="flow_3_desc">Bot replies with a pinned location link in seconds.</p>',
    
    # Security 2
    '<h2 class="fade-in-up">Zero Retention.</h2>': '<h2 class="fade-in-up" data-i18n="sec2_title">Zero Retention.</h2>',
    '<p class="fade-in-up" style="max-width: 600px; margin: 0 auto 32px;">\n                Images processed. Discarded. No data stored.\n            </p>': '<p class="fade-in-up" style="max-width: 600px; margin: 0 auto 32px;" data-i18n="sec2_desc">Images processed. Discarded. No data stored.</p>',
    '<h3>\n                        < 15s</h3>': '<h3 data-i18n="sec2_stat1_title">< 15s</h3>',
    '<p>Avg. Response</p>': '<p data-i18n="sec2_stat1_desc">Avg. Response</p>',
    '<h3>99.9%</h3>': '<h3 data-i18n="sec2_stat2_title">99.9%</h3>',
    '<p>Uptime</p>': '<p data-i18n="sec2_stat2_desc">Uptime</p>',
    '<h3>GDPR</h3>': '<h3 data-i18n="sec2_stat3_title">GDPR</h3>',
    '<p>Compliant</p>': '<p data-i18n="sec2_stat3_desc">Compliant</p>'
}

for old, new in replacements.items():
    if old in content:
        content = content.replace(old, new)
        print(f"Replaced {old[:20]}...")
    else:
        print(f"WARNING: Could not find: {old}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done patching index.html.")
