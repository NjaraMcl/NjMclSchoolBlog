const tete = document.getElementById('catp');
if (postdata) {
    var postdata = JSON.parse(postdata);
    for (const item of postdata){
        const date = new Date(item.fields.created_on);
        const formattedDate = date.toLocaleDateString();
        const newDiv = document.createElement("div");
        newDiv.innerHTML = `By ${item.fields.title} | ${formattedDate}`;
        tete.appendChild(newDiv);
    }
} else {
    console.log('tsy mande')
}
