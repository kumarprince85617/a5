/**
 * Footlet Crystal Atelier - Interactive Engine
 * Synchronized Mobile Drawer, Accordions, Smooth Scroll & Form Interactivity
 */

document.addEventListener('DOMContentLoaded', function () {
  // 1. Mobile Drawer Toggle (Rule 11)
  const hamburger = document.getElementById('fc-hamburger');
  const drawer = document.getElementById('mobile-drawer');
  const drawerClose = document.getElementById('mobile-drawer-close');
  const drawerBackdrop = document.getElementById('mobile-drawer-backdrop');

  function openDrawer() {
    if (drawer) drawer.classList.add('active');
    if (drawerBackdrop) drawerBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (drawer) drawer.classList.remove('active');
    if (drawerBackdrop) drawerBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (hamburger) {
    hamburger.addEventListener('click', function(e) {
      e.preventDefault();
      openDrawer();
    });
  }

  if (drawerClose) {
    drawerClose.addEventListener('click', function(e) {
      e.preventDefault();
      closeDrawer();
    });
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', closeDrawer);
  }

  const mobileLinks = document.querySelectorAll('.mobile-nav-link');
  mobileLinks.forEach(function (link) {
    link.addEventListener('click', closeDrawer);
  });

  // 2. Accordions (FAQ & Technical Care)
  const accordionHeaders = document.querySelectorAll('.fc-accordion-header');
  accordionHeaders.forEach(function (header) {
    header.addEventListener('click', function () {
      const item = this.parentElement;
      const isActive = item.classList.contains('active');

      const parentList = item.parentElement;
      if (parentList && parentList.classList.contains('fc-accordion-list')) {
        parentList.querySelectorAll('.fc-accordion-item').forEach(function (sibling) {
          sibling.classList.remove('active');
        });
      }

      if (!isActive) {
        item.classList.add('active');
      }
    });
  });

  // 3. Contact Form Submission Feedback
  const contactForm = document.getElementById('fc-contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const submitBtn = contactForm.querySelector('.fc-btn-primary');
      const originalText = submitBtn.innerText;
      submitBtn.innerText = 'TRANSMITTING SPECIFICATIONS...';
      submitBtn.disabled = true;

      setTimeout(function () {
        submitBtn.innerText = 'INQUIRY LOGGED WITH ATELIER';
        submitBtn.style.background = '#0284c7';
        submitBtn.style.borderColor = '#38bdf8';

        const successNotice = document.createElement('div');
        successNotice.style.marginTop = '18px';
        successNotice.style.padding = '14px 18px';
        successNotice.style.borderRadius = '6px';
        successNotice.style.background = 'rgba(2, 132, 199, 0.12)';
        successNotice.style.border = '1px solid #0284c7';
        successNotice.style.color = '#0284c7';
        successNotice.style.fontSize = '0.9rem';
        successNotice.style.fontFamily = 'var(--fc-font-body)';
        successNotice.innerText = 'Thank you for contacting Footlet Crystal Atelier. A dedicated hosiery specialist has received your specifications and will respond within 24 business hours.';
        
        contactForm.appendChild(successNotice);
        contactForm.reset();
      }, 1200);
    });
  }
});
