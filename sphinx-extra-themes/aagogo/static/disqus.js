var disqus_config = function () {
this.page.url = 'http://'+location.host+location.pathname;
this.page.identifier = $("#disqus_thread").attr("data-disqus-identifier");
};

(function() { 
var d = document, s = d.createElement('script');
s.src = '//programmeerimine.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
