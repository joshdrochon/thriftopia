$('form').submit(function(e){
    e.preventDefault();
    $.ajax({
        url: `${$(this)[0].action}`,
        method: "post",
        data: $(this).serialize(),
        success: serverResponse => {
            let events = JSON.parse(serverResponse).reverse(),
            content = ""
            for (let i = 0; i < events.length; i+=1) {
                // console.log(events[i].message)
                content += `<p class="text-style-p">${events[i].message}</p>`
            }
            $('.activity').html(content)
        }
    })
});

function handleXP() {
    $.ajax({
        url: `/get_experience`,
        method: "get",
        data: $(this).serialize(),
        success: serverResponse => {
            let xp = serverResponse
            console.log(serverResponse)
            $(".progress-bar").css("width", function() {
                return `${xp}%`
            });
        }
    })
}




