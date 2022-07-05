chrome.webRequest.onBeforeRequest.addListener(
  function(details) {
    if(details.method == "POST") {
      let formData = details.requestBody.formData;
      let cancel = false;

      if(formData) {
        Object.keys(formData).forEach(key => {
          formData[key].forEach(value => {
            var url = "https://sql-model.herokuapp.com/predict?sentence=" + value;
            var response = httpGet(url);
            console.log(response);
            if(response.includes("yes")) {
              cancel = true;
            }
          });
        });
      }

      if(cancel){
        let redirectUrl = "https://sql-model.herokuapp.com/sqlerror";
        return {
          redirectUrl : redirectUrl
        }
      }else {
        return {
          cancel : false
        }
      }
    }
  },
  {urls: ["<all_urls>"]},
  ["blocking", "requestBody"]
);

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

let image = `
<svg width="800" height="600" style="margin: 0 auto" xmlns="http://www.w3.org/2000/svg">

 <g>
  <title>Layer 1</title>
  <g transform="matrix(1.00111 0 0 1 -0.120972 0)" stroke="null">
   <path fill="#ff4d4d" d="m356.84653,152.09003a7.42466,7.125 0 0 1 5.24677,-2.09003l75.87021,0a7.42466,7.125 0 0 1 5.24673,2.09003l53.63574,51.47098c1.39578,1.32983 2.17795,3.15402 2.17795,5.035l0,72.80798a7.42466,7.125 0 0 1 -2.17795,5.035l-53.63574,51.47098a7.42466,7.125 0 0 1 -5.24673,2.09003l-75.87021,0a7.42466,7.125 0 0 1 -5.24677,-2.09003l-53.6557,-51.47098a7.42466,7.125 0 0 1 -2.16788,-5.035l0,-72.80798a7.42466,7.125 0 0 1 2.17792,-5.035l53.63574,-51.49011l0.00992,0.01913zm8.33557,12.15997l-49.29993,47.31012l0,66.87979l49.29993,47.31009l69.69263,0l49.2999,-47.31009l0,-66.87979l-49.2999,-47.31012l-69.69263,0zm-14.65149,78.375a7.42466,7.125 0 0 1 7.42468,-7.125l84.14621,0a7.42466,7.125 0 0 1 0,14.25l-84.14621,0a7.42466,7.125 0 0 1 -7.42468,-7.125z" fill-rule="evenodd"/>
  </g>
  <text transform="matrix(1.00111 0 0 1 -0.120972 0)" xml:space="preserve" text-anchor="start" font-family="Noto Sans JP" font-size="24" id="svg_4" y="379" x="275.7968" stroke-width="0" stroke="#000" fill="#000000">Request has been blocked</text>
  <text stroke="#000" transform="matrix(1.00111 0 0 1 -0.120972 0)" xml:space="preserve" text-anchor="start" font-family="Noto Sans JP" font-size="20" id="svg_5" y="408" x="24.81999" stroke-width="0" fill="#000000">One or more parameters in the request contains characters or keywords which are not allowed</text>
  <text xml:space="preserve" text-anchor="start" font-family="Noto Sans JP" font-size="17" id="svg_6" y="436" x="313.64063" stroke-width="0" fill="#000000">(SQL Injection Detected)</text>
 </g>
</svg>

`;
