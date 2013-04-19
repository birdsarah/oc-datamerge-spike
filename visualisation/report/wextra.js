d3.json("wextra.json", function(error, json){

    var oc = OCDATAVIS({cellSize: 10}),
        cellSize = oc.cellSize,
        width = oc.width,
        height = oc.height,
        blockheight = oc.blockheight,
        capitaliseFirstLetter = oc.capitaliseFirstLetter,
        getColumn = oc.getColumn,
        getRow = oc.getRow,
        getQuestionColor = oc.getQuestionColor,
        requiredblocks = ['World Bank',
                        'Colombia',
                        'Philippines Awards',
                        'Philippines Bids',
                        'UK Bids',
                        'UK Awards',
                        'US (Partial)'];

    var svg = d3.select("#wextra").selectAll("svg")
        .data(function() { var alldata = d3.entries(json),
                                filtereddata = [];
                            for (var i=0; i < alldata.length; i++) {
                                if (requiredblocks.indexOf(alldata[i].key) >= 0) {
                                    filtereddata.push(alldata[i])
                                }
                            }
                            return filtereddata;  })
        .enter().append("svg")
        .attr("width", width)
        .attr("height", height)

    svg.append("text")
        .attr("transform", "translate(0, 15)")
        .attr("class", "title")
        .text(function(d) { return d.key.toUpperCase(); });

    var questionblock = svg.selectAll(".questionblock")
        .data(function(d) { return d.value })
        .enter().append("g")
        .attr({
            "class": (function(d) { return "questionblock" + " " + d.name }),
            "transform": (function(d, i) { amount = 10 + i*100; return "translate(" + amount +", 30)" })
        })

    questionblock.append("text")
        .attr("transform", (function() {var h = blockheight + 25; return "translate(0, " + h +")"; }))
        .text(function(d) { var name = d.name;
                            if (name == 'extra') {
                                name = 'unused';
                            }
                            return capitaliseFirstLetter(name);
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

