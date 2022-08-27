
function changeLanguage(el) {
    languageCode = window.location.pathname.split("/")[1]
    elementVal = $("#"+el.id).val()

    // if they are not the same change to the selected language
    if (elementVal != languageCode){
        $("#langForm").submit()
    }
}
