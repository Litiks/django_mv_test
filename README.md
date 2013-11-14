django_mv_test
==============

Dead simple multivariate testing app for django, with no dependancies.

Setup
-----

1. Add to Installed Apps::

    INSTALLED_APPS += (
        'mv_test',
    )
    
2. Add to Middleware Classes::

    MIDDLEWARE_CLASSES += (
        'mv_test.middleware.MVMiddleware',
    )

3. Add to Template Context Processors::
    
    TEMPLATE_CONTEXT_PROCESSORS += (
        "mv_test.context.mv_test",
    )

4. Add to your urls.py::

    urlpatterns += patterns('',
        url(r'^mv_test/', include('mv_test.urls')),
    )

    
Usage
-----

There's no setup. Groups, Variations, and Goals are all created on demand.
You should create a 'control' variation for each group, but it's not mandatory.

In templates:
    {% if mv_profile.v.<group_name>.<variation_name> %}
    Example:
        {% if mv_profile.v.landing_text.control %}
            We build custom web applications for small businesses.
        {% endif %}
        {% if mv_profile.v.landing_text.time_and_money %}
            We build custom web applications that save businesses time and money.
        {% endif %}
        
    #record a goal success
    {{ mv_profile.goal.<goal_name> }}
    Example:
        {{ mv_profile.goal.newsletter_signup }}
        
In python:
    profile = request.mv_profile
    if profile.v().landing_text.control:
        #they see the usual text
    if profile.v().landing_text.time_and_money:
        #they see something different
        
    #record a goal success
    profile.goal().newsletter_signup



