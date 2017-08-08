ip_address = "lab.songli.io/imageCompare/";
var Collector = function() {
  // used for sending images back to server
  this.send = function(dataURL) {
    $.ajax({
      context:this,
      url : "http://" + ip_address + "pictures",
      type : 'POST',
      async: false,
      data : {
        dataurl:dataURL,
        flag: "2"

      },
      success : function(img_id) {
        console.log(img_id);
        //parent.postMessage(data,"http://uniquemachine.org");
      },
      error: function (xhr, ajaxOptions, thrownError) {
        //alert(thrownError);
      }
    });
  }
}

function tryTest(dataURL) {
  var collector = new Collector;
  collector.send(dataURL);
}
