# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517811273.25522
_enable_loop = True
_template_filename = 'templates/js-app.mako'
_template_uri = '/js-app.mako'
_source_encoding = 'ascii'
_exports = ['page_setup', 'js_disabled_warning']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        js_app_entry_fn = context.get('js_app_entry_fn', UNDEFINED)
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        def js_disabled_warning():
            return render_js_disabled_warning(context._locals(__M_locals))
        bootstrapped = context.get('bootstrapped', UNDEFINED)
        def page_setup():
            return render_page_setup(context._locals(__M_locals))
        masthead = context.get('masthead', UNDEFINED)
        options = context.get('options', UNDEFINED)
        js_app_name = context.get('js_app_name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE HTML>\n<html>\n    <!--js-app.mako-->\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
        __M_writer(u'        <meta name="viewport" content="maximum-scale=1.0">\n')
        __M_writer(u'        <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1">\n\n        <title>\n            Galaxy\n')
        if app.config.brand:
            __M_writer(u'            | ')
            __M_writer(unicode(app.config.brand))
            __M_writer(u'\n')
        __M_writer(u'        </title>\n')
        __M_writer(u'        <link rel="index" href="')
        __M_writer(unicode( h.url_for( '/' ) ))
        __M_writer(u'"/>\n')
        __M_writer(u'        ')
        __M_writer(unicode( h.css(
            'jquery.rating',
            'jquery-ui/smoothness/jquery-ui',
            ## base needs to come after jquery-ui because of ui-button, ui- etc. name collision
            'base',
            'bootstrap-tour',
        )))
        __M_writer(u'\n        ')
        __M_writer(unicode( page_setup() ))
        __M_writer(u'\n    </head>\n\n    <body scroll="no" class="full-content">\n        <div id="everything" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;">\n')
        __M_writer(u'            <div id="background"></div>\n\n')
        if masthead:
            __M_writer(u'            <div id="masthead" class="navbar navbar-fixed-top navbar-inverse"></div>\n')
            __M_writer(u'            <div id="messagebox" style="display: none;"></div>\n')
            __M_writer(u'            <div id="inactivebox" class="panel-warning-message" style="display: none;"></div>\n')
        __M_writer(u'\n        </div><!--end everything-->\n        <div id=\'dd-helper\' style="display: none;"></div>\n        ')
        __M_writer(unicode( js_disabled_warning() ))
        __M_writer(u'\n\n')
        __M_writer(u'        ')
        __M_writer(unicode( h.js(
            'libs/require',
            'bundled/libs.bundled',
            'bundled/' + js_app_name + '.bundled'
        )))
        __M_writer(u'\n        <script type="text/javascript">\n            require.config({\n                baseUrl: "')
        __M_writer(unicode(h.url_for('/static/scripts') ))
        __M_writer(u'",\n                shim: {\n                    "libs/underscore": {\n                        exports: "_"\n                    },\n                    "libs/backbone": {\n                        deps: [ \'jquery\', \'libs/underscore\' ],\n                        exports: "Backbone"\n                    }\n                },\n                // cache busting using time server was restarted\n                urlArgs: \'v=')
        __M_writer(unicode(app.server_starttime))
        __M_writer(u"',\n            });\n            ")
        __M_writer(unicode(js_app_entry_fn))
        __M_writer(u'(\n                ')
        __M_writer(unicode( h.dumps( options ) ))
        __M_writer(u',\n                ')
        __M_writer(unicode( h.dumps( bootstrapped ) ))
        __M_writer(u'\n            );\n        </script>\n    </body>\n</html>\n\n')
        __M_writer(u'\n\n')
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_page_setup(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        app = context.get('app', UNDEFINED)
        trans = context.get('trans', UNDEFINED)
        options = context.get('options', UNDEFINED)
        form_input_auto_focus = context.get('form_input_auto_focus', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        if app.config.sentry_dsn:
            __M_writer(u'    ')
            __M_writer(unicode(h.js( "libs/raven" )))
            __M_writer(u"\n    <script>\n        Raven.config('")
            __M_writer(unicode(app.config.sentry_dsn_public))
            __M_writer(u"').install();\n")
            if trans.user:
                __M_writer(u'            Raven.setUser( { email: "')
                __M_writer(filters.html_escape(unicode(trans.user.email)))
                __M_writer(u'" } );\n')
            __M_writer(u'    </script>\n')
        __M_writer(u'\n    <script type="text/javascript">\n        // this is needed *before* the app code is loaded - many MVC access Galaxy.root for their url\n        // TODO: change this by using a common Backbone.Model base class and url fn\n        window.Galaxy = { root: \'')
        __M_writer(unicode( options[ "root" ] ))
        __M_writer(u"' };\n    </script>\n\n")
        if not form_input_auto_focus is UNDEFINED and form_input_auto_focus:
            __M_writer(u'    <script type="text/javascript">\n        $(document).ready( function() {\n            // Auto Focus on first item on form\n            if ( $("*:focus").html() == null ) {\n                $(":input:not([type=hidden]):visible:enabled:first").focus();\n            }\n        });\n    </script>\n')
        __M_writer(u'\n')
        if app.config.ga_code:
            __M_writer(u'    <script type="text/javascript">\n        (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n        })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n        ga(\'create\', \'')
            __M_writer(unicode(app.config.ga_code))
            __M_writer(u"', 'auto');\n        ga('send', 'pageview');\n    </script>\n")
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js_disabled_warning(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer(u'\n    <noscript>\n        <div class="overlay overlay-background noscript-overlay">\n            <div>\n                <h3 class="title">Javascript Required for Galaxy</h3>\n                <div>\n                    The Galaxy analysis interface requires a browser with Javascript enabled.<br>\n                    Please enable Javascript and refresh this page.\n                </div>\n            </div>\n        </div>\n    </noscript>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"133": 127, "16": 0, "32": 1, "33": 8, "34": 10, "35": 14, "36": 15, "37": 15, "38": 15, "39": 17, "40": 19, "41": 19, "42": 19, "43": 21, "44": 21, "51": 27, "52": 28, "53": 28, "54": 34, "55": 36, "56": 37, "57": 39, "58": 41, "59": 43, "60": 46, "61": 46, "62": 49, "63": 49, "68": 53, "69": 56, "70": 56, "71": 67, "72": 67, "73": 69, "74": 69, "75": 70, "76": 70, "77": 71, "78": 71, "79": 119, "80": 134, "86": 78, "95": 78, "96": 80, "97": 81, "98": 81, "99": 81, "100": 83, "101": 83, "102": 84, "103": 85, "104": 85, "105": 85, "106": 87, "107": 89, "108": 93, "109": 93, "110": 96, "111": 97, "112": 106, "113": 108, "114": 109, "115": 114, "116": 114, "117": 118, "123": 122, "127": 122}, "uri": "/js-app.mako", "filename": "templates/js-app.mako"}
__M_END_METADATA
"""
