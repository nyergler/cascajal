const {Cu} = require("chrome");
Cu.import("resource://gre/modules/FileUtils.jsm");

var prefs = require("sdk/preferences/service"),
    system = require("sdk/system"),
    timers = require("sdk/timers");

var printContentScript =
    "window.onafterprint = function(e) {  };" +
    "self.port.on('print', function(message) {" +
    "  window.print();" +
    "  self.port.emit('done', 'printing');" +
    "})";

var LAST_MTIME = 0,
    COUNT = 0;

function watch_file() {

    var filename = prefs.get("print.print_to_filename"),
        output_file = new FileUtils.File(filename),
        mtime = output_file.lastModifiedTime;

    if (mtime == LAST_MTIME) {
        COUNT++;
    } else {
        LAST_MTIME = mtime;
        COUNT = 0;
    }

    if (COUNT > 100) {
        system.exit();
    }

    timers.setTimeout(watch_file, 75);

};

require("sdk/tabs").on("ready", function(tab) {

    worker = tab.attach({
      contentScript: printContentScript
    });
    worker.port.on('done', function(message) {

        timers.setTimeout(watch_file, 1)

        // some day this will exit when it should; right now it's too
        // early :/
        // system.exit();
    });
    worker.port.emit('print');

});
