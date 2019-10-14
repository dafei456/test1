$(".login-wrap .do-login").click(function(){
    var login_name =  $(".login-wrap input[name='login_name']").val()
    var login_pwd =  $(".login-wrap input[name='login_pwd']").val()

    $.ajax({
        url: common_ops.buildUrl("/user/login"),
        type: "POST",
        data: {'login_name': login_name, 'login_pwd': login_pwd},
        dataType: "json",
        success: function (res) {
            // console.log(res)
            var callback = null;
            // 判断res.result是否等于0，如果等于0，代表登录成功；如果不等于0，就代表登录失败
            if(res.result == 0) {
                // console.log('ok')
                callback = function () {
                    // 跳转到后台首页
                    window.location.href = common_ops.buildUrl("/")
                }
            }
            // 提示框
            common_ops.alert(res.reason, callback)
        }
    })

})