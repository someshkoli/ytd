
let link=$("#link").html()

$("#send").click(() => {
    console.log(link)
    $.ajax({
        method: "POST",
        url: "http://localhost:8000/yt/download/",
        data: JSON.stringify({
            add:link
        }).done((data)=>{
            jsondata=JSON.parse(data)
            console.log(jsondata)
        })
    })
})