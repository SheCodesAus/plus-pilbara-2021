console.log(statedata)
let courseType = 'all';
let map;
let geojson;
let redrawLayer;

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
    return metroflashWA() + metroflashSA() + metroflashNT() + metroflashQLD() + metroflashNSW() + metroflashVIC() + metroflashACT() + metroflashTAS()
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
    return statedata['WA']['regional']['1 day'] + statedata['WA']['regional']['flash'] + statedata['WA']['regional']['plus'] + statedata['WA']['regional']['alumni_mentor'] + statedata['WA']['metro']['1 day'] + statedata['WA']['metro']['flash'] + statedata['WA']['metro']['plus'] + statedata['WA']['metro']['alumni_mentor']
}

function metroallcoursesWA() {
    return metroworkshopWA() + metroflashWA() + metroplusWA() + metroalumni_mentorWA()
}

function regionalallcoursesWA() {
    return regionalworkshopWA() + regionalflashWA() + regionalplusWA() + regionalalumni_mentorWA()
}

//  WA hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over WA
function workshopWA() {
    return statedata['WA']['regional']['1 day'] + statedata['WA']['metro']['1 day']
}
function metroworkshopWA() {
    return statedata['WA']['metro']['1 day']
}
function regionalworkshopWA() {
    return statedata['WA']['regional']['1 day']
}

// WA hover -  flash course button - map output box when selected FLASH filter and hovering over WA
function flashWA() {
    return statedata['WA']['regional']['flash'] + statedata['WA']['metro']['flash']
}
function metroflashWA() {
    return statedata['WA']['metro']['flash']
}
function regionalflashWA() {
    return statedata['WA']['regional']['flash']
}

// WA hover -  plus course button - map output box when selected PLUS filter and hovering over WA
function plusWA() {
    return statedata['WA']['regional']['plus'] + statedata['WA']['metro']['plus']
}
function metroplusWA() {
    return statedata['WA']['metro']['plus']
}
function regionalplusWA() {
    return statedata['WA']['regional']['plus']
}
// WA hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over WA
function alumni_mentorWA() {
    return statedata['WA']['regional']['alumni_mentor'] + statedata['WA']['metro']['alumni_mentor']
}
function metroalumni_mentorWA() {
    return statedata['WA']['metro']['alumni_mentor']
}
function regionalalumni_mentorWA() {
    return statedata['WA']['regional']['alumni_mentor']
}

//  SA Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over SA
function totalSA() {
    return statedata['SA']['regional']['1 day'] + statedata['SA']['regional']['flash'] + statedata['SA']['regional']['plus'] + statedata['SA']['regional']['alumni_mentor'] + statedata['SA']['metro']['1 day'] + statedata['SA']['metro']['flash'] + statedata['SA']['metro']['plus'] + statedata['SA']['metro']['alumni_mentor']
}

function metroallcoursesSA() {
    return metroworkshopSA() + metroflashSA() + metroplusSA() + metroalumni_mentorSA()
}

function regionalallcoursesSA() {
    return regionalworkshopSA() + regionalflashSA() + regionalplusSA() + regionalalumni_mentorSA()
}

//  SA hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over SA
function workshopSA() {
    return statedata['SA']['regional']['1 day'] + statedata['SA']['metro']['1 day']
}
function metroworkshopSA() {
    return statedata['SA']['metro']['1 day']
}
function regionalworkshopSA() {
    return statedata['SA']['regional']['1 day']
}

// SA hover -  flash course button - map output box when selected FLASH filter and hovering over SA
function flashSA() {
    return statedata['SA']['regional']['flash'] + statedata['SA']['metro']['flash']
}
function metroflashSA() {
    return statedata['SA']['metro']['flash']
}
function regionalflashSA() {
    return statedata['SA']['regional']['flash']
}

// SA hover -  plus course button - map output box when selected PLUS filter and hovering over SA
function plusSA() {
    return statedata['SA']['regional']['plus'] + statedata['SA']['metro']['plus']
}
function metroplusSA() {
    return statedata['SA']['metro']['plus']
}
function regionalplusSA() {
    return statedata['SA']['regional']['plus']
}
// SA hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over SA
function alumni_mentorSA() {
    return statedata['SA']['regional']['alumni_mentor'] + statedata['SA']['metro']['alumni_mentor']
}
function metroalumni_mentorSA() {
    return statedata['SA']['metro']['alumni_mentor']
}
function regionalalumni_mentorSA() {
    return statedata['SA']['regional']['alumni_mentor']
}

//  NT Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over NT
function totalNT() {
    return statedata['NT']['regional']['1 day'] + statedata['NT']['regional']['flash'] + statedata['NT']['regional']['plus'] + statedata['NT']['regional']['alumni_mentor'] + statedata['NT']['metro']['1 day'] + statedata['NT']['metro']['flash'] + statedata['NT']['metro']['plus'] + statedata['NT']['metro']['alumni_mentor']
}

function metroallcoursesNT() {
    return metroworkshopNT() + metroflashNT() + metroplusNT() + metroalumni_mentorNT()
}

function regionalallcoursesNT() {
    return regionalworkshopNT() + regionalflashNT() + regionalplusNT() + regionalalumni_mentorNT()
}

//  NT hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over NT
function workshopNT() {
    return statedata['NT']['regional']['1 day'] + statedata['NT']['metro']['1 day']
}
function metroworkshopNT() {
    return statedata['NT']['metro']['1 day']
}
function regionalworkshopNT() {
    return statedata['NT']['regional']['1 day']
}

// NT hover -  flash course button - map output box when selected FLASH filter and hovering over NT
function flashNT() {
    return statedata['NT']['regional']['flash'] + statedata['NT']['metro']['flash']
}
function metroflashNT() {
    return statedata['NT']['metro']['flash']
}
function regionalflashNT() {
    return statedata['NT']['regional']['flash']
}

// NT hover -  plus course button - map output box when selected PLUS filter and hovering over NT
function plusNT() {
    return statedata['NT']['regional']['plus'] + statedata['NT']['metro']['plus']
}
function metroplusNT() {
    return statedata['NT']['metro']['plus']
}
function regionalplusNT() {
    return statedata['NT']['regional']['plus']
}
// NT hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over NT
function alumni_mentorNT() {
    return statedata['NT']['regional']['alumni_mentor'] + statedata['NT']['metro']['alumni_mentor']
}
function metroalumni_mentorNT() {
    return statedata['NT']['metro']['alumni_mentor']
}
function regionalalumni_mentorNT() {
    return statedata['NT']['regional']['alumni_mentor']
}

//  QLD Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over QLD
function totalQLD() {
    return statedata['QLD']['regional']['1 day'] + statedata['QLD']['regional']['flash'] + statedata['QLD']['regional']['plus'] + statedata['QLD']['regional']['alumni_mentor'] + statedata['QLD']['metro']['1 day'] + statedata['QLD']['metro']['flash'] + statedata['QLD']['metro']['plus'] + statedata['QLD']['metro']['alumni_mentor']
}

function metroallcoursesQLD() {
    return metroworkshopQLD() + metroflashQLD() + metroplusQLD() + metroalumni_mentorQLD()
}

function regionalallcoursesQLD() {
    return regionalworkshopQLD() + regionalflashQLD() + regionalplusQLD() + regionalalumni_mentorQLD()
}

//  QLD hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over QLD
function workshopQLD() {
    return statedata['QLD']['regional']['1 day'] + statedata['QLD']['metro']['1 day']
}
function metroworkshopQLD() {
    return statedata['QLD']['metro']['1 day']
}
function regionalworkshopQLD() {
    return statedata['QLD']['regional']['1 day']
}

// QLD hover -  flash course button - map output box when selected FLASH filter and hovering over QLD
function flashQLD() {
    return statedata['QLD']['regional']['flash'] + statedata['QLD']['metro']['flash']
}
function metroflashQLD() {
    return statedata['QLD']['metro']['flash']
}
function regionalflashQLD() {
    return statedata['QLD']['regional']['flash']
}

// QLD hover -  plus course button - map output box when selected PLUS filter and hovering over QLD
function plusQLD() {
    return statedata['QLD']['regional']['plus'] + statedata['QLD']['metro']['plus']
}
function metroplusQLD() {
    return statedata['QLD']['metro']['plus']
}
function regionalplusQLD() {
    return statedata['QLD']['regional']['plus']
}
// QLD hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over QLD
function alumni_mentorQLD() {
    return statedata['QLD']['regional']['alumni_mentor'] + statedata['QLD']['metro']['alumni_mentor']
}
function metroalumni_mentorQLD() {
    return statedata['QLD']['metro']['alumni_mentor']
}
function regionalalumni_mentorQLD() {
    return statedata['QLD']['regional']['alumni_mentor']
}

//  NSW Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over NSW
function totalNSW() {
    return statedata['NSW']['regional']['1 day'] + statedata['NSW']['regional']['flash'] + statedata['NSW']['regional']['plus'] + statedata['NSW']['regional']['alumni_mentor'] + statedata['NSW']['metro']['1 day'] + statedata['NSW']['metro']['flash'] + statedata['NSW']['metro']['plus'] + statedata['NSW']['metro']['alumni_mentor']
}

function metroallcoursesNSW() {
    return metroworkshopNSW() + metroflashNSW() + metroplusNSW() + metroalumni_mentorNSW()
}

function regionalallcoursesNSW() {
    return regionalworkshopNSW() + regionalflashNSW() + regionalplusNSW() + regionalalumni_mentorNSW()
}

//  NSW hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over NSW
function workshopNSW() {
    return statedata['NSW']['regional']['1 day'] + statedata['NSW']['metro']['1 day']
}
function metroworkshopNSW() {
    return statedata['NSW']['metro']['1 day']
}
function regionalworkshopNSW() {
    return statedata['NSW']['regional']['1 day']
}

// NSW hover -  flash course button - map output box when selected FLASH filter and hovering over NSW
function flashNSW() {
    return statedata['NSW']['regional']['flash'] + statedata['NSW']['metro']['flash']
}
function metroflashNSW() {
    return statedata['NSW']['metro']['flash']
}
function regionalflashNSW() {
    return statedata['NSW']['regional']['flash']
}

// NSW hover -  plus course button - map output box when selected PLUS filter and hovering over NSW
function plusNSW() {
    return statedata['NSW']['regional']['plus'] + statedata['NSW']['metro']['plus']
}
function metroplusNSW() {
    return statedata['NSW']['metro']['plus']
}
function regionalplusNSW() {
    return statedata['NSW']['regional']['plus']
}
// NSW hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over NSW
function alumni_mentorNSW() {
    return statedata['NSW']['regional']['alumni_mentor'] + statedata['NSW']['metro']['alumni_mentor']
}
function metroalumni_mentorNSW() {
    return statedata['NSW']['metro']['alumni_mentor']
}
function regionalalumni_mentorNSW() {
    return statedata['NSW']['regional']['alumni_mentor']
}

//  VIC Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over VIC
function totalVIC() {
    return statedata['VIC']['regional']['1 day'] + statedata['VIC']['regional']['flash'] + statedata['VIC']['regional']['plus'] + statedata['VIC']['regional']['alumni_mentor'] + statedata['VIC']['metro']['1 day'] + statedata['VIC']['metro']['flash'] + statedata['VIC']['metro']['plus'] + statedata['VIC']['metro']['alumni_mentor']
}

function metroallcoursesVIC() {
    return metroworkshopVIC() + metroflashVIC() + metroplusVIC() + metroalumni_mentorVIC()
}

function regionalallcoursesVIC() {
    return regionalworkshopVIC() + regionalflashVIC() + regionalplusVIC() + regionalalumni_mentorVIC()
}

//  VIC hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over VIC
function workshopVIC() {
    return statedata['VIC']['regional']['1 day'] + statedata['VIC']['metro']['1 day']
}
function metroworkshopVIC() {
    return statedata['VIC']['metro']['1 day']
}
function regionalworkshopVIC() {
    return statedata['VIC']['regional']['1 day']
}

// VIC hover -  flash course button - map output box when selected FLASH filter and hovering over VIC
function flashVIC() {
    return statedata['VIC']['regional']['flash'] + statedata['VIC']['metro']['flash']
}
function metroflashVIC() {
    return statedata['VIC']['metro']['flash']
}
function regionalflashVIC() {
    return statedata['VIC']['regional']['flash']
}

// VIC hover -  plus course button - map output box when selected PLUS filter and hovering over VIC
function plusVIC() {
    return statedata['VIC']['regional']['plus'] + statedata['VIC']['metro']['plus']
}
function metroplusVIC() {
    return statedata['VIC']['metro']['plus']
}
function regionalplusVIC() {
    return statedata['VIC']['regional']['plus']
}
// VIC hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over VIC
function alumni_mentorVIC() {
    return statedata['VIC']['regional']['alumni_mentor'] + statedata['VIC']['metro']['alumni_mentor']
}
function metroalumni_mentorVIC() {
    return statedata['VIC']['metro']['alumni_mentor']
}
function regionalalumni_mentorVIC() {
    return statedata['VIC']['regional']['alumni_mentor']
}

//  ACT Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over ACT
function totalACT() {
    return statedata['ACT']['regional']['1 day'] + statedata['ACT']['regional']['flash'] + statedata['ACT']['regional']['plus'] + statedata['ACT']['regional']['alumni_mentor'] + statedata['ACT']['metro']['1 day'] + statedata['ACT']['metro']['flash'] + statedata['ACT']['metro']['plus'] + statedata['ACT']['metro']['alumni_mentor']
}

function metroallcoursesACT() {
    return metroworkshopACT() + metroflashACT() + metroplusACT() + metroalumni_mentorACT()
}

function regionalallcoursesACT() {
    return regionalworkshopACT() + regionalflashACT() + regionalplusACT() + regionalalumni_mentorACT()
}

//  ACT hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over ACT
function workshopACT() {
    return statedata['ACT']['regional']['1 day'] + statedata['ACT']['metro']['1 day']
}
function metroworkshopACT() {
    return statedata['ACT']['metro']['1 day']
}
function regionalworkshopACT() {
    return statedata['ACT']['regional']['1 day']
}

// ACT hover -  flash course button - map output box when selected FLASH filter and hovering over ACT
function flashACT() {
    return statedata['ACT']['regional']['flash'] + statedata['ACT']['metro']['flash']
}
function metroflashACT() {
    return statedata['ACT']['metro']['flash']
}
function regionalflashACT() {
    return statedata['ACT']['regional']['flash']
}

// ACT hover -  plus course button - map output box when selected PLUS filter and hovering over ACT
function plusACT() {
    return statedata['ACT']['regional']['plus'] + statedata['ACT']['metro']['plus']
}
function metroplusACT() {
    return statedata['ACT']['metro']['plus']
}
function regionalplusACT() {
    return statedata['ACT']['regional']['plus']
}
// ACT hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over ACT
function alumni_mentorACT() {
    return statedata['ACT']['regional']['alumni_mentor'] + statedata['ACT']['metro']['alumni_mentor']
}
function metroalumni_mentorACT() {
    return statedata['ACT']['metro']['alumni_mentor']
}
function regionalalumni_mentorACT() {
    return statedata['ACT']['regional']['alumni_mentor']
}

//  TAS Total hover -  All courses course button - map output box when selected ALL COURSES filter and hovering over TAS
function totalTAS() {
    return statedata['TAS']['regional']['1 day'] + statedata['TAS']['regional']['flash'] + statedata['TAS']['regional']['plus'] + statedata['TAS']['regional']['alumni_mentor'] + statedata['TAS']['metro']['1 day'] + statedata['TAS']['metro']['flash'] + statedata['TAS']['metro']['plus'] + statedata['TAS']['metro']['alumni_mentor']
}

function metroallcoursesTAS() {
    return metroworkshopTAS() + metroflashTAS() + metroplusTAS() + metroalumni_mentorTAS()
}

function regionalallcoursesTAS() {
    return regionalworkshopTAS() + regionalflashTAS() + regionalplusTAS() + regionalalumni_mentorTAS()
}

//  TAS hover -  workshop course button - map output box when selected WORKSHOP filter and hovering over TAS
function workshopTAS() {
    return statedata['TAS']['regional']['1 day'] + statedata['TAS']['metro']['1 day']
}
function metroworkshopTAS() {
    return statedata['TAS']['metro']['1 day']
}
function regionalworkshopTAS() {
    return statedata['TAS']['regional']['1 day']
}

// TAS hover -  flash course button - map output box when selected FLASH filter and hovering over TAS
function flashTAS() {
    return statedata['TAS']['regional']['flash'] + statedata['TAS']['metro']['flash']
}
function metroflashTAS() {
    return statedata['TAS']['metro']['flash']
}
function regionalflashTAS() {
    return statedata['TAS']['regional']['flash']
}

// TAS hover -  plus course button - map output box when selected PLUS filter and hovering over TAS
function plusTAS() {
    return statedata['TAS']['regional']['plus'] + statedata['TAS']['metro']['plus']
}
function metroplusTAS() {
    return statedata['TAS']['metro']['plus']
}
function regionalplusTAS() {
    return statedata['TAS']['regional']['plus']
}
// TAS hover -  alumi mentor course button - map output box when selected ALUMNI MENTOR filter and hovering over TAS
function alumni_mentorTAS() {
    return statedata['TAS']['regional']['alumni_mentor'] + statedata['TAS']['metro']['alumni_mentor']
}
function metroalumni_mentorTAS() {
    return statedata['TAS']['metro']['alumni_mentor']
}
function regionalalumni_mentorTAS() {
    return statedata['TAS']['regional']['alumni_mentor']
}

function getStateCounts() {
    
    // DATA COLOUR ON MAP
    const stateCounts = {
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
        stateCounts.SA = flashSA(),
        stateCounts.NT = flashNT(),
        stateCounts.QLD = flashQLD(),
        stateCounts.NSW = flashNSW(),
        stateCounts.VIC = flashVIC(),
        stateCounts.ACT = flashACT(),
        stateCounts.TAS = flashTAS()
    };
    if (courseType == 'plus') {
        stateCounts.WA = plusWA()
        stateCounts.SA = plusSA(),
        stateCounts.NT = plusNT(),
        stateCounts.QLD = plusQLD(),
        stateCounts.NSW = plusNSW(),
        stateCounts.VIC = plusVIC(),
        stateCounts.ACT = plusACT(),
        stateCounts.TAS = plusTAS()
    };
    if (courseType == 'alumni_mentor') {
        stateCounts.WA = alumni_mentorWA()
        stateCounts.SA = alumni_mentorSA(),
        stateCounts.NT = alumni_mentorNT(),
        stateCounts.QLD = alumni_mentorQLD(),
        stateCounts.NSW = alumni_mentorNSW(),
        stateCounts.VIC = alumni_mentorVIC(),
        stateCounts.ACT = alumni_mentorACT(),
        stateCounts.TAS = alumni_mentorTAS()
    };

    return stateCounts
}

const drawMap = function () {
    map = L.map('map').setView([-27.833, 133.583], 4);
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox/light-v9',
        tileSize: 512,
        zoomOffset: -1
    }).addTo(map);

    // control that shows state info on hover
    var info = L.control();
    info.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info');
        this.update();
        return this._div;
    };

    const sum = (obj) => {
        return Object.values(obj).reduce((a, b) => a + b, 0);
    }

    info.update = function (props) {
        if (!props) {
            const regional = sum(Object.values(statedata).map(o => courseType === 'all' ? sum(o.regional) : o.regional[courseType]))
            const metro = sum(Object.values(statedata).map(o => courseType === 'all' ? sum(o.metro) : o.metro[courseType]))
            const count = regional + metro
            console.log({regional, metro, count})
            this._div.innerHTML = 'Australia' + '<h4>Total SheCodes Participants = </h4>' + count +
            '<b>' + '<h4>Metro Participants = </h4>' + metro + '</b>' + '<h4>Regional Participants = </h4>' + regional;
            return;
        }
        const stateCounts = getStateCounts();
        const count = stateCounts[props.STATE_NAME]
        const regional = courseType === 'all'? sum(statedata[props.STATE_NAME].regional) : statedata[props.STATE_NAME].regional[courseType];
        const metro =  courseType === 'all'? sum(statedata[props.STATE_NAME].metro):statedata[props.STATE_NAME].metro[courseType]; // TODO same as above
        
        this._div.innerHTML = props.STATE_NAME + '<h4>Total SheCodes Participants = </h4>' + count +
         '<b>' + '<h4>Metro Participants = </h4>' + metro + '</b>' + '<h4>Regional Participants = </h4>' + regional;
    };
   
 
    info.addTo(map);

    // get color depending on population density value
    function getColor(d) {
        // d = d * 100
        // d=d +50
        return d > 1000 ? '#6e016b' :
            d > 500 ? '#88419d' :
                d > 200 ? '#8c6bb1' :
                    d > 100 ? '#8c96c6' :
                        d > 50 ? '#9ebcda' :
                            d > 20 ? '#bfd3e6' :
                                d > 10 ? '#e0ecf4' :
                                    '#ffefc4';
    }
    function style(feature) {
        const stateCounts = getStateCounts();
        const number = stateCounts[feature.properties.STATE_NAME];
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
    redrawLayer = () => {
        if (geojson) { map.removeLayer(L.geoJson) }            
        geojson = L.geoJson(statesData, {
            style: style,
            onEachFeature: onEachFeature
        }).addTo(map);
        info.update();
    }
    redrawLayer();
    var legend = L.control({ position: 'bottomright' });
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

function changeCourseType(newType, button) {
    courseType = newType;
    console.log(`New map type: ${newType}`)
    // redraw map
    map.invalidateSize();
    redrawLayer();
    document.querySelectorAll('button').forEach(button => button.classList.remove('selected'))
    button.classList.add('selected')
}

window.onload = () => { drawMap()};
