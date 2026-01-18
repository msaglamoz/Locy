document.addEventListener('DOMContentLoaded', () => {

    // Mobile Menu Logic
    const hamburger = document.querySelector('.hamburger-btn');
    const mobileMenu = document.querySelector('.mobile-menu-overlay');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');

    if (hamburger && mobileMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            mobileMenu.classList.toggle('active');

            // Lock scroll when menu is open
            if (mobileMenu.classList.contains('active')) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        });

        // Close menu when a link is clicked
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                mobileMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Mobile Dropdown Logic (Solutions)
        // Select the dropdown in mobile menu context if it exists, or bind to main nav dropdown if that's what's shown
        // Since the current mobile menu is a separate overlay with flat links, we need to ensure 'Solutions' behaves correctly there.
        // Looking at index.html, the mobile menu currently FLATTENS the structure:
        // <a href="/use-cases/restaurants" class="mobile-nav-link">Restaurants</a>
        // It does NOT have a collapsible "Solutions" item.
        // User likely meant the DESKTOP menu when resized to mobile, OR they want a collapsible in the mobile menu.
        // HOWEVER, the user said "Solutions menu... if it opens with hover on desktop -> make it touch on mobile".
        // This implies they might be using a tablet where they see the desktop menu, OR they want the mobile overlay to have a hierarchy.
        // Given the current mobile menu is flat (lines 78-83 in index.html), the "Solutions" parent doesn't exist there.
        // I will assume they mean the Desktop Navbar behavior on Touch devices (Tablet/Hybrid).

        const dropdowns = document.querySelectorAll('.dropdown');
        dropdowns.forEach(dropdown => {
            const dropbtn = dropdown.querySelector('.dropbtn');
            if (dropbtn) {
                dropbtn.addEventListener('click', (e) => {
                    // On touch devices, prevent default link behavior and toggle
                    if (window.innerWidth <= 1024) {
                        e.preventDefault();
                        dropdown.classList.toggle('active');
                    }
                });
            }
        });
    }

    // Scroll Effect (Navbar)
    const navbar = document.getElementById('navbar');

    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Intersection Observer for Animations
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-in-up');
    animatedElements.forEach(el => observer.observe(el));

    // Smart Copy Logic
    const copyBtns = document.querySelectorAll('.btn-smart-copy');
    copyBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const textToCopy = btn.getAttribute('data-copy');

            // Check if button has structure (Hero) or is simple link (Footer)
            const btnText = btn.querySelector('.btn-text');
            const btnIcon = btn.querySelector('.btn-icon');

            const originalText = btnText ? btnText.innerText : btn.innerText;
            const originalIconContent = btnIcon ? btnIcon.innerText : '';

            navigator.clipboard.writeText(textToCopy).then(() => {
                // Success Feedback
                btn.classList.add('copied');

                if (btnText && btnIcon) {
                    // Complex Button Feedback
                    btnText.innerText = 'Email Copied!';
                    btnIcon.innerText = 'check';
                } else {
                    // Simple Link Feedback
                    btn.innerText = 'Email Copied! ✓';
                }

                // Revert after 2 seconds
                setTimeout(() => {
                    btn.classList.remove('copied');
                    if (btnText && btnIcon) {
                        btnText.innerText = originalText;
                        btnIcon.innerText = originalIconContent;
                    } else {
                        btn.innerText = originalText;
                    }
                }, 2000);
            }).catch(err => {
                // Fallback to mailto if copy fails
                window.location.href = btn.href;
            });
        });
    });

    // Google Translate Logic - Prevent Icon Translation
    // Adds 'notranslate' class to all Material Icons to prevent Google Translate from breaking them
    const icons = document.querySelectorAll('.material-symbols-outlined');
    icons.forEach(icon => {
        icon.classList.add('notranslate');
    });

    // Active Navigation State Logic
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-links a, .mobile-nav-link');

    navLinks.forEach(link => {
        // Check if link href matches current path (considering root /)
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath || (linkPath === '/' && currentPath === '/index.html')) {
            link.classList.add('active');
        }
    });

    // Google Translate Integration
    const script = document.createElement('script');
    script.src = "//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
    document.body.appendChild(script);

    window.googleTranslateElementInit = function () {
        new google.translate.TranslateElement({
            pageLanguage: 'en',
            includedLanguages: 'en,tr,de,fr,it,es,nl,pt,pl,ro,el,cs,ar',
            layout: google.translate.TranslateElement.InlineLayout.SIMPLE,
            autoDisplay: false
        }, 'google_translate_element');
    };

    // Bind Custom Select to Google Translate with Retry Logic
    const customSelector = document.getElementById('custom-language-selector');
    if (customSelector) {
        customSelector.addEventListener('change', function () {
            const lang = this.value;
            const googleCombo = document.querySelector('.goog-te-combo');

            if (googleCombo) {
                // If loaded, trigger immediately
                googleCombo.value = lang;
                googleCombo.dispatchEvent(new Event('change'));
            } else {
                // If not loaded yet, retry a few times
                console.log('Google Translate not ready, retrying...');
                let attempts = 0;
                const interval = setInterval(() => {
                    const retryCombo = document.querySelector('.goog-te-combo');
                    if (retryCombo) {
                        retryCombo.value = lang;
                        retryCombo.dispatchEvent(new Event('change'));
                        clearInterval(interval);
                    }
                    attempts++;
                    if (attempts > 10) clearInterval(interval); // Stop after 2 seconds
                }, 200);
            }
        });
    }

});


