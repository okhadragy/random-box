var usernameValue = "",
    emailValue = "",
    passwordValue = "",
    confirmPasswordValue = "",
    loginUsernameValue = "",
    loginPasswordValue = "";


startListening = function (element, element2, e) {
    value = e.target.value;
    $(element).removeClass("invalid")
    $(element2).css({
        "display": "none"
    })
    $(element2).empty()
    return value
}

inValidElement = function (element, element2, errors, submitButton) {
    $(element).addClass("invalid")
    $(element2).css({
        "display": "block"
    })
    $(element2).addClass("invalid")
    $(element2).text(errors)
    $(submitButton).prop("disabled", "true")
}

validElement = function (element, element2, submitButton) {
    $(element).removeClass("invalid")
    $(element2).css({
        "display": "none"
    })
    $(element2).empty()
    $(submitButton).removeAttr("disabled")
}

$("#signup_username").keyup((e) => {
    usernameValue = startListening("#signup_username", ".invalid-signup-username", e)
    if (usernameValue.length > 0) {
        data = {
            sign_up_username: usernameValue
        }
        $.ajax({
            type: "POST",
            url: "/validate/",
            data: data,
            error: (res)=>{inValidElement("#signup_username", ".invalid-signup-username", res.responseJSON.errors, "#submitSignUp")},
            success: ()=>{
                if ($(".invalid-signup-email").is(":visible") || $(".invalid-signup-password2").is(":visible")) {
                    $("#submitSignUp").prop("disabled", "true")
                } else {
                    validElement("#signup_username", ".invalid-signup-username",'#submitSignUp')
                }
            }
        })
    } else if ($(".invalid-signup-email").is(":visible") || $(".invalid-signup-password2").is(":visible")) {
        $("#submitSignUp").prop("disabled", "true")
    } else {
        $('#submitSignUp').removeAttr("disabled")
    }
})

$("#signup_email").keyup((e) => {
    emailValue = startListening("#signup_email", ".invalid-signup-email", e)
    if (emailValue.length > 0) {
        data = {
            sign_up_email: emailValue
        }
        $.ajax({
            type: "POST",
            url: "/validate/",
            data: data,
            error: (res)=>{inValidElement("#signup_email", ".invalid-signup-email", res.responseJSON.errors, "#submitSignUp")},
            success: ()=>{
                if ($(".invalid-signup-username").is(":visible") || $(".invalid-signup-password2").is(":visible")) {
                    $("#submitSignUp").prop("disabled", "true")
                } else {
                    validElement("#signup_email", ".invalid-signup-email",'#submitSignUp')
                }
            }
        })
    } else if ($(".invalid-signup-email").is(":visible") || $(".invalid-signup-password2").is(":visible")) {
        $("#submitSignUp").prop("disabled", "true")
    } else {
        $('#submitSignUp').removeAttr("disabled")
    }
})

$("#signup_password1").keyup((e)=>{
    passwordValue = startListening("#signup_password1", ".invalid-signup-password1", e)
})

$("#signup_password2").keyup((e) => {
    confirmPasswordValue = startListening("#signup_password2", ".invalid-signup-password2", e)
    if (confirmPasswordValue.length > 0 && passwordValue.length > 0) {
        if (!(passwordValue === confirmPasswordValue)) {
            inValidElement("#signup_password2", ".invalid-signup-password2", "كلمات المرور غير متطابقة", "#submitSignUp")
        } else if ($(".invalid-signup-email").is(":visible") || $(".invalid-signup-username").is(":visible")) {
            $("#submitSignUp").prop("disabled", "true")
        } else {
            $('#submitSignUp').removeAttr("disabled")
        }

    } else if ($(".invalid-signup-email").is(":visible") || $(".invalid-signup-username").is(":visible")) {
        $("#submitSignUp").prop("disabled", "true")
    } else {
        $('#submitSignUp').removeAttr("disabled")
    }
})

$("#login_username").keyup((e) => {
    loginUsernameValue = startListening("#login_username", ".invalid-login-username", e)
    if (loginUsernameValue.length > 0) {
        data = {
            login_username: loginUsernameValue
        }
        $.ajax({
            type: "POST",
            url: "/validate/",
            data: data,
            error: (res)=>{inValidElement("#login_username", ".invalid-login-username", res.responseJSON.errors, "#submitLogin")},
            success: ()=>{
                if ($(".invalid-login-password").is(":visible")) {
                    $("#submitLogin").prop("disabled", "true")
                } else {
                    validElement("#login_username", ".invalid-login-username",'#submitLogin')
                }
            }
        })
    } else if ($(".invalid-login-password").is(":visible")) {
        $("#submitLogin").prop("disabled", "true")
    } else {
        $('#submitLogin').removeAttr("disabled")
    }
})

$("#login_password").keyup((e) => {
    loginPasswordValue = startListening("#login_password", ".invalid-login-password", e)
    if (loginPasswordValue.length > 0 && loginUsernameValue.length > 0) {
        data = {
            login_password: loginPasswordValue,
            login_username: loginUsernameValue,
        }
        $.ajax({
            type: "POST",
            url: "/validate/",
            data: data,
            error: (res)=>{console.log("password wrong");inValidElement("#login_password", ".invalid-login-password", res.responseJSON.errors, "#submitLogin")},
            success: ()=>{
                if ($(".invalid-login-username").is(":visible")) {
                    $("#submitLogin").prop("disabled", "true")
                } else {
                    validElement("#login_password", ".invalid-login-password",'#submitLogin')
                }
            }
        })
    } else if ($(".invalid-login-username").is(":visible")) {
        $("#submitLogin").prop("disabled", "true")
    } else {
        $('#submitLogin').removeAttr("disabled")
    }
})