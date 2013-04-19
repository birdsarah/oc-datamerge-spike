var OCDATAVIS = function(options) {
    'use strict';

    var options = options || {},
        cellSize = options.cellSize || 20,
        itemsPerColumn = 5,
        blockheight = cellSize * itemsPerColumn,
        width = 1200,
        height = 70 + blockheight,
        //initializes blockx & blockwidth which is used in loops to store prev
        blockx = 0,
        blockwidth = 0,
        questionColor = options.questionColor || "#CCC";

    function getRow(id) {
        var row =  id % itemsPerColumn;
        return row;
    }

    function getColumn(id) {
        return Math.floor(id / itemsPerColumn);
    }

    function getBlockWidth(elements) {
        var elementcount = elements.length,
            numberofcolumns = Math.ceil(elementcount / itemsPerColumn),
            blockwidth = numberofcolumns * cellSize;
        return blockwidth;
    }

    function getQuestionColor(question) {
        var qc = questionColor;
        if (question.hasmap === "True") {
            qc = "#6FA2FF";
        }
        if (!question.hasOwnProperty('hasmap')) {
            qc = "#FFD48E";
        }
        return qc;
    }

    function capitaliseFirstLetter(string) {
        return string.charAt(0).toUpperCase() + string.slice(1);
    }

    return {
        cellSize: cellSize,
        width: width,
        height: height,
        blockheight: blockheight,
        getRow: getRow,
        getColumn: getColumn,
        getQuestionColor: getQuestionColor,
        capitaliseFirstLetter: capitaliseFirstLetter
    }

};

