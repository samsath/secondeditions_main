::

        _/      _/    _/_/    
       _/_/  _/_/  _/    _/   
      _/  _/  _/  _/_/_/_/    
     _/      _/  _/    _/     
    _/      _/  _/    _/      
                            

Mediastore Documentation
==============================

You can take the same code as in /display.html template, put it in where you want it and wrap the code with:

{% with object.media.all.0.object as object %}
... code from display.html ...
{% endwith %}

or for MediaField:

{% with object.primary_image.object as object %}
... code from display.html ...
{% endwith %}


or for multiple media (for loops)

displays all the media within a MultipleMediaField:
{% display_media object.primary_media.all %}

displays each type of media within a MultipleMediaField:
{% display_video object.media.all %}
{% display_image object.media.all %}
{% display_embeded object.media.all %}


---------------

REQUIRED

{% media_requirements video %}

and

{% media_requirements image %}
