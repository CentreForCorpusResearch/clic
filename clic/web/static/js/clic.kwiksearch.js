;(function ( $, window, document, undefined ) {

  // Create the defaults once
  var pluginName = "kwikSearch",
      defaults = {
      };

  // The actual plugin constructor
  function Plugin( element, options ) {
    this.element = element;

    // jQuery has an extend method that merges the
    // contents of two or more objects, storing the
    // result in the first object. The first object
    // is generally empty because we don't want to alter
    // the default options for future instances of the plugin
    this.options = $.extend( {}, defaults, options) ;

    this._defaults = defaults;
    this._name = pluginName;

    this.init();
  }

  Plugin.prototype = {

    init: function() {
      var self = this;

      $('input', self.element)
        .autosizeInput();
    }

    fixSize: function() {
      var self = this;

      $('input.concordance', self.element);
        .css('min-width', '10px;');
    }

  }

  $.fn[pluginName] = function(methodOrOptions) {

    return this.each(function () {

      // attempt to fetch existing plugin
      var plugin = $.data(this, "plugin_" + pluginName);

      // make if it it doesn't exist
      if (!plugin) {
        plugin = new Plugin( this, methodOrOptions );
        $.data(this, "plugin_" + pluginName, plugin);
      }

      // call the appropriate method on it
      if ( plugin[methodOrOptions] ) {
        return plugin[ methodOrOptions ].apply( this, Array.prototype.slice.call( arguments, 1 ));
      } else if ( typeof methodOrOptions === 'object' || ! methodOrOptions ) {
        // init method called as part of initial construction
        return;
      } else {
        $.error( 'Method ' +  methodOrOptions + ' does not exist on jQuery.kwikSearch' );
      }
    });
  };

})( jQuery, window, document );
