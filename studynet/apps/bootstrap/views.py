# Not real BigPipe yet, but HTTP streaming only. 

#from django import settings
from django.http import HttpResponse
from django.core.cache import cache
from django.template.loader import render_to_string
from django.views.decorators.http import condition
from django.template import RequestContext

@condition(etag_func=None)  # for HTTP streaming
def ship(request):

    resp = HttpResponse(do_ship(request), mimetype='text/html')

    return resp

def do_ship(request):

    # for debugging. TODO: remove while deploy.
    #cache.clear()

    # character '.' will cause empty content.
    resources = { 
      'home_css': "/** Merged and Compiled LESS file here **/",
      'home_js' : "/** Merged Javascript file here **/",
      'course_css': "/** Merged and Compiled LESS file here **/",
      'course_js' : "/** Merged Javascript file here **/",
      'course_css': "/** Merged and Compiled LESS file here **/",
      'course_js' : "/** Merged Javascript file here **/",
      'application_css': "/** Merged and Compiled LESS file here **/",
      'application_js' : "/** Merged Javascript file here **/"+APPLICATION_JS,
    }

    # context_instance for STATIC_URL in templates.
    yield render_to_string("application/initialize.html", resources, context_instance=RequestContext(request) ).ljust(4096) 
    yield render_to_string("home/home.html", resources, context_instance=RequestContext(request) ).ljust(4096)
    yield render_to_string("widget/activity.html", resources, context_instance=RequestContext(request) ).ljust(4096)
    yield render_to_string("widget/side-chatroom-message.html", resources, context_instance=RequestContext(request) ).ljust(4096)
    yield render_to_string("widget/course-nav-section.html", resources, context_instance=RequestContext(request) ).ljust(4096)
    yield render_to_string("course/course.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-note.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-map.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-index.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-comment.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-media.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-main-note-row.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("course/course-students-slot.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("courses/courses.html", resources, context_instance=RequestContext(request)  ).ljust(4096) 
    yield render_to_string("application/finalize.html", resources, context_instance=RequestContext(request) ).ljust(4096) 

# Temporarily bootstraping Javascript should be replaced in application.js .
APPLICATION_JS = """
    self.app = self.app || {}
    self.app.settings  = self.app.settings || {}
    self.app.bootstrap = {}
    self.app.bootstrap.onArrive = function(id)
    {   
        $('script[subpage="'+id+'"]').remove()
        if( true == self.app.settings.DEBUG ){ console.log("[DEBUG] Subpage arrived: ",id) }

        var $subpage = $('[subpage="'+id+'"]')

        // Template will not be append into normal place.
        if(! $subpage.hasClass('template') )
        {
            $('#'+id).replaceWith($subpage)
            $('[subpage="'+id+'"]').attr('id',id)
        }
        else
        {
            $('#template').append($subpage)
        }
    }

"""

APPLICATION_CSS = """
    div.subpage
    {
        display:none;
    }

    div.subpage.active
    {
        display:block;
    }
"""
