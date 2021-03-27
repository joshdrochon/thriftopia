function getSkills(name, char_name, intel, luck, cunning, img_path) {
    $("#skillsModalLabel").html(name)

    let content = ""

    let skills = [
        {"intelligence":intel}, 
        {"luck":luck}, 
        {"cunning":cunning},
    ]

    let descs = ["Higher intelligence yields higher xp gains per activity", "Higher luck yields higher chance of more rare item drops.", "Higher cunning means more profit when selling items."]

    let idx = 0

    for (let skill of skills) {
        for (key in skill) {
            content += `<li class="skill" data-toggle="tooltip" data-placement="right" title="${descs[idx]}">${key}: <strong>${skill[key]}</strong></li>`
        }
        idx +=1
    }
    $("#skills-list").html(content)

    $("#character-name").html(char_name)

    $("#character-pic").attr("src", "/static/" + img_path);
    
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })
}