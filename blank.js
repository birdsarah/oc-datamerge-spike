d3.json("blank.json", function(error, json){

    var oc = OCDATAVIS({cellSize: 30}),
        cellSize = oc.cellSize,
        width = oc.width,
        height = oc.height,
        blockheight = oc.blockheight,
        capitaliseFirstLetter = oc.capitaliseFirstLetter,
        getColumn = oc.getColumn,
        getRow = oc.getRow,
        getQuestionColor = oc.getQuestionColor;

    var svg = d3.select("#blank").selectAll("svg")
            .data(d3.entries(json))
            .enter().append("svg")
            .attr("width", width)
            .attr("height", height);

    var questionblock = svg.selectAll(".questionblock")
            .data(function(d) { return d.value })
            .enter().append("g")
            .attr({
                "class": (function(d) { return "questionblock" + " " + d.name }),
                "transform": (function(d, i) { amount = i*150; return "translate(" + amount +", 25)" })
            });

    questionblock.append("text")
        .attr("transform", (function() {var h = blockheight + 25; return "translate(0, " + h +")"; }))
        .text(function(d) { var name = d.name;
                                if (name == 'extra') {
                                name = 'unused';
                                }
                                return capitaliseFirstLetter(name)
                                }
                );

    questionblock.selectAll(".question")
        .data(function(d) { return d.children })
        .enter().append("rect")
        .attr({
            "class": "question",
            "x": (function(d, i) { return cellSize*getColumn(i) }),
            "y": (function(d, i) { return blockheight - cellSize*(getRow(i)+1) }),
            "width": cellSize,
            "height": cellSize,
            "fill": getQuestionColor,
            "stroke": "#fff",
            "stroke-weight": "1px",
            "title": (function(d) { return d.questionkey })
        });
});
