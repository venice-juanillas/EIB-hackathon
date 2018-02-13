function append_notebook(a){clear_main_area(),$("#main").append('<iframe frameBorder="0" seamless="seamless" style="width: 100%; height: 100%; overflow:hidden;" scrolling="no" src="'+a+'"></iframe>')}function clear_main_area(){$("#spinner").remove(),$("#main").children().remove()}function display_spinner(){$("#main").append('<img id="spinner" src="'+galaxy_root+'static/style/largespinner.gif" style="position:absolute;margin:auto;top:0;left:0;right:0;bottom:0;">')}function make_spin_state(a,b,c,d,e,f,g,h){var i={type:"undefined"!=typeof a?a:"GIE spin",ajax_timeout:"undefined"!=typeof b?b:2e3,ajax_timeout_max:"undefined"!=typeof c?c:16e3,ajax_timeout_step:"undefined"!=typeof d?d:500,sleep:"undefined"!=typeof e?e:500,sleep_max:"undefined"!=typeof f?f:8e3,sleep_step:"undefined"!=typeof g?g:100,log_attempts:"undefined"!=typeof h?h:!0,count:0};return i}function spin_error(a,b,c){console.log(a),c&&clear_main_area(),"string"==typeof b&&(toastr.clear(),toastr.error(b,"Error",{closeButton:!0,timeOut:0,extendedTimeOut:0,tapToDismiss:!1}))}function spin_again(a){a.sleep<a.sleep_max&&(a.sleep+=a.sleep_step),a.log_attempts&&console.log(a.type+" request "+a.count+" request timeout "+a.ajax_timeout+"ms sleeping "+a.sleep/1e3+"s"),window.setTimeout(a.spinner,a.sleep)}function spin(a,b,c,d,e,f){var g=function(){var g={url:a,xhrFields:{withCredentials:!0},type:"GET",timeout:f.ajax_timeout,success:function(a,b,d){c(a,b,d)||(f.count++,spin_again(f))},error:function(a,b,c){"timeout"==b?(f.ajax_timeout<f.ajax_timeout_max&&(f.ajax_timeout+=f.ajax_timeout_step),f.count++,d(a,b,c)||spin_again(f)):(f.count++,e(a,b,c)||spin_again(f))}};b&&(g.dataType="json"),$.ajax(g)};console.log("Setting up new spinner for "+f.type+" on "+a),f.spinner=g,window.setTimeout(g,f.sleep)}function spin_until(a,b,c,d,e){var f=40,g=function(a,b){1==b.count&&(display_spinner(),toastr.info(a,null,{closeButton:!0,timeOut:0,extendedTimeOut:0,tapToDismiss:!1}))},h=function(a){if(!b||b&&1==a)console.log(c.success),clear_main_area(),toastr.clear(),d();else{if(b&&0==a)return g(c.not_ready,e),!1;spin_error("Invalid response to "+e.type+" request",c.invalid_response,!0)}return!0},i=function(){return g(c.waiting,e),e.count==f&&toastr.warning(c.wait_warn,"Warning",{closeButton:!0,timeOut:0,extendedTimeOut:0,tapToDismiss:!1}),!1};spin(a,b,h,i,i,e)}function load_when_ready(a,b){var c={success:"Galaxy reports IE container ready, returning",not_ready:"Galaxy is launching a container in which to run this interactive environment. Please wait...",unknown_response:"Galaxy failed to launch a container in which to run this interactive environment, contact a Galaxy administrator.",waiting:"Galaxy is launching a container in which to run this interactive environment. Please wait...",wait_warn:"It is taking an usually long time to start a container. Attempts will continue but you may want to report this condition to a Galaxy administrator if it does not succeed soon.",error:"Galaxy encountered an error while attempting to determine the readiness of this interactive environment's container, contact a Galaxy administrator."},d=make_spin_state("IE container readiness");spin_until(a,!0,c,b,d)}function test_ie_availability(a,b){var c={success:"IE connection succeeded, returning",waiting:"Interactive environment container is running, attempting to connect to the IE. Please wait...",wait_warn:"It is taking an usually long time to connect to the interactive environment. Attempts will continue but you may want to report this condition to a Galaxy administrator if it does not succeed soon.",error:"An error was encountered while attempting to connect to the interactive environment, contact your administrator."},d=make_spin_state("IE availability");spin_until(a,!1,c,b,d)}
//# sourceMappingURL=../maps/galaxy.interactive_environments.js.map