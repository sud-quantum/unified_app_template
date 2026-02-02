/**
 * Theme switching functionality
 * Handles light/dark mode toggle with localStorage persistence
 */

(function() {
    'use strict';
    
    const THEME_KEY = 'app-theme';
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const html = document.documentElement;
    
    /**
     * Get the current theme from localStorage or default to light
     */
    function getCurrentTheme() {
        return localStorage.getItem(THEME_KEY) || 'light';
    }
    
    /**
     * Set the theme and update UI
     */
    function setTheme(theme) {
        html.setAttribute('data-bs-theme', theme);
        localStorage.setItem(THEME_KEY, theme);
        updateThemeIcon(theme);
    }
    
    /**
     * Update the theme toggle icon
     */
    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        
        if (theme === 'dark') {
            themeIcon.classList.remove('bi-sun-fill');
            themeIcon.classList.add('bi-moon-fill');
        } else {
            themeIcon.classList.remove('bi-moon-fill');
            themeIcon.classList.add('bi-sun-fill');
        }
    }
    
    /**
     * Toggle between light and dark themes
     */
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        setTheme(newTheme);
    }
    
    /**
     * Initialize theme on page load
     */
    function initTheme() {
        const savedTheme = getCurrentTheme();
        setTheme(savedTheme);
    }
    
    // Initialize theme when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
    
    // Add click event listener to theme toggle button
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }
})();
