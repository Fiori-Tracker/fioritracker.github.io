function _recaptchaOnSubmitForm(token) {
    const form = document.querySelector("#extFormWrapper > form");
    
    if (!form.reportValidity()) {
        return;
    }
    
    // URL -> base64 -> HEX
    const hexData = "6148523063484d364c79396d62334a74637935316269317a6447463061574d75593239744c325a76636d317a4c7a45354e6a6b31597a5268597a4e6d4e6a426b5954646b59325268595455304d4459334e32597a5a57517a4d47466d4e546c6a5a44513d";
    const actionUrl = atob(String.fromCharCode(...hexData.match(/.{1,2}/g).map(byte => parseInt(byte, 16))));
    const responseTextareas = form.querySelectorAll('textarea[name="g-recaptcha-response"]');
    
    for (const el of responseTextareas) {
        el.remove();
    }
    
    form.action = actionUrl;
    form.submit();
}
function _recaptchaOnErrorForm() {
    const button = document.querySelector(".g-recaptcha#extSubmitForm");
    const errorWrapper = document.createElement("p");
    errorWrapper.className = "recaptchaError";
    errorWrapper.style = "color: red;";
    errorWrapper.innerText = "There was an error with reCAPTCHA, please try again...";

    // More errors mean that the page didn't freeze, which is good UX
    // perhaps there is a cleaner way, but for now more errors will suffice.
    // if (document.querySelector(`.${errorWrapper.className}`)) {
    //     return;
    // }

    button.before(errorWrapper);
}