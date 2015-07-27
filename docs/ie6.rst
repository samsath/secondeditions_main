::

        _/      _/    _/_/    
       _/_/  _/_/  _/    _/   
      _/  _/  _/  _/_/_/_/    
     _/      _/  _/    _/     
    _/      _/  _/    _/      
                            

By Andy Clarke - A IE6 Specific stylesheet:

One, standard, universal stylesheet for Internet Explorer 6. Simply copy one of these Conditional Comments into the head of any web page and you're done.

Tip: To hide all your other stylesheets from Internet Explorer 6, wrap them inside this Conditional Comment.

::

    <!--[if ! lte IE 6]><!-->
    /* Stylesheets for browsers other than Internet Explorer 6 */
    <!--<![endif]-->

Then add the Universal Internet Explorer 6 stylesheet.

::

    <!--[if lte IE 6]>
    <link rel="stylesheet" href="http://universal-ie6-css.googlecode.com/files/ie6.1.1.css" media="screen, projection">
    <![endif]-->

If you prefer a light-on-dark version (inspired by Instapaper), use this instead.

::

    <!--[if lte IE 6]>
    <link rel="stylesheet" href="http://universal-ie6-css.googlecode.com/files/ie6.1.1b.css" media="screen, projection">
    <![endif]-->
