/*
  Markdown Block
*/

SirTrevor.Blocks.Sketch = (function(){

  var md_template = _.template([
    '<div class="expanding-sketcharea ">',
      '<canvas class="st-sketch" width="1024" height="640" />',
      '<img src="" class="st-image" style="display:none;"/>',
      '<a class="st-done">Done Drawing</a>',
    '</div>'
  ].join("\n"));

  return SirTrevor.Block.extend({

    type: "sketch",

    icon_name: "Sketch.svg",

    title: function() { return "Sketch" },

    editorHTML: function() {
      return md_template(this);
    },

    loadData: function(data){
      this.$('.st-sketch');
    },

    onBlockRender: function(transferData) {
      var cont = this.$('.expanding-sketcharea'),
          img = cont.find(".st-image");
      require.config({
        paths: {
          "js": "/static/sketchpad/"
        },
        waitSeconds: 15
      }); 
      require(["js/sketcher","js/trigonometry","js/modernizr.custom.34982"],function(){
        var sketches = this.$("[data-type='sketch']");
        var dataString = null;
        var brush = new Image();
        brush.src = '/apps/sketchpad/brush2.png';
        sketches.find(".expanding-sketcharea").each(function(index,value){
          var sketch = $(value).find(".st-sketch")[0];
          var done = $(value).find(".st-done")[0];
          var sketcher = new Sketcher(sketch);
          done.addEventListener("click", function (){
            var dataString = sketcher.canvas.toDataURL("image/png");
            img.attr("src",dataString);
            img.show();
            $(sketch).hide();
            return false;
          });
        });
        this.uploader(
              dataString,
              function(data) {
                this.setData(data);
                this.ready();
              },
              function(error){
                this.addMessage(i18n.t('blocks:image:upload_error'));
                this.ready();
              }
            );
      });
    },

    toData: function() {
      var dataObj = {};
      dataObj.text = this.$('.expanding-sketcharea').find('.st-image').attr("src");
      this.setData(dataObj);
      return false;
    }

  });

})();