console.log(statedata)
// function filterMap(allcoursefilterMap) {
//  // does some math and gets numbers from the context data
//  statedata['WA']['SA']['NT']['QLD']['NSW']['VIC']['ACT']['TAS']
//  // update the map
// }

// DATA TO BE DISPLAYED ON OUTPUT BOX IN TOP RIGHT OF MAP

// Aust - all courses button - map output box when selected ALL COURSES filter not hovering over a state
function totalParticipantsAustralia() {
    return totalWA() + totalSA() + totalNT() + totalQLD() + totalNSW() + totalVIC() + totalACT() + totalTAS()
}
function metroParticipantsAustralia() {
    return metroWorkshopAustralia() + metroFlashAustralia() + metroPlusAustralia() + metroAlumni_mentorAustralia()
}
function regionalParticipantsAustralia() {
    return regionalWorkshopAustralia() + regionalFlashAustralia() + regionalPlusAustralia() + regionalAlumni_mentorAustralia()
}

// Aust - workshop courses button - map output box when selected WORKSHOP filter not hovering over a state
function totalWorkshopAustralia() {
    return workshopWA() + workshopSA() + workshopNT() + workshopQLD() + workshopNSW() + workshopVIC() + workshopACT() + workshopTAS()
}
function metroWorkshopAustralia() {
    return metroworkshopWA() + metroworkshopSA() + metroworkshopNT() + metroworkshopQLD() + metroworkshopNSW() + metroworkshopVIC() + metroworkshopACT() + metroworkshopTAS()
}
function regionalWorkshopAustralia() {
    return regionalworkshopWA() + regionalworkshopSA() + regionalworkshopNT() + regionalworkshopQLD() + regionalworkshopNSW() + regionalworkshopVIC() + regionalworkshopACT() + regionalworkshopTAS()
}

//  Aust - flash courses button - map output box when selected FLASH filter not hovering over a state
function totalFlashAustralia() {
    return flashWA() + flashSA() + flashNT() + flashQLD() + flashNSW() + flashVIC() + flashACT() + flashTAS()
}
function metroWorkshopAustralia() {
    return metroflashWA() + metroflashSA () + metroflashNT () + metroflashQLD () + metroflashNSW () + metroflashVIC () + metroflashACT () + metroflashTAS () 
}
function regionalWorkshopAustralia() {
    return regionalflashWA() + regionalflashSA() + regionalflashNT() + regionalflashQLD() + regionalflashNSW() + regionalflashVIC() + regionalflashACT() + regionalflashTAS()
}

//  Aust - plus courses button - map output box when selected PLUS filter not hovering over a state
function totalPlusAustralia() {
    return plusWA() + plusSA() + plusNT() + plusQLD() + plusNSW() + plusVIC() + plusACT() + plusTAS()
}
function metroWorkshopAustralia() {
    return metroplusWA() + metroplusSA() + metroplusNT() + metroplusQLD() + metroplusNSW() + metroplusVIC() + metroplusACT() + metroplusTAS()
}
function regionalWorkshopAustralia() {
    return regionalplusWA() + regionalplusSA() + regionalplusNT() + regionalplusQLD() + regionalplusNSW() + regionalplusVIC() + regionalplusACT() + regionalplusTAS()
}

//  Aust - alumni_mentor courses button - map output box when selected ALUMNI MENTOR filter not hovering over a state
function totalAlumni_mentorAustralia() {
    return alumni_mentorWA() + alumni_mentorSA() + alumni_mentorNT() + alumni_mentorQLD() + alumni_mentorNSW() + alumni_mentorVIC() + alumni_mentorACT() + alumni_mentorTAS()
}
function metroWorkshopAustralia() {
    return metroalumni_mentorWA() + metroalumni_mentorSA() + metroalumni_mentorNT() + metroalumni_mentorQLD() + metroalumni_mentorNSW() + metroalumni_mentorVIC() + metroalumni_mentorACT() + metroalumni_mentorTAS()
}
function regionalWorkshopAustralia() {
    return regionalalumni_mentorWA() + regionalalumni_mentorSA() + regionalalumni_mentorNT() + regionalalumni_mentorQLD() + regionalalumni_mentorNSW() + regionalalumni_mentorVIC() + regionalalumni_mentorACT() + regionalalumni_mentorTAS()
}

//  WA Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over WA
function totalWA() {
    return shecodes_statedata['WA']['regional']['1 day'] + shecodes_statedata['WA']['regional']['flash'] + shecodes_statedata['WA']['regional']['plus'] + shecodes_statedata['WA']['regional']['alumni_mentor'] + shecodes_statedata['WA']['metro']['1 day'] + shecodes_statedata['WA']['metro']['flash'] + shecodes_statedata['WA']['metro']['plus'] + shecodes_statedata['WA']['metro']['alumni_mentor']
}

function metroallcoursesWA() {
	return metroworkshopWA() + metroflashWA() + metroplusWA() + metroalumni_mentorWA()
}

function regionalallcoursesWA() {
	return regionalworkshopWA() + regionalflashWA() + regionalplusWA() + regionalalumni_mentorWA()
}

//  WA hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over WA
function workshopWA() {
    return shecodes_statedata['WA']['regional']['1 day'] + shecodes_statedata['WA']['metro']['1 day']
}
function metroworkshopWA() {
    return shecodes_statedata['WA']['metro']['1 day']
}
function regionalworkshopWA() {
    return shecodes_statedata['WA']['regional']['1 day']
}

// WA hover -  flash course button - map output box when selected FLASH filter and hovering over WA
function flashWA() {
    return shecodes_statedata['WA']['regional']['flash'] + shecodes_statedata['WA']['metro']['flash']
}
function metroflashWA() {
    return shecodes_statedata['WA']['metro']['flash']
}
function regionalflashWA() {
    return shecodes_statedata['WA']['regional']['flash']
}

// WA hover -  plus course button - map output box when selected PLUS filter and hovering over WA
function plusWA() {
    return shecodes_statedata['WA']['regional']['plus'] + shecodes_statedata['WA']['metro']['plus']
}
function metroplusWA() {
    return shecodes_statedata['WA']['metro']['plus']
}
function regionalplusWA() {
    return shecodes_statedata['WA']['regional']['plus']
}
// WA hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over WA
function alumni_mentorWA() {
    return shecodes_statedata['WA']['regional']['alumni_mentor'] + shecodes_statedata['WA']['metro']['alumni_mentor']
}
function metroalumni_mentorWA() {
    return shecodes_statedata['WA']['metro']['alumni_mentor']
}
function regionalalumni_mentorWA() {
    return shecodes_statedata['WA']['regional']['alumni_mentor']
}


// State total all courses

function totalSA() {
    return shecodes_statedata['SA']['regional']['1 day'] + shecodes_statedata['SA']['regional']['flash'] + shecodes_statedata['SA']['regional']['plus'] + shecodes_statedata['SA']['regional']['alumni_mentor'] + shecodes_statedata['SA']['metro']['1 day'] + shecodes_statedata['SA']['metro']['flash'] + shecodes_statedata['SA']['metro']['plus'] + shecodes_statedata['SA']['metro']['alumni_mentor']
}
function totalNT() {
    return shecodes_statedata['NT']['regional']['1 day'] + shecodes_statedata['NT']['regional']['flash'] + shecodes_statedata['NT']['regional']['plus'] + shecodes_statedata['NT']['regional']['alumni_mentor'] + shecodes_statedata['NT']['metro']['1 day'] + shecodes_statedata['NT']['metro']['flash'] + shecodes_statedata['NT']['metro']['plus'] + shecodes_statedata['NT']['metro']['alumni_mentor']
}
function totalQLD() {
    return shecodes_statedata['QLD']['regional']['1 day'] + shecodes_statedata['QLD']['regional']['flash'] + shecodes_statedata['QLD']['regional']['plus'] + shecodes_statedata['QLD']['regional']['alumni_mentor'] + shecodes_statedata['QLD']['metro']['1 day'] + shecodes_statedata['QLD']['metro']['flash'] + shecodes_statedata['QLD']['metro']['plus'] + shecodes_statedata['QLD']['metro']['alumni_mentor']
}
function totalNSW() {
    return shecodes_statedata['NSW']['regional']['1 day'] + shecodes_statedata['NSW']['regional']['flash'] + shecodes_statedata['NSW']['regional']['plus'] + shecodes_statedata['NSW']['regional']['alumni_mentor'] + shecodes_statedata['NSW']['metro']['1 day'] + shecodes_statedata['NSW']['metro']['flash'] + shecodes_statedata['NSW']['metro']['plus'] + shecodes_statedata['NSW']['metro']['alumni_mentor']
}
function totalVIC() {
    return shecodes_statedata['VIC']['regional']['1 day'] + shecodes_statedata['VIC']['regional']['flash'] + shecodes_statedata['VIC']['regional']['plus'] + shecodes_statedata['VIC']['regional']['alumni_mentor'] + shecodes_statedata['VIC']['metro']['1 day'] + shecodes_statedata['VIC']['metro']['flash'] + shecodes_statedata['VIC']['metro']['plus'] + shecodes_statedata['VIC']['metro']['alumni_mentor']
}
function totalACT() {
    return shecodes_statedata['ACT']['regional']['1 day'] + shecodes_statedata['ACT']['regional']['flash'] + shecodes_statedata['ACT']['regional']['plus'] + shecodes_statedata['ACT']['regional']['alumni_mentor'] + shecodes_statedata['ACT']['metro']['1 day'] + shecodes_statedata['ACT']['metro']['flash'] + shecodes_statedata['ACT']['metro']['plus'] + shecodes_statedata['ACT']['metro']['alumni_mentor']
}
function totalTAS() {
    return shecodes_statedata['TAS']['regional']['1 day'] + shecodes_statedata['TAS']['regional']['flash'] + shecodes_statedata['TAS']['regional']['plus'] + shecodes_statedata['TAS']['regional']['alumni_mentor'] + shecodes_statedata['TAS']['metro']['1 day'] + shecodes_statedata['TAS']['metro']['flash'] + shecodes_statedata['TAS']['metro']['plus'] + shecodes_statedata['TAS']['metro']['alumni_mentor']
}


const drawMap = function(courseType) {
  var map = L.map('map').setView([-27.833, 133.583], 4);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/light-v9',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);

    // DATA COLOUR ON MAP
    let stateCounts = {
        WA: 0,
        SA: 0,
        NT: 0,
        QLD: 0,
        NSW: 0,
        VIC: 0,
        ACT: 0,
        TAS: 0,
    }
        if (courseType == 'all') {
            // call the function taht counts all  numbers
            stateCounts.WA = totalWA(),
            stateCounts.SA = totalSA(),
            stateCounts.NT = totalNT(),
            stateCounts.QLD = totalQLD(),
            stateCounts.NSW = totalNSW(),
            stateCounts.VIC = totalVIC(),
            stateCounts.ACT = totalACT(),
            stateCounts.TAS = totalTAS()
    };
        if (courseType == '1 day') {
            stateCounts.WA = workshopWA(),
            stateCounts.SA = workshopSA(),
            stateCounts.NT = workshopNT(),
            stateCounts.QLD = workshopQLD(),
            stateCounts.NSW = workshopNSW(),
            stateCounts.VIC = workshopVIC(),
            stateCounts.ACT = workshopACT(),
            stateCounts.TAS = workshopTAS()
    };
        if (courseType == 'flash') {
            stateCounts.WA = flashWA()
    };
        if (courseType == 'plus') {
            stateCounts.WA = plusWA()
    };
        if (courseType == 'alumni_mentor') {
            stateCounts.WA = alumni_mentorWA()
    };

	let metrostateCounts = {
        WA: 0,
        SA: 0,
        NT: 0,
        QLD: 0,
        NSW: 0,
        VIC: 0,
        ACT: 0,
        TAS: 0,
    }
        if (courseType == 'all') {
            // call the function taht counts all  numbers
            metrostateCounts.WA = metroallcoursesWA,
    };
        if (courseType == '1 day') {
            metrostateCounts.WA = metroworkshopWA(),
    };
        if (courseType == 'flash') {
			metrostateCounts.WA = metroflashWA()
    };
        if (courseType == 'plus') {
            metrostateCounts.WA = metroplusWA()
    };
        if (courseType == 'alumni_mentor') {
			metrostateCounts.WA = metroalumni_mentorWA()
    };

	let regionalstateCounts = {
        WA: 0,
        SA: 0,
        NT: 0,
        QLD: 0,
        NSW: 0,
        VIC: 0,
        ACT: 0,
        TAS: 0,
    }
        if (courseType == 'all') {
            // call the function taht counts all  numbers
            regionalstateCounts.WA = regionalallcoursesWA,
    };
        if (courseType == '1 day') {
            regionalstateCounts.WA = regionalworkshopWA(),
    };
        if (courseType == 'flash') {
			regionalstateCounts.WA = regionalflashWA()
    };
        if (courseType == 'plus') {
            regionalstateCounts.WA = regionalplusWA()
    };
        if (courseType == 'alumni_mentor') {
			regionalstateCounts.WA = regionalalumni_mentorWA()
    };
// output box rules

	info.update = function () {
        this._div.innerHTML = STATE_NAME +'<h4>SheCodes Participants = </h4>' +  (stateCounts)
            '<b>' + '<h4>Metro Participants = </h4>' + (metrostateCounts) + '</b>' +'<h4>Regional Participants = </h4>'+ (regionalstateCounts);
    };





    // control that shows state info on hover
    var info = L.control();
    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };
    info.update = function (props) {
        this._div.innerHTML = '<h4>Australian SheCodes Participants</h4>' +  (props ?
            '<b>' + STATE_NAME + '</b><br />' + participant_number + 'SheCodes Participants'
            : 'Hover over a state');
    };

    info.addTo(map);

    // get color depending on population density value
    function getColor(d) {
        return d > 1000 ? '#6e016b':
                d > 500  ? '#88419d':
                d > 200  ? '#8c6bb1' :
                d > 100  ? '#8c96c6':
                d > 50   ? '#9ebcda' :
                d > 20   ? '#bfd3e6' :
                d > 10   ? '#e0ecf4' :
                '#f7fcfd';
    }
    function style(feature) {
    const number = statedata[feature.properties.STATE_NAME];
        return {
            weight: 2,
            opacity: 1,
            color: 'white',
            dashArray: '3',
            fillOpacity: 0.7,
            fillColor: getColor(number)
        };
    }
    function highlightFeature(e) {
        var layer = e.target;
        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });
        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
        info.update(layer.feature.properties);
    }
    var geojson;
    function resetHighlight(e) {
        geojson.resetStyle(e.target);
        info.update();
    }
    function zoomToFeature(e) {
        map.fitBounds(e.target.getBounds());
    }
    function onEachFeature(feature, layer) {
        layer.on({
            mouseover: highlightFeature,
            mouseout: resetHighlight,
            click: zoomToFeature
        });
    }
    geojson = L.geoJson(statesData, {
        style: style,
        onEachFeature: onEachFeature
    }).addTo(map);
    var legend = L.control({position: 'bottomright'});
    legend.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 10, 20, 50, 100, 200, 500, 1000],
            labels = [],
            from, to;
        for (var i = 0; i < grades.length; i++) {
            from = grades[i];
            to = grades[i + 1];
            labels.push(
                '<i style="background:' + getColor(from + 1) + '"></i> ' +
                from + (to ? '&ndash;' + to : '+'));
        }
        div.innerHTML = labels.join('<br>');
        return div;
    };
    legend.addTo(map);
}
window.onload = drawMap;
