// Theme Management System for RentEasy
class ThemeManager {
  constructor() {
    this.init();
  }

  init() {
    this.setupThemeToggle();
    this.setupSystemThemeListener();
    this.updateThemeIcon();
  }

  setupThemeToggle() {
    const themeToggleDesktop = document.getElementById('theme-toggle-desktop');
    const themeToggleMobile = document.getElementById('theme-toggle-mobile');

    if (themeToggleDesktop) {
      themeToggleDesktop.addEventListener('click', () => this.toggleTheme());
    }
    if (themeToggleMobile) {
      themeToggleMobile.addEventListener('click', () => this.toggleTheme());
    }
  }

  setupSystemThemeListener() {
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem('theme')) {
        const newTheme = e.matches ? 'dark' : 'light';
        this.setTheme(newTheme);
      }
    });
  }

  getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  }

  setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);

    // Add/remove dark class for Tailwind CSS dark mode
    if (theme === 'dark') {
      document.documentElement.classList.add('dark');
      document.body.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
      document.body.classList.remove('dark');
    }

    localStorage.setItem('theme', theme);
    this.updateThemeIcon();
    this.announceThemeChange(theme);
  }

  toggleTheme() {
    const currentTheme = this.getCurrentTheme();
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    this.setTheme(newTheme);
  }

  updateThemeIcon() {
    const currentTheme = this.getCurrentTheme();
    const iconClass = currentTheme === 'dark' ? 'bi-moon-fill' : 'bi-sun-fill';

    const themeIconDesktop = document.getElementById('theme-icon-desktop');
    const themeIconMobile = document.getElementById('theme-icon-mobile');

    if (themeIconDesktop) {
      themeIconDesktop.className = `bi ${iconClass}`;
    }
    if (themeIconMobile) {
      themeIconMobile.className = `bi ${iconClass}`;
    }
  }

  announceThemeChange(theme) {
    // Announce theme change for screen readers
    const announcement = `Theme changed to ${theme} mode`;
    const announcer = document.createElement('div');
    announcer.setAttribute('aria-live', 'polite');
    announcer.setAttribute('aria-atomic', 'true');
    announcer.className = 'sr-only';
    announcer.textContent = announcement;
    document.body.appendChild(announcer);
    setTimeout(() => document.body.removeChild(announcer), 1000);
  }
}

// Initialize theme manager when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  new ThemeManager();
});

// Utility functions for theme-aware components
window.RentEasyTheme = {
  // Get current theme
  getCurrentTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  },

  // Check if dark theme is active
  isDarkTheme() {
    return this.getCurrentTheme() === 'dark';
  },

  // Listen for theme changes
  onThemeChange(callback) {
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'attributes' && mutation.attributeName === 'data-theme') {
          callback(document.documentElement.getAttribute('data-theme'));
        }
      });
    });

    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['data-theme']
    });

    return observer;
  }
};