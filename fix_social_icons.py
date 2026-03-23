import os
import re

files_to_fix = [
    'c:/Users/Mahir/Desktop/Locy/index.html',
    'c:/Users/Mahir/Desktop/Locy/product/index.html',
    'c:/Users/Mahir/Desktop/Locy/pricing/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/ecommerce/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/emergency/index.html',
    'c:/Users/Mahir/Desktop/Locy/use-cases/restaurants/index.html',
    'c:/Users/Mahir/Desktop/Locy/company/index.html',
    'c:/Users/Mahir/Desktop/Locy/privacy/index.html',
    'c:/Users/Mahir/Desktop/Locy/terms/index.html'
]

instagram_html = r'''                <div class="social-links">
                    <a href="https://instagram.com/locy.ai" class="social-icon" title="Instagram" target="_blank">
                        <svg width="20" height="20" fill="currentColor" viewBox="0 0 24 24">
                            <path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 1.76-6.98 6.208-.058 1.28-.072 1.688-.072 4.947s.014 3.667.072 4.947c.2 4.448 2.622 6.008 6.98 6.208 1.28.058 1.688.072 4.947.072s3.668-.014 4.947-.072c4.358-.2 6.78-1.76 6.98-6.208.058-1.28.072-1.688.072-4.947s-.014-3.667-.072-4.947c-.2-4.448-2.622-6.008-6.98-6.208-1.28-.058-1.688-.072-4.947-.072zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.162 6.162 6.162 6.162-2.759 6.162-6.162-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4s1.791-4 4-4 4 1.79 4 4-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.441 1.441 1.441 1.441-.645 1.441-1.441-.645-1.44-1.441-1.44z"/>
                        </svg>
                    </a>
                </div>
            </div>
        </div>
    </footer>'''

# We want to replace whatever comes after `<div class="copyright">...</div>` until `</div>\n        </div>\n    </footer>`

for file in files_to_fix:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()

        # The pattern looks for the copyright div (which ends with </div>) and captures it as group 1.
        # Then matches everything until </div>\n        </div>\n    </footer>
        pattern = re.compile(r'(<div class="copyright">.*?</div>).*?</div>\s*</div>\s*</footer>', re.DOTALL)
        
        def repl(m):
            return m.group(1) + '\n' + instagram_html
        
        new_content = re.sub(pattern, repl, content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated social icons in {file}")
    else:
        print(f"File not found: {file}")
