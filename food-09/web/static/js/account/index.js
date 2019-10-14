var acount_index_ops = {
    init: function () {
        this.eventBind();
    },
    eventBind: function () {
        $("#search").click(function () {
            $(".wrap_search").submit()
        })
    }
}

$(document).ready(function () {
    acount_index_ops.init();
})