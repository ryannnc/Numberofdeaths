function getData()
{
  ajaxGetRequest("/line",plotLine1);
  ajaxGetRequest("/pie",plotLine2);
  ajaxGetRequest("/send",plotLine3);
}

function plotLine1(response)
{
  let data=JSON.parse(response);
  let layout=
  {
    title:'Deaths by Date',
    xaxis:{title:'Year'},
    yaxis:{title:'# of Deaths'}
  };
  Plotly.newPlot('graph1',data,layout);
}


function plotLine2(response)
{
  let data=JSON.parse(response);
  let layout={title:"Deaths by Month"}
  Plotly.newPlot('graph2',data,layout);
}

function plotLine3(response)
{
  let myState = document.getElementById('state');
  let data=JSON.parse(response);
  let layout=
  {
    title:'Deaths in ' + myState.value,
    xaxis:{title:'Year'},
    yaxis:{title:'# of Deaths'}
  };
  myState.value="";
  Plotly.newPlot('graph3',data,layout);
}

function getStateCode()
{
  let myState = document.getElementById('state');
  let statecode = myState.value;
  let toSend = JSON.stringify({"state":statecode});
  ajaxPostRequest("/send",toSend,plotLine3);
}