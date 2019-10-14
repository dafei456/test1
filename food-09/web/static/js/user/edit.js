$('.user_edit_wrap .save').click(function(){
    var moblie = $(".user_edit_wrap input[name='mobile']").val()
    var nickname = $(".user_edit_wrap input[name='nickname']").val()
    var email = $(".user_edit_wrap input[name='email']").val()

    if(!nickname || nickname.length < 2){
        common_ops.alert("请输入正确的姓名！")
        return false
    }

    if(!email || email.length < 2){
        common_ops.alert("请输入正确的邮箱！")
        return false
    }

    var data = {
        moblie: moblie,
        nickname: nickname,
        email: email
    }

    $.ajax({
        url: common_ops.buildUrl("/user/edit"),
        type: "POST",
        data: data,
        dataType: "json",
        success: function (res) {
            // console.log(res)
            common_ops.alert(res.reason)
        }
    })
})