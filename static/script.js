// ======================================================
// CUSTOMER INSIGHT RECOMMENDATION SYSTEM
// PROFESSIONAL CHART.JS
// ======================================================

Chart.defaults.color = "#E5E7EB";
Chart.defaults.font.family = "'Poppins', sans-serif";
Chart.defaults.font.size = 13;

const gridColor = "rgba(255,255,255,.08)";
const tickColor = "#CBD5E1";

const COLORS = {

    blue: "#4F8BFF",
    cyan: "#00D4FF",
    purple: "#8B5CF6",
    green: "#22C55E",
    orange: "#FF9F1C",
    yellow: "#FFD166",
    red: "#EF4444",
    pink: "#EC4899"

};


// ======================================================
// COMMON OPTIONS
// ======================================================

const commonOptions = {

    responsive: true,

    maintainAspectRatio: false,

    animation: {

        duration: 1200,

        easing: "easeOutQuart"

    },

    plugins: {

        legend: {

            labels: {

                color: "#E5E7EB",

                padding: 20,

                usePointStyle: true,

                pointStyle: "circle"

            }

        }

    }

};
// ======================================================
// TOP SELLING PRODUCTS (Horizontal Bar)
// ======================================================

const productCtx = document.getElementById("productChart");

if (productCtx) {

new Chart(productCtx,{

    type:"bar",

    data:{

        labels:productLabels,

        datasets:[{

            label:"Units Sold",

            data:productValues,

            borderRadius:12,

            borderSkipped:false,

            backgroundColor:[

                "#00D4FF",
                "#31C8FF",
                "#52BCFF",
                "#6CB0FF",
                "#82A6FF",
                "#999CFF",
                "#AF92FF",
                "#C289FF",
                "#D680FF",
                "#EC4899"

            ],

            hoverBackgroundColor:[

                "#4FE8FF",
                "#56D7FF",
                "#74CBFF",
                "#8CBFFF",
                "#A3B5FF",
                "#B5AEFF",
                "#C8A7FF",
                "#D89EFF",
                "#EA95FF",
                "#FF6FB6"

            ]

        }]

    },

    options:{

        ...commonOptions,

        indexAxis:"y",

        plugins:{

            legend:{
                display:false
            },

            tooltip:{

                backgroundColor:"#0F172A",

                borderColor:"#4F8BFF",

                borderWidth:1,

                padding:12,

                titleColor:"#fff",

                bodyColor:"#fff"

            }

        },

        scales:{

            x:{

                grid:{
                    color:gridColor
                },

                ticks:{
                    color:tickColor
                }

            },

            y:{

                grid:{
                    display:false
                },

                ticks:{
                    color:"#F8FAFC"
                }

            }

        }

    }

});

}
// ======================================================
// COUNTRY REVENUE (DOUGHNUT)
// ======================================================

const countryCtx = document.getElementById("countryChart");

if(countryCtx){

new Chart(countryCtx,{

    type:"doughnut",

    data:{

        labels:countryLabels,

        datasets:[{

            data:countryValues,

            borderWidth:2,

            borderColor:"#0F172A",

            hoverBorderWidth:4,

            hoverOffset:15,

            backgroundColor:[

                "#00D4FF",
                "#24C7FF",
                "#45BAFF",
                "#66ADFF",
                "#869FFF",
                "#A391FF",
                "#BE83FF",
                "#D775FF",
                "#EE67F8",
                "#FF5DB1"

            ]

        }]

    },

    options:{

        ...commonOptions,

        cutout:"68%",

        plugins:{

            legend:{

                position:"bottom",

                labels:{

                    color:"#F8FAFC",

                    padding:20,

                    usePointStyle:true,

                    pointStyle:"circle",

                    boxWidth:12,

                    font:{

                        size:12,

                        weight:"600"

                    }

                }

            },

            tooltip:{

                backgroundColor:"#111827",

                borderColor:"#4F8BFF",

                borderWidth:1,

                titleColor:"#fff",

                bodyColor:"#fff",

                padding:12,

                callbacks:{

                    label:function(context){

                        const value=context.parsed;

                        const total=context.dataset.data.reduce((a,b)=>a+b,0);

                        const percent=((value/total)*100).toFixed(1);

                        return `${context.label}: £${value.toLocaleString()} (${percent}%)`;

                    }

                }

            }

        },

        animation:{

            animateRotate:true,

            animateScale:true,

            duration:2200,

            easing:"easeOutExpo"

        }

    }

});

}
// ======================================================
// MONTHLY SALES TREND
// ======================================================

const salesCtx = document.getElementById("salesChart");

if (salesCtx) {

    const gradient = salesCtx.getContext("2d").createLinearGradient(0, 0, 0, 350);

    gradient.addColorStop(0, "rgba(0,212,255,0.45)");
    gradient.addColorStop(0.4, "rgba(79,139,255,0.25)");
    gradient.addColorStop(1, "rgba(79,139,255,0)");

    new Chart(salesCtx, {

        type: "line",

        data: {

            labels: monthlyLabels,

            datasets: [{

                label: "Monthly Revenue",

                data: monthlyValues,

                borderColor: "#38BDF8",

                backgroundColor: gradient,

                fill: true,

                tension: 0.45,

                borderWidth: 4,

                pointRadius: 5,

                pointHoverRadius: 9,

                pointBackgroundColor: "#ffffff",

                pointBorderColor: "#38BDF8",

                pointBorderWidth: 3,

                pointHoverBackgroundColor: "#38BDF8",

                pointHoverBorderColor: "#ffffff"

            }]

        },

        options: {

            ...commonOptions,

            interaction: {

                intersect: false,

                mode: "index"

            },

            scales: {

                x: {

                    grid: {

                        display: false

                    },

                    ticks: {

                        color: "#CBD5E1",

                        font: {

                            size: 12,

                            weight: "600"

                        }

                    }

                },

                y: {

                    beginAtZero: true,

                    grid: {

                        color: "rgba(255,255,255,.08)"

                    },

                    ticks: {

                        color: "#CBD5E1",

                        callback: function(value){

                            return "£" + Number(value).toLocaleString();

                        }

                    }

                }

            },

            plugins: {

                legend: {

                    display: false

                },

                tooltip: {

                    backgroundColor: "#111827",

                    borderColor: "#38BDF8",

                    borderWidth: 1,

                    titleColor: "#fff",

                    bodyColor: "#fff",

                    padding: 12,

                    displayColors: false,

                    callbacks: {

                        label: function(context){

                            return "Revenue : £" + context.parsed.y.toLocaleString();

                        }

                    }

                }

            },

            animation: {

                duration: 2200,

                easing: "easeOutQuart"

            }

        }

    });

}
// ======================================================
// CUSTOMER SEGMENTS
// ======================================================

const segmentCtx = document.getElementById("segmentChart");

if(segmentCtx){

new Chart(segmentCtx,{

    type:"doughnut",

    data:{

        labels:segmentLabels,

        datasets:[{

            data:segmentValues,

            borderWidth:3,

            borderColor:"#111827",

            hoverBorderWidth:5,

            hoverOffset:18,

            backgroundColor:[

                "#22C55E",   // High Value

                "#F59E0B",   // Medium Value

                "#EF4444"    // Low Value

            ]

        }]

    },

    options:{

        ...commonOptions,

        cutout:"65%",

        layout:{

            padding:15

        },

        plugins:{

            legend:{

                position:"bottom",

                labels:{

                    color:"#E5E7EB",

                    padding:18,

                    usePointStyle:true,

                    pointStyle:"circle",

                    font:{

                        size:13,

                        weight:"600"

                    }

                }

            },

            tooltip:{

                backgroundColor:"#111827",

                borderColor:"#22C55E",

                borderWidth:1,

                titleColor:"#ffffff",

                bodyColor:"#ffffff",

                padding:12,

                callbacks:{

                    label:function(context){

                        const value=context.parsed;

                        const total=context.dataset.data.reduce((a,b)=>a+b,0);

                        const percentage=((value/total)*100).toFixed(1);

                        return `${context.label}: ${value} Customers (${percentage}%)`;

                    }

                }

            }

        },

        animation:{

            animateRotate:true,

            animateScale:true,

            duration:1800,

            easing:"easeOutQuart"

        }

    }

});

}
