// Ajaxify
// v1.0.1 - 30 September, 2012
// https://github.com/browserstate/ajaxify
//
// Many modifications made by Gregor Müllegger

(function(window,undefined){

        // Prepare our Variables
        var
                History = window.History,
                $ = window.jQuery,
                document = window.document;

        // Check to see if History.js is enabled for our Browser
        if ( !History.enabled ) {
                return false;
        }

        // Wait for Document
        $(function(){
                // Prepare Variables
                var
                        /* Application Specific Variables */
                        contentSelector = '#frame',
                        $content = $(contentSelector).filter(':first'),
                        contentNode = $content.get(0),
                        $menu = $('#menu,#nav,nav:first,.nav:first').filter(':first'),
                        activeClass = 'active selected current youarehere',
                        activeSelector = '.active,.selected,.current,.youarehere',
                        menuChildrenSelector = '> li,> ul > li',
                        /* Application Generic Variables */
                        $window = $(window),
                        $html = $('html'),
                        $body = $(document.body),
                        rootUrl = History.getRootUrl(),
                        scrollOptions = {
                                duration: 800,
                                easing:'swing'
                        };

                // Ensure Content
                if ( $content.length === 0 ) {
                        $content = $body;
                }

                // Internal Helper
                $.expr[':'].internal = function(obj, index, meta, stack){
                        // Prepare
                        var
                                $this = $(obj),
                                url = $this.attr('href')||'',
                                isInternalLink;

                        // Check link
                        isInternalLink = url.substring(0,rootUrl.length) === rootUrl || url.indexOf(':') === -1;

                        // Ignore or Keep
                        return isInternalLink;
                };

                // HTML Helper
                var documentHtml = function(html){
                        // Prepare
                        var result = String(html)
                                .replace(/<\!DOCTYPE[^>]*>/i, '')
                                .replace(/<(html|head|body)([\s\>])/gi,'<div data-ajaxify-id="document-$1"$2')
                                .replace(/<(title|meta|script)([\s\>])/gi,'<div class="document-$1"$2')
                                .replace(/<\/(html|head|body|title|meta|script)\>/gi,'</div>')
                        ;

                        // Return
                        return $.trim(result);
                };

                // Ajaxify Helper
                $.fn.ajaxify = function(){
                        // Prepare
                        var $this = $(this);

                        // Ajaxify
                        $this.find('a:internal:not(.no-ajax)').click(function(event){
                                // Prepare
                                var
                                        $this = $(this),
                                        url = $this.attr('href'),
                                        title = $this.attr('title')||null;

                                // Continue as normal for cmd clicks etc
                                if ( event.which == 2 || event.metaKey ) { return true; }

                                // Ajaxify this link
                                History.pushState(null,title,url);
                                event.preventDefault();
                                return false;
                        });

                        // Chain
                        return $this;
                };

                // Hook into State Changes
                $window.bind('statechange',function(){
                        // Prepare Variables
                        var
                                State = History.getState(),
                                url = State.url,
                                relativeUrl = url.replace(rootUrl,'');

                        $window.trigger('ajaxify-start');

                        // Set Loading
                        $html.addClass('loading');
                        var minLoadingTime = parseInt($html.attr('data-ajaxify-loading-min'));
                        if (isNaN(minLoadingTime)) {
                            minLoadingTime = 0;
                        }
                        var startLoadingTimestamp = new Date().getTime();

                        // Ajax Request the Traditional Page
                        $.ajax({
                                url: url,
                                success: function(data, textStatus, jqXHR){

                                        // Prepare
                                        var
                                                $data = $(documentHtml(data)),
                                                $dataBody = $data.find('[data-ajaxify-id=document-body]:first'),
                                                $dataContent = $dataBody.find(contentSelector).filter(':first'),
                                                $menuChildren, contentHtml, $scripts;

                                        // Fetch the scripts
                                        $scripts = $dataContent.find('.document-script');
                                        if ( $scripts.length ) {
                                                $scripts.detach();
                                        }

                                        // Fetch the content
                                        contentHtml = $dataContent.html()||$data.html();
                                        if ( !contentHtml ) {
                                                document.location.href = url;
                                                return false;
                                        }

                                        var transitionPage = function () {
                                            // Update the menu
                                            $menuChildren = $menu.find(menuChildrenSelector);
                                            $menuChildren.filter(activeSelector).removeClass(activeClass);
                                            $menuChildren = $menuChildren.has('a[href^="'+relativeUrl+'"],a[href^="/'+relativeUrl+'"],a[href^="'+url+'"]');
                                            if ( $menuChildren.length === 1 ) { $menuChildren.addClass(activeClass); }

                                            // Update the content
                                            $content.stop(true,true);
                                            $content.html(contentHtml).ajaxify();

                                            $window.trigger('ajaxify-enter', {
                                                data: data,
                                                $data: $data,
                                                $dataBody: $dataBody,
                                                $dataContent: $dataContent,
                                                $content: $content,
                                                callback: function () {
                                                    $window.trigger('ajaxify-end');
                                                }
                                            });

                                            // Update the title
                                            document.title = $data.find('.document-title:first').text();
                                            try {
                                                    document.getElementsByTagName('title')[0].innerHTML = document.title.replace('<','&lt;').replace('>','&gt;').replace(' & ',' &amp; ');
                                            }
                                            catch ( Exception ) { }

                                            // Update body attributes
                                            // first: remove all existing attributes
                                            $.each($body[0].attributes, function (index, attr) {
                                                if (attr !== undefined) {
                                                    $body.removeAttr(attr.name);
                                                }
                                            });
                                            // second: assign new attributes
                                            $.each($dataBody[0].attributes, function (index, attr) {
                                                if (attr !== undefined) {
                                                    $body.attr(attr.name, attr.value);
                                                }
                                            });

                                            // Add the scripts
                                            $scripts.each(function(){
                                                    var $script = $(this), scriptText = $script.text(), scriptNode = document.createElement('script');
                                                    if ( $script.attr('src') ) {
                                                            if ( !$script[0].async ) { scriptNode.async = false; }
                                                            scriptNode.src = $script.attr('src');
                                                    }
                                                    scriptNode.appendChild(document.createTextNode(scriptText));
                                                    contentNode.appendChild(scriptNode);
                                            });

                                            // Complete the change
                                            if ( $body.ScrollTo||false ) { $body.ScrollTo(scrollOptions); } /* http://balupton.com/projects/jquery-scrollto */

                                            var stopLoading = function () {
                                                $html.removeClass('loading');
                                            };
                                            var sinceLoadingStarted = (new Date().getTime()) - startLoadingTimestamp;
                                            if (sinceLoadingStarted < minLoadingTime) {
                                                setTimeout(stopLoading, minLoadingTime - sinceLoadingStarted);   
                                            } else {
                                                stopLoading();
                                            }

                                            $window.trigger('ajaxify-ready');

                                            // Inform Google Analytics of the change
                                            if ( typeof window._gaq !== 'undefined' ) {
                                                    window._gaq.push(['_trackPageview', relativeUrl]);
                                            }

                                            // Inform ReInvigorate of a state change
                                            if ( typeof window.reinvigorate !== 'undefined' && typeof window.reinvigorate.ajax_track !== 'undefined' ) {
                                                    reinvigorate.ajax_track(url);
                                                    // ^ we use the full url here as that is what reinvigorate supports
                                            }
                                        };

                                        $window.trigger('ajaxify-leave', {
                                            data: data,
                                            '$data': $data,
                                            '$dataBody': $dataBody,
                                            '$dataContent': $dataContent,
                                            '$content': $content,
                                            callback: transitionPage
                                        });
                                },
                                error: function(jqXHR, textStatus, errorThrown){
                                        document.location.href = url;
                                        return false;
                                }
                        }); // end ajax

                }); // end onStateChange

        }); // end onDomLoad

})(window); // end closure

