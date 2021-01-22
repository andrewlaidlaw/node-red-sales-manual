$(document).ready(function() {
    javascriptCheck();
    $('#id_contextdump').hide();
    enterbutton();
    invokeAjax ("Hello");
});

// if javascript is enabled on the browser then can remove the warning message
function javascriptCheck() {
    $('#no-script').remove();
}

// creates div for interaction with bot      
function createNewDiv(who, message) {
    var emoji;
    var html = '<div class="container">';
    if (who == "Bot") {
        emoji = "&#129409 Bot";
        html += '<div class="boticon">' + emoji + '</div><div class="botspeak">';
    }
    else if (who == "Error") {
        emoji = "&#128165 Error";
        html += '<div class="erricon">' + emoji + '</div><div class="errspeak">';
    }
    else if (who == "You") {
        emoji = "&#128055 You";
        html += '<div class="youicon">' + emoji + '</div><div class="youspeak">';
    }
    html +=  message;
    html += '</div></div>'
    return html;
}

// appends latest communication with bot to botchathistory
function chat(person, txt) {
    $('#id_botchathistory').append(createNewDiv(person, txt));
}    

// sets pressing of enter key to perform same action as send button
function enterbutton(){
    $(function() {
        $("form input").keypress(function (e) {
        if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
             $('#id_enter').click();
             return false;
        } else {
        return true;
        }
     });
    });
}

// User has entered some text.
function onChatClick() {
    var txt = $('#id_chattext').val();
    chat('You', txt); 
    invokeAjax(txt);
    $('#id_chattext').val('');
}

function processOK(response) {
    console.log(response);
    console.log(response.botresponse.messageout);
    console.log(response.botresponse.messageout.output.text);
    console.log(response.botresponse.messageout.context);
    chat('Bot', response.botresponse.messageout.output.text); 
    $('#id_contextdump').data('convContext', response.botresponse.messageout.context);
}
      
function processNotOK() {
    chat('Error', 'Error whilst attempting to talk to Bot');
}
      
function invokeAjax(message) {
    var contextdata = $('#id_contextdump').data('convContext');
    console.log('checking stashed context data');
    console.log(contextdata);
        
    var ajaxData = {};
    ajaxData.msgdata = message;
    if (contextdata) {
        ajaxData.context = contextdata;    
    }

    $.ajax({
        type: 'POST',
        url: 'botchat',
        data: ajaxData,
        success: processOK,
        error: processNotOK
    });
}