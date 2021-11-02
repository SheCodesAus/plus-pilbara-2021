console.log(chartdata)

const labels = Object.keys(chartdata);

const data = {
    labels: labels,
    datasets: [{
        label: 'She Codes Participants',
        backgroundColor: 'rgb(255,99,132)',
        borderColor: 'rgb(255,99,132)',
        data: Object.values(chartdata),
    }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
        plugins: {
        title: {
            display: true,
            text: 'She Codes Pathways'
        }
        legend: {

        }
    }
}};

document.addEventListener('DOMContentLoaded', (event) => {
    const myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
});


