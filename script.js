(function () {
  "use strict";

  function initIcons() {
    if (window.lucide) window.lucide.createIcons();
  }

  function initReveal() {
    var els = Array.prototype.slice.call(document.querySelectorAll("[data-reveal]"));
    if (!("IntersectionObserver" in window)) {
      els.forEach(function (el) { el.classList.add("is-visible"); });
      return;
    }
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    els.forEach(function (el) { io.observe(el); });
  }

  function initVideoEmbeds() {
    var thumbs = Array.prototype.slice.call(document.querySelectorAll(".video-card__thumb[data-embed]"));
    thumbs.forEach(function (thumb) {
      thumb.addEventListener("click", function () {
        var url = thumb.getAttribute("data-embed");
        var title = thumb.getAttribute("data-title") || "Video";
        var iframe = document.createElement("iframe");
        iframe.src = url;
        iframe.title = title;
        iframe.loading = "lazy";
        iframe.setAttribute("allow", "autoplay; fullscreen");
        iframe.setAttribute("allowfullscreen", "");
        thumb.innerHTML = "";
        thumb.appendChild(iframe);
        thumb.removeAttribute("data-embed");
        thumb.style.cursor = "default";
      }, { once: true });
    });
  }

  function initVideoFilter() {
    var search = document.getElementById("videoSearch");
    var grid = document.getElementById("videoGrid");
    var empty = document.getElementById("videoEmpty");
    if (!search || !grid) return;
    var cards = Array.prototype.slice.call(grid.querySelectorAll(".video-card"));
    var pills = Array.prototype.slice.call(document.querySelectorAll(".filter-pill"));
    var activeFilter = "all";

    function apply() {
      var query = search.value.trim().toLowerCase();
      var visibleCount = 0;
      cards.forEach(function (card) {
        var title = card.querySelector("h3").textContent.toLowerCase();
        var category = card.getAttribute("data-category");
        var matchesFilter = activeFilter === "all" || category === activeFilter;
        var matchesSearch = !query || title.indexOf(query) !== -1;
        var visible = matchesFilter && matchesSearch;
        card.style.display = visible ? "" : "none";
        if (visible) visibleCount += 1;
      });
      if (empty) empty.hidden = visibleCount !== 0;
    }

    search.addEventListener("input", apply);
    pills.forEach(function (pill) {
      pill.addEventListener("click", function () {
        pills.forEach(function (p) { p.classList.remove("is-active"); });
        pill.classList.add("is-active");
        activeFilter = pill.getAttribute("data-filter");
        apply();
      });
    });
  }

  function initHeaderScroll() {
    var header = document.querySelector(".site-header");
    if (!header) return;
    function onScroll() {
      header.classList.toggle("is-scrolled", window.scrollY > 8);
    }
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  function initCounters() {
    var els = Array.prototype.slice.call(document.querySelectorAll(".stat strong, .hero__stat strong"));
    if (!els.length) return;
    if (!("IntersectionObserver" in window)) return;
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          io.unobserve(entry.target);
          var el = entry.target;
          var match = el.textContent.trim().match(/^(\d+)(.*)$/);
          if (!match) return;
          var target = parseInt(match[1], 10);
          var suffix = match[2];
          var duration = 900;
          var start = null;
          function step(ts) {
            if (start === null) start = ts;
            var progress = Math.min((ts - start) / duration, 1);
            var eased = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(eased * target) + suffix;
            if (progress < 1) requestAnimationFrame(step);
            else el.textContent = target + suffix;
          }
          requestAnimationFrame(step);
        });
      },
      { threshold: 0.4 }
    );
    els.forEach(function (el) { io.observe(el); });
  }

  function initNavToggle() {
    var toggle = document.getElementById("navToggle");
    var nav = document.getElementById("siteNav");
    if (!toggle || !nav) return;
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    nav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  function initJobAccordion() {
    var list = document.getElementById("jobsList");
    if (!list) return;
    var jobs = Array.prototype.slice.call(list.querySelectorAll(".job"));
    jobs.forEach(function (job) {
      var header = job.querySelector(".job__header");
      header.addEventListener("click", function () {
        var willOpen = !job.classList.contains("is-open");
        jobs.forEach(function (other) { other.classList.remove("is-open"); });
        if (willOpen) job.classList.add("is-open");
      });
    });
  }

  function initFaqAccordion() {
    var lists = Array.prototype.slice.call(document.querySelectorAll(".faq-list"));
    lists.forEach(function (list) {
      var items = Array.prototype.slice.call(list.querySelectorAll(".faq-item"));
      items.forEach(function (item) {
        var header = item.querySelector(".faq-item__header");
        header.addEventListener("click", function () {
          item.classList.toggle("is-open");
        });
      });
    });
  }

  function stepFields(step) {
    return Array.prototype.slice.call(step.querySelectorAll("input, select, textarea"));
  }

  function stepIsValid(step) {
    var valid = true;
    stepFields(step).forEach(function (field) {
      if (!field.checkValidity()) {
        field.reportValidity();
        valid = false;
      }
    });
    return valid;
  }

  function initMultistepForm() {
    var form = document.getElementById("applicationForm");
    if (!form) return;
    var steps = Array.prototype.slice.call(form.querySelectorAll(".form-step"));
    if (!steps.length) return;
    var progressEls = Array.prototype.slice.call(form.querySelectorAll(".multistep__step"));
    var current = 0;

    function show(index) {
      current = index;
      steps.forEach(function (step, i) {
        step.classList.toggle("is-active", i === index);
      });
      progressEls.forEach(function (el, i) {
        el.classList.toggle("is-current", i === index);
        el.classList.toggle("is-done", i < index);
      });
    }

    form.querySelectorAll("[data-next]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        if (!stepIsValid(steps[current])) return;
        show(Math.min(current + 1, steps.length - 1));
      });
    });

    form.querySelectorAll("[data-back]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        show(Math.max(current - 1, 0));
      });
    });

    form.addEventListener("keydown", function (e) {
      if (e.key !== "Enter") return;
      if (e.target.tagName === "TEXTAREA") return;
      if (current === steps.length - 1) return;
      e.preventDefault();
      var nextBtn = steps[current].querySelector("[data-next]");
      if (nextBtn) nextBtn.click();
    });

    form.__isStepValid = function () { return stepIsValid(steps[current]); };
  }

  function initForms() {
    var applicationForm = document.getElementById("applicationForm");
    var applicationSuccess = document.getElementById("applicationSuccess");
    if (applicationForm) {
      applicationForm.addEventListener("submit", function (e) {
        e.preventDefault();
        if (applicationForm.__isStepValid && !applicationForm.__isStepValid()) return;
        applicationSuccess.classList.add("is-visible");
      });
    }

    var contactForm = document.getElementById("contactForm");
    var contactSuccess = document.getElementById("contactSuccess");
    if (contactForm) {
      contactForm.addEventListener("submit", function (e) {
        e.preventDefault();
        contactSuccess.classList.add("is-visible");
      });
    }
  }

  document.addEventListener("DOMContentLoaded", function () {
    initIcons();
    initReveal();
    initHeaderScroll();
    initCounters();
    initVideoEmbeds();
    initVideoFilter();
    initNavToggle();
    initJobAccordion();
    initFaqAccordion();
    initMultistepForm();
    initForms();
    setTimeout(initIcons, 400);
  });
})();
