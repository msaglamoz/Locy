document.addEventListener("DOMContentLoaded", () => {
    const supportedLangs = ['en', 'tr', 'de', 'fr', 'es', 'et', 'it'];
    const defaultLang = 'en';

    // Determine current language
    let currentLang = localStorage.getItem('locy_lang');
    if (!currentLang) {
        // Example: 'tr-TR' -> 'tr'
        const browserLang = navigator.language.slice(0, 2).toLowerCase();
        if (supportedLangs.includes(browserLang)) {
            currentLang = browserLang;
        } else {
            currentLang = defaultLang;
        }
    } else if (!supportedLangs.includes(currentLang)) {
        currentLang = defaultLang;
    }

    // Apply translations
    function applyTranslations(lang) {
        if (!LocyTranslations[lang]) {
            lang = defaultLang; // fallback if dictionary is missing
        }
        
        const dict = LocyTranslations[lang];
        if (!dict) return;

        document.querySelectorAll("[data-i18n]").forEach(el => {
            const key = el.getAttribute("data-i18n");
            if (dict[key]) {
                el.innerHTML = dict[key];
            }
        });

        // Update any language select elements to show the correct value
        document.querySelectorAll('.language-switcher').forEach(select => {
            if (select.value !== lang) {
                select.value = lang;
            }
        });
        
        // Save to locale storage
        localStorage.setItem('locy_lang', lang);
        
        // Update document lang attribute
        document.documentElement.lang = lang;
    }

    // Initial apply
    applyTranslations(currentLang);

    // Make applyTranslations available globally
    window.locyChangeLanguage = function(lang) {
        if (supportedLangs.includes(lang)) {
            applyTranslations(lang);
        }
    };

    // Attach listener to switchers
    document.querySelectorAll('.language-switcher').forEach(select => {
        select.addEventListener('change', (e) => {
            window.locyChangeLanguage(e.target.value);
        });
    });
});
