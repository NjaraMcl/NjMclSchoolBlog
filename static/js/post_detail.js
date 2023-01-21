const tete = document.getElementById('catp');
const post_content = document.getElementById('post_cnt');

if (postdata) {
    var postdata = JSON.parse(postdata);
    var auteurs = JSON.parse(author);
    for (const item of postdata){
        const date = new Date(item.fields.created_on);
        const formattedDate = date.toLocaleDateString();
        const newDivtete = document.createElement("div");
        newDivtete.className = "text-muted fst-italic mb-2";
        const newPost_content = document.createElement("p");
        for (const auteur of auteurs){
        newDivtete.innerHTML = `By ${auteur.fields.username} | ${formattedDate}`;
        tete.appendChild(newDivtete);
    }}
} else {
    console.log('tsy mande')
}
