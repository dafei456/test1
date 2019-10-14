$("#save").click(function(){
    var old_password = $("#old_password").val();
    var new_password = $("#new_password").val();

    if(!old_password){
        common_ops.alert("请输入原始密码！")
        return false
    }

    if(!new_password || new_password.length < 6){
        common_ops.alert("请输入不少于6位的密码！")
        return false
    }

    var data = {
        old_password: old_password,
        new_password: new_password
    }

    $.ajax({
        url: common_ops.buildUrl("/user/reset-pwd"),
        type: "POST",
        data: data,
        dataType: "json",
        success: function (res) {
            // console.log(res)
            common_ops.alert(res.reason)
        }
    })
})