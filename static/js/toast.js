/**
 * Toast notification system
 * Supports success, error, warning, and info message types
 */

(function () {
    'use strict';

    const TOAST_DURATION = 5000; // 5 seconds
    const TOAST_ICONS = {
        success: 'bi-check-circle-fill',
        error: 'bi-x-circle-fill',
        warning: 'bi-exclamation-triangle-fill',
        info: 'bi-info-circle-fill'
    };

    /**
     * Show a toast notification
     * @param {string} message - The message to display
     * @param {string} type - The type of toast (success, error, warning, info)
     * @param {number} duration - How long to show the toast in milliseconds
     */
    window.showToast = function (message, type = 'info', duration = TOAST_DURATION) {
        const container = document.getElementById('toastContainer');
        if (!container) {
            console.error('Toast container not found');
            return;
        }

        // Normalize type
        type = type.toLowerCase();
        if (type === 'danger') type = 'error';

        // Create toast element
        const toastId = 'toast-' + Date.now();
        const iconClass = TOAST_ICONS[type] || TOAST_ICONS.info;

        const toastHTML = `
            <div id="${toastId}" class="toast toast-${type}" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <i class="bi ${iconClass} me-2"></i>
                    <strong class="me-auto">${capitalizeFirst(type)}</strong>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                    ${escapeHtml(message)}
                </div>
            </div>
        `;

        // Add toast to container
        container.insertAdjacentHTML('beforeend', toastHTML);

        // Get the toast element
        const toastElement = document.getElementById(toastId);

        // Initialize Bootstrap toast
        const bsToast = new bootstrap.Toast(toastElement, {
            autohide: true,
            delay: duration
        });

        // Show the toast
        bsToast.show();

        // Remove toast from DOM after it's hidden
        toastElement.addEventListener('hidden.bs.toast', function () {
            toastElement.remove();
        });
    };

    /**
     * Capitalize the first letter of a string
     */
    function capitalizeFirst(str) {
        return str.charAt(0).toUpperCase() + str.slice(1);
    }

    /**
     * Escape HTML to prevent XSS
     */
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Show success toast
     */
    window.showSuccess = function (message, duration) {
        showToast(message, 'success', duration);
    };

    /**
     * Show error toast
     */
    window.showError = function (message, duration) {
        showToast(message, 'error', duration);
    };

    /**
     * Show warning toast
     */
    window.showWarning = function (message, duration) {
        showToast(message, 'warning', duration);
    };

    /**
     * Show info toast
     */
    window.showInfo = function (message, duration) {
        showToast(message, 'info', duration);
    };
})();
