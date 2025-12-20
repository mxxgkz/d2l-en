// Hypothesis annotation client
// This script loads Hypothesis for collaborative annotation on the D2L book
// Using the official Hypothesis embed method
(function() {
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.async = true;
  script.src = 'https://hypothes.is/embed.js';
  document.getElementsByTagName('head')[0].appendChild(script);
})();

