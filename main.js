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

    // Simple console log to verify load
    console.log('Locy UI Loaded - Material Intelligence Active');

});


