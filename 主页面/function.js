function showInDegree() {
  document.getElementById('word').style.display = "none";
  document.getElementById('image').style.display = "none";
  document.getElementById('main').style.display = "block";
  document.getElementById('title1').style.display = "none";
  document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "none";
  var chartDom = document.getElementById('main');
   var myChart = echarts.init(chartDom);
    var option;

    option = {
      title: {
        text: "InDegree Image",
        subtext: "",
        left: "center",
        top:"top",
        textStyle: {
          color: "black",
          fontSize:40
        },
      },
      
        tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b}: {c} ({d}%)'
        },
        legend: {
            top: '10%',
            left: 'center',
            data: ['0','1','2','others']
        },
        series: [
            {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                itemStyle: {
                    borderRadius: 10,
                    borderColor: '#fff',
                    borderWidth: 2
                },
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '40',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                  {value:34489,name:'0'},
{value:7875,name:'1'},
{value:3446,name:'2'},
{value:7459,name:'others'}
                ]
            }
        ]
    };
     option&&myChart.setOption(option);

}

function showOutDegree() {
  document.getElementById('word').style.display = "none";
  document.getElementById('image').style.display = "none";
  document.getElementById('main').style.display = "block";
  document.getElementById('title1').style.display = "none";
  document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "none";
  var chartDom = document.getElementById('main');
   var myChart = echarts.init(chartDom);
    var option;
  
    option = {
      title: {
        text: "OutDegree Image",
        subtext: "",
        left: "center",
        top:"top",
        textStyle: {
          color: "black",
          fontSize:40
        },
      },
      color: [
        '#19CAAD', 
        '#BEEDC7',
        '#D6D5B7' ,   
        '#D1BA74'  ,  
        '#E6CEAC'   , 
        '#ECAD9E',    
        '#F4606C',
        '#8CC7B5',   
        '#A0EEE1' ,
        '#BEE7E9'
      ],
    
      tooltip: {
        trigger: 'item',
        formatter: '{a} <br/>{b}: {c} ({d}%)'
      },
      legend: {
        top: '10%',
        left: 'center',
        data: ['0','1','2','3','4','5','6','7','8','others']
      },
      series: [
        {
          name: 'Access From',
          type: 'pie',
          radius: ['40%', '70%'],
          avoidLabelOverlap: false,
          itemStyle: {
            borderRadius: 10,
            borderColor: '#fff',
            borderWidth: 2
          },
          label: {
            show: false,
            position: 'center'
          },
          emphasis: {
            label: {
              show: true,
              fontSize: '40',
              fontWeight: 'bold'
            }
          },
          labelLine: {
            show: false
          },
          data: [
            {value:24905,name:'0'},
{value:5583,name:'1'},
{value:4871,name:'2'},
{value:3877,name:'3'},
{value:3041,name:'4'},
{value:2257,name:'5'},
{value:1774,name:'6'},
{value:1468,name:'7'},
{value:1314,name:'8'},
{value:7709,name:'others'}
          ]
        }
      ]
    };
    option && myChart.setOption(option);
  } 

  function Home(){
    document.getElementById('main').style.display="none";
    document.getElementById('image').style.display = "none";
    document.getElementById('Img1').style.display="none";
    document.getElementById('Img2').style.display = "none";
    document.getElementById('Img3').style.display = "none";
    document.getElementById('Img4').style.display = "none";
    document.getElementById('title1').style.display = "none";
    document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "none";
  document.getElementById('word').style.display = "block";
  }  

function show39496(){
  document.getElementById('image').style.display = "block";
  document.getElementById('main').style.display="none";
  document.getElementById('Img1').style.display="none";
  document.getElementById('Img2').style.display = "none";
  document.getElementById('Img4').style.display = "none";
  document.getElementById('Img3').style.display = "block";
  document.getElementById('title1').style.display = "block";
  document.getElementById('title2').style.display = "block";
  document.getElementById('title3').style.display = "none";
  document.getElementById('word').style.display = "none";
}
function show47265(){
  document.getElementById('main').style.display="none";
  document.getElementById('image').style.display = "block";
  document.getElementById('Img1').style.display="none";
  document.getElementById('Img2').style.display = "none";
  document.getElementById('Img3').style.display = "none";
  document.getElementById('Img4').style.display = "block";
  document.getElementById('title1').style.display = "block";
  document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "block";
  document.getElementById('word').style.display = "none";
}

function showall(){
  document.getElementById('image').style.display = "block";
  document.getElementById('main').style.display="none";
  document.getElementById('Img1').style.display="none";
  document.getElementById('Img4').style.display = "none";
  document.getElementById('Img2').style.display = "block";
  document.getElementById('Img3').style.display = "none";
  document.getElementById('title1').style.display = "none";
  document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "none";
  document.getElementById('word').style.display = "none";
}
function TOP40(){
  document.getElementById('image').style.display = "block";
  document.getElementById('main').style.display="none";
  document.getElementById('Img4').style.display = "none";
  document.getElementById('Img1').style.display = "block";
  document.getElementById('Img2').style.display = "none";
  document.getElementById('Img3').style.display = "none";
  document.getElementById('title1').style.display = "none";
  document.getElementById('title2').style.display = "none";
  document.getElementById('title3').style.display = "none";
  document.getElementById('word').style.display = "none";
}