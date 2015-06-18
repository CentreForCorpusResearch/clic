;(function ( $, window, document, undefined ) {

    // Create the defaults once
    var pluginName = "concordanceResults",
        defaults = {
            concordanceEndpointUrl : "/api/concordances_ajax/",
            bookCountsEndpointUrl : "/exampleJson/bookcounts.json"
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

        searchTerms: "",
        searchSpace: "",
        totalNumberOfHits: 0,

        init: function() {
            var that = this;

            var params = location.search;
            this.processParameters(params);
            this.concordanceUrl = this.options.concordanceEndpointUrl + params;

            $.when(
                $.ajax({
                    url: that.options.bookCountsEndpointUrl,
                    type: 'GET',
                    dataType: 'json'}),
                $.ajax({
                    url: this.concordanceUrl,
                    type: 'GET',
                    dataType: 'json'})
            ).then(
                function(chaptersData, concordancesData) { // success
                    var chData = chaptersData[0];
                    var coData = concordancesData[0];

                    var chapterData = that.processChapterMarkers(chData);
                    //var concordanceContent = that.processConcordanceData(coData);
                    //var concordancePlot = that.processConcordancePlot(coData, chapterData);

                    //that.renderConcordance(concordanceContent, concordancePlot);
                    that.setupDataTables();
                    Pace.stop();
                },
                function(e) { // failure
                    console.log(e);
                    alert("Sorry. Failed to load data. Please try again.");
                    Pace.stop()
                }
            );
        },

        processParameters: function( params ) {
            var searchTerms = params.slice(params.indexOf("terms=") + 6);
            this.searchTerms = decodeURIComponent(searchTerms.slice(0, searchTerms.indexOf("&")).replace(/\+/g, ' '));

            var testIdxMod = params.slice(params.indexOf("testIdxMod=") + 11);

            switch(testIdxMod) {
                case "quote":
                    this.searchSpace = "quotes";
                    break;

                case "non-quote":
                    this.searchSpace = "non-quotes";
                    break;

                case "longsus":
                    this.searchSpace = "long suspensions";
                    break;

                case "shortsus":
                    this.searchSpace = "short suspensions";
                    break;

                default:
                    this.searchSpace = "whole text";
                    break;
            }
        },

        processChapterMarkers: function( data ) {
            chapterDataArray = [];
            for (var x = 0; x < data[1].length; x++) {

                // Per book chapter SVG shading
                var bookTitle = data[1][x][1];
                var chapters = data[1][x][3]; // chapter data
                var total = (data[1][x][2][0] / 1000);// <total words in book> / <length of SVG (constant) >

                var xVal = '';
                var wVal = '';
                var svg = '';

                for (var i = 1; i < chapters.length; i = i + 2) {
                    xVal = chapters[i] / total;
                    wVal = (chapters[i + 1] - chapters[i]) / total; //width
                    svg += '<rect x="' + xVal + '" y="0" width="' + wVal + '" height="27" fill="#bbb"/>';
                }

                chapterDataArray.push({
                    booktitle: bookTitle,
                    svgMarkup: svg
                });
            }

            return chapterDataArray;
        },

        processConcordanceData: function( data ) {
            this.totalNumberOfHits = data.concordances[0];

            var content = '';
            // loop out values
            for (var x = 1; x < data.concordances.length; x++) {
                var wordsLhs = '';
                var wordsRhs = '';
                var node = '';

                var chapterViewUrl = '/chapter/' + data.concordances[x][3][0] + '/' + data.concordances[x][3][2] + '/' + data.concordances[x][3][5] + '/' + this.searchTerms + '/#concordance';

                content += '<tr class="clickable_row" data-url="' + chapterViewUrl + '">';
                // counter
                content += '<td>' + x + '</td>';
                // words left
                for (var s = 0; s < data.concordances[x][0].length; s++) {
                    wordsLhs += data.concordances[x][0][s] + ' ';
                }

                content += '<td class="left nowrap" align="right"><span>' + wordsLhs + '</span></td>';

                // node
                for (var s = 0; s < data.concordances[x][1].length; s++) {
                    node += data.concordances[x][1][s] + ' ';
                }
                content += '<td class="hilight">' + node + '</td>';

                // words right
                for (var s = 0; s < data.concordances[x][2].length; s++) {
                    wordsRhs += data.concordances[x][2][s] + ' ';
                }
                content += '<td class="right nowrap">' + wordsRhs + '</td>';
                //Book
                content += '<td class="book">' + data.concordances[x][3][1] + '</td>';
                // Chapter
                content += '<td>' + data.concordances[x][3][2] + '</td>';
                // Paragraph
                content += '<td>' + data.concordances[x][3][3] + '</td>';
                // Sentence
                content += '<td>' + data.concordances[x][3][4] + '</td>';
                // % In book
                var wordInBook = (data.concordances[x][4][2] / data.concordances[x][4][3]) * 100; // word in book / total word count
                var xVal = Math.round(wordInBook) / 2;
                content += '<td><svg width="50px" height="15px" xmlns="http://www.w3.org/2000/svg">' +
                        '<rect x="0" y="4" width="50" height="7" fill="#ccc"/>' +
                        '<line x1="' + xVal + '" x2="' + xVal + '" y1="0" y2="15" stroke="black" stroke-width="2px"/>' +
                        '</svg>';
                content += '</tr></td>';
            }

            return content;
        },

        processConcordancePlot: function( data, chapterDataArray ) {
            // Add unique book titles to array
            var uniqueBookTitles = [];
            for (var x = 1; x < data.concordances.length; x++) {
                var bookTitle = data.concordances[x][3][1];
                if (uniqueBookTitles.indexOf(bookTitle) < 0) {
                    uniqueBookTitles.push(bookTitle);
                }
            }
            uniqueBookTitles.sort();

            var plotContent = '';
            for (var i = 0; i < uniqueBookTitles.length; i++) {

                // loop out line values
                var lines = '';
                var lineCount = 0; // no of occurrences of word
                for (var x = 1; x < data.concordances.length; x++) {
                    // if this is the book title we want
                    if (data.concordances[x][3][1] == uniqueBookTitles[i]) {
                        // calculate line values
                        var totalWordCountInBook = data.concordances[x][4][3];
                        var adjustedTotalWordCountInBook = totalWordCountInBook / 1000;
                        var wordInBook = data.concordances[x][4][2];
                        var xVal = wordInBook / adjustedTotalWordCountInBook;

                        // line here
                        lines += '<line x1="' + xVal + '" x2="' + xVal + '" y1="0" y2="27" stroke="#468847" stroke-width="3px"/>';
                        lineCount++;
                    }

                }
                plotContent += '<tr>';
                plotContent += '<td class="book">' + uniqueBookTitles[i] + '</td><td>'+lineCount+'</td>';
                plotContent += '<td class="plot">';
                plotContent += '<svg width="100%" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 27" preserveAspectRatio="none">';

                plotContent += '<rect x="0" y="0" width="1000" height="27" fill="#ccc"/>';

                // Add chapter shading to SVG
                var thisSvgMarkup = $.grep(chapterDataArray, function (e) { return e.booktitle == uniqueBookTitles[i]; }); // lookup
                if (typeof thisSvgMarkup[0] != "undefined") {
                    plotContent += thisSvgMarkup[0].svgMarkup;
                }
                plotContent += lines + '</svg></td></tr>';
            }

            return plotContent;
        },

        renderConcordance: function( content, plotContent ) {
            $('#resultsTbody').html(content);
            $('#plotTbody').html(plotContent);

            $('#dataTableConcordance tbody').on( 'click', 'tr', function () {
                window.location = $(this).data('url');
            });

            $("#searchedFor").html("Searched for <b>" + this.searchTerms + "</b> within <b>" + this.searchSpace + "</b>.");

            $('#concordanceWrap').show();
        },

        setupDataTables: function() {
            alert(this.concordanceUrl);
            $('#dataTableConcordance').DataTable({
                "ajax": true,
                "url": this.concordanceUrl,
                "columns": [
                    { "data": "left_text" },
                    { "data": "node_text" },
                    { "data": "right_text" },
                    { "data": "book_title" },
                    { "data": "chapter" },
                    { "data": "para_chap" },
                    { "data": "sent_chap" },
                    { "data": "sent_book" }
                ]
            });
        }
    };

    // A really lightweight plugin wrapper around the constructor,
    // preventing against multiple instantiations
    $.fn[pluginName] = function ( options ) {
        return this.each(function () {
            if (!$.data(this, "plugin_" + pluginName)) {
                $.data(this, "plugin_" + pluginName,
                new Plugin( this, options ));
            }
        });
    };

})( jQuery, window, document );
