/*
1 - Functions
2 - Main variables
3 - Events ( listening to the input in each of the register form inputs)

*/


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

getCurrentLanguage = function () {
    return window.location.pathname.split("/")[1]
}

var usernameValue = "",
    emailValue = "",
    passwordValue = "",
    confirmPasswordValue = "",
    loginUsernameValue = "",
    loginPasswordValue = "";
    Lang = getCurrentLanguage()


$("#signup_username").keyup((e) => {
    usernameValue = startListening("#signup_username", ".invalid-signup-username", e)
    if (usernameValue.length > 0) {
        data = {
            sign_up_username: usernameValue
        }
        $.ajax({
            type: "POST",
            url: "/"+Lang+"/validate/",
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
            url: "/"+Lang+"/validate/",
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
