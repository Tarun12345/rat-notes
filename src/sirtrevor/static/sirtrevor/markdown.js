/*
  Markdown Block
*/

SirTrevor.Blocks.Markdown = (function(){

  var md_template = _.template([
    '<div class="expanding-textarea">',
      '<pre><span></span><br></pre>',
      '<textarea class="st-markdown st-required"></textarea>',
    '</div>'
  ].join("\n"));

  return SirTrevor.Block.extend({

    type: "Markdown",

    icon_name: "Markdown.svg",

    title: function() { return "Markdown" },

    editorHTML: function() {
      return md_template(this);
    },

    loadData: function(data){
      console.log(data.text);
    },

    onBlockRender: function() {
      /* Make our expanding text area */
      var cont = this.$('.expanding-textarea'),
          area = cont.find('textarea'),
          span = cont.find('span');

      require.config({
        paths: {
          "pagedown": "/static/sirtrevor/"
        },
        waitSeconds: 15
      });
      area.bind('input', function(){    
        require(["pagedown/Markdown.Converter.min"],function(){
          var converter = new Markdown.Converter();
          span.html(converter.makeHtml(area.val()));
        });
      });

      cont.addClass('active');
    },

    toData: function() {
      var dataObj = {};

      dataObj.text = this.$('.st-markdown').val();
      this.setData(dataObj);
    }

  });

})();