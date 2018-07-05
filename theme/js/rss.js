function mkPost(item) {
    var template = ' \
    <li class="post"> \
        <header class="posttitle"> \
        <h3><a target="_blank" href="' + item.link + '" \
                rel="bookmark" \
                class="nodec" \
                title="' + item.title + '">'+ item.title +'</a> \
        </h3> \
        </header> \
        <div class="postinfo"> \
        <p class="published" title="'+ item.categories.join(", ") +'"> Categorias: '+ item.categories.join(", ") +' </p> \
        </div> \
        <div class="postsummary"> '+ $(item.description).filter("p:first").text().slice(0,-1) +'... </div> \
    </li> \
    ';
    return template;
}

function getRss(url) {
    var data = {
        rss_url: url
    };
    var output = "";
    $.get('https://api.rss2json.com/v1/api.json', data, function(response) {
        if (response.status == 'ok') {
            $.each(response.items, function(k, item) {
                output += mkPost(item);
            });
            writePosts(output);
        }
    });
    return output;
}

function writePosts(output) {
    var $content = $('#postlist');
    $content.append(output);
}

$(function() {

    var rss = ['https://medium.com/feed/@diogomunarovieira', 'https://medium.com/feed/databootcamp', 'https://medium.com/feed/exatifica']

    for (var i = 0; i < rss.length; i++) {
        getRss(rss[i]);
    }

});
