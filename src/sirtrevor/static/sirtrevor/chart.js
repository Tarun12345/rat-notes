/*
  Markdown Block
*/

SirTrevor.Blocks.Chart = (function(){

  var md_template = _.template([
    '<div class="chart-area">',
      '<canvas width="600" height="400"></canvas>',
      '<textarea class="st-chart st-required"></textarea>',
    '</div>'
  ].join("\n"));

  return SirTrevor.Block.extend({

    type: "Chart",

    icon_name: "Chart.svg",

    title: function() { return "Chart" },

    editorHTML: function() {
      return md_template(this);
    },

    loadData: function(data){
      console.log(data.text);
      var complete = this.$('.chart-area'),
          cont = complete.find('canvas'),
          area = complete.find('.st-chart');
      area.val(JSON.stringify(data.text));
      console.log(area.val());
    },

    onBlockRender: function() {
      /* Make our expanding text area */
      var complete = this.$('.chart-area'),
          cont = complete.find('canvas'),
          area = complete.find('.st-chart');
      require.config({
        paths: {
          "sirtrevor": "/static/sirtrevor/"
        },
        waitSeconds: 15
      });
      require(["sirtrevor/Chart.min","sirtrevor/ChartData"],function(){
          cont = cont.get(0).getContext("2d");
          data = Data;
          console.log(data);
          area.val(JSON.stringify(data));
          console.log(area.val());
          data = jQuery.parseJSON(area.val());
          myChart = new Chart(cont).Line(Data);
      });

      area.bind('input', function(){    
        require(["sirtrevor/Chart.min","sirtrevor/ChartData"],function(){
          myChart = new Chart(cont).Line(jQuery.parseJSON(area.val()));
        });
      });

      cont.addClass('active');
    },

    toData: function() {
      var dataObj = {};

      dataObj.text = jQuery.parseJSON(this.$('.st-chart').val());
      this.setData(dataObj);
    }

  });

})();