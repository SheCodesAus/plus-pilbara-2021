const labels = [
    'Workshop',
    'Flash',
    'Plus',
    'Internship',
    'Mentor',
];

const data = {
    labels: labels,
    datasets: [{
        label: 'My First Dataset',
        backgroundColor: 'rgb(255,99,132)',
        borderColor: 'rgb(255,99,132)',
        data: [0,10,5,2,20,30,45],
    }]
};

const config = {
    type: 'line',
    data: data,
    options: {}
};

document.addEventListener('DOMContentLoaded', (event) => {
    const myChart = new Chart(
        document.getElementById('myChart'),
        config
    );
});


