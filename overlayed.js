d3.json("overlayed.json", function(error, json){

    var oc = OCDATAVIS({cellSize: 30, questionColor: "#FFF"}),
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
            'US (Partial)'],
        dataset = d3.entries(json),
        filtereddata = [];

    for (var i=0; i < dataset.length; i++) {
        if (requiredblocks.indexOf(dataset[i].key) >= 0) {
            filtereddata.push(dataset[i])
        }
    }

    var questionblock = d3.select("#overlayed")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .selectAll(".questionblock")
        .data(filtereddata)
        .enter().append("g")
        .attr({
            "class": (function(d) { return d.key }),
        })

    var addlayer = questionblock.selectAll(".added")
        .data(function(d) { return d.value })
        .enter().append("g")
        .attr({
            "class": (function(d) { return "addlayer" + " " + d.key }),
            "transform": (function(d, i) { amount = i*150; return "translate(" + amount +", 25)" })
        })

    addlayer.append("text")
    .attr("transform", (function() {var h = blockheight + 25; return "translate(0, " + h +")"; }))
    .text(function(d) { var name = d.name;
                        if (this.parentNode.parentNode.className.animVal === requiredblocks[1]) {
                        if (name == 'extra') {
                            name = '';
                        }
                        return capitaliseFirstLetter(name);
                        }}
        );

    addlayer.selectAll(".question")
        .data(function(d) { return d.children })
        .enter().append("rect")
        .attr({
            "class": "question",
            "x": (function(d, i) { return cellSize*getColumn(i) }),
            "y": (function(d, i) { return blockheight - cellSize*(getRow(i)+1) }),
            "width": cellSize,
            "height": cellSize,
            "fill": getQuestionColor,
            "fill-opacity": ".35",
            "stroke": "#eee",
            "stroke-weight": "1px",
            "title": (function(d) { return d.questionkey })
        });

});

